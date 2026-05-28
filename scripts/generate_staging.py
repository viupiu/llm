# -*- coding: utf-8 -*-
import json, secrets, string
from pathlib import Path

BASE = Path(r"C:\Users\Mariyaa\Desktop\скрипты\LLM\work\FPK")
S = BASE / "staging"
TS = "2026-05-26T12:00:00.000000"
CR = "00000000-0000-0000-0000-000000000000"
PID = "205359"
EB = {"blocks": [], "entityMap": {}}

def rk(n=5):
    a = string.ascii_lowercase + string.digits
    return "".join(secrets.choice(a) for _ in range(n))

def si():
    h = secrets.token_hex(10)
    return f"{h[:8]}-{h[8:12]}-{h[12:16]}-{h[16:20]}"

def fi():
    h = secrets.token_hex(16)
    return f"{h[:8]}-{h[8:12]}-{h[12:16]}-{h[16:20]}-{h[20:32]}"

def bld(t):
    return {"key": rk(), "data": {}, "text": t, "type": "unstyled",
            "depth": 0, "entityRanges": [], "inlineStyleRanges": []}

def mb(ts):
    return {"blocks": [bld(t) for t in ts] if ts else [], "entityMap": {}}

def sav(sd, fn, o):
    p = S / sd / fn
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(o, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

def slt():
    return [{"id": secrets.token_urlsafe(8)[:10], "entity": {"id": "", "name": ""},
             "question": "", "required": False, "variable": {"id": "", "name": ""}}]

def mn(name, sk, dl=None, ans=None, cond=None, par=None):
    nid = si()
    return nid, {"id": nid, "name": name, "description": "", "parent": par,
                 "shortcuts": [], "conditions": cond,
                 "dl_rules": mb(dl if dl is not None else ["*"]),
                 "ml_examples": EB, "intent_id": None, "skill_id": sk,
                 "answers": mb(ans), "responses": [], "slot_filling": slt(),
                 "is_active": True, "auto_conflict_resolution": None, "meta": {},
                 "created": TS, "updated": None, "state_score": 0,
                 "creator": CR, "editors": []}

S.mkdir(parents=True, exist_ok=True)

# ── manifest ──
sav("", "9_PACKAGER__MANIFEST.json", {
    "bot_name": "FPK", "export_basename": "FPK",
    "project_id": PID, "creator": "a04359b1-6422-4e56-9792-bf13f40afb9b"
})

# ── Assistant ──
aid = fi()
sav("Assistant", f"{aid}.json", {
    "id": aid, "name": "FPK",
    "description": "Входящий голосовой бот ФПК",
    "is_active": True, "meta": {}, "avatar_url": None,
    "project_id": PID, "created": TS, "updated": None,
    "creator": CR, "editors": []
})

# ── Branch ──
bid = fi()
sav("Branch", f"{bid}.json", {
    "id": bid, "assistant_id": aid, "parent_id": None,
    "name": "master", "is_loaded": False, "project_id": PID,
    "created": TS, "synced": None, "updated": None,
    "is_sync_db_git": True, "creator": None, "editors": []
})

# ── Skills ──
ske = si()
skw = si()
skfpk = si()
for sid, sn, ic in [(ske, "EVENTS", False), (skw, "*", True), (skfpk, "FPK_Входящий", False)]:
    sav("Skill", f"{sid}.json", {
        "id": sid, "name": sn, "is_common": ic, "is_active": True,
        "meta": {}, "created": TS, "updated": TS, "creator": CR, "editors": []
    })

# ── Variables ──
for vn, vd, vv in [
    ("nomatch_counter", "Счётчик подряд идущих попаданий", "0"),
    ("user_type", "Результат физ/юр", ""),
    ("transfer", "Куда ведёт заглушка", ""),
    ("voice.end_call", "Флаг завершения звонка", ""),
]:
    vid = si()
    sav("Variable", f"{vid}.json", {
        "id": vid, "name": vn, "description": vd, "type": "user",
        "value": vv, "life_cycle": "0",
        "extra": {"api": True, "scope": "session", "secret": False},
        "is_editable": None, "created": TS, "updated": None,
        "creator": CR, "editors": []
    })

# ── Dictionaries ──
for dn, items, ic in [
    ("common_yes", ["да", "да пожалуйста", "да переведите", "да хочу", "конечно", "угу да", "так точно", "да конечно", "переводите", "да можно"], True),
    ("common_no", ["нет", "нет спасибо", "не нужно", "не надо", "нет не переводи", "не хочу", "не обязательно", "нет всё", "не надо спасибо"], True),
    ("otkaz", ["откажусь"], True),
    ("keywords_appeal", ["обращен~", "заявк~", "реквизит~", "запрос~"], False),
    ("keywords_tickets", ["билет~", "поезд~", "рейс~", "отмен~", "перенос~", "задерж~", "брон~", "расписан~", "маршрут~"], False),
    ("keywords_other", ["директор~", "представительств~", "проезд~", "приложен~", "скидк~", "лояльн~", "оператор~", "проводник~", "обслуживан~"], False),
    ("user_type_physical", ["физическ~", "частн~", "гражданин~", "пассажир~", "я сам", "просто человек"], False),
    ("user_type_legal", ["юридическ~", "юрлиц~", "сотрудник~", "организац~", "фирм~", "компан~", "корпоративн~", "кадр~"], False),
]:
    did = si()
    sav("Dictionary", f"{did}.json", {
        "id": did, "name": dn, "description": "",
        "content": mb(items), "is_common": ic, "is_hidden": False,
        "is_active": True, "meta": {}, "created": TS, "updated": None,
        "creator": CR, "editors": []
    })

# ── Tag ──
tid = si()
sav("Tag", f"{tid}.json", {
    "id": tid, "name": "voice", "is_active": True,
    "created": TS, "updated": TS, "description": "",
    "answers": mb(["voice"]), "conditions": "",
    "creator": CR, "editors": []
})

# ── DialogNodes ──
CA = '%that_anchor="Чем я могу вам помочь?"'
CB = '%that_anchor="8 (800) 775-00-00, перевести вас?"'
CC = '%that_anchor="delo@fpc.ru, могу вам помочь чем-нибудь еще?"'
CD = '%that_anchor="Вы обращаетесь как физическое лицо или как сотрудник компании?"'
CE = '%that_anchor="Могу вам помочь чем-нибудь еще?"'
CCIAS = '%that_anchor="CIAS"'

nodes = []

# 1. Загрузка (EVENTS)
nid, n = mn("Загрузка", ske, ans=["[@goto(Приветствие)]"], cond=CCIAS)
nodes.append((nid, n))

# 2. Тишина (EVENTS)
nid, n = mn("Тишина", ske,
    ans=[
        ":lu: Извините, не услышала вас. Повторите, пожалуйста. [disableautovars]",
        ":lu: Я вас не расслышала. Повторите, пожалуйста. [disableautovars]",
    ], cond=CCIAS)
nodes.append((nid, n))

# 3. Конец разговора (EVENTS)
nid, n = mn("Конец разговора", ske,
    ans=['<speak>До свидания.<break time=\'1500ms\'></speak> [%voice.end_call="True"]'],
    cond=CCIAS)
nodes.append((nid, n))

# 4. Fallback - * (wildcard)
nid, n = mn("Fallback - *", skw,
    ans=["Извините, не поняла ваш запрос. [disableautovars]"])
nodes.append((nid, n))

# 5. Приветствие (FPK)
nid, n = mn("Приветствие", skfpk,
    ans=["Здравствуйте. Вы позвонили в Федеральную пассажирскую компанию. [@goto(Чем я могу Вам помощь?)]"])
nodes.append((nid, n))

# 6. Чем я могу Вам помощь? (Question Setter - parent)
nid, n = mn("Чем я могу Вам помощь?", skfpk,
    ans=['Чем я могу вам помочь? [%that_anchor="Чем я могу вам помочь?"]'])
nodes.append((nid, n))
qs1 = nid

# 7. Обращение (Answer Handler)
nid, n = mn("Чем я могу Вам помощь? - Обращение", skfpk,
    dl=[
        "* [@cmb({номер~}, {{моего/моей}}, {[dict(keywords_appeal)]})] *",
        "* [@cmb({статус~}, {[dict(keywords_appeal)]})] *",
        "* [@cmb({где}, {{мой/мое/моя}}, {[dict(keywords_appeal)]})] *",
        "* [@cmb({хочу}, {узнать}, {[dict(keywords_appeal)]})] *",
        "* [@cmb({проверьте}, {статус~}, {[dict(keywords_appeal)]})] *",
        "* [@cmb({рассмотрен~}, {[dict(keywords_appeal)]})] *",
        "* [@cmb({отслеж~}, {[dict(keywords_appeal)]})] *",
    ],
    ans=['[%nomatch_counter="0"] [%transfer="specialist"] [@goto("Кто вы - корень")]'],
    cond=CA, par=qs1)
nodes.append((nid, n))

# 8. Поезда и билеты (Answer Handler)
nid, n = mn("Чем я могу Вам помощь? - Поезда и билеты", skfpk,
    dl=[
        "* [@cmb({билет~}, {{купить/вернуть/обмен}})] *",
        "* [@cmb({[dict(keywords_tickets)]}, {{отмен~/перенос~/задерж~}})] *",
        "* [@cmb({брон~}, {{забронир~/мест~}})] *",
        "* [@cmb({расписан~}, {{отправл~/прибыти~}})] *",
        "* [@cmb({где}, {мой}, {поезд~})] *",
        "[dict(keywords_tickets)] *",
    ],
    ans=['[%nomatch_counter="0"] [@goto("Перевести на 8-800? - корень")]'],
    cond=CA, par=qs1)
nodes.append((nid, n))

# 9. Прочее (Answer Handler)
nid, n = mn("Чем я могу Вам помощь? - Прочее", skfpk,
    dl=[
        "* [@cmb({[dict(keywords_other)]}, {{выясн~/поговорить/уточн~/связаться}})] *",
        "* [@cmb({переведите}, {{оператор~/человек~}})] *",
        "* [@cmb({[dict(keywords_other)]}, {{директор/представительств}})] *",
        "* [@cmb({{правила/документ}}, {{ребен~/проезд~}})] *",
        "* [@cmb({[dict(keywords_other)]}, {приложен~})] *",
        "* [@cmb({{график/скидк}}, {{работ~/--}})] *",
        "* [@cmb({отдел}, {качеств~})] *",
        "* [@cmb({{собак/животн}}, {поезд~})] *",
        "* [@cmb({программ~}, {лояльн~})] *",
    ],
    ans=['[@Inc("nomatch_counter")] [if([@Greater("[%nomatch_counter]", "2")])]{[@goto("Прощание - Исчерпание помощи")]} [@goto("delo@ и ещё помочь? - корень")]'],
    cond=CA, par=qs1)
nodes.append((nid, n))

# 10. Чем я могу Вам помощь? - * (Fallback)
nid, n = mn("Чем я могу Вам помощь? - *", skfpk,
    ans=['Чем я могу вам помочь? [%that_anchor="Чем я могу вам помочь?"] [disableautovars]'],
    cond=CA, par=qs1)
nodes.append((nid, n))

# 11. Перевести на 8-800? - корень (Question Setter)
nid, n = mn("Перевести на 8-800? - корень", skfpk,
    ans=['Поняла вас, по данному запросу вам необходимо обратиться по телефону справочной службы: 8 (800) 775-00-00, перевести вас? [%that_anchor="8 (800) 775-00-00, перевести вас?"]'])
nodes.append((nid, n))
qs2 = nid

# 12. Перевести на 8-800? - Да
nid, n = mn("Перевести на 8-800? - Да", skfpk,
    dl=["[dict(common_yes)]"],
    ans=['[%transfer="hotline_800"] [@goto("Кто вы - корень")]'],
    cond=CB, par=qs2)
nodes.append((nid, n))

# 13. Перевести на 8-800? - Нет
nid, n = mn("Перевести на 8-800? - Нет", skfpk,
    dl=["[dict(common_no)]", "[dict(otkaz)]"],
    ans=['[@goto("Могу помочь ещё? - корень")]'],
    cond=CB, par=qs2)
nodes.append((nid, n))

# 14. Перевести на 8-800? - *
nid, n = mn("Перевести на 8-800? - *", skfpk,
    ans=['Поняла вас, по данному запросу вам необходимо обратиться по телефону справочной службы: 8 (800) 775-00-00, перевести вас? [disableautovars]'],
    cond=CB, par=qs2)
nodes.append((nid, n))

# 15. delo@ и ещё помочь? - корень (Question Setter)
nid, n = mn("delo@ и ещё помочь? - корень", skfpk,
    ans=['Поняла вас, по данному запросу вам необходимо отправить запрос на официальный электронный адрес компании: delo@fpc.ru, могу вам помочь чем-нибудь еще? [%that_anchor="delo@fpc.ru, могу вам помочь чем-нибудь еще?"]'])
nodes.append((nid, n))
qs3 = nid

# 16. delo@ и ещё помочь? - Да
nid, n = mn("delo@ и ещё помочь? - Да", skfpk,
    dl=["[dict(common_yes)]"],
    ans=['[@goto("Чем я могу Вам помощь?")]'],
    cond=CC, par=qs3)
nodes.append((nid, n))

# 17. delo@ и ещё помочь? - Нет
nid, n = mn("delo@ и ещё помочь? - Нет", skfpk,
    dl=["[dict(common_no)]", "[dict(otkaz)]"],
    ans=['[@goto("Прощание - Рада была помочь")]'],
    cond=CC, par=qs3)
nodes.append((nid, n))

# 18. delo@ и ещё помочь? - *
nid, n = mn("delo@ и ещё помочь? - *", skfpk,
    ans=['Поняла вас, по данному запросу вам необходимо отправить запрос на официальный электронный адрес компании: delo@fpc.ru, могу вам помочь чем-нибудь еще? [disableautovars]'],
    cond=CC, par=qs3)
nodes.append((nid, n))

# 19. Кто вы - корень (Question Setter)
nid, n = mn("Кто вы - корень", skfpk,
    ans=['Подскажите, пожалуйста, вы обращаетесь как физическое лицо или как сотрудник компании? [%that_anchor="Вы обращаетесь как физическое лицо или как сотрудник компании?"]'])
nodes.append((nid, n))
qs4 = nid

# 20. Кто вы - Физическое лицо
nid, n = mn("Кто вы - Физическое лицо", skfpk,
    dl=[
        "* [@cmb({[dict(user_type_physical)]}, {{лицо/--}})] *",
        "* [@cmb({гражданин~}, {{рф/--}})] *",
    ],
    ans=['[%user_type="physical"] [@goto("Заглушка перевода")]'],
    cond=CD, par=qs4)
nodes.append((nid, n))

# 21. Кто вы - Юридическое лицо
nid, n = mn("Кто вы - Юридическое лицо", skfpk,
    dl=[
        "* [@cmb({[dict(user_type_legal)]}, {{лицо/компан~}})] *",
        "* [@cmb({сотрудник~}, {[dict(user_type_legal)]})] *",
    ],
    ans=['[%user_type="legal"] [@goto("Заглушка перевода")]'],
    cond=CD, par=qs4)
nodes.append((nid, n))

# 22. Кто вы - *
nid, n = mn("Кто вы - *", skfpk,
    ans=['Подскажите, пожалуйста, вы обращаетесь как физическое лицо или как сотрудник компании? [disableautovars]'],
    cond=CD, par=qs4)
nodes.append((nid, n))

# 23. Могу помочь ещё? - корень (Question Setter)
nid, n = mn("Могу помочь ещё? - корень", skfpk,
    ans=['Могу вам помочь чем-нибудь еще? [%that_anchor="Могу вам помочь чем-нибудь еще?"]'])
nodes.append((nid, n))
qs5 = nid

# 24. Могу помочь ещё? - Да
nid, n = mn("Могу помочь ещё? - Да", skfpk,
    dl=["[dict(common_yes)]"],
    ans=['[@goto("Чем я могу Вам помощь?")]'],
    cond=CE, par=qs5)
nodes.append((nid, n))

# 25. Могу помочь ещё? - Нет
nid, n = mn("Могу помочь ещё? - Нет", skfpk,
    dl=["[dict(common_no)]", "[dict(otkaz)]"],
    ans=['[@goto("Прощание - Рада была помочь")]'],
    cond=CE, par=qs5)
nodes.append((nid, n))

# 26. Могу помочь ещё? - *
nid, n = mn("Могу помочь ещё? - *", skfpk,
    ans=['Могу вам помочь чем-нибудь еще? [disableautovars]'],
    cond=CE, par=qs5)
nodes.append((nid, n))

# 27. Заглушка перевода (router)
nid, n = mn("Заглушка перевода", skfpk,
    ans=['[if(%transfer="specialist")]{[if(%user_type="physical")]{[@goto("Заглушка - Специалист - Физ")]}}[elsif(%transfer="specialist")]{[if(%user_type="legal")]{[@goto("Заглушка - Специалист - Юр")]}}[elsif(%transfer="hotline_800")]{[if(%user_type="physical")]{[@goto("Заглушка - 8-800 - Физ")]}}[elsif(%transfer="hotline_800")]{[if(%user_type="legal")]{[@goto("Заглушка - 8-800 - Юр")]}}'])
nodes.append((nid, n))

# 28-31: Заглушки перевода (linear, DL-only) → беклог S-2, docs/беклог.md
nid, n = mn("Заглушка - Специалист - Физ", skfpk,
    ans=["[TODO S-2: VoIP-transfer на специалиста, физ. лицо]"])
nodes.append((nid, n))

nid, n = mn("Заглушка - Специалист - Юр", skfpk,
    ans=["[TODO S-2: VoIP-transfer на специалиста, юр. лицо]"])
nodes.append((nid, n))

nid, n = mn("Заглушка - 8-800 - Физ", skfpk,
    ans=["[TODO S-2: VoIP-transfer на 8-800, физ. лицо]"])
nodes.append((nid, n))

nid, n = mn("Заглушка - 8-800 - Юр", skfpk,
    ans=["[TODO S-2: VoIP-transfer на 8-800, юр. лицо]"])
nodes.append((nid, n))

# 31. Прощание - Рада была помочь
nid, n = mn("Прощание - Рада была помочь", skfpk,
    ans=['<speak>Рада была помочь. До свидания.<break time=\'1500ms\'></speak> [%voice.end_call="True"]'])
nodes.append((nid, n))

# 32. Прощание - Исчерпание помощи
nid, n = mn("Прощание - Исчерпание помощи", skfpk,
    ans=["К сожалению, ничем больше не могу вам помочь, большое спасибо за ваш звонок! Хорошего дня! [%voice.end_call=\"True\"]"])
nodes.append((nid, n))

# Save all nodes
for nid, obj in nodes:
    sav("DialogNode", f"{nid}.json", obj)

# ── DialogNodeTags ──
for nid, _ in nodes:
    dtid = si()
    sav("DialogNodeTag", f"{dtid}.json", {
        "id": dtid, "dialog_node_id": nid, "tag_id": tid,
        "is_active": True, "created": TS
    })

print(f"Generated {len(nodes)} DialogNodes")
print(f"Tag ID: {tid}")
print("Done!")
