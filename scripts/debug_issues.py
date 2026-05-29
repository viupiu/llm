# -*- coding: utf-8 -*-
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

resp = open('work/cat_simulator/6_RESPONSES_AUTHOR__RESPONSES.md', encoding='utf-8').read()
rules = open('work/cat_simulator/3_RULES_AUTHOR__RULES_AND_DICTIONARIES.md', encoding='utf-8').read()

# Debug goto
gotos = re.findall(r'@goto\("([^"]+)"\)', resp)
resp_nodes = re.findall(r'## Узел:\s*(.+)', resp)
rule_nodes = re.findall(r'## Узел:\s*(.+)', rules)
all_nodes = set(resp_nodes) | set(rule_nodes)

print("=== GOTO TARGETS ===")
for g in set(gotos):
    print(f"  [{g}] in all_nodes: {g in all_nodes}")
    if g not in all_nodes:
        # Check for whitespace/encoding issues
        matches = [n for n in all_nodes if n.strip() == g.strip()]
        print(f"    Strip matches: {matches}")
        print(f"    GOTO repr: {repr(g)}")
        # Find closest matches
        for n in resp_nodes:
            if "Мяу" in n:
                print(f"    Node: {repr(n)}")
                print(f"    Match: {n == g}")

print("\n=== DICTIONARY ISSUES ===")
# Check мат vs mat
for m in re.finditer(r'\[dict\(([^)]+)\)\]', rules):
    ref = m.group(1)
    if ref in ['mat', 'keywords_cat_insult']:
        line_start = rules.rfind('\n', 0, m.start()) + 1
        line_end = rules.find('\n', m.start())
        line = rules[line_start:line_end]
        print(f"  Ref: {repr(ref)} in line: {line}")

# Check мат definition
mat_match = re.search(r'## Словарь:\s*(\S+)', rules, re.M)
if mat_match:
    # Find the мат dictionary
    for m in re.finditer(r'## Словарь:\s*(\S+)', rules):
        name = m.group(1)
        if name in ['мат', 'mat']:
            # Check first char
            print(f"  Dict def: {repr(name)} (first char code: {ord(name[0])})")
