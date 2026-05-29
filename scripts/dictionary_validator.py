# -*- coding: utf-8 -*-
"""
Dictionary Validator — детерминированная проверка целостности словарей.

Находит ошибки ДО сборки, без LLM, без эвристик, только строгие проверки.

Использование:
    python dictionary_validator.py --rules MD_path --ref-dir REF_path

Возвращает exit code 0 при успехе, 1 при наличии ERROR.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import List, Tuple


# --- Парсинг ---

RE_DICT_REF = re.compile(r"\[dict\(([^)]+)\)\]")
RE_DICT_DEF = re.compile(r"^##\s*Словарь:\s*([a-z][a-z0-9_]*)\s*$")
RE_INCLUDE_REF = re.compile(r"--include\((\w[\w_]*)\s*\)")
RE_CATALOG_NAME = re.compile(r"^\|\s*`([^`]+)`\s*\|")


def load_common_dictionary_names(catalog_path: Path) -> set:
    """
    Извлекает имена словарей из реестра COMMON_DICTIONARIES.md.
    Формат каталога:
        | `common_yes` | ...
    Возвращает все уникальные имена из первой колонки таблицы.
    """
    names = set()
    if not catalog_path.exists():
        return names
    text = catalog_path.read_text(encoding="utf-8")
    for line in text.splitlines():
        m = RE_CATALOG_NAME.match(line.strip())
        if m:
            names.add(m.group(1))
    return names


def read_reference_dictionary(ref_file: Path) -> List[str]:
    """Извлекает строки тела из референсного файла словаря.

    Формат:
        #name
        description
        Строк в словаре: N.
        ```text
        line1
        =>line2
        ...
        ```
    """
    text = ref_file.read_text(encoding="utf-8")
    lines = text.splitlines()

    in_code = False
    body: List[str] = []
    for line in lines:
        stripped = line.strip()
        if not in_code:
            if stripped.startswith("```"):
                in_code = True
            continue
        if stripped.startswith("```"):
            break
        body.append(stripped)

    return body


def parse_rules_file(rules_path: Path) -> Tuple[
    dict,  # name -> list[str] (defined dictionaries: name -> body lines)
    set,  # referenced dictionary names
    dict,  # name -> set of included names
    list,  # all `## Словарь: name` occurrences for duplicate check
]:
    """Парсит файл правил и извлекает:
    - Определения словарей (имя -> строки тела)
    - Ссылки на словари [dict(name)]
    - Include-зависимости --include(name)
    """
    text = rules_path.read_text(encoding="utf-8")
    lines = text.splitlines()

    defined: dict = {}
    referenced: set = set()
    includes: dict = {}  # dict_name -> set of included names
    definition_names_ordered: list = []

    for line in lines:
        for m in RE_DICT_REF.finditer(line):
            referenced.add(m.group(1))

    i = 0
    while i < len(lines):
        line = lines[i]
        m = RE_DICT_DEF.match(line.strip())
        if m:
            name = m.group(1)
            definition_names_ordered.append(name)

            if name not in defined:
                i += 1
                body: List[str] = []
                include_deps: set = set()
                while i < len(lines):
                    t = lines[i].strip()
                    if not t:
                        i += 1
                        continue
                    if RE_DICT_DEF.match(t):
                        break
                    if t.startswith("## ") or t.startswith("#"):
                        if t.startswith("## Узел:") or t.startswith("### ") or t.startswith("## "):
                            break
                    for inc_m in RE_INCLUDE_REF.finditer(t):
                        include_deps.add(inc_m.group(1))
                    if RE_INCLUDE_REF.search(t):
                        i += 1
                        continue
                    if t.startswith("*") or t.startswith("[") or t.startswith("{"):
                        i += 1
                        continue
                    body.append(t)
                    i += 1
                defined[name] = body
                includes[name] = include_deps
            else:
                i += 1
            continue
        i += 1

    return defined, referenced, includes, definition_names_ordered


# --- Проверки ---

class ValidationResult:
    def __init__(self):
        self.errors: List[str] = []
        self.warnings: List[str] = []

    @property
    def has_errors(self) -> bool:
        return len(self.errors) > 0


def check_1_missing(res: ValidationResult, referenced: set, defined: dict) -> None:
    """Проверка 1. Отсутствующий словарь.
    Каждый [dict(name)] должен иметь определение ## Словарь: name.
    """
    for name in sorted(referenced):
        if name not in defined:
            res.errors.append(f"ERROR: Dictionary '{name}' is referenced but not defined.")


def check_2_unknown(res: ValidationResult, defined: dict, referenced: set,
                    ref_dir: Path, common_names: set) -> None:
    """Проверка 2. Неизвестный словарь.
    Для словарей, перечисленных в COMMON_DICTIONARIES.md (общие словари),
    проверяем существование референсного файла в библиотеке.
    Локальные словари проекта пропускаются.
    """
    all_checked = set()
    for name in sorted(set(defined.keys()) | referenced):
        if name in all_checked:
            continue
        all_checked.add(name)
        if name not in common_names:
            continue
        ref_file = ref_dir / f"{name}.md"
        if not ref_file.exists():
            res.errors.append(
                f"ERROR: Dictionary '{name}' does not exist in reference library "
                f"({ref_file})."
            )


def check_3_truncated(res: ValidationResult, defined: dict, ref_dir: Path,
                      common_names: set) -> None:
    """Проверка 3. Усечённый словарь.
    Для общих словарей (из COMMON_DICTIONARIES.md) сравнивает содержимое
    с оригиналом из библиотеки. Локальные словари проекта skip-аются.
    """
    for name in sorted(defined.keys()):
        if name not in common_names:
            continue
        ref_file = ref_dir / f"{name}.md"
        if not ref_file.exists():
            continue
        ref_lines = read_reference_dictionary(ref_file)
        local_lines = defined[name]
        if ref_lines != local_lines:
            missing = []
            extra = []
            changed = []
            for i, (r, l) in enumerate(zip(ref_lines, local_lines)):
                if r != l:
                    changed.append((i, r, l))
            if len(ref_lines) > len(local_lines):
                missing = ref_lines[len(local_lines):]
            elif len(local_lines) > len(ref_lines):
                extra = local_lines[len(ref_lines):]

            detail_parts = []
            if len(ref_lines) != len(local_lines):
                detail_parts.append(
                    f"expected {len(ref_lines)} lines, got {len(local_lines)}"
                )
            if changed:
                detail_parts.append(f"{len(changed)} line(s) differ")
            if missing:
                detail_parts.append(f"{len(missing)} line(s) missing at end")
            if extra:
                detail_parts.append(f"{len(extra)} line(s) extra at end")
            detail = "; ".join(detail_parts)
            res.errors.append(
                f"ERROR: Dictionary '{name}' differs from reference version "
                f"({detail})."
            )


def check_4_include(res: ValidationResult, includes: dict, defined: dict) -> None:
    """Проверка 4. Include-зависимости.
    Каждый --include(other) должен иметь определение ## Словарь: other.
    """
    all_defined_names = set(defined.keys())
    for dict_name in sorted(includes.keys()):
        for inc_name in sorted(includes[dict_name]):
            if inc_name not in all_defined_names:
                res.errors.append(
                    f"ERROR: Included dictionary '{inc_name}' (required by "
                    f"'{dict_name}') is missing."
                )


def check_5_unused(res: ValidationResult, defined: dict, referenced: set) -> None:
    """Проверка 5. Невостребованные словари.
    Словари, определённые в файле, но нигде не используемые через [dict()].
    Это WARNING, не ERROR.
    """
    for name in sorted(defined.keys()):
        if name not in referenced:
            res.warnings.append(
                f"WARNING: Dictionary '{name}' is defined but never referenced "
                f"via [dict()]."
            )


def check_6_duplicates(res: ValidationResult, definition_names_ordered: list) -> None:
    """Проверка 6. Дубликаты словарей.
    Если одно имя словаря определено несколько раз.
    """
    seen: dict = {}
    for name in definition_names_ordered:
        if name not in seen:
            seen[name] = 0
        seen[name] += 1

    for name in sorted(seen.keys()):
        if seen[name] > 1:
            res.errors.append(
                f"ERROR: Dictionary '{name}' defined {seen[name]} times "
                f"(expected: 1)."
            )


# --- Основная логика ---

def validate(rules_path: Path, ref_dir: Path, catalog_path: Path) -> ValidationResult:
    """Запускает все 6 проверок и возвращает результат."""
    res = ValidationResult()

    if not rules_path.exists():
        res.errors.append(f"ERROR: Rules file not found: {rules_path}")
        return res

    common_names = load_common_dictionary_names(catalog_path)
    defined, referenced, includes, definition_names_ordered = parse_rules_file(rules_path)

    check_1_missing(res, referenced, defined)
    check_2_unknown(res, defined, referenced, ref_dir, common_names)
    check_3_truncated(res, defined, ref_dir, common_names)
    check_4_include(res, includes, defined)
    check_5_unused(res, defined, referenced)
    check_6_duplicates(res, definition_names_ordered)

    return res


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(
        description="Dictionary Validator — строгая детерминированная "
                    "проверка целостности словарей"
    )
    parser.add_argument(
        "--rules",
        type=Path,
        required=True,
        help="Путь к файлу 3_RULES_AUTHOR__RULES_AND_DICTIONARIES.md",
    )
    parser.add_argument(
        "--ref-dir",
        type=Path,
        required=True,
        help="Путь к docs/reference/dictionaries/",
    )
    parser.add_argument(
        "--catalog",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "docs" / "reference" / "COMMON_DICTIONARIES.md",
        help="Путь к реестру COMMON_DICTIONARIES.md (авто-определение по умолчанию)",
    )
    args = parser.parse_args()

    rules_path = args.rules if args.rules.is_absolute() else Path.cwd() / args.rules
    ref_dir = args.ref_dir if args.ref_dir.is_absolute() else Path.cwd() / args.ref_dir
    catalog_path = args.catalog if args.catalog.is_absolute() else Path.cwd() / args.catalog

    if not rules_path.exists():
        print(f"ERROR: File not found: {rules_path}", file=sys.stderr)
        return 1

    if not ref_dir.is_dir():
        print(f"ERROR: Directory not found: {ref_dir}", file=sys.stderr)
        return 1

    print(f"=== Dictionary Validator ===")
    print(f"Rules file  : {rules_path}")
    print(f"Ref directory: {ref_dir}")
    print(f"Catalog     : {catalog_path}")
    print()

    res = validate(rules_path, ref_dir, catalog_path)

    if res.warnings:
        for w in res.warnings:
            print(f"  {w}")

    if res.errors:
        print()
        for e in res.errors:
            print(f"  {e}")

    print()
    print(f"Errors   : {len(res.errors)}")
    print(f"Warnings : {len(res.warnings)}")
    print()

    if res.has_errors:
        print("RESULT: FAILED — build must be aborted.")
        return 1
    else:
        print("RESULT: PASSED")
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
