import json, pathlib

staging = pathlib.Path("work/mini_quest_bot/9_PACKAGER__STAGING/DialogNode")
for f in sorted(staging.glob("*.json")):
    d = json.loads(f.read_text(encoding="utf-8"))
    ml = d.get("ml_examples", {}).get("blocks", [])
    dl = d.get("dl_rules", {}).get("blocks", [])
    ml_c = len([b for b in ml if b.get("text", "").strip()])
    dl_c = len([b for b in dl if b.get("text", "").strip()])
    name = d["name"][:55]
    print(f"{name:55s}  ML={ml_c:3d}  DL={dl_c:3d}")
