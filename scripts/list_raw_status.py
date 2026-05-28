# -*- coding: utf-8 -*-
import json, re
from pathlib import Path

ROOT = Path(r'C:\Users\Mariyaa\Desktop\скрипты\LLM')
RAW = ROOT / 'docs' / 'reference' / 'raw_dicts'
MD = ROOT / 'docs' / 'reference' / 'COMMON_DICTIONARIES.md'

content = MD.read_text(encoding='utf-8')
registry_start = content.find('## Реестр словарей')
first_section = content.find('\n## `', registry_start + 1)
registry_block = content[registry_start:first_section] if first_section > 0 else content[registry_start:]
registry_names = set()
for m in re.finditer(r'\|\s*`([^`]+)`\s*\|', registry_block):
    v = m.group(1)
    if v in ('Словарь', 'Смысл', 'Строк'):
        continue
    registry_names.add(v)

raw_in = []
raw_out = []
for jf in sorted(RAW.glob('*.json')):
    data = json.loads(jf.read_text(encoding='utf-8'))
    item = data[0] if isinstance(data, list) else data
    cn = item.get('name', '')
    lc = len(item.get('content', {}).get('blocks', []))
    if cn in registry_names:
        raw_in.append((cn, jf.name, lc))
    else:
        raw_out.append((cn, jf.name, lc))

out = []
out.append('=== RAW DICTS PENDING IMPORT (%d) ===' % len(raw_out))
for cn, fn, lc in raw_out:
    out.append('  %s (%d lines) <- %s' % (cn, lc, fn))
out.append('')
out.append('=== RAW DICTS ALREADY IN REGISTRY - skipped (%d) ===' % len(raw_in))
for cn, fn, lc in raw_in:
    out.append('  %s (%d lines) <- %s' % (cn, lc, fn))

full = '\n'.join(out)
Path(r'C:\Users\Mariyaa\Desktop\скрипты\LLM\scripts\raw_dicts_status.txt').write_text(full, encoding='utf-8')
print(full)
print('\n(Retained raw_dicts in registry: %d)' % len(raw_in))
print('(Pending import: %d)' % len(raw_out))