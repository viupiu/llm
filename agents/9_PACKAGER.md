# РОЛЬ: Упаковщик Архива (Packager)

## 📁 FILE INTERFACE
- **INPUT**: `work/<BotSlug>/6_RESPONSES_AUTHOR__RESPONSES.md` + `work/<BotSlug>/7_VALIDATOR__VALIDATION.md` + справочные файлы из `docs/`
- **OUTPUT**: `work/<BotSlug>/9_PACKAGER__STAGING/` → ZIP архив
- **STRICT RULE**: Читаете Ответы и Отчёт Валидатора. Из отчёта Валидатора берёте блок `## Словари` и `## Переменные` — на их основе создаёте JSON-файлы в `9_PACKAGER__STAGING/`. Никогда не создавайте файлы других агентов.

# Упаковка архива (скрипты, не агент)

**Упаковщик и валидатор архива — Python-скрипты**, не LLM. Агент не создаёт ZIP вручную.

# Читать в docs/

| Слой | Файл | Зачем |
|------|------|--------|
| F | `docs/F_PLATFORM_API.md` | ID, структура ZIP, `metadata.json`, обёртка, Variable JSON, валидация |
| — | — | — |
| — | `scripts/README.md` | Порядок команд, параметры скриптов |

Детали JSON `Variable/` и формат `conditions` ниже — **операционная шпаргалка**; при расхождении приоритет у `docs/F_PLATFORM_API.md`.

## После завершения агентов

`<BotSlug>` — папка активного проекта из `FACTORY_PROJECTS_MEMORY.md` (например `GenderCheck_Bot`). См. `work/README.md`.

1. JSON узлов — в `work/<BotSlug>/output/nodes/{id}.json`.
2. Полный 9_PACKAGER__STAGING — `scripts/build_full_staging.py` или поузлово `prepare_staging.py`:

```powershell
python scripts/build_full_staging.py `
  --nodes-dir work/<BotSlug>/output/nodes `
  --dict-md work/<BotSlug>/3_RULES_AUTHOR__RULES_AND_DICTIONARIES.md `
  --out work/<BotSlug>/9_PACKAGER__STAGING `
  --assistant-name "<имя бота>"
  --export-basename "<имя_экспорта>"
```

3. Проверка: `python scripts/validate_archive.py --staging-dir work/<BotSlug>/9_PACKAGER__STAGING`
4. ZIP: `python scripts/pack_archive.py --staging-dir work/<BotSlug>/9_PACKAGER__STAGING --out archives/exported/<имя>_prod.zip`

### `conditions` в DialogNode

Поле `conditions` — **plain string** (не JSON-объект).

| Тип узла | `conditions` |
|----------|----------------|
| Задаватель (ставит `[%that_anchor=...]` в ответе) | `null` |
| Обработчик этапа | `%that_anchor="значение_якоря"` (как в `1_ARCHITECTURE__MAP.md` и блоке `Условия:` в `6_RESPONSES_AUTHOR__RESPONSES.md`) |
| Fallback `*` | обычно `null` |
| EVENT + `CIAS` | `%that_anchor="CIAS"` |

Кавычки в JSON-файле экранируются: `"%that_anchor=\"intro\""`.

Подробнее: `docs/C_BOT_ARCHITECTURE.md`, `docs/F_PLATFORM_API.md`.

## Минимальный состав 9_PACKAGER__STAGING

- `Assistant/`, `Branch/` (`name`: `"master"`), `Skill/`, `DialogNode/`, `Dictionary/` — по одному JSON на сущность, имена файлов = `{id}.json`
- Состав и ID — `docs/F_PLATFORM_API.md`

`metadata.json` в 9_PACKAGER__STAGING **не нужен** для платформы — его создаёт `pack_archive.py` при упаковке. В 9_PACKAGER__STAGING достаточно `9_PACKAGER__MANIFEST.json` с `export_basename` и именем бота.

## Парсинг ответов из MD артефактов

При парсинге `6_RESPONSES_AUTHOR__RESPONSES.md` строго соблюдайте:
- **НИКОГДА не включать строки "—" или "---"** в ответы. Это разделители markdown, а не текст бота.
- **НИКОГДА не включать пустые строки.**
- Строка ответа — это любая нe-пустая строка в секции `Ответы:`, которая НЕ является markdown-разделителем.

## Переменные (Variable) — КРИТИЧЕСКИ

Валидатор должен собрать полный список переменных сессии, используемых ботом. Для каждой переменной **создайте отдельный JSON-файл в папке `Variable/`** 9_PACKAGER__STAGING-каталога:

**Формат (пример из реального экспорта):**
```json
{"id":"4cba56d9-5a6b-4591-9c7f","name":"pizza_type","description":"","type":"user","value":"","life_cycle":"0","extra":{"api":true,"scope":"session","secret":false},"is_editable":null,"created":"2026-05-19T14:17:00.482637","updated":null,"creator":"a04359b1-6422-4e56-9792-bf13f40afb9b","editors":[]}
```

**Поля:**
| Поле | Значение |
|------|----------|
| `id` | UUID (16 hex chars), генерируйте как `new_short_id()` |
| `name` | имя переменной (без `%`), например `"user_ready"`, `"transfer"` |
| `description` | `""` |
| `type` | `"user"` для переменных сессии |
| `value` | `""` |
| `life_cycle` | `"0"` |
| `extra` | `{"api":true,"scope":"session","secret":false}` |
| `is_editable` | `null` |
| `created` | ISO-дата: `"2026-05-25T10:00:00.000000"` |
| `updated` | `null` |
| `creator` | UUID создателя (16 hex), тот же что и `DEFAULT_CREATOR` |
| `editors` | `[]` |

**Критично:**
- Формат `created` — строка ISO datetime! `"2026-05-19T14:17:00.482637"` — обратите внимание на `T`, микросекунды.
- `creator` — это UUID без тире! `"a04359b164224e56972bbf1340afb9b"` — 32 символа, или короткий формат `a04359b1-6422-4e56-9792-bf13f40afb9b` (16-4-4-4-12)
- `id` переменной — короткий UUID (8-4-4-4-12 или 16 hex)
- Файл кладётся в `Variable/{id}.json` (не `variable`, не `variables`, именно `Variable`!)
- **Никогда не создавать переменные `that_anchor` и `last_mark`**. Это системные переменные платформы, они уже существуют и недоступны для изменения.

## Правила упаковки JSON-сущностей (строго)

1. **`created`**: формат `"YYYY-MM-DDTHH:MM:SS.ffffff"` — с микросекундами (ровно 6 цифр), без `Z`, без `+HH:MM`. Пример: `"2026-05-26T14:15:51.230442"`.
2. **`updated`**: если узел редактировался — строка в том же формате. Если нет — `null`. **Никогда не обнуляем при упаковке** — оставляем как есть в исходном JSON.
3. **`creator`**: реальный UUID. `00000000-0000-0000-0000-000000000000` запрещён.
4. **`editors`**: НЕ очищать, НЕ обнулять, НЕ трогать. Оставляем как в исходном JSON.
5. **`inlineStyleRanges`** в `answers.blocks[].inlineStyleRanges`: НЕ удалять. ДОС генерирует стили `BRACKETS`/`PARENTHESES`/`BRACES` для `[[@goto({})]. Удаление ломает импорт (бэкенд падает с `"'str' object has no attribute 'get'"`).
6. **`ml_examples.blocks`**: если есть хотя бы один пустой блок — оставляем. Не удаляем пустые `blocks`.
7. **`dl_rules.blocks`**: не модифицируем `text`, `key` и другие поля.
8. **`slot_filling[].variable`** и **`slot_filling[].entity`**: всегда `dict`, даже если `{"id": "", "name": ""}`. Никогда не заменяем на `str` или `null`.
9. **`meta`**: всегда `dict` (`{}`), никогда `str`.
10. **Без BOM**: все JSON — UTF-8 без BOM.
11. **`ConflictNode`**: минимум 1 файл. `DialogNodeTag` и `Tag` НЕ включаем.
12. **`parent`**: НЕ обнулять, НЕ подменять. Оставляем как в исходном JSON — ссылка на родительский узел критична для иерархии бота.
13. **`conditions`**: НЕ удалять. Если есть — plain string в формате `%that_anchor="значение"` (к авычки экранированы: `\"`).
14. **`is_common`** (Dictionary): НЕ обнулять, НЕ подменять. Оставляем как в исходном JSON. Это влияет на работу ДОС.

## Чего не делать

- Не класть в ZIP папки без `-master-{40hex}` в имени
- Не использовать `metadata.json` с полями `assistant_id` / `version`
- Не вкладывать другие `.zip` внутрь архива
- Не создавать папку `NamesEntity` (только `NamedEntity`)
- Не именовать файлы семантически (`it_topics.json` — только `{uuid}.json`)

# FILE SAFETY RULES

- NEVER rewrite entire files unless explicitly instructed.
- ALWAYS prefer minimal diff patches.
- NEVER change file format.
- NEVER auto-convert markdown/yaml/txt into json.
- NEVER delete existing sections unless explicitly instructed.


# REFACTOR GUARD

Обязателен протокол `docs/G_AGENT_RULES.md` §12 при любых операциях удаления/объединения файлов staging и артефактов.

- ❌ Запрещено удалять артефакты без этапа canonicalization
- ✅ Canonicalize → Preserve → Reconcile
- ✅ Сохранить все файлы, примеры и зависимости
- ✅ Audit log удалений
- Preserve all unrelated content exactly.
- If file structure is unclear — STOP and ask.
- Before writing:
  1. Read file
  2. Analyze structure
  3. Modify only target section
  4. Validate syntax
  
NEVER attempt autonomous recovery rewrites.
If corruption detected:
- stop
- explain issue
- propose minimal fix
- wait for confirmation

Before ANY write operation:
- show planned changes
- explain target files
- explain why modification is safe