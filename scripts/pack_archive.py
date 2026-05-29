# -*- coding: utf-8 -*-
"""
Упаковка каталога staging в ZIP для импорта в ДОС.

Структура staging:
  9_PACKAGER__MANIFEST.json — имя бота, export_basename, project_id (опционально)
  Assistant/{uuid}.json
  Branch/{uuid}.json
  Skill/{short-id}.json
  DialogNode/{short-id}.json
  Dictionary/{short-id}.json  — по необходимости

Пример:
   python pack_archive.py --staging work/<BotSlug>/staging --out archives/exported/<имя>.zip
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from archive_core import pack_staging_to_zip, print_report, validate_staging

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description="Упаковка staging → ZIP ДОС")
    parser.add_argument(
        "--staging",
        type=Path,
        required=True,
        help="Каталог staging (EntityType/*.json + 9_PACKAGER__MANIFEST.json)",
    )
    parser.add_argument(
        "--out",
        type=Path,
        help="Путь к выходному .zip (по умолчанию из manifest.export_basename)",
    )
    parser.add_argument(
        "--no-normalize",
        action="store_true",
        help="Не исправлять key блоков и [@goto] при упаковке",
    )
    parser.add_argument(
        "--validate-only",
        action="store_true",
        help="Только проверить staging, не создавать zip",
    )
    args = parser.parse_args()

    staging = args.staging if args.staging.is_absolute() else ROOT / args.staging

    if args.validate_only:
        pre = validate_staging(staging)
        if not pre.ok:
            print("Staging (без нормализации) не прошёл проверку:")
        return print_report(pre)

    manifest = {}
    mp = staging / "9_PACKAGER__MANIFEST.json"
    if mp.exists():
        manifest = json.loads(mp.read_text(encoding="utf-8"))

    assistants = list((staging / "Assistant").glob("*.json"))
    assistant_id = json.loads(assistants[0].read_text(encoding="utf-8"))["id"]
    basename = manifest.get("export_basename", "bot_master")
    # Инцидент 2026-05-29: UUID ассистента убран из имени архива.
    # Каноническое имя — только export_basename (совпадает с названием папки в work/).
    default_name = f"{basename}.zip"
    out = args.out or (ROOT / "archives" / "exported" / default_name)
    out = out if out.is_absolute() else ROOT / out

    report = pack_staging_to_zip(
        staging, out, normalize=not args.no_normalize
    )
    if not report.ok:
        return print_report(report)

    print(f"Архив создан: {out}")
    # повторная проверка zip
    from archive_core import validate_zip

    post = validate_zip(out)
    if not post.ok:
        print("Предупреждение: zip создан, но самопроверка нашла проблемы:")
        return print_report(post)

    print("ZIP прошёл самопроверку.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
