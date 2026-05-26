import json
import os
import shutil
import random
import uuid
import zipfile
from pathlib import Path

LLM_DIR = Path(r"C:\Users\Mariyaa\Desktop\скрипты\LLM")
BASE = LLM_DIR / "simple_assistant"
SRC = BASE / r"a1b2c3d4-e5f6-7890-abcd-ef1234567890-master-00000000000000000000000000000000000001"
OUT = LLM_DIR / "rebuilt"

if OUT.exists():
    shutil.rmtree(OUT)
OUT.mkdir()

def rand_uuid4():
    return str(uuid.uuid4())

def rand_short_id():
    u = str(uuid.uuid4())
    parts = u.split("-")
    return f"{parts[0]}-{parts[1]}-{parts[2]}-{parts[3]}"

old_ids = {
    "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    "a1b2c3d4-e5f6-7890-abcd-0001",
    "a1b2c3d4-e5f6-7890-abcd-0002",
    "n1000000-0000-0000-0000-000000000001",
    "n1000000-0000-0000-0000-000000000002",
    "n1000000-0000-0000-0000-000000000003",
    "d1000000-0000-0000-0000-000000000001",
    "d1000000-0000-0000-0000-000000000002",
    "v1000000-0000-0000-0000-000000000001",
    "v1000000-0000-0000-0000-000000000002",
    "aeeb1e18-bb4f-4c71-a050-09489d44b751",
}

id_map = {}
for oid in old_ids:
    if oid.startswith("a1b2c3d4-e5f6-7890-abcd-ef12"):
        id_map[oid] = rand_uuid4()
    elif oid.startswith("aeeb1e18"):
        id_map[oid] = rand_uuid4()
    else:
        id_map[oid] = rand_short_id()

ASSISTANT_ID = id_map["a1b2c3d4-e5f6-7890-abcd-ef1234567890"]
MASTER_HASH = hex(random.getrandbits(160))[2:].zfill(40)
WRAPPER = f"{ASSISTANT_ID}-master-{MASTER_HASH}"

print("ID mapping:")
for k, v in sorted(id_map.items()):
    print(f"  {k} -> {v}")
print(f"\nWrapper: {WRAPPER}")

wrapper_dir = OUT / WRAPPER
wrapper_dir.mkdir(parents=True)

for d in ["Answer", "DialogNodeTag", "Tag", "Assistant", "Branch", "DialogNode", "Dictionary", "Skill", "Variable"]:
    (wrapper_dir / d).mkdir()

replace_keys = {"id", "assistant_id", "skill_id", "parent_id", "intent_id"}

def replace_ids(obj):
    if isinstance(obj, dict):
        result = {}
        for k, v in obj.items():
            if k in replace_keys and v and v in id_map:
                result[k] = id_map[v]
            else:
                result[k] = replace_ids(v)
        return result
    elif isinstance(obj, list):
        return [replace_ids(item) for item in obj]
    elif isinstance(obj, str):
        for oid in id_map:
            obj = obj.replace(oid, id_map[oid])
        return obj
    return obj

for json_path in SRC.rglob("*.json"):
    rel = json_path.relative_to(SRC)
    entity_type = rel.parts[0]
    filename = rel.parts[1]
    old_id = filename.replace(".json", "")
    
    if old_id not in id_map:
        continue
    
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.loads(f.read())
    
    data = replace_ids(data)
    
    new_id = id_map[old_id]
    new_filename = f"{new_id}.json"
    dest = wrapper_dir / entity_type / new_filename
    
    with open(dest, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, separators=(",", ":"))

shutil.copy2(BASE / "metadata.json", OUT / "metadata.json")

zip_path = LLM_DIR / "simple_assistant_prod.zip"
if zip_path.exists():
    zip_path.unlink()

with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
    z.write(OUT / "metadata.json", "metadata.json")
    for root, dirs, files in os.walk(wrapper_dir):
        for fn in files:
            fp = Path(root) / fn
            arc = fp.relative_to(OUT)
            z.write(fp, str(arc).replace("\\", "/"))

print(f"\nDone! Archive: {zip_path}")
print(f"Size: {zip_path.stat().st_size} bytes")
