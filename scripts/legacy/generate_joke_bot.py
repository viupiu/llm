import json
import uuid
import zipfile
import hashlib
import os
import string
import random

BASE = r"C:\Users\Mariyaa\Desktop\скрипты\LLM"
OUT_ZIP = os.path.join(BASE, "joke_bot_prod.zip")

random.seed(42)

def short_id():
    h = uuid.uuid4().hex[:20]
    return f"{h[:8]}-{h[8:12]}-{h[12:16]}-{h[16:20]}"

def full_id():
    return str(uuid.uuid4())

def bk(text, data=None):
    k = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
    return {
        "key": k,
        "data": data if data else {},
        "text": text,
        "type": "unstyled",
        "depth": 0,
        "entityRanges": [],
        "inlineStyleRanges": []
    }

def draft(texts, block_data=None):
    if isinstance(texts, str):
        texts = [texts]
    blocks = []
    for t in texts:
        if block_data:
            bd = block_data if callable(block_data) else block_data
            if callable(bd):
                blocks.append(bk(t, bd))
            else:
                blocks.append(bk(t, bd))
        else:
            blocks.append(bk(t))
    return {"blocks": blocks, "entityMap": {}}

def lu_rare(text, data=None):
    d = {"DLAnswerLU": "rare"}
    if data:
        d.update(data)
    return bk(text, d)

CREATOR = "00000000-0000-0000-0000-000000000000"
NOW = "2026-05-20T14:00:00.000000"
PROJECT = "205359"

AID = full_id()
BRANCH_ID = full_id()

# --- Skills ---
SK_HELLO = short_id()
SK_JOKES = short_id()
SK_CATS = short_id()
SK_BYE = short_id()

# --- Variables ---
VAR_NAME = short_id()
VAR_CAT = short_id()
VAR_LAST_JOKEDICT = short_id()
VAR_JOKECOUNT = short_id()

# --- Dictionaries ---
DICT_HELLO = short_id()
DICT_BYE = short_id()
DICT_CATS = short_id()
DICT_J_ANIMALS = short_id()
DICT_J_OFFICE = short_id()
DICT_J_TECH = short_id()
DICT_CHEERIO = short_id()
DICT_LAUGH = short_id()

# --- Tags ---
TAG_DEFAULT = short_id()

def make_node(name, skill_id, dl_texts, ml_texts, answer_texts, conditions=None, slot_filling=None):
    nid = short_id()
    sfill = slot_filling if slot_filling else [{
        "id": ''.join(random.choices(string.ascii_letters + string.digits, k=10)),
        "entity": {"id": "", "name": ""},
        "question": "",
        "required": False,
        "variable": {"id": "", "name": ""}
    }]
    return {
        "id": nid,
        "name": name,
        "description": "",
        "parent": None,
        "shortcuts": [],
        "conditions": conditions,
        "dl_rules": draft(dl_texts),
        "ml_examples": draft(ml_texts) if ml_texts else draft(""),
        "intent_id": None,
        "skill_id": skill_id,
        "answers": draft(answer_texts),
        "responses": [],
        "slot_filling": sfill,
        "is_active": True,
        "auto_conflict_resolution": None,
        "meta": {},
        "created": NOW,
        "updated": None,
        "state_score": 0,
        "creator": CREATOR,
        "editors": []
    }, nid

NODES = {}

# ============================================
# 1. PRIVETSTVIIE (Hello / Greeting)
# ============================================

# Node: Пользователь здоровается
NODES["greet"], _ = make_node(
    name="1_Здоровается",
    skill_id=SK_HELLO,
    dl_texts=["[dict(hello)] <!>"],
    ml_texts=[
        "Привет", "Здравствуйте", "Добрый день", "Доброе утро",
        "Добрый вечер", "Салют", "Здарова", "Хэй",
        "Приветики", "Дзень", "Хай", "Приветик",
    ],
    answer_texts=[
        ":lu: Привет! Я бот-анекдотист. Могу рассказать шутку про животных, офис или технологии. [br][@setvalue(\"msg_count\", \"1\", \"hide\")]",
        ":lu: Здравствуй! Хочешь анекдот? Говори: \"расскажи анекдот\" или выбери категорию.",
        ":lu: Хаюшки! Я знаю много анекдотов — спрашивай!",
        ":lu: Привет-привет! Готов тебя позабавить. Просто скажи: анекдот!",
        ":lu: Здарова! Анекдоты уже загружены. Жду команды!",
    ],
)

# Node: Как тебя зовут
NODES["ask_name"], nid_ask = make_node(
    name="2_Как_тебя_зовут",
    skill_id=SK_HELLO,
    dl_texts=["как тебя зовут", "твоё имя", "кто ты"],
    ml_texts=[
        "как тебя зовут", "кто ты такой", "как тебя называть",
        "твоё имя", "тебя как зовут", "ты кто",
        "назови себя", "расскажи о себе", "ты кто такой",
        "какое у тебя имя", "как к тебе обращаться",
    ],
    answer_texts=[
        "Меня зовут Анекдотик! А как тебя зовут? [@setvalue(\"user_name\", \"\", \"hide\")]",
        "Я — Анекдотик, твой бот-шутник! А тебя как зовут?",
        "Зови меня Анекдотик. А тебя как зовут, друг?",
    ],
)

# Node: Пользователь говорит имя
NODES["has_name"], nid_hasname = make_node(
    name="3_Пользователь_сказал_имя",
    skill_id=SK_HELLO,
    dl_texts=["[- -]"],
    ml_texts=[
        "меня зовут Алексей", "Анастасия", "Иван",
        "Аня", "Сергей", "Марина",
        "меня зовут Дима", "Олег", "Лена",
        "я Максим", "Ирина",
    ],
    answer_texts=[
        "[&1]! Рад познакомиться, дружище! [@setvalue(\"user_name\", \"[&1]\", \"hide\")]",
        "Приятно, [&1]! Теперь я буду звать тебя так. [%user_name], держи анекдот? [@setvalue(\"user_name\", \"[&1]\", \"hide\")]",
        "Привет, [&1]! Запомнил. Хочешь анекдот? [@setvalue(\"user_name\", \"[&1]\", \"hide\")]",
    ],
)

# ============================================
# 2. ANEKDOTY (Jokes)
# ============================================

# Node: Рассказать анекдот (без категории)
NODES["joke_any"], nid_joke_any = make_node(
    name="4_Расскажи_анекдот",
    skill_id=SK_JOKES,
    dl_texts=[
        "расскажи анекдот",
        "расскажи шутку",
        "пошути",
        "что-нибудь смешное",
        "потешь меня",
    ],
    ml_texts=[
        "расскажи анекдот", "расскажи анекдот пожалуйста", "расскажи шутку",
        "хочу анекдот", "скажи что нибудь смешное", "хочу посмеяться",
        "расскажи что нибудь веселое", "пошути", "анекдот",
        "анекдот пожалуйста", "потешь меня",
    ],
    answer_texts=[
        ":lu: Вот тебе случайный анекдот: [dict(random_joke)]",
        ":lu: Держи шутку: [dict(random_joke)]",
        "Слушай-ка: [dict(random_joke)]",
        "О, классный анекдот: [dict(random_joke)]",
    ],
)

# Node: Анекдот про животных
NODES["joke_animals"], nid_joke_anim = make_node(
    name="5_Анекдот_про_животных",
    skill_id=SK_JOKES,
    dl_texts=[
        "[&1] про [- -]",
        "анекдот {*про животных*/про зверей/про кошек/про котов/про собак/про котиков*}",
    ],
    ml_texts=[
        "расскажи анекдот про животных", "анекдот про кота",
        "анекдот про собак", "шутку про зверей",
        "расскажи что нибудь про зверушек", "анекдот про кошек",
        "про котиков анекдот", "расскажи про животных",
        "шутку про котов", "анекдот про кошку",
        "что нибудь про собак",
    ],
    answer_texts=[
        ":lu: Про животных: [dict(jokes_animals)]",
        ":lu: [dict(jokes_animals)]",
        "Вот про зверушек: [dict(jokes_animals)]",
    ],
)

# Node: Анекдот про офис
NODES["joke_office"], nid_joke_office = make_node(
    name="6_Анекдот_про_офис",
    skill_id=SK_JOKES,
    dl_texts=[
        "анекдот {*про офис*/про работу/про начальника/про коллег/про менеджеров*}",
        "[&1] [- -]",
    ],
    ml_texts=[
        "расскажи анекдот про офис", "анекдот про работу",
        "шутку про начальника", "анекдот про коллег",
        "расскажи про рабочий день", "анекдот про менеджеров",
        "что нибудь смешное про офис", "шутку про работу",
        "анекдот про начальника", "про офис анекдот",
        "расскажи анекдот про коллег",
    ],
    answer_texts=[
        ":lu: Про офис: [dict(jokes_office)]",
        ":lu: [dict(jokes_office)]",
        "Офисный анекдот: [dict(jokes_office)]",
        "Вот тебе про работу: [dict(jokes_office)]",
    ],
)

# Node: Анекдот про технологии
NODES["joke_tech"], nid_joke_tech = make_node(
    name="7_Анекдот_про_технологии",
    skill_id=SK_JOKES,
    dl_texts=[
        "анекдот {*про технологии*/про IT/про программистов/про компьютеры*}",
        "[&1] [- -]",
    ],
    ml_texts=[
        "расскажи анекдот про технологии", "анекдот про IT",
        "шутку про программистов", "анекдот про компьютеры",
        "расскажи про техно", "анекдот про хакеров",
        "что нибудь смешное про IT", "шутку про код",
        "анекдот про гиков", "про технологии анекдот",
        "расскажи анекдот про айдиэшники",
    ],
    answer_texts=[
        ":lu: Про технологии: [dict(jokes_tech)]",
        ":lu: [dict(jokes_tech)]",
        "IT-анекдот: [dict(jokes_tech)]",
        "Про гиков: [dict(jokes_tech)]",
    ],
)

# Node: Ещё анекдот
NODES["joke_again"], nid_again = make_node(
    name="8_Еще_анекдот",
    skill_id=SK_JOKES,
    dl_texts=["ещё анекдот", "ещё шутку", "ещё один", "расскажи ещё", "ещё расскажи"],
    ml_texts=[
        "ещё", "ещё анекдот", "ещё один анекдот",
        "ещё пожалуйста", "расскажи ещё", "ещё шутку",
        "ещё один", "ещё что нибудь", "ещё расскажи",
        "расскажи ещё разок", "покажи ещё",
    ],
    answer_texts=[
        ":lu: Давай! [dict(random_joke)]",
        ":lu: [dict(random_joke)]",
        "Ещё: [dict(random_joke)]",
        "Лови: [dict(random_joke)]",
    ],
)

# Node: Смешно
NODES["joke_lol"], nid_lol = make_node(
    name="9_Смешно",
    skill_id=SK_JOKES,
    dl_texts=["[- {&1} -]", "смешно", "ха-ха", "ржу", "лол", "ахах"],
    ml_texts=[
        "смешно", "хаха", "рофлол", "лол", "ахаха",
        "ха-ха-ха", "ржу в пол", "смешной", "ха-ха",
        "прикольно", "ахахahaha", "ржу",
    ],
    answer_texts=[
        "Рад, что понравилось! Хочешь ещё? [@goto node_еще_анекдот]",
        "Класс! Ещё один? [@goto node_еще_анекдот]",
        "Ура! [dict(cheerio)]",
    ],
)

# Node: Не смешно
NODES["joke_boring"], nid_boring = make_node(
    name="10_Не_смешно",
    skill_id=SK_JOKES,
    dl_texts=["скучно", "не смешно", "банально", "никак", "нормально"],
    ml_texts=[
        "не смешно", "скучно", "никак не смешно",
        "банально", "нормально", "так себе",
        "ничего особенного", "незатейливо", "мeh",
        "никакого юмора", "хм",
    ],
    answer_texts=[
        "Ну, у каждого свой вкус. Попробую другой раз: [dict(random_joke)]",
        "Ладно, попробую другой анекдот: [dict(random_joke)]",
        "Не судьба? Вот тебе другой: [dict(random_joke)]",
    ],
)

# Node: Спасибо
NODES["joke_thanks"], nid_thanks = make_node(
    name="11_Спасибо_за_анекдот",
    skill_id=SK_JOKES,
    dl_texts=["спасибо за анекдот", "спасибо за шутку", "спасибо за юмор"],
    ml_texts=[
        "спасибо", "спасибо за анекдот", "спасибо за шутку",
        "благодарю", "спасибо было смешно", "спасибо за юмор",
        "спасибо посмеялся", "спс", "благодарю тебя",
        "красавчик спасибо", "спасибо за смех",
    ],
    answer_texts=[
        "Всегда пожалуйста! [dict(cheerio)]",
        "Не за что! Заходи ещё!",
        "Рад был помочь!",
    ],
)

# Node: Сколько анекдотов знаешь
NODES["joke_count"], nid_count = make_node(
    name="12_Сколько_знаешь",
    skill_id=SK_JOKES,
    dl_texts=["сколько анекдотов", "сколько шуток знаешь", "сколько всего"],
    ml_texts=[
        "сколько анекдотов знаешь", "сколько шуток",
        "какой у тебя репертуар", "сколько всего анекдотов",
        "большой выбор", "много знаешь анекдотов",
        "какой у тебя список", "сколько у тебя",
        "все анекдоты", "сколько всего шуток",
        "дай список шуток",
    ],
    answer_texts=[
        "У меня 30 анекдотов! 10 про животных, 10 про офис и 10 про технологии. Спрашивай любой!",
        "Знаю 30 штук. Три категории по 10 анекдотов. Выбирай!",
    ],
)

# ============================================
# 3. KATEGORII (Categories)
# ============================================

NODES["cat_list"], nid_cats = make_node(
    name="13_Категории_анекдотов",
    skill_id=SK_CATS,
    dl_texts=["какие есть категории", "какие анекдоты", "список", "что умеешь", "категории"],
    ml_texts=[
        "какие есть анекдоты", "какие категории", "что умеешь",
        "какие анекдоты знаешь", "дай список категорий",
        "какие шутки", "что можешь рассказать",
        "какие у тебя категории", "перечисли категории",
        "список анекдотов", "покажи категории",
    ],
    answer_texts=[
        ":lu: Знаю анекдоты про: [br]Животных [br]Офис [br]Технологии [br][br] Скажи: \"анекдот про животных\", \"анекдот про офис\" или \"анекдот про технологии\"!",
        "Мои категории: Животные, Офис, Технологии. Или просто скажи \"расскажи анекдот\" — выберу случайный!",
    ],
)

# ============================================
# 4. PROSHCHANIE (Bye)
# ============================================

NODES["bye"], nid_bye = make_node(
    name="14_Пока",
    skill_id=SK_BYE,
    dl_texts=["[dict(byes)] <!>", "пока", "до свидания", "прощай", "ухожу"],
    ml_texts=[
        "пока", "до свидания", "прощай", "до встречи",
        "пока пока", "бывай", "до скорого", "удалиться",
        "пойду", "мне пора", "всего хорошего",
        "до связи", "убираться",
    ],
    answer_texts=[
        "Пока! Заходи ещё за анекдотами! [dict(bye_phrases)]",
        "До встречи! Буду ждать! [dict(bye_phrases)]",
        "Бывай! Рад был пообщаться!",
    ],
)

# ============================================
# 5. FALLOUT / UNKNOWN
# ============================================

NODES["unknown"], nid_unknown = make_node(
    name="15_Не_понял",
    skill_id=SK_JOKES,
    dl_texts=["*"],
    ml_texts=[],
    answer_texts=[
        "Не понял. Скажи \"расскажи анекдот\" или \"какие категории\"?",
        "Хм, не знаю что ответить. Попробуй: \"анекдот\", \"пока\" или \"категории\".",
    ],
    conditions=None,
)

all_nodes = list(NODES.values())

# ============================================
# SKILLS
# ============================================
skills = {
    SK_HELLO: {
        "id": SK_HELLO, "name": "Приветствие",
        "is_common": False, "is_active": True,
        "meta": {}, "created": NOW, "updated": NOW,
        "creator": CREATOR, "editors": [],
    },
    SK_JOKES: {
        "id": SK_JOKES, "name": "Анекдоты",
        "is_common": False, "is_active": True,
        "meta": {}, "created": NOW, "updated": NOW,
        "creator": CREATOR, "editors": [],
    },
    SK_CATS: {
        "id": SK_CATS, "name": "Категории_Анекдотов",
        "is_common": False, "is_active": True,
        "meta": {}, "created": NOW, "updated": NOW,
        "creator": CREATOR, "editors": [],
    },
    SK_BYE: {
        "id": SK_BYE, "name": "Прощание",
        "is_common": False, "is_active": True,
        "meta": {}, "created": NOW, "updated": NOW,
        "creator": CREATOR, "editors": [],
    },
}

# ============================================
# VARIABLES
# ============================================
variables = {
    VAR_NAME: {
        "id": VAR_NAME, "name": "user_name",
        "description": "Имя пользователя",
        "type": "user", "value": "",
        "life_cycle": "0",
        "extra": {"api": True, "scope": "session", "secret": False},
        "is_editable": None, "created": NOW, "updated": None,
        "creator": CREATOR, "editors": [],
    },
    VAR_CAT: {
        "id": VAR_CAT, "name": "joke_category",
        "description": "Последняя выбранная категория",
        "type": "user", "value": "",
        "life_cycle": "0",
        "extra": {"api": True, "scope": "session", "secret": False},
        "is_editable": None, "created": NOW, "updated": None,
        "creator": CREATOR, "editors": [],
    },
    VAR_LAST_JOKEDICT: {
        "id": VAR_LAST_JOKEDICT, "name": "last_joke_dict",
        "description": "Словарь последнего анекдота",
        "type": "user", "value": "",
        "life_cycle": "0",
        "extra": {"api": True, "scope": "session", "secret": False},
        "is_editable": None, "created": NOW, "updated": None,
        "creator": CREATOR, "editors": [],
    },
    VAR_JOKECOUNT: {
        "id": VAR_JOKECOUNT, "name": "msg_count",
        "description": "Счётчик сообщений",
        "type": "user", "value": "0",
        "life_cycle": "0",
        "extra": {"api": True, "scope": "session", "secret": False},
        "is_editable": None, "created": NOW, "updated": None,
        "creator": CREATOR, "editors": [],
    },
}

# ============================================
# DICTIONARIES
# ============================================
dictionaries = {
    DICT_HELLO: {
        "id": DICT_HELLO, "name": "hello",
        "description": "Приветственные слова пользователя",
        "content": {"blocks": [bk(t) for t in [
            "Привет", "=>приветствую~", "Приветик",
            "Здарова", "=>здоров~", "Салют",
            "Добрый день", "Доброе утро", "Добрый вечер",
            "Здравствуйте", "Хэй", "Хай",
            "Дзень", "Приветики", "Здаров",
        ]], "entityMap": {}},
        "is_common": True, "is_hidden": False, "is_active": True,
        "meta": {}, "created": NOW, "updated": None,
        "creator": CREATOR, "editors": [],
    },
    DICT_BYE: {
        "id": DICT_BYE, "name": "byes",
        "description": "Прощальные слова",
        "content": {"blocks": [bk(t) for t in [
            "Пока", "Пока-пока", "До свидания",
            "До встречи", "Прощай", "Бывай",
            "До скорого", "Всего хорошего", "До связи",
        ]], "entityMap": {}},
        "is_common": True, "is_hidden": False, "is_active": True,
        "meta": {}, "created": NOW, "updated": None,
        "creator": CREATOR, "editors": [],
    },
    DICT_CHEERIO: {
        "id": DICT_CHEERIO, "name": "cheerio",
        "description": "Фразы радости",
        "content": {"blocks": [bk(t) for t in [
            "Ура!", "Класс!", "Браво!", "Хорошо!", "Отлично!"
        ]], "entityMap": {}},
        "is_common": False, "is_hidden": False, "is_active": True,
        "meta": {}, "created": NOW, "updated": None,
        "creator": CREATOR, "editors": [],
    },
    DICT_CATS: {
        "id": DICT_CATS, "name": "cat_jokes",
        "description": "Категории анекдотов",
        "content": {"blocks": [bk(t) for t in [
            "Животные", "=>звери~", "=>питомцы~", "=>кот~", "=>собак~",
            "Офис", "=>работ~", "=>офис~", "=>начальник~", "=>коллег~",
            "Технологии", "=>ИТ~", "=>программист~", "=>компьютер~", "=>хакер~", "=>IT~",
        ]], "entityMap": {}},
        "is_common": False, "is_hidden": False, "is_active": True,
        "meta": {}, "created": NOW, "updated": None,
        "creator": CREATOR, "editors": [],
    },
    DICT_J_ANIMALS: {
        "id": DICT_J_ANIMALS, "name": "jokes_animals",
        "description": "Анекдоты про животных",
        "content": {"blocks": [bk(t) for t in [
            "Жили-были два кота. Один спросил: «Ты почему грустный?» — «Жена ушла к коту.»",
            "— Кот, а как называется тот, кто не знает ни одной песни? — Бескультурный.",
            "Два кота на заборе. Один: «Хочу быть человеком.» Второй: «Зачем?» — «Чтоб жена приходила.»",
            "Пес на экзамене: «Ты что, ничего не знаешь?» — «Лает, значит знаю!»",
            "Собака-писатель. Сын журналиста: «Папа, у тебя тоже лапы!»",
            "Кот идёт к психологу: — Доки, у меня проблемы. — Какие? — Ко мне никто не ходит. — А почему вы не идёте к ним?",
            "— Кот, в чём разница между тобой и лошадью? — В 250 рублях. А что дальше?",
            "Кошка: «Ты зачем мне розу подарил?» Кот: «Чтоб поняла, роза — не шутка.»",
            "Пёс-философ: «Если ты не знаешь куда идёшь — лает!»",
            "Заяц-спортсмен: «Почему так быстро бегаешь?» — «Масло подливает!»",
        ]], "entityMap": {}},
        "is_common": False, "is_hidden": False, "is_active": True,
        "meta": {}, "created": NOW, "updated": None,
        "creator": CREATOR, "editors": [],
    },
    DICT_J_OFFICE: {
        "id": DICT_J_OFFICE, "name": "jokes_office",
        "description": "Анекдоты про офис",
        "content": {"blocks": [bk(t) for t in [
            "— Почему программисты путают Хэллоуин и Рождество? — Oct 31 == Dec 25.",
            "— Сколько программистов нужно, чтобы вкрутить лампочку? — Никаких, это проблема железа.",
            "— На работе мне платят за то, чтобы я думал. Вот я и сижу думаю.",
            "— Что общего между резюме и жизнью? — В обоих нет ничего интересного.",
            "— Как называется девушка программиста? — Пятница. — Почему? — На понедельник она уже не нужна.",
            "— Сколько нужно менеджеров, чтобы закрутить лампочку? — Ни одного. Менеджер — это про людей.",
            "Коллега: «Я работаю из дома.» Начальник: «Тогда работай из офиса.»",
            "— Начальник, зачем вы ушли на обед на час раньше? — Я хочу быть свободным и счастливым.",
            "— Что общего между работой и жизнью? — В обеих ничего не понимаю и всё равно сижу.",
            "Офисный планктон: «Спасибо за ваш вклад в проект.» — «Пожалуйста. Спасибо, что выдохнули.»",
        ]], "entityMap": {}},
        "is_common": False, "is_hidden": False, "is_active": True,
        "meta": {}, "created": NOW, "updated": None,
        "creator": CREATOR, "editors": [],
    },
    DICT_J_TECH: {
        "id": DICT_J_TECH, "name": "jokes_tech",
        "description": "Анекдоты про технологии",
        "content": {"blocks": [bk(t) for t in [
            "— WiFi, ты меня слышишь? — Нет, я тебя теряю.",
            "— Что было раньше: курица или яйцо? — Синтаксическая ошибка.",
            "Программист ставит будильник: «Кот, если ночью что-то понадобится — мяузни.»",
            "— Как называется девушка программиста? — Среда. — Почему? — Остальные дни работает.",
            "— Что общего между моим кодом и жизнью? — В обоих нет комментариев.",
            "— Сколько программистов нужно для замены лампочки? — Три: один крутит, два держат стул, третий пишет баг-репорт.",
            "IT-специалист: «Сначала подумай.» — «А подумать не бесплатно?» — «Бесплатно, но результат платный.»",
            "Гугл: «Извините, не удалось найти.» Пользователь: «Вот, и я такого же ответа ждал.»",
            "— Что такое тестирование? — Прога: «Работает!» Тестер: «Не работает!»",
            "Чат-бот: «Как я могу помочь?» Пользователь: «Прекратите существовать.» Бот: «Хорошо!»",
        ]], "entityMap": {}},
        "is_common": False, "is_hidden": False, "is_active": True,
        "meta": {}, "created": NOW, "updated": None,
        "creator": CREATOR, "editors": [],
    },
}

# ============================================
# TAGS + DIALOGNODETAGS
# ============================================
tags_data = {
    TAG_DEFAULT: {
        "id": TAG_DEFAULT, "name": "default",
        "is_active": True, "created": NOW, "updated": NOW,
        "description": "",
        "answers": {"blocks": [bk("default")], "entityMap": {}},
        "conditions": "",
        "creator": CREATOR, "editors": [],
    },
}

dn_tags = []
for tag_id in tags_data:
    for nkey, node_obj in NODES.items():
        dn_tags.append({
            "dialog_node_id": node_obj["id"],
            "tag_id": tag_id,
            "is_active": True,
            "created": NOW,
        })

# ============================================
# ASSISTANT + BRANCH
# ============================================
assistant = {
    "id": AID, "name": "Анекдотик_Бот",
    "description": "Бот рассказывает анекдоты про животных, офис и технологии",
    "is_active": True, "meta": {}, "avatar_url": None,
    "project_id": PROJECT, "created": NOW, "updated": None,
    "creator": CREATOR, "editors": [],
}

branch = {
    "id": BRANCH_ID,
    "assistant_id": AID,
    "parent_id": None,
    "name": "master",
    "is_loaded": False,
    "project_id": PROJECT,
    "created": NOW, "synced": None, "updated": None,
    "is_sync_db_git": True,
    "creator": None, "editors": [],
}

# ============================================
# COLLECT & WRITE
# ============================================
hash40 = hashlib.md5(AID.encode()).hexdigest()
wr_name = f"{AID}-master-{hash40}"

tmp_root = os.path.join(BASE, "temp_joke_bot")
wr_dir = os.path.join(tmp_root, wr_name)

if os.path.exists(tmp_root):
    import shutil
    shutil.rmtree(tmp_root)
os.makedirs(wr_dir, exist_ok=True)

# metadata.json
metadata = {
    "lc_version": "0.96.1",
    "timestamp": NOW,
    "options": {"exclude_tables": ["AutotestScenario"]},
}
with open(os.path.join(tmp_root, "metadata.json"), "w", encoding="utf-8") as f:
    json.dump(metadata, f, indent=2, ensure_ascii=False, default=str)

# Write entity folders
folder_map = {
    "DialogNode": list(NODES.values()),
    "Skill": list(skills.values()),
    "Dictionary": list(dictionaries.values()),
    "Variable": list(variables.values()),
    "Tag": list(tags_data.values()),
    "DialogNodeTag": dn_tags,
    "Assistant": [assistant],
    "Branch": [branch],
}

for folder, items in folder_map.items():
    d = os.path.join(wr_dir, folder)
    os.makedirs(d, exist_ok=True)
    for item in items:
        if folder == "DialogNodeTag":
            fname = f"{item['dialog_node_id']}_{item['tag_id']}.json"
        else:
            fname = f"{item['id']}.json"
        with open(os.path.join(d, fname), "w", encoding="utf-8") as f:
            json.dump(item, f, indent=2, ensure_ascii=False, default=str)

# ZIP
with zipfile.ZipFile(OUT_ZIP, "w", zipfile.ZIP_DEFLATED) as z:
    z.write(os.path.join(tmp_root, "metadata.json"), "metadata.json")
    for root, dirs, files in os.walk(wr_dir):
        for fl in sorted(files):
            fp = os.path.join(root, fl)
            arc = os.path.relpath(fp, tmp_root)
            z.write(fp, arc)

print(f"Archive created: {OUT_ZIP}")
print(f"Nodes: {len(NODES)}")
print(f"Skills: {len(skills)}")
print(f"Dictionaries: {len(dictionaries)}")
print(f"Variables: {len(variables)}")
print(f"Tags: {len(tags_data)}")
print(f"DialogNodeTags: {len(dn_tags)}")
