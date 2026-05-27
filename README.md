# Фабрика чат-ботов для ДОС

Многоагентный пайплайн: агенты пишут сценарий на языке DL, скрипты проверяют и упаковывают ZIP для импорта в платформу.

Запуск агентов — через **OpenCode** в VS Code (`opencode.json`, папка `.opencode/`).

## Структура

| Папка | Назначение |
|-------|------------|
| `docs/` | База знаний: синтаксис DL, правила генерации, архитектура ботов |
| `agents/` | Промпты агентов (оркестратор, архитектор, DL-авторы, …) |
| `work/<BotSlug>/` | Артефакты одного бота (см. `work/README.md`) |
| `work/<BotSlug>/output/nodes/` | JSON узлов |
| `work/<BotSlug>/9_PACKAGER__STAGING/` | Сборка перед упаковкой |
| `archives/exported/` | Готовые ZIP для загрузки в ДОС |
| `scripts/` | `prepare_staging.py`, `validate_archive.py`, `pack_archive.py` |

## Быстрый старт

1. Откройте папку `LLM` в VS Code.
2. Запустите конвейер с `agents/1_ORCHESTRATOR.md`.
3. После агентов — упаковка по `agents/9_PACKAGER.md` и `scripts/README.md`.

Успешный пример: 
`archives/exported/JokeBot_prod.zip`,
`archives/exported/NeoCall_Solutions_prod.zip`,
`archives/exported/FPK_prod.zip`.


## Память (обновлять постоянно)

Два MD-файла нужно **регулярно дополнять и править** — иначе при паузе нельзя возобновить работу с нужного места, а агенты повторяют старые ошибки:

| Файл | Что хранит |
|------|------------|
| [`docs/PROJECT_MEMORY.md`](docs/PROJECT_MEMORY.md) | Как устроена фабрика: этапы репозитория, конвейер, критические правила |
| [`docs/FACTORY_PROJECTS_MEMORY.md`](docs/FACTORY_PROJECTS_MEMORY.md) | Состояние **конкретных ботов**: текущий узел, агент, этап, «продолжаем с…» |

**Когда обновлять:** после каждого шага конвейера, при паузе/возобновлении, при смене узла, при замечании пользователя.

**Если пользователь указывает на ошибку** — необходимо не только исправить артефакт, но и **записать урок** в подходящий MD (`docs/G_AGENT_RULES.md`, `docs/D_GENERATION_RULES.md`, промпт агента или секцию «Замечания» в `FACTORY_PROJECTS_MEMORY.md`), чтобы ошибка не повторялась.

**В чате** каждый агент подписывает ответ: «(Архитектор:)…», «(Креативщик:)…» и т.д. — см. `agents/1_ORCHESTRATOR.md`.

## Документация

- Обзор фабрики: `docs/PROJECT_MEMORY.md`
- Прогресс ботов в работе: `docs/FACTORY_PROJECTS_MEMORY.md`
- Документы SSOT: `docs/A_LANGUAGE_SPEC.md` через `docs/G_AGENT_RULES.md`
