import re

path = r'C:\Users\Mariyaa\Desktop\скрипты\LLM\work\cat_simulator\6_RESPONSES_AUTHOR__RESPONSES.md'
with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

fixed = []
count = 0
for line in lines:
    m = re.match(r'\[if\(%cat_mood="([^"]+)"\)\]\{:lu:\s*(.+?)\}\s*$', line)
    if m:
        mood = m.group(1)
        inner = m.group(2)
        fixed.append(':lu: [if(%cat_mood="' + mood + '")]{ ' + inner + '} ' + '\n')
        count += 1
    else:
        fixed.append(line)

with open(path, 'w', encoding='utf-8') as f:
    f.writelines(fixed)

print('Done: fixed ' + str(count) + ' lines, total ' + str(len(fixed)) + ' lines')
