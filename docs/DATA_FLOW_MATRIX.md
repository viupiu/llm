# Матрица потоков данных (Data Flow Matrix)

Единый источник истины: кто что получает, кто что создаёт и куда пишет.

## Общие правила
- **Все агенты читают справочные файлы из папки `docs/`** (A–G слои).
- **Все агенты создают файлы в `work/<BotSlug>/`** — slug берётся из `docs/FACTORY_PROJECTS_MEMORY.md`.
- **Координатор** знает, где что лежит, и подсказывает Оркестратору.

## Матрица

| # | Агент | Файл-промпт | Входные файлы (созданные другими агентами) | Создаваемый файл | Зависит от |
|---|-------|-------------|-------------------------------------------|------------------|------------|
| 0 | Оркестратор | `agents/1_ORCHESTRATOR.md` | ТЗ пользователя (чат, файлы, картинки) + `docs/беклог.md` (Backlog Memory Loop) | `work/<BotSlug>/0_ORCHESTRATOR__BRIEF.md` + `docs/беклог.md` (Post-Task Backlog Check) | Пользователь |
| 0.5 | Менеджер Глоссария | `agents/10_GLOSSARY_MANAGER.md` | Любой файл агента + `0_GLOSSARY__TERMS.md` | `docs/GLOSSARY_TERMS.md` (обновления) | Активируется по запросу на любом этапе |
| 1 | Архитектор | `agents/2_ARCHITECT.md` | `0_ORCHESTRATOR__BRIEF.md` | `work/<BotSlug>/1_ARCHITECTURE__MAP.md` | Оркестратор |
| 2 | Креативщик | `agents/3_CREATIVE.md` | `1_ARCHITECTURE__MAP.md` | `work/<BotSlug>/2_CREATIVE__PHRASES.md` | Архитектор |
| 3 | Автор Правил | `agents/4_RULES_AUTHOR.md` | `1_ARCHITECTURE__MAP.md` + `2_CREATIVE__PHRASES.md` | `work/<BotSlug>/3_RULES_AUTHOR__RULES_AND_DICTIONARIES.md` | Архитектор + Креативщик |
| 3.5 | Тестировщик | `agents/11_TESTER.md` | `2_CREATIVE__PHRASES.md` + `3_RULES_AUTHOR__RULES_AND_DICTIONARIES.md` | Устный отчёт Оркестратору (список непокрытых фраз) | Автор Правил + Креативщик |
| 4 | Автор Примеров | `agents/5_EXAMPLES_AUTHOR.md` | `1_ARCHITECTURE__MAP.md` + `2_CREATIVE__PHRASES.md` | `work/<BotSlug>/4_EXAMPLES_AUTHOR__DATASET.md` | Архитектор + Креативщик |
| 5 | Копирайтер | `agents/6_COPYWRITER.md` | `1_ARCHITECTURE__MAP.md` | `work/<BotSlug>/5_COPYWRITER__TEXTS.md` | Архитектор |
| 6 | Автор Ответов | `agents/7_RESPONSES_AUTHOR.md` | `1_ARCHITECTURE__MAP.md` + `5_COPYWRITER__TEXTS.md` | `work/<BotSlug>/6_RESPONSES_AUTHOR__RESPONSES.md` | Архитектор + Копирайтер |
| 7 | Валидатор | `agents/8_VALIDATOR.md` | `1_ARCHITECTURE__MAP.md` + `3_RULES_AUTHOR__RULES_AND_DICTIONARIES.md` + `4_EXAMPLES_AUTHOR__DATASET.md` + `6_RESPONSES_AUTHOR__RESPONSES.md` | `work/<BotSlug>/7_VALIDATOR__VALIDATION.md` | Все предыдущие агенты |
| 8 | Упаковщик | `agents/9_PACKAGER.md` | `6_RESPONSES_AUTHOR__RESPONSES.md` + `7_VALIDATOR__VALIDATION.md` | `work/<BotSlug>/9_PACKAGER__STAGING/` → ZIP | Валидатор + Автор Ответов |
| 9 | Координатор | `agents/12_COORDINATOR.md` | Запросы Оркестратора | Устное ответное сообщение Оркестратору | — |
| 13 | Библиотекарь | `agents/13_LIBRARIAN.md` | `docs/reference/COMMON_DICTIONARIES.md` + `docs/reference/raw_dicts/*.json` | Обновлённый `COMMON_DICTIONARIES.md` + Import Report. Удаляет успешно импортированные файлы из `raw_dicts/` | Сквозной агент референсного слоя (между проектами). Ответственный за весь dictionary ingestion pipeline |

## Исключения из конвейера
- **Автор Примеров (#4)** пропускается, если узлов с реальным вводом пользователя ≤ 2.
- **Креативщик (#2)** не пишет фразы для узлов Fallback, noMatch, Unknown, EVENT, goto-only.
- **Тестировщик (#3.5)** не тестирует узлы Fallback, noMatch, Unknown, EVENT, goto-only (у них нет правил матчинга в обычном смысле или фраз отсутствует).
- **Тестировщик (#3.5)** выполняется после Автора Правил. Если фразы непокрыты — Оркестратор возвращает задачу назад (Автор Правил или Креативщик) по решению пользователя.
- **Валидатор (#7)** должен вернуть в отчёте список пользовательских словарей для Упаковщика.

## Память проекта
- `docs/FACTORY_PROJECTS_MEMORY.md` — текущий бот, узел, агент, этап, «Следующий шаг».
- `docs/PROJECT_MEMORY.md` — общие правила фабрики, не меняется от бота к боту.
