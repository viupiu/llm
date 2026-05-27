# Скрипты упаковки и валидации (ДОС)

Упаковщик и валидатор — **Python-скрипты**, не LLM-агенты. Агенты пишут в `work/<BotSlug>/`; скрипты собирают ZIP в `archives/exported/`. См. `work/README.md`.

## Быстрый старт (один узел)

Из корня проекта `LLM/`:

```powershell
cd scripts

# 1. Собрать 9_PACKAGER__STAGING из узла + словарей из 4_RULES_AUTHOR__RULES_AND_DICTIONARIES.md
python prepare_staging.py `
  --node ..\work\GenderCheck_Bot\output\nodes\<id>.json `
  --dict-md ..\work\GenderCheck_Bot\4_RULES_AUTHOR__RULES_AND_DICTIONARIES.md `
  --out ..\work\GenderCheck_Bot\9_PACKAGER__STAGING `
  --assistant-name "Анекдот-Мастер" `
  --skill-name "Выбор категории" `
  --export-basename "JokeBot"

# 2. Проверить артефакты проекта
python validate_archive.py ..\work\GenderCheck_Bot

# 3. Упаковать ZIP для импорта в ДОС
python pack_archive.py --staging ..\work\GenderCheck_Bot\9_PACKAGER__STAGING --out ..\archives\exported\<имя>_prod.zip
```

## Команды

| Скрипт | Назначение |
|--------|------------|
| `prepare_staging.py` | Assistant + Branch + Skill + DialogNode + Dictionary из артефактов агентов |
| `validate_archive.py` | Проверка md-артефактов проекта (positional: `work/<BotSlug>`) |
| `pack_archive.py` | Staging → ZIP (`--staging <path>`, нормализует `[@goto]`, ключи блоков) |
| `unpack_archive.py` | ZIP из `archives/exported/` → 9_PACKAGER__STAGING для правок |
| `build_full_staging.py` | Все узлы из `output/nodes/` + словари из `4_RULES_AUTHOR__RULES_AND_DICTIONARIES.md` |
| `generate_all_nodes.py` | MD-артефакты → JSON узлов (`conditions` из блока `Условия:` в responses) |
| `merge_raw_dictionaries.py` | JSON-словари из `docs/reference/raw_dicts/` → `docs/reference/COMMON_DICTIONARIES.md` (автоочистка) |

## Структура 9_PACKAGER__STAGING

```
work/<BotSlug>/9_PACKAGER__STAGING/
  9_PACKAGER__MANIFEST.json
  Assistant/{full-uuid}.json
  Branch/{full-uuid}.json
  Skill/{short-id}.json
  DialogNode/{short-id}.json
  Dictionary/{short-id}.json   # по одному файлу на словарь
```

Минимальный состав и формат ID — в `docs/D_GENERATION_RULES.md` и `docs/F_PLATFORM_API.md`.

## `creator` и даты

Скопируйте **creator** из любого вашего экспорта (`Assistant/....json` → поле `creator`) и передайте в manifest или CLI:

```powershell
python prepare_staging.py ... --creator "a04359b1-6422-4e56-9792-bf13f40afb9b"
```

Даты: `2026-05-25T06:54:24.862973` (без `+03:00`). Скрипт нормализует их при упаковке.

## Словари: не терять канон

В md Автора ДЛ канон идёт **отдельной строкой** (`IT`, `Москва`), синонимы — `=>...`.  
`prepare_staging.py` переносит **все** строки тела словаря в `content.blocks`.  
Валидатор выдаст `DICT_NO_CANON`, если в JSON остались только `=>`.

## Объединение словарей

Словари из `docs/reference/raw_dicts/` можно слить в `COMMON_DICTIONARIES.md`:

```powershell
python merge_raw_dictionaries.py
```

Скрипт:
- Читает все `*.json` из `raw_dicts/`
- Извлекает имя (`name`) и строки (`content.blocks[].text`)
- Обновляет таблицу реестра
- Добавляет новые секции в конец файла
- Удаляет обработанные JSON-файлы

## Что проверяет валидатор

- `metadata.json` с полями `lc_version`, `timestamp`, `options`
- `timestamp` / `created` без таймзоны; `creator` не `00000000-...`
- Обёртка `{assistant_id}-master-{40 hex}`
- Нет вложенных `.zip`, нет папки `NamesEntity`
- Формат ID и имён файлов `{id}.json`
- `skill_id`, `assistant_id`, ссылки `[dict(name)]`
- Запрет `[goto(...)]` — только `[@goto("...")]`
