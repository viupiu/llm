# -*- coding: utf-8 -*-
import re
import sys
sys.stdout.reconfigure(encoding="utf-8")

rules = open('work/cat_simulator/3_RULES_AUTHOR__RULES_AND_DICTIONARIES.md', encoding='utf-8').read()

# Check dictionary parsing
dicts_simple = re.findall(r'## Словарь:\s*(\S+)', rules)
print("=== SIMPLE DICT FINDING ===")
for d in dicts_simple:
    print(f"  [{d}]")

# Check the issue - мат vs mat
print("\n=== MAT vs мат ===")
for m in re.finditer(r'## Словарь:\s*(\S+)', rules):
    name = m.group(1)
    if 'мат' in name or name == 'mat':
        print(f"  Found dict: {repr(name)} at position {m.start()}")

# Check keywords_cat_insult
print("\n=== KEYWORDS_CAT_INSULT ===")
idx = rules.find('keywords_cat_insult')
print(f"  Position in file: {idx}")
if idx > 0:
    print(f"  Context: {repr(rules[max(0,idx-50):idx+50])}")
