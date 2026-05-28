# -*- coding: utf-8 -*-
"""
Update placeholder and tautology descriptions in COMMON_DICTIONARIES.md.
Uses simple string matching instead of fragile regex.
"""
from pathlib import Path

ROOT = Path(r'C:\Users\Mariyaa\Desktop\скрипты\LLM')
MD = ROOT / 'docs' / 'reference' / 'COMMON_DICTIONARIES.md'

content = MD.read_text(encoding='utf-8')

descriptions = {
    'hello_all': 'Агрегатный словарь приветствий (объединяет hello_hello, hello_zdravstvuy, hello_helloenglish через --include)',
    'hello_dobr_utro': 'Приветствие «доброе утро» и опечатки',
    'hello_dobr_vecher': 'Приветствие «добрый вечер» и опчатки',
    'hello_hello': 'Неформальные приветствия: привет, салют, добрый день, интернациональные формы (хай, шалом, бонжур)',
    'hello_helloenglish': 'Приветствие на английском: хай, хэллоу и опечатки',
    'hello_zdravstvuy': 'Формальное приветствие «здравствуйте», «дарова» и опечатки',
    'horoscope_horoscope': 'Гороскоп, астрологический прогноз',
    'inf_vocatives': 'Обращения к ИИ-ассистенту: инф, бот, робот, железяка',
    'infius2_inf': 'Словари обращений к ИИ: инф, бот, робот, чатбот, персонаж, виртуальный собеседник (падежи и опечатки)',
    'infius2_know_2': 'Глагол «знать» во 2-м лице: знаешь, знаете (опечатки)',
    'infius2_question': 'Слово «вопрос» и опечатки',
    'infius2_speak_2': 'Глагол «разговаривать» во 2-м лице: разговариваешь, разговариваете (опечатки)',
    'infius2_word': 'Русские буквы алфавита для распознания одиночных символов',
    'infius_mudak_all': 'Оскорбления: мудазвон, мудак и производные',
    'infs_create_past': 'Глаголы создания в прошедшем времени: создал, сделал, разработал, написал, запрограммировал (опечатки)',
    'infs_created': 'Пассивные формы создания: создан, сделан, реализован, разработан, написан (опечатки)',
    'infs_creator': 'Роли авторов и создателей: автор, программист, разработчик, дизайнер, создатель (опечатки)',
    'internet_vkontakte': 'Социальная сеть ВКонтакте и опечатки',
    'intrj_all': 'Междометия, вводные слова и разговорные частицы: короче, типа, блин, вообще, как бы, вроде',
    'juice': 'Сок, сок и падежные формы',
    'rus_names_female': 'Женские имена: стандартные, уменьшительно-ласкательные и производные формы',
    'rus_names_male': 'Мужские имена: стандартные, уменьшительно-ласкательные и производные формы',
    'rus_names_malefemale': 'Унисекс и андрогинные имена',
}

placeholder = '\u2014 \u0441\u043c\u044b\u0441\u043b \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0438\u0442\u044c \u0411\u0438\u0431\u043b\u0438\u043e\u0442\u0435\u043a\u0430\u0440\u044e \u2014'
# Tautology patterns: "Словарь {name} — описание словаря `name`"
# We'll look for lines containing the dict name in the description

lines = content.split('\n')
updated = 0

for dict_name, new_desc in descriptions.items():
    # Track what we've updated for this dict
    table_done = False
    section_done = False
    
    for i, line in enumerate(lines):
        # --- Registry table entries ---
        # Format: | `dict_name` | description | count |
        if not table_done and line.startswith('| `' + dict_name + '` |'):
            # Find the description (between 2nd and 3rd pipe)
            pipe1 = line.index('|', 3)  # after `name`
            pipe2 = line.rindex(' |')   # before count
            before = line[:pipe1 + 1] + ' '
            after = line[pipe2:]
            lines[i] = before + new_desc + after
            table_done = True
            updated += 1
            print(f'  [TABLE] Updated {dict_name}')
            continue
        
        # --- Section entries ---
        # Format: ## `dict_name`\n\n<description>\n\nСтрок в словаре:
        if not section_done and line == '## `' + dict_name + '`':
            # Next non-empty line should be the description
            for j in range(i+1, min(i+5, len(lines))):
                stripped = lines[j].strip()
                if stripped == '':
                    continue
                # This is the description line (or paragraph)
                # Replace it with new description
                if placeholder in stripped:
                    lines[j] = new_desc
                    section_done = True
                    updated += 1
                    print(f'  [SECTION] Updated {dict_name} (placeholder)')
                    break
                elif f'`{dict_name}`' in stripped and stripped.startswith('Словарь '):
                    lines[j] = new_desc
                    section_done = True
                    updated += 1
                    print(f'  [SECTION] Updated {dict_name} (tautology)')
                    break
                else:
                    break
    
    if not table_done:
        print(f'  [MISSING TABLE] {dict_name}')
    if not section_done:
        print(f'  [MISSING SECTION] {dict_name}')

new_content = '\n'.join(lines)
MD.write_text(new_content, encoding='utf-8')
print(f'\nTotal updates: {updated}')
print(f'File size: {MD.stat().st_size} bytes')
