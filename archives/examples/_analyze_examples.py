# -*- coding: utf-8 -*-
import json
from pathlib import Path
from collections import Counter, defaultdict

base = Path(__file__).parent / "_extracted"
bots = [d for d in base.iterdir() if d.is_dir()]


def load_folder(bot_root):
    inner = [p for p in bot_root.iterdir() if p.is_dir()]
    if not inner:
        return None
    root = inner[0]
    data = {"name": bot_root.name, "root": root}
    for sub in [
        "Assistant",
        "DialogNode",
        "Variable",
        "Skill",
        "Dictionary",
        "Branch",
        "Answer",
        "ConflictNode",
    ]:
        p = root / sub
        data[sub] = []
        if p.exists():
            for f in p.glob("*.json"):
                try:
                    data[sub].append(json.loads(f.read_text(encoding="utf-8")))
                except Exception:
                    pass
    meta = bot_root / "metadata.json"
    if meta.exists():
        data["metadata"] = json.loads(meta.read_text(encoding="utf-8"))
    return data


all_vars = {}
all_skills = {}
all_dicts = {}
all_event_types = Counter()
all_node_types = Counter()

for bot_dir in sorted(bots):
    d = load_folder(bot_dir)
    if not d:
        continue
    short = "KLINING" if "Klining" in d["name"] or "Klining" in bot_dir.name else "FPK"
    print("=" * 80)
    print("BOT:", short, "|", d["name"][:70])
    print("=" * 80)

    if d.get("metadata"):
        print("metadata:", json.dumps(d["metadata"], ensure_ascii=False))

    for a in d["Assistant"]:
        print("\n--- ASSISTANT ---")
        for k in ("id", "name", "description", "type", "status", "language", "channelType"):
            if k in a:
                print(f"  {k}: {a[k]}")

    print(f"\n--- VARIABLES ({len(d['Variable'])}) ---")
    for v in sorted(d["Variable"], key=lambda x: x.get("name", "")):
        dv = v.get("defaultValue", v.get("default", ""))
        print(
            f"  {v.get('name')} | type={v.get('type')} | scope={v.get('scope')} | default={str(dv)[:60]}"
        )
        all_vars.setdefault(v.get("name"), []).append(short)

    print(f"\n--- SKILLS ({len(d['Skill'])}) ---")
    for s in sorted(d["Skill"], key=lambda x: x.get("name", "")):
        print(f"  {s.get('name')} | type={s.get('type')} | desc={str(s.get('description',''))[:50]}")
        all_skills.setdefault(s.get("name"), []).append(short)

    print(f"\n--- DICTIONARIES ({len(d['Dictionary'])}) ---")
    for dic in sorted(d["Dictionary"], key=lambda x: x.get("name", "")):
        content = dic.get("content", {})
        blocks = content.get("blocks", []) if isinstance(content, dict) else []
        print(f"  {dic.get('name')} | blocks={len(blocks)}")
        all_dicts.setdefault(dic.get("name"), []).append(short)

    nodes = d["DialogNode"]
    print(f"\n--- DIALOG NODES ({len(nodes)}) ---")
    types = Counter(n.get("type") for n in nodes)
    print("  node types:", dict(types))
    all_node_types.update(types)

    events_by_type = Counter()
    events_by_name = Counter()
    slot_nodes = []
    anchors = []
    marks = []
    actions = []

    for n in nodes:
        for e in n.get("events") or []:
            et = e.get("type", "?")
            events_by_type[et] += 1
            all_event_types[et] += 1
            if e.get("name"):
                events_by_name[e.get("name")] += 1
        if n.get("slot_filling"):
            slot_nodes.append(n.get("name"))
        cond = n.get("conditions") or ""
        if "that_anchor" in str(cond):
            anchors.append((n.get("name"), cond[:80]))
        if "last_mark" in str(cond):
            marks.append(n.get("name"))
        ans = n.get("answers") or {}
        for b in (ans.get("blocks") or [] if isinstance(ans, dict) else []):
            t = b.get("text", "")
            if "[action]" in t or "action" in t.lower():
                actions.append(n.get("name"))

    print("  event types:", dict(events_by_type.most_common()))
    print("  event names:", dict(events_by_name.most_common(20)))
    if slot_nodes:
        print(f"  slot_filling nodes ({len(slot_nodes)}):", slot_nodes[:15])
    if anchors:
        print(f"  that_anchor nodes ({len(anchors)}): sample", anchors[:5])
    if marks:
        print(f"  last_mark nodes ({len(marks)}):", marks[:10])

    # Skills per node
    by_skill = defaultdict(list)
    for n in nodes:
        by_skill[n.get("skill_id", "none")].append(n.get("name"))
    skill_map = {s["id"]: s.get("name") for s in d["Skill"]}
    print("\n  nodes per skill:")
    for sid, names in sorted(by_skill.items(), key=lambda x: -len(x[1])):
        sname = skill_map.get(sid, sid[:8] if sid else "?")
        print(f"    {sname}: {len(names)} nodes")

    print("\n  ALL NODES:")
    for n in sorted(nodes, key=lambda x: (x.get("skill_id", ""), x.get("type", ""), x.get("name", ""))):
        ev = [e.get("type") for e in (n.get("events") or [])]
        skill = skill_map.get(n.get("skill_id"), "?")
        rules = n.get("dl_rules") or n.get("rules")
        has_rules = bool(rules)
        cond = (n.get("conditions") or "")[:40]
        print(
            f"    [{n.get('type')}] {n.get('name')} | skill={skill} | events={ev} | rules={has_rules} | cond={cond}"
        )

    print(f"\n--- BRANCH ({len(d['Branch'])}) ---")
    for b in d["Branch"]:
        print(f"  {b.get('name')} | id={b.get('id')}")

    print(f"\n--- ANSWERS ({len(d['Answer'])}) ---")
    print(f"--- CONFLICT ({len(d['ConflictNode'])}) ---")

print("\n" + "=" * 80)
print("CROSS-BOT COMPARISON")
print("=" * 80)
print("Common variables:", [k for k, v in all_vars.items() if len(v) == 2])
print("Common skills:", [k for k, v in all_skills.items() if len(v) == 2])
print("KLINING-only vars:", [k for k, v in all_vars.items() if v == ["KLINING"]])
print("FPK-only vars:", [k for k, v in all_vars.items() if v == ["FPK"]])
print("Node types overall:", dict(all_node_types))
print("Event types overall:", dict(all_event_types))
