# -*- coding: utf-8 -*-
"""Export popular shared dictionaries from example archives to docs/reference/COMMON_DICTIONARIES.md."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = ROOT / "archives" / "examples" / "_extracted"
OUT = ROOT / "docs" / "reference" / "COMMON_DICTIONARIES.md"

NAMES = [
    "common_yes",
    "common_no",
    "common_want_1_pres",
    "otkaz",
    "soglasen",
    "dontwant",
    "common_change",
    "common_how",
    "day",
    "month",
    "year",
    "switchdate",
    "time",
]

DESCRIPTIONS = {
    "common_yes": "Согласие, подтверждение («да», «верно», «именно так»).",
    "common_no": "Отрицание без жёсткого отказа.",
    "common_want_1_pres": "Желание в настоящем времени («хочу», «нужно», «надо»).",
    "otkaz": "Отказ, не хочу, не надо.",
    "soglasen": "Согласие разговорное («согласен», «ладно», «ок»).",
    "dontwant": "Не хочу / не нужно.",
    "common_change": "Смена, перенос, изменение (дата/время).",
    "common_how": "Вопросы «как» (инструкции, способ).",
    "day": "Числа и словоформы дня месяца.",
    "month": "Названия месяцев.",
    "year": "Год, «год», двузначные/четырёхзначные формы.",
    "switchdate": "Относительные даты: завтра, послезавтра, через неделю.",
    "time": "Время суток, часы, «в … часов».",
}


def load_all_dicts():
    merged = {}
    if not EXAMPLES.exists():
        return merged
    for bot_dir in EXAMPLES.iterdir():
        if not bot_dir.is_dir():
            continue
        inner_dirs = [p for p in bot_dir.iterdir() if p.is_dir()]
        if not inner_dirs:
            continue
        dict_dir = inner_dirs[0] / "Dictionary"
        if not dict_dir.exists():
            continue
        for f in dict_dir.glob("*.json"):
            d = json.loads(f.read_text(encoding="utf-8"))
            name = d.get("name")
            if not name:
                continue
            blocks = d.get("content", {}).get("blocks", [])
            lines = [
                b.get("text", "")
                for b in blocks
                if b.get("text") and not (b.get("data") or {}).get("inactive")
            ]
            if name not in merged or len(lines) > len(merged[name]):
                merged[name] = lines
    return merged


def main():
    merged = load_all_dicts()
    parts = [
        "# Популярные общие словари (переиспользование)",
        "",
        "Готовые словари из успешных голосовых обзвонщиков (эталоны в `archives/examples/`).",
        "**DL-автор:** перед созданием нового словаря с тем же смыслом проверьте этот файл —",
        "копируйте имя и содержимое, не изобретайте синонимы с нуля.",
        "",
        "Правила оформления: `docs/D_GENERATION_RULES.md`, `docs/A_LANGUAGE_SPEC.md` (раздел «Словари»).",
        "В правилах узла: `[dict(common_yes)]`, в ответах с нормализацией: `[&dict(last_names, norm)]`.",
        "",
        "---",
        "",
    ]
    for name in NAMES:
        lines = merged.get(name, [])
        desc = DESCRIPTIONS.get(name, "")
        parts.append(f"## `{name}`")
        parts.append("")
        if desc:
            parts.append(desc)
            parts.append("")
        parts.append(f"Строк в словаре: {len(lines)}.")
        parts.append("")
        parts.append("```text")
        parts.extend(lines if lines else ["# нет данных в archives/examples — дополните из экспорта"])
        parts.append("```")
        parts.append("")
    OUT.write_text("\n".join(parts), encoding="utf-8")
    print(f"Wrote {OUT} ({OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
