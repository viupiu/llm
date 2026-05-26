# -*- coding: utf-8 -*-
"""
Валидация md-файлов проекта (ответы от агентов).

python validate_archive.py work/<ProjectName>
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def parse_node_from_header(text: str) -> str:
    m = re.search(r"## Узел:\s*(.+)", text)
    return m.group(1).strip() if m else ""


def parse_nodes_from_dl_responses(text: str) -> list[str]:
    return [parse_node_from_header(h) for h in re.split(r"---\s*$", text, flags=re.M)
            if parse_node_from_header(h)]


def parse_nodes_from_dl_rules(text: str) -> list[str]:
    return [parse_node_from_header(h) for h in re.split(r"---\s*$", text, flags=re.M)
            if parse_node_from_header(h)]


def parse_dictionaries_from_rules(text: str) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    for m in re.finditer(r"## Словарь:\s*(\S+)\n((?!##).*?)^(?=\n##|\Z)", text, re.M | re.S):
        name = m.group(1).strip()
        entries = [l.strip() for l in m.group(2).strip().splitlines() if l.strip()]
        result[name] = entries
    return result


def parse_registry_nodes(text: str) -> list[str]:
    nodes = []
    in_registry = False
    for line in text.splitlines():
        if "Реестр узлов" in line:
            in_registry = True
            continue
        if in_registry:
            m = re.match(r"\|\s*\d+\s*\|\s*([^\|]+)\|", line)
            if m:
                nodes.append(m.group(1).strip())
            elif line.startswith("##") or (line.strip() and not line.startswith("|") and line.strip() != "---"):
                break
    return nodes


def parse_anchor_registry(text: str) -> list[str]:
    anchors = []
    in_section = False
    for line in text.splitlines():
        if "Реестр якорей" in line:
            in_section = True
            continue
        if in_section:
            m = re.match(r"\|\s*(.+?)\s*\|\s*[^|]+\|", line)
            if m and not line.strip().startswith("---"):
                val = m.group(1).strip().strip("`")
                anchors.append(val)
            elif line.startswith("##") or (line.strip() and not line.startswith("|")):
                break
    return anchors


def parse_that_anchors(text: str) -> set[str]:
    return set(re.findall(r'%that_anchor="([^"]+)"', text))


def parse_gotos(text: str) -> set[str]:
    return set(re.findall(r'@goto\("([^"]+)"\)', text))


def parse_dict_refs(text: str) -> set[str]:
    return set(re.findall(r'\[dict\(([^)]+)\)\]', text))


def run(project_dir: Path) -> int:
    errors: list[str] = []
    warns: list[str] = []

    required_files = {
        "architecture_map.md": "Карта архитектуры",
        "dl_responses_result.md": "DL-ответы",
        "dl_rules_result.md": "DL-правила",
        "copywriter_result.md": "Тексты бота",
        "user_phrases.md": "Фразы пользователей",
    }

    files: dict[str, str] = {}
    for fname, label in required_files.items():
        fpath = project_dir / fname
        if not fpath.exists():
            errors.append(f"MISSING_FILE: {fname} ({label})")
        else:
            files[fname] = fpath.read_text(encoding="utf-8")

    if errors:
        for e in errors:
            print(f"[ERROR] {e}")
        print(f"\nFAILED: ошибок — {len(errors)}.")
        return 1

    arch = files["architecture_map.md"]
    dl_resp = files["dl_responses_result.md"]
    dl_rules = files["dl_rules_result.md"]
    user_phrases = files["user_phrases.md"]

    # 1. Registry coverage
    registry = parse_registry_nodes(arch)
    resp_nodes = parse_nodes_from_dl_responses(dl_resp)

    if not registry:
        errors.append("PARSE_ERROR: Не удалось разобрать реестр узлов §9 из architecture_map.md")
    else:
        for node in registry:
            if node not in resp_nodes:
                errors.append(f"MISSING_RESPONSE: Узел «{node}» есть в реестре, но нет в dl_responses_result.md")

    # 2. Nodes with DL rules must have responses
    rule_nodes = parse_nodes_from_dl_rules(dl_rules)
    for node in rule_nodes:
        if node not in resp_nodes:
            errors.append(f"MISSING_RESPONSE_FOR_RULE: Узел «{node}» есть в dl_rules, но нет в dl_responses")

    # 3. Dictionaries: every [dict(...)] in rules must be defined
    dicts_defined = parse_dictionaries_from_rules(dl_rules)
    external_dicts = {"common_yes", "common_no", "otkaz"}
    dict_refs = parse_dict_refs(dl_rules)
    for dref in dict_refs:
        if dref in external_dicts:
            continue
        if dref not in dicts_defined:
            errors.append(f"MISSING_DICTIONARY: [dict({dref})] используется в правилах, но словарь не определён")

    # 4. Dictionaries have entries in user_phrases
    for dict_name, entries in dicts_defined.items():
        if dict_name not in user_phrases.lower():
            warns.append(f"DICT_NO_PHRASES: Словарь «{dict_name}» ({len(entries)} стемм), но нет секции в user_phrases.md")

    # 5. %that_anchor values match anchor registry
    anchor_registry = parse_anchor_registry(arch)
    used_anchors = parse_that_anchors(dl_resp)
    special_anchors = {"CIAS"}
    for anchor in used_anchors:
        if anchor in special_anchors:
            continue
        if anchor not in anchor_registry:
            errors.append(f"UNKNOWN_ANCHOR: %that_anchor=\"{anchor}\" используется, но нет в реестре якорей (§4)")

    # 6. [@goto] targets reference valid nodes
    goto_targets = parse_gotos(dl_resp)
    all_known_nodes = set(resp_nodes) | set(rule_nodes)
    for target in goto_targets:
        if target not in all_known_nodes:
            found = any(target.lower() == n.lower() for n in all_known_nodes)
            if found:
                warns.append(f"GOTO_CASE_MISMATCH: [@goto(\"{target}\")] найден с другим регистром")
            else:
                errors.append(f"GOTO_NOT_FOUND: [@goto(\"{target}\")] целевой узел не существует")

    # 7. EVENT UUIDs in dl_rules are valid format
    event_patterns = re.findall(r'EVENT\s+([0-9a-f-]+)\s+\*', dl_rules)
    uuid_re = re.compile(r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$')
    for uuid in event_patterns:
        if not uuid_re.match(uuid):
            errors.append(f"INVALID_UUID: EVENT UUID {uuid} в dl_rules невалидный формат")

    # 8. Question Setter roots set %that_anchor
    current_node = ""
    has_that_anchor = False
    for line in dl_resp.splitlines():
        m = re.match(r"## Узел:\s*(.+)", line)
        if m:
            current_node = m.group(1).strip()
            has_that_anchor = False
            continue
        if "%that_anchor=" in line:
            has_that_anchor = True
        if line.strip() == "---":
            if "корень" in current_node:
                if not has_that_anchor:
                    warns.append(f"NO_ANCHOR_ROOT: Узел «{current_node}» (корень) не устанавливает %that_anchor")
            current_node = ""

    # 9. @Inc variable consistency
    inc_refs = re.findall(r'@Inc\("(\w+)"\)', dl_resp)
    var_assigns = re.findall(r'%([\w_]+)=', dl_resp)
    for var in inc_refs:
        if var not in var_assigns:
            warns.append(f"VAR_INCREMENT_NO_DECL: [@Inc(\"{var}\")] но переменная %{var} не инициализируется")

    # 10. Female voice check
    if "был" in dl_resp.lower().replace("была", "") and "была" not in dl_resp.lower():
        warns.append("VOICE_GENDER: Найдено «был», но нет «была» (женский голос)")

    # Report
    for e in errors:
        print(f"[ERROR] {e}")
    for w in warns:
        print(f"[WARN] {w}")

    nerr = len(errors)
    nwarn = len(warns)

    # Extract state variables manifest for packer
    variables: dict[str, str] = {}
    for m in re.finditer(r'%([a-zA-Z_]\w*)=', dl_resp):
        variables[m.group(1)] = "assigned"
    for m in re.finditer(r'@Inc\("([a-zA-Z_]\w*)"', dl_resp):
        variables[m.group(1)] = variables.get(m.group(1), "incremented")

    if nerr == 0:
        if nwarn:
            print(f"\nOK: проверка пройдена ({nwarn} предупреждений).")
        else:
            print("\nOK: проверка пройдена.")

        # Output variable manifest as JSON to stdout
        if variables:
            manifest = json.dumps({
                "variables": list(variables.keys()),
                "details": variables,
            }, ensure_ascii=False)
            print(f"\nMANIFEST:variables:{manifest}")
        return 0
    else:
        print(f"\nFAILED: ошибок — {nerr}, предупреждений — {nwarn}.")
        return 1


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description="Валидация md-файлов проекта")
    parser.add_argument(
        "project_dir",
        type=Path,
        help="Путь к папке проекта (например work/FPK)",
    )
    args = parser.parse_args()

    pdir = args.project_dir if args.project_dir.is_absolute() else ROOT / args.project_dir
    ret = run(pdir)

    # If validation passed, also output manifest to a file
    if ret == 0:
        manifest_path = pdir / "manifest.json"
        variables: dict[str, str] = {}
        dl_resp = (pdir / "dl_responses_result.md").read_text(encoding="utf-8")
        for m in re.finditer(r'%([a-zA-Z_]\w*)=', dl_resp):
            variables[m.group(1)] = "assigned"
        for m in re.finditer(r'@Inc\("([a-zA-Z_]\w*)"', dl_resp):
            variables[m.group(1)] = variables.get(m.group(1), "incremented")
        manifest = {
            "variables": list(variables.keys()),
            "details": variables,
            "dictionaries": list(parse_dictionaries_from_rules(
                (pdir / "dl_rules_result.md").read_text(encoding="utf-8")).keys()),
        }
        manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"\nMANIFEST written to: {manifest_path}")

    return ret


if __name__ == "__main__":
    raise SystemExit(main())