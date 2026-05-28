# -*- coding: utf-8 -*-
"""
Final cleanup:
1. Remove vtb_cities from registry table and section
2. Update descriptions for overlap pairs with usage notes
"""
from pathlib import Path

MD = Path(r'C:\Users\Mariyaa\Desktop\скрипты\LLM\docs\reference\COMMON_DICTIONARIES.md')
content = MD.read_text(encoding='utf-8')

# Normalize line endings
content = content.replace('\r\n', '\n').replace('\r', '\n')

lines = content.split('\n')
new_lines = []
skip_section = False
i = 0

while i < len(lines):
    line = lines[i]

    # --- 1. Remove vtb_cities section ---
    if line.strip() == '## `vtb_cities`':
        skip_section = True
        i += 1
        continue

    if skip_section:
        if line.startswith('## `'):
            skip_section = False
            new_lines.append('')
            new_lines.append(line)
            i += 1
        else:
            i += 1
        continue

    # --- 2. Remove vtb_cities registry entry ---
    if line.startswith('| `vtb_cities` |'):
        i += 1
        continue

    # --- 3. Update common_yes section description ---
    if line.strip() == '## `common_yes`':
        new_lines.append(line)
        i += 1
        if i < len(lines) and lines[i].strip() == '':
            new_lines.append('')
            i += 1
        if i < len(lines) and 'Согласие' in lines[i] and 'подтверждение' in lines[i]:
            new_lines.append('Согласие, подтверждение (да, верно, именно так). Используйте вместе с soglasen в ветках дерева — охватывает базовые утвердительные формы.')
            i += 1
        continue

    # --- 4. Update common_yes registry entry ---
    if line.startswith('| `common_yes` |'):
        parts = line.split('|')
        if len(parts) >= 4:
            new_line = '| `common_yes` | Согласие, подтверждение (да, верно). Используйте вместе с soglasen — охватывает базовые утвердительные формы. |%s' % parts[3]
            new_lines.append(new_line)
            i += 1
        else:
            new_lines.append(line)
            i += 1
        continue

    # --- 5. Update soglasen section description ---
    if line.strip() == '## `soglasen`':
        new_lines.append(line)
        i += 1
        if i < len(lines) and lines[i].strip() == '':
            new_lines.append('')
            i += 1
        if i < len(lines) and 'Согласие пользователя' in lines[i]:
            new_lines.append('Согласие пользователя (одобрение, подтверждение намерения). Используйте вместе с common_yes — охватывает контексты подтверждения.')
            i += 1
        continue

    # --- 6. Update soglasen registry entry ---
    if line.startswith('| `soglasen` |'):
        parts = line.split('|')
        if len(parts) >= 4:
            new_line = '| `soglasen` | Согласие пользователя (одобрение, подтверждение). Используйте вместе с common_yes. |%s' % parts[3]
            new_lines.append(new_line)
            i += 1
        else:
            new_lines.append(line)
            i += 1
        continue

    # --- 7. Update otkaz section description ---
    if line.strip() == '## `otkaz`':
        new_lines.append(line)
        i += 1
        if i < len(lines) and lines[i].strip() == '':
            new_lines.append('')
            i += 1
        if i < len(lines) and 'Отказ' in lines[i]:
            new_lines.append('Отказ, нет, не надо. Используйте вместе с dontwant в ветках дерева — охватывает прямые отказы и отрицания.')
            i += 1
        continue

    # --- 8. Update otkaz registry entry ---
    if line.startswith('| `otkaz` |'):
        parts = line.split('|')
        if len(parts) >= 4:
            new_line = '| `otkaz` | Отказ, нет, не надо. Используйте вместе с dontwant — охватывает прямые отказы. |%s' % parts[3]
            new_lines.append(new_line)
            i += 1
        else:
            new_lines.append(line)
            i += 1
        continue

    # --- 9. Update dontwant section description ---
    if line.strip() == '## `dontwant`':
        new_lines.append(line)
        i += 1
        if i < len(lines) and lines[i].strip() == '':
            new_lines.append('')
            i += 1
        if i < len(lines) and 'Не надо' in lines[i]:
            new_lines.append('Не надо, не хочу. Используйте вместе с otkaz — охватывает нежелание и отказ от действия.')
            i += 1
        continue

    # --- 10. Update dontwant registry entry ---
    if line.startswith('| `dontwant` |'):
        parts = line.split('|')
        if len(parts) >= 4:
            new_line = '| `dontwant` | Не надо, не хочу. Используйте вместе с otkaz — охватывает нежелание. |%s' % parts[3]
            new_lines.append(new_line)
            i += 1
        else:
            new_lines.append(line)
            i += 1
        continue

    # --- 11. Update common_like_2 section description ---
    if line.strip() == '## `common_like_2`':
        new_lines.append(line)
        i += 1
        if i < len(lines) and lines[i].strip() == '':
            new_lines.append('')
            i += 1
        if i < len(lines) and 'Строк' not in lines[i]:
            new_lines.append('Нравится, лайк, все времена. Общий словарь-объединённый. Для строгого настоящего времени используйте common_like_2_pres.')
            i += 1
        continue

    # --- 12. Update common_like_2 registry entry ---
    if line.startswith('| `common_like_2` |'):
        parts = line.split('|')
        if len(parts) >= 4:
            new_line = '| `common_like_2` | Нравится, лайк, все времена. Общий объединённый. Для настоящего используйте common_like_2_pres. |%s' % parts[3]
            new_lines.append(new_line)
            i += 1
        else:
            new_lines.append(line)
            i += 1
        continue

    # --- 13. Update common_like_2_pres section description ---
    if line.strip() == '## `common_like_2_pres`':
        new_lines.append(line)
        i += 1
        if i < len(lines) and lines[i].strip() == '':
            new_lines.append('')
            i += 1
        if i < len(lines) and 'Строк' not in lines[i]:
            new_lines.append('Нравится, лайк, настоящее время. Узкая present-форма. Для всех времён используйте common_like_2.')
            i += 1
        continue

    # --- 14. Update common_like_2_pres registry entry ---
    if line.startswith('| `common_like_2_pres` |'):
        parts = line.split('|')
        if len(parts) >= 4:
            new_line = '| `common_like_2_pres` | Нравится, лайк, настоящее время. Узкая present. Для всех времён используйте common_like_2. |%s' % parts[3]
            new_lines.append(new_line)
            i += 1
        else:
            new_lines.append(line)
            i += 1
        continue

    new_lines.append(line)
    i += 1

content = '\n'.join(new_lines)
MD.write_text(content, encoding='utf-8')

# Verify
final = MD.read_text(encoding='utf-8')
print('vtb_cities section present:', '## `vtb_cities`' in final)
print('vtb_cities in table:', '| `vtb_cities`' in final)
print('File size:', MD.stat().st_size)
print('Done.')
