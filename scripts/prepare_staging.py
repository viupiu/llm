# -*- coding: utf-8 -*-
"""
Собирает каталог staging из артефактов агентов (один узел + словари).

  python prepare_staging.py ^
    --node work/<BotSlug>/output/nodes/<id>.json ^
    --dict-md work/<BotSlug>/4_RULES_AUTHOR__RULES_AND_DICTIONARIES.md ^
    --out work/<BotSlug>/staging ^
    --assistant-name "Анекдот-Мастер" ^
    --skill-name "Выбор категории"
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime
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

ROOT = Path(__file__).resolve().parents[2]

RE_DICT_NAME = re.compile(r"^[a-z][a-z0-9_]*$")
RE_DICT_HEADER = re.compile(r"^##\s*Словарь:\s*([a-z][a-z0-9_]*)\s*$")


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


def parse_dictionary_body_lines(body_lines: list[str]) -> list[dict]:
    """
    Строки тела словаря → blocks.
    Канон без префикса =>, затем синонимы =>...
    Пример:
      Москва
      =>москв~
      Санкт-Петербург
      =>питер~
    """
    blocks: list[dict] = []
    for raw in body_lines:
        line = raw.strip()
        if not line or line.startswith("//"):
            continue
        blocks.append(_dict_line_to_block(line))
    return blocks


def parse_dictionaries_from_md(md_text: str) -> list[dict]:
    """Парсит блоки словарей из 4_RULES_AUTHOR__RULES_AND_DICTIONARIES.md (формат Автора ДЛ)."""
    dictionaries = []
    seen = set()
    lines = md_text.splitlines()
    i = 0
    # Try to find legacy "** Словари **" section start
    while i < len(lines):
        if "Словари" in lines[i] and lines[i].strip().startswith("**"):
            i += 1
            break
        i += 1

    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
        # Поддержка формата "## Словарь: name"
        if RE_DICT_HEADER.match(line):
            name = RE_DICT_HEADER.match(line).group(1)
            if name in seen:
                i += 1
                continue
            seen.add(name)
            i += 1
            body: list[str] = []
            while i < len(lines):
                t = lines[i].strip()
                if not t:
                    i += 1
                    continue
                if t.startswith("## ") or t.startswith("#"):
                    break
                if RE_DICT_HEADER.match(t):
                    break
                if RE_DICT_NAME.match(t):
                    break
                if t.startswith("*") or t.startswith("[") or t.startswith("{"):
                    i += 1
                    continue
                body.append(t)
                i += 1
            blocks = parse_dictionary_body_lines(body)
            if not blocks:
                continue
            did = new_short_id()
            dictionaries.append(
                {
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
                }
            )
            continue
        if line.startswith("**") and "Словари" not in line:
            break
        if line.startswith("//") or line.startswith("#") and not RE_DICT_HEADER.match(line):
            i += 1
            continue
        if RE_DICT_NAME.match(line):
            name = line
            if name in seen:
                i += 1
                continue
            seen.add(name)
            i += 1
            body: list[str] = []
            while i < len(lines):
                t = lines[i].strip()
                if not t:
                    i += 1
                    continue
                if t.startswith("**"):
                    break
                if RE_DICT_NAME.match(t):
                    break
                body.append(t)
                i += 1
            blocks = parse_dictionary_body_lines(body)
            if not blocks:
                continue
            did = new_short_id()
            dictionaries.append(
                {
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
                }
            )
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
    parser = argparse.ArgumentParser(description="Сборка staging из узла и md словарей")
    parser.add_argument("--node", type=Path, required=True)
    parser.add_argument("--dict-md", type=Path, help="4_RULES_AUTHOR__RULES_AND_DICTIONARIES.md со словарями")
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--assistant-name", default="Generated Bot")
    parser.add_argument("--skill-name", default="main")
    parser.add_argument("--export-basename", default="GeneratedBot")
    parser.add_argument("--project-id", default="205473")
    parser.add_argument(
        "--creator",
        default=DEFAULT_CREATOR,
        help="UUID пользователя из вашего экспорта ДОС (поле creator в Assistant.json)",
    )
    args = parser.parse_args()

    node_path = args.node if args.node.is_absolute() else ROOT / args.node
    out_dir = args.out if args.out.is_absolute() else ROOT / args.out
    if out_dir.exists():
        for p in out_dir.iterdir():
            if p.is_dir():
                for f in p.glob("*.json"):
                    f.unlink()
            elif p.name == "9_PACKAGER__MANIFEST.json":
                p.unlink()

    node = json.loads(node_path.read_text(encoding="utf-8"))
    node_id = new_short_id()
    node["id"] = node_id
    node["parent"] = None
    node = normalize_dialog_node(node)

    assistant_id = new_full_id()
    branch_id = new_full_id()
    skill_id = new_short_id()
    node["skill_id"] = skill_id

    now = format_dos_datetime()
    creator = args.creator

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
    skill = {
        "id": skill_id,
        "name": args.skill_name,
        "is_common": False,
        "is_active": True,
        "meta": {},
        "created": now,
        "updated": None,
        "creator": creator,
        "editors": [],
    }

    node = normalize_entity_export_fields(
        node, "DialogNode", creator=creator, created=now
    )

    write_entity(out_dir, "Assistant", assistant)
    write_entity(out_dir, "Branch", branch)
    write_entity(out_dir, "Skill", skill)
    write_entity(out_dir, "DialogNode", node)

    if args.dict_md:
        md_path = args.dict_md if args.dict_md.is_absolute() else ROOT / args.dict_md
        for d in parse_dictionaries_from_md(md_path.read_text(encoding="utf-8")):
            d = normalize_entity_export_fields(
                d, "Dictionary", creator=creator, created=now
            )
            write_entity(out_dir, "Dictionary", d)

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

    print(f"Staging: {out_dir}")
    print(f"  Assistant: {assistant_id}")
    print(f"  DialogNode: {node_id} ({node.get('name')})")
    print(f"  Dictionaries: {len(list((out_dir / 'Dictionary').glob('*.json'))) if (out_dir / 'Dictionary').exists() else 0}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
