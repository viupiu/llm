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
import sys
from pathlib import Path

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

ROOT = Path(__file__).resolve().parents[1]


def clean_name(name: str) -> str:
    """Убирает ВСЕ обратные кавычки и пробелы из имён узлов/скиллов."""
    return name.strip().replace("\u0060", "").strip()


def parse_skills_from_map(map_md_path: Path | None) -> list[str]:
    """Парсит названия навыков из файла архитектурной карты (### Skill: <name>). Дедупликация: dict.fromkeys сохраняет порядок."""
    if map_md_path is None or not map_md_path.exists():
        return []
    text = map_md_path.read_text(encoding="utf-8")
    return list(dict.fromkeys(clean_name(m.group(1)) for m in RE_SKILL_NAME.finditer(text)))


RE_TABLE_NODE = re.compile(r"\|\s*\S+\s*\|\s*`([^`]+)`")


def parse_skill_to_nodes_map(map_md_path: Path | None) -> dict[str, list[str]]:
    """
    Парсит из архитектурной карты какие узлы принадлежат какому скиллу.
    Поддерживает два формата:
      1. Table rows: `| G1 | `node_name` | TYPE | ...` (наиболее распространённый)
      2. Header nodes: `#### Узел: `Bot_Start`` (legacy)
    Возвращает {skill_name: [node_name, ...]}
    """
    if map_md_path is None or not map_md_path.exists():
        return {}
    text = map_md_path.read_text(encoding="utf-8")
    skill_to_nodes: dict[str, list[str]] = {}
    current_skill = None
    for line in text.splitlines():
        s = line.strip()
        m_skill = RE_SKILL_NAME.match(s)
        if m_skill:
            current_skill = clean_name(m_skill.group(1))
            if current_skill not in skill_to_nodes:
                skill_to_nodes[current_skill] = []
            continue
        if not current_skill:
            continue
        # 1) Table rows: `| G1 | `node_name` | ...`
        m_table = RE_TABLE_NODE.search(s)
        if m_table:
            node_name = clean_name(m_table.group(1))
            skill_to_nodes[current_skill].append(node_name)
            continue
        # 2) Legacy header format: `#### Узел: `name``
        m_node = re.match(r"#{4,5}\s*Узел:\s*(.+)", s)
        if m_node:
            node_name = clean_name(m_node.group(1))
            skill_to_nodes[current_skill].append(node_name)
    return skill_to_nodes


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


def parse_dictionaries_from_md(md_text: str) -> list[dict]:
    """Парсит словари из 4_RULES_AUTHOR__RULES_AND_DICTIONARIES.md (разбросаны по секциям узлов)."""
    dictionaries = []
    seen = set()
    lines = md_text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        # Поддержка формата "## Словарь: name"
        m = RE_DICT_HEADER.match(line)
        if m:
            name = m.group(1)
            if name in seen:
                i += 1
                continue
            seen.add(name)
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
                # Пропускаем DL-правила (паттерны с [@cmb, [dict, * и т.д.)
                if t.startswith("*") or t.startswith("[") or t.startswith("{"):
                    i += 1
                    continue
                body.append(t)
                i += 1
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
            continue
        if line.startswith("## ") or line.startswith("#"):
            i += 1
            continue
        if RE_DICT_NAME.match(line):
            name = line
            if name in seen:
                i += 1
                continue
            seen.add(name)
            i += 1
            body = []
            while i < len(lines):
                t = lines[i].strip()
                if not t:
                    i += 1
                    continue
                if t.startswith("## ") or t.startswith("#"):
                    break
                if RE_DICT_NAME.match(t):
                    break
                if t.startswith("*") or t.startswith("[") or t.startswith("{"):
                    i += 1
                    continue
                body.append(t)
                i += 1
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
            continue
        i += 1
    return dictionaries


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
    skill_names = parse_skills_from_map(args.map_md)
    if not skill_names:
        print("WARNING: No skills found in map file, nodes will have skill_id=None", file=sys.stderr)

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
            "is_common": False,
            "is_active": True,
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
    for np in sorted(nodes_dir.glob("*.json")):
        node = json.loads(np.read_text(encoding="utf-8"))
        node_name = clean_name(node.get("name", ""))
        node["name"] = node_name

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
        dicts = parse_dictionaries_from_md(md_path.read_text(encoding="utf-8"))
        for d in dicts:
            d = normalize_entity_export_fields(d, "Dictionary", creator=creator, created=now)
            write_entity(out_dir, "Dictionary", d)
            print(f"  Dictionary: {d['id']} ({d['name']})")

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
