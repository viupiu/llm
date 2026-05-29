# -*- coding: utf-8 -*-
import re
import sys
sys.stdout.reconfigure(encoding="utf-8")

resp = open('work/cat_simulator/6_RESPONSES_AUTHOR__RESPONSES.md', encoding='utf-8').read()

def parse_node_from_header(text):
    m = re.search(r"## Узел:\s*(.+)", text)
    return m.group(1).strip() if m else ""

sections = re.split(r"---\s*$", resp, flags=re.M)
print(f"Number of sections: {len(sections)}")
result = []
for i, sec in enumerate(sections):
    node = parse_node_from_header(sec)
    if node:
        result.append(node)
        print(f"  Section {i}: {repr(node)}")
    else:
        preview = sec[:100].replace('\n', '\\n')
        print(f"  Section {i}: NO NODE (preview: {preview})")

print(f"\nResult: {len(result)} nodes: {result}")
