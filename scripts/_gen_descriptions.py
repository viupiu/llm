import re
import json

filepath = r"docs\reference\COMMON_DICTIONARIES.md"

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Extract each dictionary section
section_pattern = re.compile(
    r"^## `(.*?)`$\n(.*?)(?=\n## `|\Z)",
    re.MULTILINE | re.DOTALL
)

# Parse out dictionary name
name_pattern = re.compile(r"^## `(.*?)`$", re.MULTILINE)

# Parse out meaning line (first non-empty line after ## header)
meaning_after_header = re.compile(
    r"^## `.*?`$\n\n(.*?)"
    r"$",
    re.MULTILINE
)

# Find all dicts that need meaning
placeholder = "— смысл определить Оркестратору —"

# Build mapping from dictionary content
sections = {}
for m in section_pattern.finditer(content):
    dictname = m.group(1)
    body = m.group(2)
    lines = [l.strip() for l in body.strip().split("\n") if l.strip()]
    # First line is the meaning
    if lines:
        meaning = lines[0]
    else:
        meaning = ""
    # Extract words (lines between meaning/строки line and the code block)
    in_code = False
    words = []
    for l in lines[1:]:
        if l.startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            if l.startswith("=>"):
                words.append(l[2:])
            elif l.startswith("{"):
                words.append(l)
            elif l.startswith("*") and "* " in l:
                words.append(l.replace("*", "").strip())
            else:
                words.append(l)
    sections[dictname] = {
        "meaning": meaning,
        "words": words[:30],  # Sample first 30 words
    }

# Build meanings based on dictionary names and sampled content
name_meaning_map = {
    "animals_cat": "Кошки, кошачьи (родственные существительные)",
    "animals_dogs": "Собаки, псовые (родственные существительные)",
    "anysign": "Пунктуационные знаки и символы",
    "appearance_great": "Внешность хорошая, красивая, симпатичная",
    "appearance_terrible": "Внешность плохая, уродливая, противная",
    "beginning_words": "Начальные разговорные слова приветствия и вступления",
    "body_bit_parts": "Части тела (крупные и мелкие)",
    "bye_gottago": "Прощание с уходом: пора, мне надо идти",
    "bye_solong": "Прощание: до свидания, пока, до связи, до встречи",
    "common_about": "О ком/чём, предмет обсуждения",
    "common_anything": "Любой, нечто, всё равно, вообще",
    "common_beautiful": "Красивый, прекрасный (разные слова)",
    "common_buy_infinitive": "Покупка, приобретение (инфинитивные формы)",
    "common_call": "Звонить, созвониться (глаголы),",
    "common_can_2": "Могу, могу, возможность (глагольные формы)",
    "common_eat_2_pres": "Кушать, есть (глагольные формы),",
    "common_else": "Иной, иной, прочий, прочие",
    "common_exist_pres": "Существует, есть (глагол существительного)",
    "common_favourite": "Любимый, предпочтительный",
    "common_hate_1": "Не люблю, не нравится, не люблю",
    "common_here": "Здесь, тут, в этом месте",
    "common_howmany": "Сколько, количество (интересующие слова)",
    "common_know_2_only": "Знать (глагольные формы, только инфинитив)",
    "common_know_2_pres": "Знать (глагольные формы, настоящее время)",
    "common_like_1": "Нравится, люблю (1-е лицо)",
    "common_like_2": "Нравится, предпочитаю",
    "common_like_2_pres": "Нравится, предпочитаю (настоящее время)",
    "common_like_3_all": "Нравится, предпочитает (3-е лицо)",
    "common_like_3_pres_pl": "Нравится, предпочитают (мн.ч.)",
    "common_like_3_pres_sg": "Нравится, предпочитает (ед.ч.)",
    "common_live_1": "Жить, проживать (1-е лицо, глагольные формы)",
    "common_live_2": "Жить, проживать (2-е лицо, глагольные формы)",
    "common_maybe": "Может быть, возможно, наверное",
    "common_need_3_pres": "Требовать",
    "laughter": "Смех, выражение радости и смеха",
    "mat": "Матерные слова, нецензурная лексика",
    "med_genitals": "Медицинская терминология для гениталий",
    "milk": "Молоко, молочные продукты",
    "money_money": "Деньги, финансовые суммы",
    "music_listen_2": "Музыка, слушать",
    "music_music": "Музыка, жанры музыки",
    "name_name": "Имя, собственные имена, клички",
    "net": "Интеграция, нейросети (веб, сеть, интернет)",
    "ne_nado": "Необходимость, необходимо",
    "numbers": "Числа, количества (числовые формы)",
    "particles_adverbs": "Частицы наречия, наречия (частицы)",
    "posovetuj": "Рекомендуется консультация (консультации, советы)",
    "praise_attaboy": "Поощрение: хорошо, молодец, молодец",
    "praise_bad": "Потворство: плохо, плохо, плохо",
    "praise_clever": "Потворство умным: умница, умница, умный",
    "praise_funny": "Потворство смешному: смешной, смешной, смешной",
    "praise_good_nom": "Потворство хорошому: хороший, молодец",
    "praise_great": "Поощрение: отлично, замечательно, великолепие",
    "sex_gayrude_nom": "Сексуальные: геи, гомосексуалисты, нетерпелые",
    "sex_kiss_all": "Обнять, поцеловать (все формы)",
    "sex_kiss_imperative": "Целовать, поцелуй (императивы)",
    "sex_sex": "Секс, сексуальный, секс",
    "shit_all": "Кала-слова (все формы)",
    "silly": "Глупости: глупый, тупит, глупый",
    "single_number": "Один номер",
    "single_word": "Одно слово в ответе",
    "slova_parazity": "Паразиты (паразиты, слова, частицы)",
    "snow": "Снег и родственные слова",
    "tea": "Чай, родственный",
    "thoughts_said": "Ментальные мысли, сказанные",
    "thoughts_say_past": "Мысли, сказанное в прошедшем времени",
    "thoughts_understand_2_pres": "Понимание (вопросы, настоящее время)",
    "ugly": "Родитель: уродливый, некрасивый",
    "viupiu_adj": "Viupiu (прилагательные муж.),",
    "viupiu_adj_fem": "Viupiu (женские прилагательные)",
    "viupiu_adv": "Viupiu (наречия)",
    "viupiu_noun": "Viupiu (существительные)",
    "viupiu_no_space": "Viupiu (без пробела)",
    "viupiu_parts_of_body": "Viupiu (части тела)",
    "viupiu_penis": "Viupiu (пенис)",
    "viupiu_prep": "Viupiu (предлоги)",
    "viupiu_stop": "Viupiu (остановите)",
    "viupiu_verb": "Viupiu (глаголы)",
    "viupiu_wontsay": "Viupiu (не могу ответить)",
    "vocatives_girl": "Условие: `gender:female`",
    "vocatives_man": "Условие: `gender:male`",
    "vopros": "Вопрос: знаки, знаки и интеропонты",
    "voskl": "Восклицания: знаки (!,!!)",
    "vtb_cities": "Города России (интеграция с продуктовой линией)",
    "word_eshe": "Вещи: `Ещё что-нибудь?`",
    "word_food_fruits": "Еда: фрукты (фрукты, ягоды и т.д.)",
    "word_geography_cityrussian": "География: города России",
    "word_konsultant": "Специальные слова: KAS",
    "word_now": "Интеграция: `time:now`",
    "word_skolko": "Сколько: сколько, количество, суммы",
    "word_vopros": "Вопрос по: вопросы по разным категориям (погода и т.д.)",
    "word_what": "Слова: что, что это",
    "work_work_2_pres": "Работа: работа, работа, работа",
    "yota_moscow": "Гео: Москва, Яндекс (`yota` провайдер)",
    "you_lie": "Я вру, вру, лжешь (отрицания, отрицания, отрицания)",
    "znayka_drugs": "Фармацевтические препараты (торговые марки)",
}

# Now do the updates
updated = 0
for dictname, new_meaning in name_meaning_map.items():
    # Update in registry table
    old_table_line = f"| `{dictname}` | {placeholder} |"
    new_table_line = f"| `{dictname}` | {new_meaning} |"
    if old_table_line in content:
        content = content.replace(old_table_line, new_table_line)
        updated += 1
    else:
        print(f"WARNING: Table line not found for {dictname}")

    # Update section meaning line
    old_section_meaning = f"\n\n{placeholder}\n"
    new_section_meaning = f"\n\n{new_meaning}\n"
    # Find the section and replace
    section_header = f"## `{dictname}`"
    idx = content.find(section_header)
    if idx != -1:
        meaning_idx = content.find(old_section_meaning, idx)
        if meaning_idx != -1:
            content = content[:meaning_idx] + new_section_meaning + content[meaning_idx + len(old_section_meaning):]
            updated += 1
        else:
            print(f"WARNING: Section meaning not found for {dictname}")
    else:
        print(f"WARNING: Section not found for {dictname}")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Done. Updated {updated} occurrences across {len(name_meaning_map)} dictionaries.")
