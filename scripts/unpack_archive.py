# -*- coding: utf-8 -*-
"""
Распаковка эталонного ZIP в каталог staging (для правок и повторной упаковки).

  python unpack_archive.py --zip archives/exported/<имя>_prod.zip --out work/<BotSlug>/staging
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[2]


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description="ZIP ДОС → staging")
    parser.add_argument("--zip", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()

    zip_path = args.zip if args.zip.is_absolute() else ROOT / args.zip
    out_dir = args.out if args.out.is_absolute() else ROOT / args.out
    out_dir.mkdir(parents=True, exist_ok=True)

    with ZipFile(zip_path) as zf:
        wrapper = next(
            n.split("/")[0]
            for n in zf.namelist()
            if "-master-" in n and "/" in n
        )
        assistant_name = ""
        assistant_id = wrapper.split("-master-")[0]
        for n in zf.namelist():
            if not n.startswith(wrapper + "/") or not n.endswith(".json"):
                continue
            rel = n[len(wrapper) + 1 :]
            parts = rel.split("/")
            if len(parts) != 2:
                continue
            entity_dir, fname = parts
            target_dir = out_dir / entity_dir
            target_dir.mkdir(parents=True, exist_ok=True)
            raw = zf.read(n)
            obj = json.loads(raw)
            (target_dir / fname).write_bytes(raw)
            if entity_dir == "Assistant":
                assistant_name = obj.get("name", "")

        meta = json.loads(zf.read("metadata.json"))
        manifest = {
            "export_basename": assistant_name.replace(" ", "_") or "bot",
            "assistant_id": assistant_id,
            "lc_version": meta.get("lc_version"),
            "source_zip": zip_path.name,
        }
        (out_dir / "9_PACKAGER__MANIFEST.json").write_text(
            json.dumps(manifest, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    print(f"Staging записан в: {out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
