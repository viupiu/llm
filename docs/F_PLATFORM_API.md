# F. ПЛАТФОРМА И API (PLATFORM_API)

**SSOT для:** ID, ZIP-архивы, metadata, валидация, слоты (JSON), action, скрипты сборки.

---

## 1. ID и Именование

### Формат ID (КРИТИЧЕСКИ)

Только сгенерированные рандомные ID. Заглушки вида `000000`, `a1b2c3d4` — недопустимы.

| Сущность | Формат | Пример |
|----------|--------|--------|
| DialogNode, Dictionary, Variable, Skill, Tag, Answer, DialogNodeTag | `8-4-4-4` (12 hex) | `0bd8d403-9eb2-42c7-a52a-8190` |
| Assistant, Branch | `8-4-4-4-12` (полный UUID, 32 hex) | `746f766e-296f-47d1-a34e-49a542d4e4b0` |

Файл JSON: `{id}.json`.

### Именование
- **Навыки/Узлы:** `Приветствие`, `Заказ пиццы`. Можно префикс с цифрой для сортировки: `1. Приветствие`, `2. Заказы`.
- **Переменные:** `snake_case` (`%user_name`, `%pizza_size`).

---

## 2. Структура ZIP-архива (КРИТИЧЕСКИ)

Корень ZIP:
1. `metadata.json` — конфигурация версии
2. **Обёрточная папка:** `[ASSISTANT_ID]-master-[40-hex-hash]`

Внутри обёртки — папки по типам сущностей:

```text
simple_assistant_prod.zip/
├── metadata.json
└── bf356a79-672e-41c6-a5c7-7abcbea23571-master-98e5f62f85aa48a4d6d627cf202f91ae5325bc6c/
    ├── Assistant/
    ├── Branch/
    ├── DialogNode/
    ├── Dictionary/
    ├── Skill/
    ├── Variable/
    └── Tag/
```

**Без обёрточной папки архив НЕ примется платформой.**

### Минимальный бот (Demo 2)

В ZIP только папки с реальными JSON (пустые `Answer/` не обязательны):

```text
Demo 2_master_prod.zip/
├── metadata.json
└── 37348a59-05ac-4c96-a3b0-0e4535e3d05d-master-13578c7a274fe9161a20cc03edd6eb2e9f3ad7bf/
    ├── Assistant/37348a59-05ac-4c96-a3b0-0e4535e3d05d.json
    ├── Branch/a1812a5c-14c3-4cd8-a60d-50c677c5497c.json   ← name: "master"
    ├── Skill/5254d8e1-782d-48d3-9914.json
    ├── DialogNode/86cf020c-1115-4cd7-8726.json
    └── Dictionary/32a21c63-cc4f-4436-b96a.json
```

### `metadata.json`

```json
{"lc_version":"0.96.1","timestamp":"...","options":{"exclude_tables":["AutotestScenario"]}}
```

Не использовать `{"assistant_id":"...","version":"1.0"}` — платформа не принимает.

---

## 3. Поля дат и creator

Как в Demo 2:

| Поле | Формат | Пример |
|------|--------|--------|
| `created`, `updated` | naive ISO, без `+03:00` и `Z` | `2026-05-25T06:54:24.862973` |
| `metadata.timestamp` | то же | `2026-05-25T06:56:22.782597` |
| `creator` (кроме Branch) | UUID пользователя | `a04359b1-6422-4e56-9792-bf13f40afb9b` |
| `Branch.creator` | всегда `null` | `null` |
| `editors[].timestamp` | UTC с `Z`, без дробей | `2026-05-25T06:56:14Z` |

Запрещены `00000000-0000-0000-0000-000000000000`. Скопировать `creator` из `Assistant/*.json`.

---

## 4. Slot Filling (JSON)

Не реализовывать через `[if]`. В JSON узла:
- `variable` — ссылка на переменную
- `entity` — словарь для распознания
- `question` — вопрос для сбора
- `retry_count` — число попыток
- `failure_answer` — ответ при неудаче
- `required` — обязательный слот

---

## 5. Action

```dl
[action(name, param="value")]{[%var="[[field]]"]}
```

- Параметры в кавычках
- Результат — `[[field]]` внутри `{}`

---

## 6. Скрипты сборки

### Порядок выполнения (из корня проекта)

```powershell
python scripts/prepare_staging.py --staging work/staging
python scripts/validate_archive.py --staging work/staging
python scripts/pack_archive.py --staging work/staging --out archives/exported/bot_prod.zip
python scripts/validate_archive.py --zip archives/exported/bot_prod.zip
```

### Что ловит `validate_archive.py`

- Отсутствие `-master-{40hex}` обёртки
- Неверный `metadata.json`
- Вложенный `.zip`
- `NamesEntity`
- Битые `skill_id` / `[dict(name)]`
- `[goto(...)]` вместо `[@goto("...")]`
- Таймзону `+03:00` в `created`/`timestamp`
- `creator` = `00000000-...`

`pack_archive.py` автоматически приводит даты и `creator` к формату экспорта.

---

## 7. Валидация

### Структура JSON
1. Все файлы — валидный JSON
2. `id` уникальны в проекте
3. Связи: `skill_id` → `Skill/`, `slot_filling.*` → `Variable/`/`Dictionary/`, `DialogNodeTag` → существующие `dialog_node_id`, `tag_id`

### DSL (текст)
- Парность тегов: `[` = `]`, `{` = `}`, `(` = `)`
- `[b]/[/b]`, `[i]/[/i]`, `[ul]/[el]`, `[ol]/[el]`
- `[dict(name)]`, `[udict(name)]`, `[sudict(name)]`, `[lcdict(name)]` → словарь существует
- `[&dict(name, norm)]` → словарь с нормализацией (`=>`)
- В каждом словаре — ≥ 1 строка без `=>` (канон)
- Имя переменной: латиница, кириллица, цифры, `_`, `-`, `.`
- `[if(...)]{...}` — без пробела между `)` и `{`
- Блочные: каждый тег отдельный блок; только `--`, не `–`
- `[@hvs("table", "row")]` или `[@hvs("table", "row", "col")]`
- `[&1]` только если в `dl_rules` есть `[- -]` или `[-{...}-]`
- `[@goto]` / `[@extend]`: имя в кавычках = `DialogNode.name`
- `[action(name, ...)]{...}` — парность `{}`

### ML примеры
- ≥ 10 уникальных примеров на класс
- ≥ 3 разных класса в боте
- Рекомендуется ≥ 100 примеров на класс

### Red Flags
- HTML `<b>`, `<br>` в обычных ответах
- `–switch` вместо `--switch`
- `slot_filling` с `required: true` без `question` или `variable`
- Пустые `dl_rules` не на фоллбэке
- `[dict]` без файла словаря
- `--switch` в одном блоке `text` с другим текстом
- Отсутствие обёртки в архиве
- Узлы/навыки `Узел 1.1`, `Навык 1` — не допустимо
- `[&1]` без референции `[- -]`
- Слоты без `retry_count` и `failure_answer`
- Словари: канон с `~` или `*`; только синонимы `=>`; `–include`
- `[dict]` выдача без нормализации, но с `=>`

---

## 8. Архиватор ДОС: правила сборки

**КЛЮЧЕВОЙ ПРИНЦИП:** Экспорт из ДОС уже правильный. НЕ модифицируй содержимое!

Пакер только:
1. Читает staging (экспорт из ДОС)
2. Упаковывает в ZIP со структурой `metadata.json` + `{assistant_id}-master-{hash}/`
3. Минимально нормализует timezone'ы (если `+HH:MM` → убрать)

### Никогда не трогать:
- `state_score` — оставлять как есть (`0` в экспорте)
- `is_common` — оставлять как есть (`true` для общих словарей)
- `created`/`updated` — НЕ ставить `null`! Оставлять из экспорта
- `creator` — НЕ ставить `null`! Оставлять UUID пользователя
- `editors` — НЕ очищать массив!
- `inlineStyleRanges` — НЕ очищать!
- `ml_examples` — НЕ модифицировать блоки
- `dl_rules` — НЕ менять текст блоков
- `content`/`answers` — НЕ модифицировать
- `value` (Variable) — НЕ менять на `"0"` или `""`
- `description` — НЕ добавлять/удалять

### Разрешено:
- Нормализовать таймзоны: `2026-05-26T14:00:00+03:00` → `2026-05-26T14:01:21.125674`
- Заменять placeholder creator `00000000-0000-0000-0000-xxxxxxxxxxxx` на реальный UUID
- Фиксить `[@goto()]` синтаксис в answers
- Генерировать random block keys для новых блоков

### Потоки работы пакетного процесса:
1. `load_staging()` — читает `staging_dir/EntityType/*.json` + `manifest.json`
2. `normalize_all_entities()` — только timezone'ы и placeholder creator'ы
3. `validate_entities()` — проверяет структуру
4. `pack_staging_to_zip()` — минифицирует JSON, вычисляет hash, создаёт ZIP

### Валидация перед упаковкой:
- Каждый файл: `EntityType/{id}.json`, где `id == obj.id`
- DialogNode: `skill_id` ссылается на существующий Skill
- DialogNode: не использует `[goto(...)]` (только `[@goto("Имя узла")]`)
- Dictionary: каждый словарь имеет хотя бы одно каноническое слово (без `=>`)
- Branch: `assistant_id` ссылается на существующий Assistant, `name == "master"`

---

## 9. Критические требования JSON: GOOD vs BAD

Различия между архивами, которые загрузились (GOOD) и не загрузились (BAD).

### `state_score`
- GOOD: `"state_score": 0` (число)
- BAD: `"state_score": null`
- Значение должно быть `0`. Удаление поля или `null` ломает импорт.

### Timestamps
- GOOD: `"created": "2026-05-26T14:40:13.363455"`
- BAD: `"created": null`
- Нужны реалистичные timestamp'ы. `null` не принимается.

### `creator`
- GOOD: `"creator": "a04359b1-6422-4e56-9792-bf13f40afb9b"`
- BAD: `"creator": null`
- `null` в creator ломает импорт (включая Dictionary, Variable, Skill).

### `editors`
- GOOD: `[{"user_id": "a04359b1-6422-4e56-9792-bf13f40afb9b", "timestamp": "2026-05-26T14:40:13Z"}]`
- BAD: `[]`
- Массив должен быть заполнен.

### Dictionary: `is_common`
- GOOD: `"is_common": true` (ВСЕ словари)
- BAD: `"is_common": false`

### `ml_examples`
- GOOD: `{"blocks": [{"key": "...", "data": {}, "text": "", "type": "unstyled", "depth": 0, "entityRanges": [], "inlineStyleRanges": []}], "entityMap": {}}`
- BAD: `{"blocks": [], "entityMap": {}}`
- Всегда должен иметь блок с пустым текстом.

### `dl_rules` в root узлах
- GOOD: `{"blocks": [{"key": "...", "data": {}, "text": "", ...}], "entityMap": {}}`
- BAD: `{"blocks": [{"key": "...", "data": {}, "text": "*", ...}], "entityMap": {}}`
- Текст блока должен быть пустым, не `"*"`.

### `inlineStyleRanges`
- GOOD: `[{"style": "BRACKETS", "length": 1, "offset": 0}, ...]`
- BAD: `[]`
- Должен быть заполнен.

### `parent` у root DialogNode
- GOOD: root узлы не имеют parent (`null`)
- BAD: некоторые root указывают parent на другой узел

### Content answers
- GOOD "Прощание - Исчерпание помощи": `"В конце... [%voice.end_call=\"True\"]"`
- GOOD "Приветствие": `"Что я могу вам помочь? [%that_anchor=\"...\"]"`
- BAD-варианты содержат другой текст.

### Slot filling IDs
- GOOD: разные short-IDs (генерируются платформой)

### Extra answer blocks в приветствии
- GOOD: 2 answer blocks, включая `"data": {"DLAnswerLU": "rare"}`
- BAD: 2 answer blocks, но без `DLAnswerLU`
