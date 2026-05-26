# -*- coding: utf-8 -*-
"""Общая логика валидации и упаковки архивов ДОС (JSON + ZIP)."""

from __future__ import annotations

import hashlib
import json
import re
import secrets
import string
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from zipfile import ZipFile

# Папки сущностей платформы (имена как в экспорте)
ENTITY_DIRS = frozenset({
    "Answer",
    "Assistant",
    "Branch",
    "ConflictNode",
    "DialogNode",
    "DialogNodeTag",
    "Dictionary",
    "Function",
    "Intent",
    "NamedEntity",
    "Skill",
    "Tag",
    "Variable",
})

# Типичные ID: короткий (20 hex) и полный UUID (32 hex)
RE_SHORT_ID = re.compile(
    r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}$", re.I
)
RE_FULL_ID = re.compile(
    r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$", re.I
)
RE_WRAPPER = re.compile(
    r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"
    r"-master-[0-9a-f]{40}$",
    re.I,
)

RE_DICT_REF = re.compile(r"\[(?:dict|udict|sudict|lcdict)\(([^)]+)\)\]")
RE_GOTO_WRONG = re.compile(r"\[goto\(([^)]+)\)\]")
RE_GOTO_NQ = re.compile(r'\[@goto\((?P<target>[^"\'\(]*)\)\]')
RE_BLOCK_KEY_BAD = re.compile(r"^(rule_|ans_|ml_)")
RE_DOS_NAIVE_TS = re.compile(
    r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d{1,6})?$"
)
RE_EDITOR_TS = re.compile(
    r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$"
)

DEFAULT_LC_VERSION = "0.96.1"
DEFAULT_METADATA_OPTIONS = {"exclude_tables": ["AutotestScenario"]}
# Возьмите creator из любого своего экспорта ДОС (поле creator в Assistant.json)
DEFAULT_CREATOR = "a04359b1-6422-4e56-9792-bf13f40afb9b"


@dataclass
class ValidationIssue:
    level: str  # error | warning
    code: str
    message: str
    path: str = ""

    def __str__(self) -> str:
        prefix = "ERROR" if self.level == "error" else "WARN"
        loc = f" ({self.path})" if self.path else ""
        return f"[{prefix}] {self.code}{loc}: {self.message}"


@dataclass
class ValidationReport:
    issues: list[ValidationIssue] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not any(i.level == "error" for i in self.issues)

    def add(self, level: str, code: str, message: str, path: str = "") -> None:
        self.issues.append(ValidationIssue(level, code, message, path))


def random_block_key(length: int = 5) -> str:
    alphabet = string.ascii_lowercase + string.digits
    return "".join(secrets.choice(alphabet) for _ in range(length))


def new_short_id() -> str:
    h = secrets.token_hex(10)
    return f"{h[0:8]}-{h[8:12]}-{h[12:16]}-{h[16:20]}"


def new_full_id() -> str:
    h = secrets.token_hex(16)
    return f"{h[0:8]}-{h[8:12]}-{h[12:16]}-{h[16:20]}-{h[20:32]}"


def is_valid_entity_id(entity_dir: str, entity_id: str) -> bool:
    if entity_dir in ("Assistant", "Branch"):
        return bool(RE_FULL_ID.match(entity_id))
    return bool(RE_SHORT_ID.match(entity_id))


def minify_json(obj: Any) -> str:
    return json.dumps(obj, ensure_ascii=False, separators=(",", ":"))


def format_dos_datetime(dt: datetime | None = None) -> str:
    """Как в экспорте ДОС: naive ISO без таймзоны, 6 знаков дробной части."""
    if dt is None:
        dt = datetime.now()
    return dt.strftime("%Y-%m-%dT%H:%M:%S.") + f"{dt.microsecond:06d}"


def normalize_timestamp_string(value: str | None) -> str | None:
    """Приводит к формату 2026-05-26T14:15:51 (без Z, без таймзоны)."""
    if value is None or not isinstance(value, str):
        return value
    v = value.strip()
    if v.endswith("Z"):
        v = v[:-1]
    if "+" in v:
        v = v.split("+", 1)[0]
    m = re.match(r"^(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2})(?:\.\d+)?", v)
    if not m:
        return v
    return m.group(1)


def is_placeholder_creator(creator: str | None) -> bool:
    if not creator:
        return False
    c = creator.lower()
    return c.startswith("00000000-0000-0000-0000-")


def generate_updated_timestamp(base_created: str | None = None) -> str:
    """Генерирует updated timestamp с небольшим смещением от created (как ДОС)."""
    if base_created and isinstance(base_created, str):
        try:
            from datetime import timedelta
            dt = datetime.strptime(base_created, "%Y-%m-%dT%H:%M:%S.%f")
            dt += timedelta(seconds=1, microseconds=1)
        except ValueError:
            dt = datetime.now()
    else:
        dt = datetime.now()
    return dt.strftime("%Y-%m-%dT%H:%M:%S.") + f"{dt.microsecond:06d}"


def normalize_entity_export_fields(
    obj: dict,
    entity_dir: str,
    *,
    creator: str,
    created: str | None = None,
) -> dict:
    """Нормализация полей экспорта: timestamps, creator, updated/editors."""
    out = dict(obj)

    # Нормализуем created timestamp
    if "created" in out and out["created"] is not None:
        val = out["created"]
        if isinstance(val, str) and ("+" in val or val.endswith("Z")):
            out["created"] = normalize_timestamp_string(val)

    # Нормализуем updated: убираем timezone, если есть
    if "updated" in out and out["updated"] is not None:
        val = out["updated"]
        if isinstance(val, str) and ("+" in val or val.endswith("Z")):
            out["updated"] = normalize_timestamp_string(val)
    # Генерируем updated для типов, где ДОС всегда его ставит
    elif entity_dir in ("DialogNode", "Dictionary", "Assistant"):
        out["updated"] = generate_updated_timestamp(out.get("created"))

    # Заменяем только placeholder creator (00000000-...) — не заменяем null!
    if entity_dir != "Branch":
        cr = out.get("creator")
        if cr is not None and is_placeholder_creator(cr):
            out["creator"] = creator

    # Генерируем editors для DialogNode и Dictionary: 1 запись с creator
    if entity_dir in ("DialogNode", "Dictionary"):
        editors = out.get("editors")
        if isinstance(editors, list) and not editors and out.get("updated"):
            upd = out["updated"]
            editor_ts = upd[:19] + "Z" if len(upd) >= 19 else upd + "Z"
            out["editors"] = [{
                "user_id": out.get("creator", creator),
                "timestamp": editor_ts,
            }]
        # Нормализуем timestamps в существующих editors
        elif isinstance(editors, list):
            fixed = []
            for ed in editors:
                if not isinstance(ed, dict):
                    fixed.append(ed)
                    continue
                e = dict(ed)
                if "timestamp" in e and isinstance(e["timestamp"], str):
                    t = e["timestamp"]
                    if "+" in t:
                        base = normalize_timestamp_string(t.split("+")[0])
                        if base:
                            e["timestamp"] = base[:19] + "Z" if len(base) >= 19 else t
                    elif not RE_EDITOR_TS.match(t) and "T" in t:
                        e["timestamp"] = t[:19] + "Z"
                fixed.append(e)
            out["editors"] = fixed
    return out


def fix_goto_syntax(text: str) -> str:
    def repl(m: re.Match[str]) -> str:
        target = m.group(1).strip()
        target = target.strip('"').strip("'")
        return '[@goto(' + '"' + target + '"' + ')]'
    text = RE_GOTO_WRONG.sub(repl, text)

    def repl_nq(m: re.Match[str]) -> str:
        target = m.group("target").strip()
        if target.startswith('"') or target.startswith("'"):
            return m.group(0)
        return '[@goto(' + '"' + target + '"' + ')]'

    return RE_GOTO_NQ.sub(repl_nq, text)


def compute_inline_style_ranges(text: str) -> list[dict]:
    """Генерирует inlineStyleRanges: [ ] -> BRACKETS, ( ) -> PARENTHESES, { } -> BRACES"""
    if not isinstance(text, str):
        return []
    ranges = []
    bracket_map = {
        "[": "BRACKETS",
        "]": "BRACKETS",
        "(": "PARENTHESES",
        ")": "PARENTHESES",
        "{": "BRACES",
        "}": "BRACES",
    }
    for i, ch in enumerate(text):
        if ch in bracket_map:
            ranges.append({
                "style": bracket_map[ch],
                "length": 1,
                "offset": i,
            })
    return ranges


def normalize_blocks_field(blocks_field: dict | None, *, fix_keys: bool = True) -> dict:
    if not blocks_field:
        return {"blocks": [], "entityMap": {}}
    blocks = blocks_field.get("blocks") or []
    out_blocks = []
    for block in blocks:
        b = dict(block)
        text = b.get("text", "")
        if isinstance(text, str):
            b["text"] = fix_goto_syntax(text)
        if fix_keys:
            key = b.get("key", "")
            if not key or RE_BLOCK_KEY_BAD.match(key) or len(key) != 5:
                b["key"] = random_block_key()
        b.setdefault("data", {})
        b.setdefault("type", "unstyled")
        b.setdefault("depth", 0)
        b.setdefault("entityRanges", [])
        # inlineStyleRanges: если уже есть — оставляем, если нет — генерируем из DSL-скобок
        if "inlineStyleRanges" not in b or not b["inlineStyleRanges"]:
            b["inlineStyleRanges"] = compute_inline_style_ranges(b.get("text", ""))
        out_blocks.append(b)
    return {"blocks": out_blocks, "entityMap": blocks_field.get("entityMap") or {}}


def ensure_ml_examples_empty_block(ml_examples: dict) -> dict:
    """ml_examples должен содержать хотя бы 1 пустой блок (как в экспорте ДОС)."""
    out = dict(ml_examples)
    out.setdefault("entityMap", {})
    blocks = out.get("blocks") or []
    if not blocks:
        out["blocks"] = [{
            "key": random_block_key(),
            "data": {},
            "text": "",
            "type": "unstyled",
            "depth": 0,
            "entityRanges": [],
            "inlineStyleRanges": [],
        }]
    return out


def normalize_dialog_node(node: dict, *, fix_keys: bool = True) -> dict:
    n = dict(node)
    for field in ("dl_rules", "answers", "ml_examples"):
        if field in n:
            n[field] = normalize_blocks_field(n.get(field), fix_keys=fix_keys)
    # ml_examples: обязательно 1 пустой блок (как в ДОС)
    n["ml_examples"] = ensure_ml_examples_empty_block(n.get("ml_examples") or {})
    if "slot_filling" not in n or not n["slot_filling"]:
        n["slot_filling"] = [
            {
                "id": secrets.token_urlsafe(8)[:10],
                "entity": {"id": "", "name": ""},
                "question": "",
                "required": False,
                "variable": {"id": "", "name": ""},
            }
        ]
    n.setdefault("responses", [])
    n.setdefault("shortcuts", [])
    n.setdefault("intent_id", None)
    n.setdefault("meta", {})
    n.setdefault("is_active", True)
    return n


def compute_master_hash(files: dict[str, bytes]) -> str:
    """40 hex-символов, детерминированно от содержимого JSON внутри обёртки."""
    digest = hashlib.sha256()
    for path in sorted(files):
        digest.update(path.encode("utf-8"))
        digest.update(b"\0")
        digest.update(files[path])
    return digest.hexdigest()[:40]


def build_metadata(
    lc_version: str | None = None,
    timestamp: str | None = None,
) -> dict:
    return {
        "lc_version": lc_version or DEFAULT_LC_VERSION,
        "timestamp": normalize_timestamp_string(timestamp) or format_dos_datetime(),
        "options": dict(DEFAULT_METADATA_OPTIONS),
    }


def load_staging(staging_dir: Path) -> tuple[dict[str, list[tuple[str, dict]]], dict | None]:
    """
    Читает staging/: EntityType/{id}.json
    Возвращает ({EntityType: [(filename, obj), ...]}, manifest или None)
    """
    manifest_path = staging_dir / "manifest.json"
    manifest = None
    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

    entities: dict[str, list[tuple[str, dict]]] = {}
    for sub in sorted(staging_dir.iterdir()):
        if not sub.is_dir():
            continue
        name = sub.name
        if name not in ENTITY_DIRS:
            continue
        items = []
        for fp in sorted(sub.glob("*.json")):
            obj = json.loads(fp.read_text(encoding="utf-8"))
            items.append((fp.name, obj))
        if items:
            entities[name] = items
    return entities, manifest


def collect_dict_names(entities: dict[str, list[tuple[str, dict]]]) -> set[str]:
    names: set[str] = set()
    for _, obj in entities.get("Dictionary", []):
        if obj.get("name"):
            names.add(obj["name"])
    for entity_dir in ("DialogNode", "Answer"):
        for _, obj in entities.get(entity_dir, []):
            blob = json.dumps(obj, ensure_ascii=False)
            for m in RE_DICT_REF.finditer(blob):
                names.add(m.group(1).strip())
    return names


def validate_entities(entities: dict[str, list[tuple[str, dict]]], report: ValidationReport) -> None:
    if "Assistant" not in entities:
        report.add("error", "MISSING_ASSISTANT", "Нет файла Assistant/*.json")
    if "Branch" not in entities:
        report.add("error", "MISSING_BRANCH", "Нет файла Branch/*.json")
    if "Skill" not in entities:
        report.add("error", "MISSING_SKILL", "Нет навыка Skill/*.json")
    if "DialogNode" not in entities:
        report.add("error", "MISSING_DIALOG_NODE", "Нет узла DialogNode/*.json")

    skill_ids = {o["id"] for _, o in entities.get("Skill", [])}
    dict_by_name = {o.get("name"): o for _, o in entities.get("Dictionary", [])}
    dict_ids = {o["id"] for _, o in entities.get("Dictionary", [])}
    assistant_ids = {o["id"] for _, o in entities.get("Assistant", [])}

    all_ids: dict[str, str] = {}
    for entity_dir, items in entities.items():
        for fname, obj in items:
            rel = f"{entity_dir}/{fname}"
            eid = obj.get("id", "")
            if not eid:
                report.add("error", "MISSING_ID", "Поле id отсутствует", rel)
                continue
            if not is_valid_entity_id(entity_dir, eid):
                report.add(
                    "error",
                    "INVALID_ID_FORMAT",
                    f"Неверный формат id для {entity_dir}: {eid}",
                    rel,
                )
            if fname != f"{eid}.json":
                report.add(
                    "error",
                    "FILENAME_ID_MISMATCH",
                    f"Имя файла должно быть {eid}.json",
                    rel,
                )
            if eid in all_ids:
                report.add(
                    "error",
                    "DUPLICATE_ID",
                    f"Дубликат id {eid} (также в {all_ids[eid]})",
                    rel,
                )
            all_ids[eid] = rel

            if entity_dir == "DialogNode":
                sk = obj.get("skill_id")
                if not sk or sk not in skill_ids:
                    report.add(
                        "error",
                        "BAD_SKILL_REF",
                        f"skill_id {sk!r} не найден в Skill/",
                        rel,
                    )
                for field in ("dl_rules", "answers", "ml_examples"):
                    for block in (obj.get(field) or {}).get("blocks") or []:
                        key = block.get("key", "")
                        if RE_BLOCK_KEY_BAD.match(key):
                            report.add(
                                "warning",
                                "SEMANTIC_BLOCK_KEY",
                                f"Семантический key блока: {key!r}",
                                f"{rel} ({field})",
                            )
                        text = block.get("text", "")
                        if "[goto(" in text:
                            report.add(
                                "error",
                                "GOTO_SYNTAX",
                                "Используйте [@goto(\"Имя узла\")], не [goto(...)]",
                                f"{rel} ({field})",
                            )

            for ts_field in ("created", "updated"):
                ts_val = obj.get(ts_field)
                if ts_val is None:
                    continue
                if not isinstance(ts_val, str):
                    continue
                if "+" in ts_val:
                    report.add(
                        "error",
                        "TIMESTAMP_TZ",
                        f'{ts_field} не должен содержать таймзону (+03:00), '
                        f'нужен формат 2026-05-25T06:54:24.862973 или 2026-05-26T14:15:51Z',
                        rel,
                    )
                elif not RE_DOS_NAIVE_TS.match(ts_val):
                    report.add(
                        "warning",
                        "TIMESTAMP_FORMAT",
                        f'{ts_field} ожидается YYYY-MM-DDTHH:MM:SS.ffffff (6 цифр после точки)',
                        rel,
                    )

            cr = obj.get("creator")
            if entity_dir != "Branch" and is_placeholder_creator(cr):
                report.add(
                    "error",
                    "PLACEHOLDER_CREATOR",
                    "creator не должен быть 00000000-... — укажите UUID пользователя "
                    "из своего экспорта ДОС (manifest.creator)",
                    rel,
                )

            if entity_dir == "Branch":
                aid = obj.get("assistant_id")
                if aid not in assistant_ids:
                    report.add(
                        "error",
                        "BAD_ASSISTANT_REF",
                        f"assistant_id {aid!r} не совпадает с Assistant/",
                        rel,
                    )
                if obj.get("name") != "master":
                    report.add(
                        "warning",
                        "BRANCH_NAME",
                        'Ожидается name="master" для ветки экспорта',
                        rel,
                    )

    referenced_dicts = collect_dict_names(entities)
    for dname in sorted(referenced_dicts):
        if dname not in dict_by_name:
            report.add(
                "error",
                "MISSING_DICTIONARY",
                f"В правилах/ответах есть [dict({dname})], но нет Dictionary с name={dname!r}",
                "DialogNode",
            )

    for _, obj in entities.get("Dictionary", []):
        rel = f"Dictionary/{obj.get('id', '')}.json"
        blocks = (obj.get("content") or {}).get("blocks") or []
        texts = [b.get("text", "") for b in blocks if b.get("text")]
        if not texts:
            report.add("error", "EMPTY_DICTIONARY", "Словарь без строк", rel)
            continue
        has_canon = any(not t.startswith("=>") for t in texts)
        if not has_canon:
            report.add(
                "error",
                "DICT_NO_CANON",
                f"Словарь {obj.get('name')!r}: нет главного слова (строка без =>). "
                "Нужен канон, затем =>синоним~",
                rel,
            )
        for t in texts:
            if not t.startswith("=>") and ("~" in t or "*" in t):
                report.add(
                    "warning",
                    "CANON_WITH_MASK",
                    f"Главное слово не должно содержать ~ или *: {t!r}",
                    rel,
                )


def validate_zip_structure(zip_path: Path, report: ValidationReport) -> dict[str, bytes] | None:
    """Проверяет layout ZIP; при успехе возвращает {path_in_zip: bytes} JSON внутри обёртки."""
    if not zip_path.exists():
        report.add("error", "FILE_NOT_FOUND", str(zip_path))
        return None

    with ZipFile(zip_path) as zf:
        names = zf.namelist()

        if any(n.endswith(".zip") and n.count("/") == 0 for n in names):
            report.add("error", "NESTED_ZIP", "Внутри архива не должно быть других .zip")

        json_top = [n for n in names if n.endswith(".json") and n.count("/") == 0]
        if "metadata.json" not in json_top:
            report.add("error", "MISSING_METADATA", "На верхнем уровне нужен metadata.json")

        wrappers = sorted({n.split("/")[0] for n in names if "/" in n and not n.endswith("/")})
        master_wrappers = [w for w in wrappers if "-master-" in w]
        bad_wrappers = [w for w in wrappers if "-master-" not in w]

        if len(master_wrappers) != 1:
            report.add(
                "error",
                "WRAPPER_COUNT",
                f"Ожидается ровно одна папка [assistant_id]-master-[40hex], найдено: {master_wrappers}",
            )
        if bad_wrappers:
            report.add(
                "error",
                "BAD_TOP_FOLDER",
                f"Лишняя папка верхнего уровня без -master-: {bad_wrappers}",
            )

        if len(master_wrappers) == 1:
            wrapper = master_wrappers[0]
            if not RE_WRAPPER.match(wrapper):
                report.add("error", "WRAPPER_FORMAT", f"Неверное имя обёртки: {wrapper}")

            for n in names:
                if n.startswith(wrapper + "/"):
                    part = n[len(wrapper) + 1 :]
                    if part and "/" not in part.rstrip("/"):
                        if part.endswith("/"):
                            folder = part.rstrip("/")
                            if folder == "NamesEntity":
                                report.add(
                                    "error",
                                    "TYPO_FOLDER",
                                    "Папка NamesEntity — опечатка, нужно NamedEntity",
                                    n,
                                )
                            elif folder not in ENTITY_DIRS:
                                report.add(
                                    "warning",
                                    "UNKNOWN_FOLDER",
                                    f"Неизвестная папка сущности: {folder}",
                                    n,
                                )

            try:
                meta = json.loads(zf.read("metadata.json"))
                for key in ("lc_version", "timestamp", "options"):
                    if key not in meta:
                        report.add(
                            "error",
                            "METADATA_SCHEMA",
                            f"metadata.json: нет поля {key}",
                            "metadata.json",
                        )
                if "assistant_id" in meta:
                    report.add(
                        "error",
                        "METADATA_SCHEMA",
                        "metadata.json: поле assistant_id не используется в экспорте ДОС",
                        "metadata.json",
                    )
                ts = meta.get("timestamp", "")
                if isinstance(ts, str) and ("+" in ts or ts.endswith("Z")):
                    report.add(
                        "error",
                        "METADATA_TIMESTAMP_TZ",
                        "metadata.timestamp без таймзоны, как 2026-05-25T06:56:22.782597",
                        "metadata.json",
                    )
            except Exception as e:
                report.add("error", "METADATA_PARSE", str(e), "metadata.json")

            inner_files: dict[str, bytes] = {}
            prefix = wrapper + "/"
            for n in names:
                if n.startswith(prefix) and n.endswith(".json"):
                    inner = n[len(prefix) :]
                    inner_files[inner] = zf.read(n)
            return inner_files

    return None


def validate_inner_json_files(
    inner_files: dict[str, bytes], report: ValidationReport
) -> None:
    entities: dict[str, list[tuple[str, dict]]] = {}
    for rel, raw in inner_files.items():
        parts = rel.split("/")
        if len(parts) != 2:
            report.add("warning", "JSON_PATH", f"Неожиданный путь JSON: {rel}")
            continue
        entity_dir, fname = parts
        if entity_dir not in ENTITY_DIRS:
            report.add("error", "UNKNOWN_ENTITY_DIR", entity_dir, rel)
            continue
        try:
            obj = json.loads(raw)
        except json.JSONDecodeError as e:
            report.add("error", "INVALID_JSON", str(e), rel)
            continue
        if "\n" in raw.decode("utf-8"):
            report.add(
                "warning",
                "JSON_NOT_MINIFIED",
                "JSON лучше хранить в одну строку (как в экспорте)",
                rel,
            )
        entities.setdefault(entity_dir, []).append((fname, obj))
    validate_entities(entities, report)


def normalize_all_entities(
    entities: dict[str, list[tuple[str, dict]]],
    manifest: dict | None,
    *,
    normalize_dsl: bool = True,
) -> dict[str, list[tuple[str, dict]]]:
    creator = (manifest or {}).get("creator") or DEFAULT_CREATOR
    export_ts = format_dos_datetime()
    out: dict[str, list[tuple[str, dict]]] = {}
    for entity_dir, items in entities.items():
        packed = []
        for fname, obj in items:
            if normalize_dsl:
                if entity_dir == "DialogNode":
                    obj = normalize_dialog_node(obj)
                elif entity_dir == "Dictionary":
                    content = obj.get("content")
                    if content:
                        obj = dict(obj)
                        obj["content"] = normalize_blocks_field(content)
            obj = normalize_entity_export_fields(
                obj, entity_dir, creator=creator, created=export_ts
            )
            packed.append((fname, obj))
        out[entity_dir] = packed
    return out


def pack_staging_to_zip(
    staging_dir: Path,
    output_zip: Path,
    *,
    normalize: bool = True,
) -> ValidationReport:
    report = ValidationReport()
    entities, manifest = load_staging(staging_dir)
    entities = normalize_all_entities(entities, manifest, normalize_dsl=normalize)
    validate_entities(entities, report)
    if not report.ok:
        return report

    assistants = [o for _, o in entities.get("Assistant", [])]
    assistant = assistants[0]
    assistant_id = assistant["id"]

    inner_bytes: dict[str, bytes] = {}
    for entity_dir, items in entities.items():
        for fname, obj in items:
            rel = f"{entity_dir}/{fname}"
            inner_bytes[rel] = minify_json(obj).encode("utf-8")

    master_hash = compute_master_hash(inner_bytes)
    wrapper = f"{assistant_id}-master-{master_hash}"

    output_zip.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(output_zip, "w") as zf:
        meta = build_metadata(
            (manifest or {}).get("lc_version"),
            (manifest or {}).get("timestamp"),
        )
        zf.writestr("metadata.json", minify_json(meta))
        for rel, data in sorted(inner_bytes.items()):
            zf.writestr(f"{wrapper}/{rel}", data)

    return report


def validate_zip(zip_path: Path) -> ValidationReport:
    report = ValidationReport()
    inner = validate_zip_structure(zip_path, report)
    if inner is not None:
        validate_inner_json_files(inner, report)
    return report


def validate_staging(staging_dir: Path) -> ValidationReport:
    report = ValidationReport()
    if not staging_dir.is_dir():
        report.add("error", "STAGING_NOT_FOUND", str(staging_dir))
        return report
    entities, _ = load_staging(staging_dir)
    validate_entities(entities, report)
    return report


def print_report(report: ValidationReport) -> int:
    for issue in report.issues:
        print(issue)
    if report.ok:
        print("OK: проверка пройдена.")
        return 0
    print(f"FAILED: ошибок — {sum(1 for i in report.issues if i.level == 'error')}.")
    return 1
