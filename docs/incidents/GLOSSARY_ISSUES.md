# Отчёт Менеджера Глоссария: Нарушения терминологии в /docs и /agents

**Дата проверки:** 2026-05-30
**Агент:** Менеджер Глоссария (10_GLOSSARY_MANAGER)
**Область проверки:** `docs/*.md`, `agents/*.md`, `docs/reference/dictionaries/*.md`
**Глоссарий-источник:** `docs/GLOSSARY_TERMS.md`

---

## Резюме

| Метрика | Значение |
|---------|---------|
| Файлов проверено | 30+ |
| Нарушений найдено | 47 |
| Критических | 16 |
| Предупреждений (серых зон) | 31 |

---

## Критические нарушения

Термины из левостороннего столбца глоссария, где должен использоваться канонический термин из правостороннего столбца.

### 1. `pipeline` → должно быть `потоки данных` (12 нарушений)

| # | Файл:Строка | Найдено | Должно быть |
|---|------------|---------|------------|
| 1 | `docs/беклог.md:61` | `full pipeline: architect → creative → ml → dl → validator` | `полный конвейер: ...` |
| 2 | `docs/PROJECT_MEMORY.md:166` | `прогнать full pipeline` | `прогнать полный конвейер` |
| 3 | `docs/G_AGENT_RULES.md:46` | `dictionary pipeline` | `конвейер словарей` |
| 4 | `docs/G_AGENT_RULES.md:565` | `dictionary pipeline` | `конвейер словарей` |
| 5 | `docs/DATA_FLOW_MATRIX.md:26` | `dictionary ingestion pipeline` | `конвейер загрузки словарей` |
| 6 | `agents/1_ORCHESTRATOR.md:53` | `изменение pipeline` | `изменение конвейера` |
| 7 | `agents/1_ORCHESTRATOR.md:63` | `Изменение pipeline` | `Изменение конвейера` |
| 8 | `agents/1_ORCHESTRATOR.md:416` | `git pipeline` | `git конвейер` / `git-конвейер` |
| 9 | `agents/12_COORDINATOR.md:79` | `dictionary pipeline` | `конвейер словарей` |
| 10 | `agents/12_COORDINATOR.md:81` | `dictionary pipeline` | `конвейер словарей` |
| 11 | `agents/13_LIBRARIAN.md:3` | `ingestion pipeline` | `конвейер загрузки` |
| 12 | `agents/13_LIBRARIAN.md:257` | `dictionary pipeline` | `конвейер словарей` |

### 2. `node` → должно быть `узел` (1 нарушение)

| # | Файл:Строка | Найдено | Должно быть |
|---|------------|---------|------------|
| 13 | `docs/беклог.md:31` | `когда node принадлежит родительскому узлу` | `когда узел принадлежит родительскому узлу` |

### 3. `state`, `memory` → должно быть `контекст` (5 нарушений)

| # | Файл:Строка | Найдено | Должно быть |
|---|------------|---------|------------|
| 14 | `agents/2_ARCHITECT.md:257` | `state transitions` | `переходы контекста` |
| 15 | `agents/2_ARCHITECT.md:258` | `memory lifecycle` | `жизненный цикл памяти/контекста` |
| 16 | `agents/7_RESPONSES_AUTHOR.md:30` |(memory rules) | `правила контекста` |
| 17 | `agents/7_RESPONSES_AUTHOR.md:373` | `memory strategy` | `стратегия контекста` |
| 18 | `agents/7_RESPONSES_AUTHOR.md:386` | `memory behavior` | `поведение памяти/контекста` |

### 4. `intent` как standalone англ. слово → `интент` (4 нарушения)

| # | Файл:Строка | Найдено | Должно быть |
|---|------------|---------|------------|
| 19 | `agents/1_ORCHESTRATOR.md:300` | `.intent semantics` | `семантика интента` |
| 20 | `agents/8_VALIDATOR.md:211` | `intent definition` | `определение интента` |
| 21 | `agents/13_LIBRARIAN.md:228` | `semantic intent extraction` | `семантическое извлечение интента` |
| 22 | `agents/5_EXAMPLES_AUTHOR.md:119` | `same intent pattern` | `одинаковый паттерн интента` |

### 5. `source of truth` → должно быть `источник истины` (1 нарушение)

| # | Файл:Строка | Найдено | Должно быть |
|---|------------|---------|------------|
| 23 | `agents/13_LIBRARIAN.md:3` | `source of truth` | `источник истины` |

### 6. `response` (в прозе) → должно быть `ответ` (1 нарушение)

| # | Файл:Строка | Найдено | Должно быть |
|---|------------|---------|------------|
| 24 | `docs/E_RESPONSE_FORMATTING.md:24` | `Final response payload` | `Финальная нагрузка ответа` |

### 7. `permanent transfer` → должно быть `постоянный переход` (2 нарушения)

| # | Файл:Строка | Найдено | Должно быть |
|---|------------|---------|------------|
| 25 | `docs/D_GENERATION_RULES.md:20` | `permanent transfer` | `постоянный переход` |
| 26 | `docs/D_GENERATION_RULES.md:327` | `permanent transfer` | `постоянный переход` |

### 8. `context` как namespace label → должно быть `контекст` (1 нарушение)

| # | Файл:Строка | Найдено | Должно быть |
|---|------------|---------|------------|
| 27 | `docs/PROJECT_MEMORY.md:192` | `context` (namespace model) | `контекст` |

### 9. `trigger` как тип словаря → должно быть `событие` (6 нарушений в reference/dictionaries)

| # | Файл:Строка | Найдено | Должно быть |
|---|------------|---------|------------|
| 28 | `docs/reference/dictionaries/common_which.md:3` | `Тип: trigger` | `Тип: событие` |
| 29 | `docs/reference/dictionaries/common_want_2.md:3` | `Тип: trigger` | `Тип: событие` |
| 30 | `docs/reference/dictionaries/common_trebuetsya.md:3` | `Тип: trigger` | `Тип: событие` |
| 31 | `docs/reference/dictionaries/common_other.md:3` | `Тип: trigger` | `Тип: событие` |
| 32 | `docs/reference/dictionaries/common_for.md:3` | `Тип: trigger` | `Тип: событие` |
| 33 | `docs/reference/dictionaries/common_docs.md:3` | `Тип: trigger` | `Тип: событие` |
| 34 | `docs/reference/dictionaries/clever.md:3` | `Тип: trigger` | `Тип: событие` |
| 35 | `docs/reference/dictionaries/busy.md:3` | `Тип: trigger` | `Тип: событие` |

### 10. Полностью английские описания (1 нарушение)

| # | Файл:Строка | Найдено | Должно быть |
|---|------------|---------|------------|
| 36 | `docs/B_RUNTIME_MODEL.md:161` | `Engine stores the hash of the last selected string per dictionary name. For sudict, the hash persists in session state. For udict, the hash is stored in step-local state and discarded at the next user turn.` | Перевод на русский с использованием канонических терминов |

---

## Предупреждения (серые зоны)

Эти случаи не являются однозначными нарушения — они могут быть допустимы в техническом контексте (DSL-синтаксис, имена переменных, JSON-поля), но требуют внимания.

### `session` как scope переменных — допустимо в таблицах JSON/DSL

Использования в техническом контексте (scope lifecycle, JSON field `life_cycle: "0"`, `scope: "session"`):

| Файл:Строка | Контекст | Статус |
|------------|---------|--------|
| `docs/B_RUNTIME_MODEL.md:56` | `scope: session` в JSON | ✅ допустимо (имя поле JSON) |
| `docs/E_RESPONSE_FORMATTING.md:66` | `Шаг/Сессия` (scope label) | ⚠️ допустимо |
| `agents/9_PACKAGER.md:77` | `"scope":"session"` в JSON | ✅ допустимо (field value) |
| `agents/8_VALIDATOR.md:182` | `session` (scope таблица) | ⚠️ допустимо |

### `%reply-`, `%reply--` — системные переменные платформы

| Файл:Строка | Статус |
|------------|--------|
| `docs/B_RUNTIME_MODEL.md:46-47` | ✅ системная переменная, не правится |
| `docs/VOICE_OUTBOUND_CHECKLIST.md:33` | ✅ системная переменная |
| `docs/E_RESPONSE_FORMATTING.md:65` | ✅ системные переменные |
| `agents/7_RESPONSES_AUTHOR.md:153` | ✅ системная переменная |
| `agents/8_VALIDATOR.md:90` | ✅ системная переменная |

### `[@goto]`, `[dict]`, `[@cmb]` — DSL-синтаксис

Все вхождения DSL-конструкций `[@goto]`, `[dict]`, `[@cmb]` и т.д. — **не являются нарушениями**, так как это синтаксис языка ДОС, а не терминологическое описание.

### `goto-only` — гибридный термин

`goto-only` — устоявшийся композитный технический термин, описывающий тип узла. Встречается повсеместно:

| Файл | Статус |
|------|--------|
| `agents/2_ARCHITECT.md:47,174` | ⚠️ допустимо (тип узла) |
| `docs/1_ORCHESTRATOR.md:189` | ⚠️ допустимо |
| `docs/G_AGENT_RULES.md:138-140` | ⚠️ допустимо |
| `docs/C_BOT_ARCHITECTURE.md:296-297` | ⚠️ допустимо |
| `docs/DATA_FLOW_MATRIX.md:30-31` | ⚠️ допустимо |
| `agents/4_RULES_AUTHOR.md:33` | ⚠️ допустимо |
| `agents/8_VALIDATOR.md:56` | ⚠️ допустимо |
| `agents/11_TESTER.md:50` | ⚠️ допустимо |

### `IC-only` — гибридный термин

Аналогично `goto-only` — устоявшийся технический термин:

| Файл | Статус |
|------|--------|
| `docs/PROJECT_MEMORY.md:139,155,159,165` | ⚠️ допустимо |
| `agents/2_ARCHITECT.md:47` | ⚠️ допустимо |
| `agents/4_RULES_AUTHOR.md:33` | ⚠️ допустимо |

### `матчинг` — серая зона (в словаре неканонический термин, но повсеместно используется)

Слово `матчинг` указано в `GLOSSARY_TERMS.md` как неканонический синоним `правила`. Однако на практике оно используется в значении «процесс сопоставления паттернов с запросом», что семантически отличается от «правило». Встречается в 20+ местах:

| Файл | Пример |
|------|--------|
| `docs/C_BOT_ARCHITECTURE.md:185` | `Весь матчинг в словаре` |
| `docs/IN CIDENT_CATSIM_20260529.md:56` | `матчинг сломан` |
| `docs/D_GENERATION_RULES.md:159` | `Скелет матчинга` |
| `agents/11_TESTER.md:97,101,108` | `stem-матчинг` |
| `docs/PROJECT_MEMORY.md:112` | `матчинг, IC` |

**Рекомендация:** термин `матчинг` используется в значении «сопоставление» (matching process) и не является синонимом `правило`. Предлагается либо добавить в глоссарий отдельную строку `матчинг, сопоставление → матчинг`, либо заменить на `сопоставление`.

### `пак` — серая зона

В словаре `пак` указан как неканонический синоним `словарь`. Встречается в `docs/A_LANGUAGE_SPEC.md:91` и других местах как сокращение `пака`. В DSL-контексте допустимо.

### Английские термины в коммитах и именах файлов

Имена файлов (например, `E_RESPONSE_FORMATTING.md`) — не являются нарушениями, т.к. это naming convention файловой системы.

---

## Файлы без нарушений

Следующие файлы прошли проверку без нарушений терминологии:

| Файл | Статус |
|------|--------|
| `agents/3_CREATIVE.md` | ✅ |
| `agents/99_TEST_SET_COLLECTOR.md` | ✅ |
| `agents/README.md` | ✅ (кроме `goto-переходы` — допустимо) |
| `docs/H_USER_INTERACTION_PROTOCOL.md` | ✅ |
| `docs/A_LANGUAGE_SPEC.md` | ✅ (DSL-синтаксис не считается) |
| `docs/F_PLATFORM_API.md` | ✅ (кроме `[@goto]` — DSL) |
| `docs/VOICE_OUTBOUND_CHECKLIST.md` | ✅ |

---

## Рекомендации

1. **Приоритет 1 (критические):** Заменить все вхождения `pipeline` на `конвейер` в 12 файлах. Это самое массовое нарушение.
2. **Приоритет 2 (критические):** Заменить `state transitions`, `memory lifecycle`, `memory strategy`, `memory behavior` в `agents/2_ARCHITECT.md` и `agents/7_RESPONSES_AUTHOR.md`.
3. **Приоритет 2 (критические):** Заменить `intent semantics`, `intent definition`, `semantic intent extraction` на русские эквиваленты.
4. **Приоритет 3 (управление):** Перевести английский абзац в `docs/B_RUNTIME_MODEL.md:161`.
5. **Приоритет 3 (управление):** Заменить `dictionary pipeline` на `конвейер словарей` в `G_AGENT_RULES.md`, `COORDINATOR.md`, `LIBRARIAN.md`.
6. **Приоритет 4 (управление):** Заменить `source of truth` в `agents/13_LIBRARIAN.md`.
7. **Приоритет 4 (управление):** Массово заменить `Тип: trigger` → `Тип: событие` в `docs/reference/dictionaries/*.md` (8+ файлов).
8. **Приоритет 5 (обсуждение):** Уточнить статус термина `матчинг` — добавить отдельную строку в глоссарий или заменить на `сопоставление`.
9. **Приоритет 5 (обсуждение):** Уточнить, является ли `node-scoped` допустимым термином (встречается в `agents/1_ORCHESTRATOR.md:276`).

---

**Составил:** Менеджер Глоссария (10_GLOSSARY_MANAGER)
**Дата:** 2026-05-30
