# -*- coding: utf-8 -*-
import re, json
from pathlib import Path
from collections import Counter

ROOT = Path(r'C:\Users\Mariyaa\Desktop\скрипты\LLM')
MD = ROOT / 'docs' / 'reference' / 'COMMON_DICTIONARIES.md'
RAW = ROOT / 'docs' / 'reference' / 'raw_dicts'

content = MD.read_text(encoding='utf-8')

# Extract section header names
section_names = []
for m in re.finditer(r'^##\s+`([^`]+)`$', content, re.MULTILINE):
    section_names.append(m.group(1))

# Extract registry table names (only the registry block)
registry_start = content.find('## Реестр словарей')
first_section = content.find('\n## `', registry_start + 1)
registry_block = content[registry_start:first_section] if first_section > 0 else content[registry_start:]
registry_table_names = set()
for m in re.finditer(r'\|\s*`([^`]+)`\s*\|', registry_block):
    val = m.group(1)
    if val in ('Словарь', 'Смысл', 'Строк'):
        continue
    registry_table_names.add(val)

section_names_set = set(section_names)

# Extract raw dict canonical names
raw_names = []
for jf in sorted(RAW.glob('*.json')):
    try:
        data = json.loads(jf.read_text(encoding='utf-8'))
        item = data[0] if isinstance(data, list) else data
        raw_names.append((item.get('name', ''), jf.name))
    except Exception as e:
        raw_names.append((None, jf.name))

print('=== CONSISTENCY CHECK ===')
print()

# 1. Registry table entries
print('Registry table entries: %d' % len(registry_table_names))

# 2. Section headers
print('Section headers: %d' % len(section_names_set))

# 3. Duplicates within registry
reg_counts = Counter(list(registry_table_names))
dupes_in_registry = {k: v for k, v in reg_counts.items() if v > 1}
if dupes_in_registry:
    print('\n!!! DUPLICATES IN REGISTRY TABLE (%d):' % len(dupes_in_registry))
    for k, v in dupes_in_registry.items():
        print('  %s: %d times' % (k, v))
else:
    print('\nRegistry table: no duplicates.')

# 4. Duplicates within sections
sec_counts = Counter(section_names)
dupes_in_sections = {k: v for k, v in sec_counts.items() if v > 1}
if dupes_in_sections:
    print('DUPLICATES IN SECTION HEADERS (%d):' % len(dupes_in_sections))
    for k, v in dupes_in_sections.items():
        print('  %s: %d times' % (k, v))
else:
    print('Section headers: no duplicates.')

# 5. Registry entries without section
missing_sections = registry_table_names - section_names_set
if missing_sections:
    print('\n!!! REGISTRY ENTRIES WITHOUT SECTION (%d):' % len(missing_sections))
    for n in sorted(missing_sections):
        print('  %s' % n)
else:
    print('All registry entries have matching sections.')

# 6. Sections without registry entry
missing_registry = section_names_set - registry_table_names
if missing_registry:
    print('\n!!! SECTIONS WITHOUT REGISTRY ENTRY (%d):' % len(missing_registry))
    for n in sorted(missing_registry):
        print('  %s' % n)
else:
    print('All sections have matching registry entries.')

# 7. Raw dicts status
raw_in_registry = []
raw_not_imported = []
raw_bad_json = []
for canon_name, fname in raw_names:
    if canon_name is None:
        raw_bad_json.append(fname)
    elif canon_name in registry_table_names:
        raw_in_registry.append((canon_name, fname))
    else:
        raw_not_imported.append((canon_name, fname))

print('\n--- RAW DICTS STATUS ---')
print('Raw dicts already in registry: %d' % len(raw_in_registry))
print('Raw dicts NOT yet imported: %d' % len(raw_not_imported))
print('Raw dicts with parse errors: %d' % len(raw_bad_json))

# 8. Semantic overlap warnings
print('\n--- SEMANTIC OVERLAP CANDIDATES ---')
if 'vtb_cities' in registry_table_names and 'word_geography_cityrussian' in registry_table_names:
    print('WARNING: vtb_cities (141 rows) vs word_geography_cityrussian (243 rows) — both Russia cities')
if 'common_yes' in registry_table_names and 'soglasen' in registry_table_names:
    print('WARNING: common_yes (186 rows) vs soglasen (159 rows) — both agreement/confirmation')
if 'otkaz' in registry_table_names and 'dontwant' in registry_table_names:
    print('WARNING: otkaz (233 rows) vs dontwant (56 rows) — both refusal/negative intent')
if 'common_like_2' in registry_table_names and 'common_like_2_pres' in registry_table_names:
    print('WARNING: common_like_2 (129 rows) vs common_like_2_pres (129 rows) — same count, possible duplicate')

# 9. Description quality check
print('\n--- DESCRIPTION QUALITY ---')
placeholder_count = 0
tautology_count = 0
bad_descriptions = []

for dict_name in sorted(registry_table_names):
    # Find description in registry table
    pattern = r'\|\s*`%s`\s*\|\s*([^|]+)\s*\|' % re.escape(dict_name)
    m = re.search(pattern, registry_block)
    if m:
        desc = m.group(1).strip()
        if desc == '— смысл определить Библиотекарю —':
            placeholder_count += 1
            bad_descriptions.append((dict_name, desc, 'placeholder'))
        # Check for tautology: description repeats the name
        if dict_name in desc and desc.startswith('Словарь'):
            tautology_count += 1
            bad_descriptions.append((dict_name, desc, 'tautology'))

print('Placeholder descriptions: %d' % placeholder_count)
print('Tautology descriptions (repeat name): %d' % tautology_count)

if bad_descriptions:
    print('\nProblematic descriptions:')
    for dn, ds, tag in bad_descriptions:
        print('  [%s] %s -> "%s"' % (tag, dn, ds))

print('\n=== END CONSISTENCY CHECK ===')
