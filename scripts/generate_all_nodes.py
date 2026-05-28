# -*- coding: utf-8 -*-
"""
Генерирует DialogNode JSON для всех узлов из артефактов агентов.

  python generate_all_nodes.py ^
    --responses work/<BotSlug>/7_RESPONSES_AUTHOR__RESPONSES.md ^
    --rules work/<BotSlug>/4_RULES_AUTHOR__RULES_AND_DICTIONARIES.md ^
    --ml-examples work/<BotSlug>/5_EXAMPLES_AUTHOR__DATASET.md ^
    --out work/<BotSlug>/output/nodes
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
    new_short_id,
    normalize_blocks_field,
    normalize_dialog_node,
    normalize_entity_export_fields,
)

ROOT = Path(__file__).resolve().parent.parent


def clean_name(name: str) -> str:
    """Убирает обратные кавычки и пробелы из имён узлов/скиллов."""
    return name.strip().strip("`").strip()


def parse_response_blocks(md_text: str) -> dict[str, dict]:
    """Парсит узлы из 6_RESPONSES_AUTHOR__RESPONSES.md -> {node_name: {answers, conditions}}."""
    nodes = {}
    lines = md_text.splitlines()
    i = 0
    while i < len(lines):
        m = re.match(r"^## Узел:\s+(.+)$", lines[i].strip())
        if not m:
            i += 1
            continue
        node_name = clean_name(m.group(1))
        i += 1
        conditions_lines = []
        answers_lines = []
        section = "unknown"
        while i < len(lines):
            line = lines[i]
            stripped = line.strip()
            if stripped.startswith("## Узел:") or stripped.startswith("## Словарь:"):
                break
            if stripped == "Условия:":
                section = "conditions"
                i += 1
                continue
            if stripped == "Ответы:":
                section = "answers"
                i += 1
                continue
            if section == "conditions" and stripped and stripped != "Нет" and stripped != "---":
                conditions_lines.append(stripped)
            if section == "answers" and stripped and stripped != "---" and stripped != "Нет":
                answers_lines.append(stripped)
            i += 1
        cond = "\n".join(conditions_lines).strip() if conditions_lines else None
        if cond and cond.lower() == "нет":
            cond = None
        nodes[node_name] = {"answers": answers_lines, "conditions": cond}
    return nodes


def parse_rule_blocks(md_text: str) -> dict[str, list[str]]:
    """Парсит узлы из 3_RULES_AUTHOR__RULES_AND_DICTIONARIES.md -> {node_name: [rule_lines]}.

    Файл имеет структуру:
      ## Узел: name
      Условия:
      %that_anchor=...
      Ответы:
      * rule1
      * rule2

    Извлекаем ТОЛЬКО строки из секции "Ответы:" (DL-правила со звёздочкой).
    """
    nodes = {}
    lines = md_text.splitlines()
    i = 0
    while i < len(lines):
        m = re.match(r"^## Узел:\s+(.+)$", lines[i].strip())
        if not m:
            i += 1
            continue
        node_name = clean_name(m.group(1))
        i += 1
        rule_lines = []
        section = None  # "conditions" | "answers" | None
        while i < len(lines):
            line = lines[i]
            stripped = line.strip()
            # Граница: новый узел, словарь, или конец файла
            if stripped.startswith("## Узел:") or stripped.startswith("## Словарь:"):
                break
            if stripped == "Условия:":
                section = "conditions"
                i += 1
                continue
            if stripped == "Ответы:":
                section = "answers"
                i += 1
                continue
            if section == "answers" and stripped:
                # Захватываем только DL-правила (начинаются с * или EVENT)
                if stripped.startswith("*") or stripped.startswith("EVENT "):
                    rule_lines.append(stripped)
            i += 1
        nodes[node_name] = rule_lines
    return nodes


ML_META_RE = re.compile(
    r"^-\s*(Intent:|Примеры:|---)$"
)

def parse_ml_blocks(md_text: str) -> dict[str, list[str]]:
    """Парсит узлы из 4_EXAMPLES_AUTHOR__DATASET.md -> {node_name: [clean_example_phrases]}.

    Файл имеет структуру:
      ## Узел: `name`
      - Intent: `intent_name`
      - Примеры:
      - фраза1
      - фраза2
      ---

    Извлекаем ТОЛЬКО чистые фразы (без заголовков).
    """
    nodes = {}
    lines = md_text.splitlines()
    i = 0
    while i < len(lines):
        m = re.match(r"^## Узел:\s+(.+)$", lines[i].strip())
        if not m:
            i += 1
            continue
        node_name = clean_name(m.group(1))
        i += 1
        examples = []
        collecting = False
        while i < len(lines):
            line = lines[i]
            stripped = line.strip()
            if stripped.startswith("## Узел:"):
                break
            if stripped.startswith("- Примеры:"):
                collecting = True
                i += 1
                continue
            if stripped == "---":
                collecting = False
                i += 1
                continue
            if not collecting:
                i += 1
                continue
            # Пропускаем строки вида "- Intent: ..." и подобные метаданные
            if stripped.startswith("- Intent:") or stripped.startswith("- Примеры:"):
                i += 1
                continue
            # Если строка начинается с "- ", убираем префикс
            if stripped.startswith("- "):
                phrase = stripped[2:].strip()
                if phrase:
                    examples.append(phrase)
            elif stripped:
                examples.append(stripped)
            i += 1
        if node_name in nodes:
            nodes[node_name].extend(examples)
        else:
            nodes[node_name] = examples
    return nodes


def split_rule_and_dsl_tags(raw_rule: str) -> tuple[str, str]:
    """Разделяет строку на DL-правило и DSL-теги.

    Формат в RULES файле: '* @cmb(...) * [%tag] * [@goto(...)]'
    Первый фрагмент — DL-паттерн (если содержит @cmb/@keyword/[-entity-]).
    Всё остальное (разделённо ' * ') — DSL-теги для ответа.

    Если строка НЕ содержит @cmb/@keyword/[-entity-] — это не DL-правило,
    а чистый DSL-тег (e.g. [disableautovars], [%that_anchor=...]) -> в answers.
    """
    parts = raw_rule.split(" * ")
    dl_part = parts[0].strip()
    if len(parts) > 1:
        tags_part = " ".join(parts[1:]).strip()
    else:
        tags_part = ""

    # Проверка: это реальный DL-паттерн?
    is_dl_rule = ('@cmb' in dl_part or '@keyword' in dl_part or '[-' in dl_part or
                  'EVENT ' in dl_part or dl_part.strip() == '*')
    if is_dl_rule:
        return dl_part, tags_part

    # Не DL-правило — весь текст идёт в answers
    combined = dl_part + (" " + tags_part if tags_part else "")
    return "", combined


def lines_to_blocks(lines: list[str]) -> dict:
    """Список строк -> blocks JSON. """
    blocks = []
    for line in lines:
        blocks.append({
            "key": "x",
            "data": {},
            "text": line,
            "type": "unstyled",
            "depth": 0,
            "entityRanges": [],
            "inlineStyleRanges": [],
        })
    return {"blocks": blocks, "entityMap": {}}


def build_condition(node_name: str, from_responses: str | None) -> str | None:
    if from_responses:
        return from_responses
    return None


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description="Генерация JSON-узлов из артефактов")
    parser.add_argument("--responses", type=Path, required=True)
    parser.add_argument("--rules", type=Path, required=True)
    parser.add_argument("--ml-examples", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--creator", default=DEFAULT_CREATOR)
    args = parser.parse_args()

    out_dir = args.out if args.out.is_absolute() else ROOT / args.out
    out_dir.mkdir(parents=True, exist_ok=True)

    responses = parse_response_blocks(args.responses.read_text(encoding="utf-8"))
    rules = parse_rule_blocks(args.rules.read_text(encoding="utf-8"))
    ml = parse_ml_blocks(args.ml_examples.read_text(encoding="utf-8"))

    all_node_names = sorted(
        set(list(responses.keys()) + list(rules.keys()) + list(ml.keys()))
    )

    now = format_dos_datetime()
    creator = args.creator
    created_count = 0

    for node_name in all_node_names:
        resp = responses.get(node_name, {})
        answer_lines = resp.get("answers", []) if isinstance(resp, dict) else resp
        rule_lines = rules.get(node_name, [])
        ml_lines = ml.get(node_name, [])

        cond_from_md = resp.get("conditions") if isinstance(resp, dict) else None
        condition = build_condition(node_name, cond_from_md)

        # Разделяем DL-правила и DSL-теги: '* @cmb(...) * [%tag] * [@goto(...)]'
        # DL-часть идёт в dl_rules, теги — в answers.
        clean_rule_lines = []
        dsl_tags_from_rules = []
        for rl in rule_lines:
            raw = rl.strip()
            # Обрезаем префикс "* " (звёздочка + пробел из markdown списка)
            if raw.startswith("* "):
                raw = raw[2:]
            elif raw == "*":
                raw = "*"
            dl_part, tags_part = split_rule_and_dsl_tags(raw.strip())
            clean_rule_lines.append(dl_part)
            if tags_part:
                dsl_tags_from_rules.append(tags_part)

        # DSL-теги из правил добавляются к ответам
        merged_answers = answer_lines + dsl_tags_from_rules

        if not merged_answers and not clean_rule_lines and not ml_lines:
            print(f"  SKIP {node_name}: нет данных")
            continue

        node_obj = {
            "id": new_short_id(),
            "name": node_name,
            "description": "",
            "parent": None,
            "shortcuts": [],
            "conditions": condition,
            "dl_rules": lines_to_blocks(clean_rule_lines),
            "ml_examples": lines_to_blocks(ml_lines),
            "intent_id": None,
            "skill_id": None,
            "answers": lines_to_blocks(merged_answers),
            "responses": [],
            "slot_filling": [
                {
                    "id": "x" * 10,
                    "entity": {"id": "", "name": ""},
                    "question": "",
                    "required": False,
                    "variable": {"id": "", "name": ""},
                }
            ],
            "is_active": True,
            "auto_conflict_resolution": None,
            "meta": {},
            "created": now,
            "updated": None,
            "creator": creator,
            "editors": [],
        }

        node_obj = normalize_dialog_node(node_obj)
        node_obj = normalize_entity_export_fields(
            node_obj, "DialogNode", creator=creator, created=now
        )

        node_id = node_obj["id"]
        out_path = out_dir / f"{node_id}.json"
        out_path.write_text(
            json.dumps(node_obj, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        cond_str = f' cond="{condition}"' if condition else ""
        print(f"  OK {node_id} -> {node_name}{cond_str}")
        created_count += 1

    print(f"\nCreated {created_count} nodes in {out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
