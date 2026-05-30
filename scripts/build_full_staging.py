# -*- coding: utf-8 -*-
"""
Собирает полный staging из всех узлов + словари.

  python build_full_staging.py ^
    --nodes-dir work/<BotSlug>/output/nodes ^
    --dict-md work/<BotSlug>/4_RULES_AUTHOR__RULES_AND_DICTIONARIES.md ^
    --out work/<BotSlug>/staging ^
    --assistant-name "<имя бота>" ^
    --export-basename "<имя_экспорта>"
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

from archive_core import (
    DEFAULT_CREATOR,
    format_dos_datetime,
    new_full_id,
    new_short_id,
    normalize_blocks_field,
    normalize_dialog_node,
    normalize_entity_export_fields,
)

RE_DICT_NAME = re.compile(r"^[a-z][a-z0-9_]*$")
RE_SKILL_NAME = re.compile(r"### Skill:\s*(.+)")
RE_DICT_HEADER = re.compile(r"^##\s*Словарь:\s*([a-z][a-z0-9_]*)\s*$")
RE_INCLUDE_REF = re.compile(r"--include\((\w[\w_]*)\s*\)")


def _collect_raw_dictionaries(md_text: str) -> dict[str, list[str]]:
    """Возвращает {name: [lines]} — raw body всех словарей (с --include строками)."""
    result = {}
    lines = md_text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        m = RE_DICT_HEADER.match(line)
        if not m:
            i += 1
            continue
        name = m.group(1)
        i += 1
        body = []
        while i < len(lines):
            t = lines[i].strip()
            if not t:
                i += 1
                continue
            if t.startswith("## ") or t.startswith("#"):
                break
            if RE_DICT_HEADER.match(t):
                break
            # Пропускаем DL-правила
            if t.startswith("*") or t.startswith("[") or t.startswith("{"):
                i += 1
                continue
            body.append(t)
            i += 1
        result[name] = body
    return result


def parse_dictionaries_from_md(md_text: str) -> list[dict]:
    """Парсит словари из 4_RULES_AUTHOR__RULES_AND_DICTIONARIES.md (разбросаны по секциями узлов)."""
    raw_dicts = _collect_raw_dictionaries(md_text)

    # Collect --include references per dict name
    dict_includes: dict[str, list[str]] = {}
    for name, body in raw_dicts.items():
        direct_includes = [m.group(1) for m in RE_INCLUDE_REF.finditer(
            md_text.splitlines()[0]  # placeholder, we'll re-scan
        )]
        dict_includes[name] = []

    # Re-scan: find --include per dict
    lines = md_text.splitlines()
    current_dict = None
    for line in lines:
        m = RE_DICT_HEADER.match(line.strip())
        if m:
            current_dict = m.group(1)
            continue
        if current_dict and line.strip().startswith("## "):
            current_dict = None
            continue
        if current_dict:
            for inc_match in RE_INCLUDE_REF.finditer(line):
                dict_includes.setdefault(current_dict, []).append(inc_match.group(1))

    # Resolve bodies recursively with cycle detection
    def resolve_body(dict_name: str, visited: set) -> list[str]:
        if dict_name in visited:
            return []
        visited.add(dict_name)
        result = []
        # First, add own raw body
        result.extend(raw_dicts.get(dict_name, []))
        # Then, recursively merge includes
        for inc_name in dict_includes.get(dict_name, []):
            result.extend(resolve_body(inc_name, visited))
        return result

    seen = set()
    dictionaries = []
    for name in sorted(raw_dicts.keys()):
        if name in seen:
            continue
        seen.add(name)
        body = resolve_body(name, set())
        blocks = [_dict_line_to_block(l) for l in body if l.strip()]
        if not blocks:
            continue
        did = new_short_id()
        dictionaries.append({
            "id": did,
            "name": name,
            "description": "",
            "content": normalize_blocks_field({"blocks": blocks}),
            "is_common": True,
            "is_hidden": False,
            "is_active": True,
            "meta": {},
            "created": format_dos_datetime(),
            "updated": None,
            "creator": DEFAULT_CREATOR,
            "editors": [],
        })

    # Validate unresolved includes
    all_defined = set(raw_dicts.keys())
    all_referenced = set()
    for refs in dict_includes.values():
        all_referenced.update(refs)
    missing = all_referenced - all_defined
    if missing:
        print(
            f"WARNING: --include references not found as defined dictionaries: {sorted(missing)}",
            file=sys.stderr,
        )

    return dictionaries


def clean_name(name: str) -> str:
    """Убирает обратные кавычки и пробелы из имён узлов/скиллов."""
    return name.strip().strip("`").strip()


def _dict_line_to_block(text: str) -> dict:
    return {
        "key": "x",
        "data": {},
        "text": text,
        "type": "unstyled",
        "depth": 0,
        "entityRanges": [],
        "inlineStyleRanges": [],
    }


RE_SKILL_HEADER = re.compile(r"^### Skill:\s*(.+?)(?:\s*\(|$)", re.MULTILINE)
RE_NODE_TABLE_ROW = re.compile(r"^\|\s*(.+?)\s*\|")


def parse_skills_from_map(map_md: Path | None) -> list[str]:
    """Извлекает уникальные имена навыков из 1_ARCHITECTURE__MAP.md.

    Формат: ### Skill: NAME ...
    Игнорирует "(объявлен выше, повтор запрещён)".
    """
    if not map_md or not map_md.exists():
        return []
    text = map_md.read_text(encoding="utf-8")
    seen = []
    seen_set = set()
    for m in RE_SKILL_HEADER.finditer(text):
        name = clean_name(m.group(1))
        if name and name.lower() != "объявлен выше, повтор запрещён" and name not in seen_set:
            seen.append(name)
            seen_set.add(name)
    return seen


def parse_skill_to_nodes_map(map_md: Path | None) -> dict[str, list[str]]:
    """Возвращает {skill_name: [node_names]} из архитектурной карты.

    Парсит таблицы узлов внутри каждого "### Skill: NAME" блока.
    Первый столбец таблицы — имя узла.
    """
    if not map_md or not map_md.exists():
        return {}
    text = map_md.read_text(encoding="utf-8")
    result: dict[str, list[str]] = {}
    lines = text.splitlines()
    current_skill = None
    in_table = False
    for line in lines:
        stripped = line.strip()
        # Начало блока скилла
        m = RE_SKILL_HEADER.match(stripped)
        if m:
            name = clean_name(m.group(1))
            if name:
                current_skill = name
                if current_skill not in result:
                    result[current_skill] = []
            in_table = False
            continue
        # Заголовки других секций обнуляют текущий скилл (но не ###)
        if re.match(r"^(?:## |# )", stripped) and not stripped.startswith("###"):
            current_skill = None
            in_table = False
            continue
        # Строки таблицы: | node_name | ...
        if current_skill and RE_NODE_TABLE_ROW.match(stripped):
            in_table = True
            parts = stripped.split("|")
            if len(parts) >= 2:
                node_name = clean_name(parts[1])
                # Пропускаем заголовочные строки таблицы (Узел, Тип, и т.д.)
                if node_name and node_name.lower() not in ("узел", "type", "тип", "purpose", "навык", "назначение") and node_name not in ("Тип", "Purpose", "Переходы", "Якорь", "Грань"):
                    if node_name not in result[current_skill]:
                        result[current_skill].append(node_name)
            continue
        # Пустая строка завершает таблицу
        if not stripped and in_table:
            in_table = False
    return result


def write_entity(out_dir: Path, entity_dir: str, obj: dict) -> None:
    folder = out_dir / entity_dir
    folder.mkdir(parents=True, exist_ok=True)
    eid = obj["id"]
    path = folder / f"{eid}.json"
    path.write_text(
        json.dumps(obj, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description="Полная сборка staging")
    parser.add_argument("--nodes-dir", type=Path, required=True)
    parser.add_argument("--dict-md", type=Path, help="4_RULES_AUTHOR__RULES_AND_DICTIONARIES.md")
    parser.add_argument("--map-md", type=Path, help="1_ARCHITECTURE__MAP.md (источник навыков)")
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--assistant-name", default="Bot")
    parser.add_argument("--export-basename", default="Bot")
    parser.add_argument("--project-id", default="205473")
    parser.add_argument("--creator", default=DEFAULT_CREATOR)
    args = parser.parse_args()

    nodes_dir = args.nodes_dir if args.nodes_dir.is_absolute() else ROOT / args.nodes_dir
    out_dir = args.out if args.out.is_absolute() else ROOT / args.out

    # Очистка staging
    if out_dir.exists():
        for p in out_dir.iterdir():
            if p.is_dir():
                for f in p.glob("*.json"):
                    f.unlink()

    now = format_dos_datetime()
    creator = args.creator
    assistant_id = new_full_id()
    branch_id = new_full_id()

    # Парсим навыки из архитектурной карты
    # Парсим навыки из архитектурной карты
    skill_names = parse_skills_from_map(args.map_md)
    # Всегда создаём как минимум один скилл
    if not skill_names:
        auto_skill_name = args.assistant_name
        skill_names = [auto_skill_name]
        print(f"INFO: No skills from map, created default skill '{auto_skill_name}'", file=sys.stderr)

    # Парсим привязку узлов к скиллам
    skill_to_nodes = parse_skill_to_nodes_map(args.map_md)
    node_to_skill: dict[str, str] = {}
    for sk, nns in skill_to_nodes.items():
        for nn in nns:
            node_to_skill[nn] = sk

    # Создаём skills из карты
    skill_ids = {}
    for skill_name in skill_names:
        sid = new_short_id()
        skill = {
            "id": sid,
            "name": skill_name,
            "description": "",
            "is_starter": False,
            "meta": {},
            "created": now,
            "updated": None,
            "creator": creator,
            "editors": [],
        }
        skill = normalize_entity_export_fields(skill, "Skill", creator=creator, created=now)
        write_entity(out_dir, "Skill", skill)
        skill_ids[skill_name] = sid
        print(f"  Skill: {sid} ({skill_name})")

    # Assistant
    assistant = {
        "id": assistant_id,
        "name": args.assistant_name,
        "description": None,
        "is_active": True,
        "meta": {},
        "avatar_url": None,
        "project_id": args.project_id,
        "created": now,
        "updated": None,
        "creator": creator,
        "editors": [],
    }
    write_entity(out_dir, "Assistant", assistant)

    # Branch
    branch = {
        "id": branch_id,
        "assistant_id": assistant_id,
        "parent_id": None,
        "name": "master",
        "is_loaded": False,
        "project_id": args.project_id,
        "created": now,
        "synced": None,
        "updated": None,
        "is_sync_db_git": True,
        "creator": None,
        "editors": [],
    }
    write_entity(out_dir, "Branch", branch)

    # DialogNodes
    node_count = 0
    seen_names = set()
    for np in sorted(nodes_dir.glob("*.json")):
        node = json.loads(np.read_text(encoding="utf-8"))
        node_name = clean_name(node.get("name", ""))
        node["name"] = node_name

        if node_name in seen_names:
            print(f"  SKIPPED duplicate: {np.name} (name={node_name})", file=sys.stderr)
            continue
        seen_names.add(node_name)

        # Присваиваем skill_id по маппингу из架构图
        target_skill = node_to_skill.get(node_name)
        if target_skill and target_skill in skill_ids:
            node["skill_id"] = skill_ids[target_skill]
        elif skill_ids:
            # Fallback: первый скилл (START) для узлов без явной привязки
            node["skill_id"] = list(skill_ids.values())[0]
            print(f"  WARNING: {node_name} не найден в карте навыков, назначен на '{list(skill_ids.keys())[0]}'", file=sys.stderr)

        node = normalize_dialog_node(node)
        node = normalize_entity_export_fields(node, "DialogNode", creator=creator, created=now)
        write_entity(out_dir, "DialogNode", node)
        cond = node.get("conditions") or ""
        assigned_skill = node_to_skill.get(node_name, list(skill_ids.keys())[0] if skill_ids else "?")
        print(f"  DialogNode: {node['id']} ({node_name}) skill={assigned_skill}{f' cond={cond}' if cond else ''}")
        node_count += 1

    # Dictionaries
    if args.dict_md:
        md_path = args.dict_md if args.dict_md.is_absolute() else ROOT / args.dict_md

        # --- Dictionary Validator (предварительная проверка) ---
        validator_script = ROOT / "scripts" / "dictionary_validator.py"
        if validator_script.exists():
            catalog_path = ROOT / "docs" / "reference" / "COMMON_DICTIONARIES.md"
            ref_dir = ROOT / "docs" / "reference" / "dictionaries"
            proc = subprocess.run(
                [sys.executable, str(validator_script),
                 "--rules", str(md_path),
                 "--ref-dir", str(ref_dir),
                 "--catalog", str(catalog_path)],
                capture_output=False
            )
            if proc.returncode != 0:
                print("\nBuild aborted: Dictionary Validator failed.", file=sys.stderr)
                return 1
        # --------------------------------------------------------

        dicts = parse_dictionaries_from_md(md_path.read_text(encoding="utf-8"))
        for d in dicts:
            d = normalize_entity_export_fields(d, "Dictionary", creator=creator, created=now)
            write_entity(out_dir, "Dictionary", d)
            print(f"  Dictionary: {d['id']} ({d['name']})")

    # --- Auto-declare variables used in nodes ---
    RE_VAR_REF = re.compile(r"%([\w_]+)")
    # Known system variables that don't need declaration
    SYS_VARS = {"context", "sys", "date", "time", "now", "input", "text", "payload",
                "user", "session", "request", "response", "counter", "random",
                "anchor", "lastinput", "that", "topic", "lang", "channel"}

    # Scan all DialogNodes for %variable references
    all_used_vars: set[str] = set()
    dn_dir = out_dir / "DialogNode"
    if dn_dir.exists():
        for np in dn_dir.glob("*.json"):
            blob = np.read_text(encoding="utf-8")
            for m in RE_VAR_REF.finditer(blob):
                vn = m.group(1).lower()
                if vn not in SYS_VARS:
                    all_used_vars.add(m.group(1))

    # Check which already have Variable entities
    var_dir = out_dir / "Variable"
    existing_vars: set[str] = set()
    if var_dir.exists():
        for vp in var_dir.glob("*.json"):
            v = json.loads(vp.read_text(encoding="utf-8"))
            existing_vars.add(v.get("name", "").lower())

    undeclared = {vn for vn in all_used_vars if vn.lower() not in existing_vars}
    var_descriptions = {
        "cat_mood": "Настроение кота",
        "that_anchor": "Якорь для задавателя вопроса",
        "user_type": "Тип пользователя: физ/юр",
    }

    for vn in sorted(undeclared):
        vid = new_short_id()
        vdesc = var_descriptions.get(vn, f"Переменная: {vn}")
        var_obj = {
            "id": vid,
            "name": vn,
            "description": vdesc,
            "type": "user",
            "value": "",
            "life_cycle": "0",
            "extra": {
                "api": True,
                "scope": "session",
                "secret": False,
            },
            "is_editable": None,
            "created": now,
            "updated": None,
            "creator": creator,
            "editors": [],
        }
        var_obj = normalize_entity_export_fields(var_obj, "Variable", creator=creator, created=now)
        write_entity(out_dir, "Variable", var_obj)
        print(f"  Variable: {vid} ({vn})")

    if undeclared:
        print(f"  Auto-declared {len(undeclared)} variable(s): {sorted(undeclared)}")

    # Manifest
    manifest = {
        "export_basename": args.export_basename,
        "assistant_id": assistant_id,
        "assistant_name": args.assistant_name,
        "project_id": args.project_id,
        "creator": creator,
    }
    (out_dir / "9_PACKAGER__MANIFEST.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print(f"\nStaging: {out_dir}")
    print(f"  Assistant: {assistant_id}")
    print(f"  Skills: {len(skill_ids)}")
    print(f"  DialogNodes: {node_count}")
    print(f"  Dictionaries: {len(list((out_dir / 'Dictionary').glob('*.json'))) if (out_dir / 'Dictionary').exists() else 0}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
