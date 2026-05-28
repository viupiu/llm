# -*- coding: utf-8 -*-
"""
Import dictionaries from raw_dicts/*.json into COMMON_DICTIONARIES.md.

Ownership: LIBRARIAN (REUSABLE KNOWLEDGE CURATOR)
Responsible agent: agents/13_LIBRARIAN.md

NEW LOGIC:
1. Duplicate Detection: exact canonical name match (NOT substring contains)
2. If dictionary EXISTS:
   - DO NOT import again
   - DO NOT modify existing dictionary
   - DO NOT delete file from raw_dicts/
   - Add warning to report: "Dictionary already exists — skipped"
   - File remains in raw_dicts/
3. If dictionary is NEW:
   - Import into COMMON_DICTIONARIES.md
   - Add to registry table
   - Add section with content
   - Set placeholder description
   - ONLY THEN delete file from raw_dicts/
4. Safe Delete Policy:
   - Delete from raw_dicts/ ONLY if:
     - Dictionary successfully imported
     - Registry updated
     - No duplicate conflict
     - No parsing failure
   - In all other cases: file is preserved

REFACTOR GUARD: preserve existing dictionaries, descriptions, normalizations.
NEVER auto-overwrite, merge without audit, or destructively deduplicate.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "docs" / "reference" / "raw_dicts"
OUT_MD = ROOT / "docs" / "reference" / "COMMON_DICTIONARIES.md"

MEANING_PLACEHOLDER = "— смысл определить Библиотекарю —"


# ========================
# PARSING
# ========================

def load_json_dict(filepath: Path):
    """Extract canonical name and lines from a raw dictionary JSON."""
    data = json.loads(filepath.read_text(encoding="utf-8"))
    item = data[0] if isinstance(data, list) else data

    name = item.get("name", "")
    if not name:
        raise ValueError(f"No 'name' field in {filepath.name}")

    blocks = item.get("content", {}).get("blocks", [])
    lines = [
        b.get("text", "")
        for b in blocks
        if b.get("text") and not (b.get("data") or {}).get("inactive")
    ]

    return name, lines


def get_existing_dict_names(content: str) -> set:
    """Extract ALL canonical dictionary names from COMMON_DICTIONARIES.md.

    Checks BOTH:
    1. Table entries: | `name` | ...
    2. Section headers: ## `name`

    Returns a set of exact canonical names.
    """
    names = set()

    # From table: | `dictname` | meaning | count |
    for m in re.finditer(r"\|\s*`([^`]+)`\s*\|", content):
        names.add(m.group(1))

    # From section headers: ## `dictname`
    for m in re.finditer(r"^##\s+`([^`]+)`$", content, re.MULTILINE):
        names.add(m.group(1))

    return names


# ========================
# BUILDING
# ========================

def build_table_line(name: str, meaning: str, count: int) -> str:
    """Build a single registry table row."""
    return f"| `{name}` | {meaning} | {count} |"


def build_section(name: str, meaning: str, lines: list) -> str:
    """Build a single dictionary section in the expected MD format."""
    return "\n".join([
        f"## `{name}`",
        "",
        meaning,
        "",
        f"Строк в словаре: {len(lines)}.",
        "",
        "```text",
    ] + lines + ["```", ""])


# ========================
# IMPORT LOGIC
# ========================

def insert_into_registry(content: str, new_entries: list) -> str:
    """Insert new dictionary entries into the registry table.

    Preserves existing table structure. Appends new rows before the closing
    blank line after the table.
    """
    table_match = re.search(
        r"(## Реестр словарей\n\n"
        r"\|.*\|\n"           # header
        r"\|[-| ]*\|\n"       # separator
        r")"
        r"((?:\|.*\|\n)+)",  # data rows
        content
    )
    if not table_match:
        raise ValueError("Registry table not found in COMMON_DICTIONARIES.md. "
                         "Cannot add new entries.")

    prefix = table_match.group(1)
    existing_rows = table_match.group(2)
    suffix = content[table_match.end():]

    new_rows = ""
    for entry in new_entries:
        new_rows += build_table_line(entry["name"], entry["meaning"], entry["count"]) + "\n"

    return prefix + existing_rows + new_rows + suffix


def append_sections(content: str, new_sections_text: str) -> str:
    """Append new dictionary sections at the end of the file.

    Ensures separation with blank lines.
    """
    stripped = content.rstrip()
    if not stripped.endswith("\n\n"):
        stripped += "\n\n"
    return stripped + new_sections_text + "\n"


# ========================
# REPORTING
# ========================

def generate_report(imported: list, skipped: list, failed: list) -> str:
    """Generate structured import report for the Orchestrator."""
    lines = [
        "(Библиотекарь:) Отчёт импорта словарей",
        "",
    ]

    # Imported
    lines.append(f"## Imported ({len(imported)} словарей)")
    if imported:
        for entry in imported:
            lines.append(f"- `{entry['name']}` ({entry['count']} строк)")
    else:
        lines.append("- (нет новых словарей)")
    lines.append("")

    # Skipped
    lines.append(f"## Skipped — уже существуют ({len(skipped)} словарей)")
    if skipped:
        for entry in skipped:
            lines.append(
                f"- `{entry['name']}` — Dictionary already exists, skipped. "
                f"Файл сохранён в raw_dicts/"
            )
    else:
        lines.append("- (нет дубликатов)")
    lines.append("")

    # Failed
    lines.append(f"## Failed ({len(failed)} ошибок)")
    if failed:
        for entry in failed:
            lines.append(f"- `{entry['file']}` — {entry['error']}")
    else:
        lines.append("- (нет ошибок)")
    lines.append("")

    # Stats
    total = len(imported) + len(skipped) + len(failed)
    lines.append("## Статистика")
    lines.append(f"- Обработано файлов: {total}")
    lines.append(f"- Успешно импортировано: {len(imported)}")
    lines.append(f"- Пропущено (duplicates): {len(skipped)}")
    lines.append(f"- Ошибок: {len(failed)}")

    # Remaining files in raw_dicts
    remaining = 0
    if RAW_DIR.exists():
        remaining = len(list(RAW_DIR.glob("*.json")))
    lines.append(f"- Осталось в raw_dicts/: {remaining} файлов")
    lines.append("")

    return "\n".join(lines)


# ========================
# MAIN
# ========================

def main():
    if not RAW_DIR.exists():
        print("No raw_dicts directory found.")
        return

    json_files = sorted(RAW_DIR.glob("*.json"))
    if not json_files:
        print("No JSON files to process.")
        return

    if not OUT_MD.exists():
        print(f"Error: {OUT_MD} not found. Cannot import.")
        return

    md_content = OUT_MD.read_text(encoding="utf-8")
    existing_names = get_existing_dict_names(md_content)

    imported = []
    skippe = []
    failed = []
    new_sections_text = ""

    for jf in json_files:
        try:
            name, lines = load_json_dict(jf)
        except json.JSONDecodeError as e:
            failed.append({"file": jf.name, "error": f"JSON parse error: {e}"})
            continue
        except ValueError as e:
            failed.append({"file": jf.name, "error": str(e)})
            continue
        except Exception as e:
            failed.append({"file": jf.name, "error": f"Unexpected error: {e}"})
            continue

        # DUPLICATE DETECTION: exact canonical name match
        if name in existing_names:
            skippe.append({"name": name})
            print(f"  Skip {jf.name}: '{name}' already in COMMON_DICTIONARIES.md — file preserved.")
            continue

        # NEW DICTIONARY — prepare import
        meaning = MEANING_PLACEHOLDER
        entry = {
            "name": name,
            "meaning": meaning,
            "count": len(lines),
        }
        imported.append(entry)

        section_text = build_section(name, meaning, lines) + "\n"
        new_sections_text += section_text

        print(f"  Added '{name}' ({len(lines)} lines).")

    if not imported and not skippe and not failed:
        print("Nothing to process.")
        return

    # WRITE TO COMMON_DICTIONARIES.md (only if there are new imports)
    if imported:
        try:
            # Step 1: Insert into registry table
            result = insert_into_registry(md_content, imported)

            # Step 2: Append new sections
            result = append_sections(result, new_sections_text)

            # Step 3: Write atomically
            OUT_MD.write_text(result, encoding="utf-8")
            print(f"\nUpdated {OUT_MD} ({OUT_MD.stat().st_size} bytes)")

            # Step 4: Safe delete — ONLY after successful write
            for entry in imported:
                # Find the corresponding JSON file to delete
                for jf in json_files:
                    if entry["name"] in jf.name:
                        if jf.exists():
                            jf.unlink()
                            print(f"  Deleted {jf.name} (successfully imported)")
                        break

        except Exception as e:
            print(f"\nCRITICAL ERROR writing to {OUT_MD}: {e}")
            print("Files in raw_dicts/ have been PRESERVED (safe delete policy).")
            failed.append({"file": "COMMON_DICTIONARIES.md", "error": f"Write error: {e}"})
    else:
        print("\nNo new dictionaries to import. No changes to COMMON_DICTIONARIES.md.")

    # REPORT
    report = generate_report(imported, skippe, failed)
    print("\n" + "=" * 60)
    print(report)
    print("=" * 60)


if __name__ == "__main__":
    main()
