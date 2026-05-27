# -*- coding: utf-8 -*-
"""Merge JSON dictionaries from raw_dicts into COMMON_DICTIONARIES.md and delete processed files."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "docs" / "reference" / "raw_dicts"
OUT_MD = ROOT / "docs" / "reference" / "COMMON_DICTIONARIES.md"

MEANING_PLACEHOLDER = "— смысл определить Оркестратору —"


def load_json_dict(filepath: Path):
    """Extract name and lines from a raw dictionary JSON. Description is handled by the Orchestrator."""
    data = json.loads(filepath.read_text(encoding="utf-8"))
    item = data[0] if isinstance(data, list) else data

    name = item.get("name", "")
    blocks = item.get("content", {}).get("blocks", [])
    lines = [
        b.get("text", "")
        for b in blocks
        if b.get("text") and not (b.get("data") or {}).get("inactive")
    ]
    return name, lines


def parse_existing_md(content: str):
    """Parse existing MD into registry entries + section dict."""
    registry = []
    table_match = re.search(r"## Реестр словарей\n\n(\|.*\n(?:\|.*\n)+)", content)
    if table_match:
        for line in table_match.group(1).strip().split("\n")[2:]:
            parts = [p.strip() for p in line.split("|")[1:-1]]
            if len(parts) >= 3:
                registry.append({"name": parts[0].strip("` "), "meaning": parts[1], "lines": parts[2]})

    sections = {}
    for m in re.finditer(r"## `([^`]+)`\n\n(.*?)(?=\n## `|\Z)", content, re.DOTALL):
        sections[m.group(1)] = m.group(2)

    return registry, sections


def build_table(registry: list) -> str:
    """Build the registry markdown table."""
    lines = [
        "## Реестр словарей",
        "",
        "| Словарь | Смысл | Строк |",
        "|---------|-------|-------|"
    ]
    for e in registry:
        lines.append(f"| `{e['name']}` | {e['meaning']} | {e['lines']} |")
    lines.append("")
    return "\n".join(lines)


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


def main():
    if not RAW_DIR.exists():
        print("No raw_dicts directory found.")
        return

    json_files = list(RAW_DIR.glob("*.json"))
    if not json_files:
        print("No JSON files to process.")
        return

    md_content = OUT_MD.read_text(encoding="utf-8")
    registry, sections = parse_existing_md(md_content)
    existing_names = {e["name"] for e in registry}

    new_dicts = []
    new_sections = []
    processed = []

    for jf in json_files:
        try:
            name, lines = load_json_dict(jf)
            if not name:
                print(f"  Skip {jf.name}: no name.")
                continue

            if name in existing_names or name in sections:
                print(f"  Skip {jf.name}: '{name}' already in MD.")
                processed.append(jf)
                continue

            # Placeholders — Orchestrator will analyze and fill in real "Смысл"
            meaning = MEANING_PLACEHOLDER
            registry.append({"name": name, "meaning": meaning, "lines": str(len(lines))})
            new_dicts.append({"name": name, "lines": lines})
            new_sections.append(build_section(name, meaning, lines))
            print(f"  Added '{name}' ({len(lines)} lines).")
            processed.append(jf)
        except Exception as e:
            print(f"  Error {jf.name}: {e}")

    if not new_dicts:
        return

    # Rebuild MD: header → new table → body after old table → new sections
    table_pat = re.compile(r"## Реестр словарей\n\n\|.*\n(?:\|.*\n)*")
    t_match = table_pat.search(md_content)
    before = md_content[:t_match.start()] if t_match else ""
    after = md_content[t_match.end():] if t_match else md_content

    result = before + build_table(registry) + after + "".join(new_sections)
    OUT_MD.write_text(result, encoding="utf-8")
    print(f"\nUpdated {OUT_MD} ({OUT_MD.stat().st_size} bytes)")

    for f in processed:
        if f.exists():
            f.unlink()
            print(f"  Deleted {f.name}")

    # Return metadata for Orchestrator to analyze
    print(f"\nDone. {len(new_dicts)} new dict(s) added with placeholder meaning.")
    print(f"Orchestrator — please analyze and fill 'Смысл' for:")
    for d in new_dicts:
        sample = "\n".join(d["lines"][:10])
        print(f"  `{d['name']}` ({d['lines']!r} …)")


if __name__ == "__main__":
    main()
