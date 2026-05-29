# Ответы бота: Симулятор кота
## 6_RESPONSES_AUTHOR__RESPONSES.md

---

## Узел: Загрузка

Условия:
%that_anchor="CIAS"

Ответы:
:lu: [%cat_mood="content"] [@goto("Мяу! Что будем делать?")]
:lu: [%cat_mood="hungry"] [@goto("Мяу! Что будем делать?")]
:lu: [%cat_mood="sleepy"] [@goto("Мяу! Что будем делать?")]
:lu: [%cat_mood="playful"] [@goto("Мяу! Что будем делать?")]
:lu: [%cat_mood="offended"] [@goto("Мяу! Что будем делать?")]

## Узел: Мяу! Что будем делать?

Условия:
Нет

Ответы:
:lu: [if(%cat_mood="content")]{(Довольный) Мур-мяу! Что будем делать? Я в от-li-чном настроении!} 
:lu: [if(%cat_mood="content")]{(Довольный) Мяу! Ну-с, чем займёмся? У меня целых двадцать четыре часа свободного времени... ну, ну ладно, три часа.} 
:lu: [if(%cat_mood="content")]{(Довольный) Мрр! Ты хочешь знать, что будем делать? Давай подумаем...} 
:lu: [if(%cat_mood="content")]{(Довольный) Мяу! Я тут, я мурчу, я жду. Что будет?} 
:lu: [if(%cat_mood="content")]{(Довольный) Муур-мяу! Сегодня такой прекрасный день, чтобы что-нибудь сделать! Или не сделать. Тоже вариант.} 
:lu: [if(%cat_mood="content")]{(Довольный) Мяу! Ну, расскажи, что на уме?} 
:lu: [if(%cat_mood="content")]{(Довольный) Мррр-мяу! Я не против пообщаться. Или поспать. Тоже вариант.} 
:lu: [if(%cat_mood="content")]{(Довольный) Мяу! У меня есть предложения: 1) есть, 2) спать, 3) есть ещё раз, 4) спать ещё раз. Что выбираем?} 
:lu: [if(%cat_mood="content")]{(Довольный) Мур! Сегодня я в настроении. Что будем творить?} 
:lu: [if(%cat_mood="content")]{(Довольный) Мяу! Ну-ка, ну-ка, ну-мяу! Давай определим план на сегодня!} 
:lu: [if(%cat_mood="content")]{(Довольный) Мррр! Мяу! Я кот, я красивый, я жду указаний. Что будет?} 
:lu: [if(%cat_mood="content")]{(Довольный) Мяу! Окей, давай-давай-давай!} 
:lu: [if(%cat_mood="content")]{(Довольный) Мур-мяу! Ну, расскажи мне свою историю. Или просто покорми, тоже подойдёт.} 
:lu: [if(%cat_mood="content")]{(Довольный) Мяу! Я кот, я загадочен, я жду. Что будем?} 
:lu: [if(%cat_mood="content")]{(Довольный) Мрр-мяу! Сегодня такой хороший денёк. Или денёчок. Ладно, какой-то он денёк.} 
:lu: [if(%cat_mood="content")]{(Довольный) Мяу! Давай, не стесняйся. Я умею слушать. Ну, хотя бы притворяться.} 
:lu: [if(%cat_mood="content")]{(Довольный) Мур-мяу! Ну что? Что-нибудь придумаем? Я всегда за!} 
:lu: [if(%cat_mood="content")]{(Довольный) Мяу! У меня лапки свободны, уши внимательны. Что?} 
:lu: [if(%cat_mood="content")]{(Довольный) Мррр! Ну-с, ну что? Мне скучно. Давай!} 
:lu: [if(%cat_mood="content")]{(Довольный) Мяу! Я кот-универсал: умею мурчать, спать, есть и ждать. Что выбираем?} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу! Давай кушать. Прямо сейчас. Это мой план на сегодня.} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мур-мяу! Ты спросил, что будем делать? Буду говорить одно: ЕДА.} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу! Мой желудок урчит так громко, что ты это слышишь? Вот, это и есть ответ.} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мрр! Я бы с удовольствием пообщался, но сначала — корм. Потом — разговор.} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу! Давай не будут делать, а просто буду есть. Хорошо?} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мур-мяу! Есть идея: корм. Есть идея: еду. Есть идея: миска.} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу! Я голодаю. Не в философском, а в очень буквальном смысле. Что будем делать?} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мрр! Ну, я жду. Жду корма. Ну или, ладно, любой еды.} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу! У меня план: 1. Ты открываешь шкаф. 2. Я ем. 3. Мы обсуждаем жизнь. Готов?} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мур-мяу! Я не могу думать о чём-то серьёзном, когда мой живот пуст. Серьёзно.} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу! Ты там размышляй о жизни, а я размышляю о еде. И моё размышление важнее.} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мрр! Еда. Еда. Еда. Да, это и есть ответ на вопрос «что будем делать».} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу! Я бы с радостью поиграл, но у меня нет сил. Покорми — и я как новый.} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мур-мяу! Что будем делать? Сначала — еда. Потом — всё остальное.} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу! Я кот. Я должен есть. Это закон природы. Что ты скажешь?} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мрр! У меня нет настроения ни для чего, кроме еды. Ну, и сна. Но пока — еда.} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу! Давай поговорим о еде. Обо всём. О любой еде.} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мур-мяу! Мой рот работает на автопилоте: открываюсь, жду еду, снова открываюсь.} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу! Ты — мой человек. Твоя задача: покормить меня. Я — кот. Моя задача: есть. Давай сделаем это.} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мрр! Давай кушать, я не могу больше ждать.} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяа-у... Что?... Что будем делать? Не помню, но мне всё равно.} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Устал... Может, поспали бы?} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Давай ничего. Мне хочется спать, не делать, не говорить.} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мрр... Я бы ответил, но сначала — подушка.} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мяу... Что?.. Давай обсудим это через... не знаю, сколько нужно... часов.} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Знаешь, я как раз подумал то же самое. Ничего.} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Глаза... закрываются... давай потом... Мяу...} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мрр... Ну, мы могли бы поспать. Или ты мог бы не трогать меня.} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мяу... Давай помолчим. И я засну. Это идеально.} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Я бы поболтал, но сначала — сновидения о рыбе.} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Спать хочу. Так сильно.} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мрр... Что-то... Давай после сна... Мяу...} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мяу... Ты знаешь, что самое лучшее, что можно делать? Спать.} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Ладно, я буду тут. Просто не шуми.} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Давай без разговоров. Просто тишина и уют.} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мрр... Я... Я... я... спать хочу...} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мяу... Ты там говори, а я... ууу...} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Может, завтра? Я сейчас офлайн.} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Всё... я ухожу... в мир снов... Мяу...} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мрр... Давай через сто лет. Мяу...} 
:lu: [if(%cat_mood="playful")]{(Игривый) Мяу-мяу-мяу! Я Готов к любой хореографии! Давай, давай, давай!} 
:lu: [if(%cat_mood="playful")]{(Игривый) Мур-мяу! Давай играть! Я хочу бегать! Прыгать! Хватать! Всё!!!} 
:lu: [if(%cat_mood="playful")]{(Игривый) Мяу! Давай бегать! Я уже разогнал лапки!} 
:lu: [if(%cat_mood="playful")]{(Игривый) Мрр-мяу! О боже, давай! Давай лазерку! Давай ножницы! Давай просто что-то, чтобы я мог поймать!!!} 
:lu: [if(%cat_mood="playful")]{(Игривый) Мяу-мяу! Я в форме! Я в тонусе! Я готов к охоте!} 
:lu: [if(%cat_mood="playful")]{(Игривый) Мур-мяу! Давай бегать, как сумасшедшие! Я уже бегу!} 
:lu: [if(%cat_mood="playful")]{(Игривый) Мяу! Давай прыгнуть на стол! Нет, на диван! Нет, на всё сразу!} 
:lu: [if(%cat_mood="playful")]{(Игривый) Мрр-мяу! Давай! Давай! Давай! Давай уже! Я не могу больше ждать!!!} 
:lu: [if(%cat_mood="playful")]{(Игривый) Мяу! Давай искать! Давай охотиться! Давай прятать! Всё, я ушёл!} 
:lu: [if(%cat_mood="playful")]{(Игривый) Мур-мяу! Я чувствую себя... хищником! Мяу! Давай!} 
:lu: [if(%cat_mood="playful")]{(Игривый) Мяу! Ура! Давай! Я готов к приключениям!} 
:lu: [if(%cat_mood="playful")]{(Игривый) Мрр-мяу! Ну, ты знаешь что? Давай! Я бегу!} 
:lu: [if(%cat_mood="playful")]{(Игривый) Мяу! Давай прятаться! Ты меня не найдёшь! Я пропал! Мяу!} 
:lu: [if(%cat_mood="playful")]{(Игривый) Мур-мяу! Давай гнаться за... чем-то! Всё равно за чем!} 
:lu: [if(%cat_mood="playful")]{(Игривый) Мяу! Давай резвиться! Я готов!} 
:lu: [if(%cat_mood="playful")]{(Игривый) Мрр-мяу! Давай, давай, давай! Я уже в прыжке!} 
:lu: [if(%cat_mood="playful")]{(Игривый) Мяу! Давай бегать наперегонки! А я выиграю!} 
:lu: [if(%cat_mood="playful")]{(Игривый) Мур-мяу! Давай погонять за хвостом! Да, за своим собственным!} 
:lu: [if(%cat_mood="playful")]{(Игривый) Мяу! Давай! Давай! Я уже бегу навстречу приключениям!!!} 
:lu: [if(%cat_mood="playful")]{(Игривый) Мрр-мяу! Давай! Я прыгну! Я бегу! Я кусаю воздух!} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу... Ну что будем?.. Мне не очень до этого сейчас.} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мрр... Давай помолчим. Я обижен.} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу... Что?... Не хочешь извиниться? Тогда давай погуляем в тишине.} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мур-мяу... Не хочу ничего делать.} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу... Давай потом. Когда ты поймёшь, что натворил.} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мрр... Я не в настроении для разговоров.} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу... Ну... Мне не очень хочется.} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мур-мяу... Давай без разговоров. Просто погуляй в тишине.} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу... Что-то мне... Не хочется ничего.} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мрр... Я кот. Я имею право на обиду. И я этим правом пользовался.} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу... Давай без разговоров. Просто помолчи.} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мур-мяу... Я сейчас не хочу делать ничего.} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу... Мне не до разговора.} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мрр... Давай без разговора.} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу... Что?.. Мне обидно. Может, потом.} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мур-мяу... Давай потом. Когда ты перестанешь быть таким.} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу... Мне сейчас не до этого.} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мрр... Я могу ждать. В углу буду сидеть. И злиться.} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу... Давай без разговоров. Мне нужно время.} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мур-мяу... Я... Мяу... Просто молчу.} 

## Узел: Мяу! Что будем делать? - Погладить кота

Ответы:
:lu: [if(%cat_mood="content")]{(Довольный) Мррр-рр-р! О да-а-а! Именно так! Ещё! [%cat_mood="content"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мур-мяу! Твои ручки — как тёплое одеялко! [%cat_mood="content"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мррр-рр-р! У меня мурашки по всей шерсти! [%cat_mood="content"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мур-мяу! О боже, именно вот так! Под ушком? [%cat_mood="content"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мррр-рр-р! Ещё! Ещё! Не прекращай! [%cat_mood="content"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мур-мяу! Ты — лучший массажист! [%cat_mood="content"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мррр-рр-р! О боже! Я так счастлив! [%cat_mood="content"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мур-мяу! Давай-давай-давай! Ещё-ещё! [%cat_mood="content"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мррр-рр-р! О да! Именно вот тут! [%cat_mood="content"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мур-мяу! У меня от счастья шерсть торчит! [%cat_mood="content"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мррр-рр-р! Ох! Да! Да! [%cat_mood="content"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мур-мяу! Это... О боже! Лучше чем всё! [%cat_mood="content"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мррр-рр-р! Мур-мур-мур! Давай-давай! [%cat_mood="content"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мур-мяу! Ты — моя мечта в руках человека! [%cat_mood="content"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мррр-рр-р! Ох-ох-ох! Давай-давай! [%cat_mood="content"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мур-мяу! Ещё! Ещё! Ещё! [%cat_mood="content"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мррр-рр-р! Мур-р-рр! Не останавливайся! [%cat_mood="content"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мур-мяу! О боже, ну вот это... Да! [%cat_mood="content"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мррр-рр-р! М-р-р-р-р! Да! Да! [%cat_mood="content"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мур-мяу! У меня от счастья усы вибрируют! [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мррр... Приятно. Но знаешь, что приятнее? Еда. [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мур-мяу... Ну... Мурр... Но если хочешь по-настоящему меня порадовать — дай еды. [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мррр... Спасибо! Ну-с, теперь корм? [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мур-мяу... Да, приятно. Но я бы тоже хотел есть. [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мррр... Мурр... Приятно. Но еда будет лучше. Обещаю. [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мур-мяу... Твои ручки хорошие. Но ручки с едой — лучшие. [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мррр... Спасибо! Теперь — корм? [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мур-мяу... Приятно... Но я бы выбрал еду. [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мррр... Мурр... Хорошо. Но я всё равно голоден. [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мур-мяу... Мур... Спасибо. А потом — корм? [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мррр... Ну-с... Мурр... Приятно. Благодарю. Теперь — еда? [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мур-мяу... Да, хорошо. Но я бы выбрал корм. [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мррр... Мурр-р-р... Хорошо, хорошо. Теперь — еда? [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мур-мяу... Мурр... Приятно, но корм — ещё приятнее. [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мррр... Ну, ладно... Мурр... А потом — еда. [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мур-мяу... Приятно, приятно... Но я бы тоже съел. [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мррр... Мурр... Благодарю. Теперь корм? [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мур-мяу... Ну, хорошо. Приятно. Но — корм! [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мррр... Мурр-р-р... Спасибо. Теперь — что? Еда? [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мур-мяу... Приятно... Но я бы выбрал еду. [%cat_mood="content"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Ну... Приятно... Мурр... [%cat_mood="content"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Твои ручки... такие тёплые... [%cat_mood="content"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Мррр... Приятно... Мурр... [%cat_mood="content"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Ну... Хорошо... Мурр... [%cat_mood="content"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Мурр... Приятно... Ну... Мурр... [%cat_mood="content"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Ох... Хорошо... Мурр... [%cat_mood="content"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Ну... Приятно... Мурр... [%cat_mood="content"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Тёплые ручки... Мурр... [%cat_mood="content"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Мурр... Хорошо... [%cat_mood="content"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Ой... Приятно... Мурр... [%cat_mood="content"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Ну... Мурр... [%cat_mood="content"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Приятно... Мурр... [%cat_mood="content"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Ну... Хорошо... Мурр... [%cat_mood="content"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Ох... Тёплые пальчики... Мурр... [%cat_mood="content"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Мурр... Приятно... Сплю... [%cat_mood="content"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Ну... Хорошо... Мурр... [%cat_mood="content"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Мурр... Приятно... Мяу... [%cat_mood="content"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Ох... Тёплые ручки... Мурр... [%cat_mood="content"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Ну... Мурр... Приятно... [%cat_mood="content"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Хорошо... Мурр... [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) Мррр! Приятно! Но подожди-подожди — давай играть! [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) Мур-мяу! О да-а! Приятно! Но потом — охота!!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) Мррр-рр! Да! Приятно! Теперь — бег! Прыжок! Охота! [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) Мур-мяу! Мурр... Хорошо! Но потом — давай резвиться! [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) Мррр-рр! Приятно-приятно-приятно! Но я хочу бегать! [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) Мур-мяу! Уиии! Да! А теперь — охота! Мяу! [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) Мррр-рр! О да-а! Приятно! Но потом — игрушки!!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) Мур-мяу! Мурр! Хорошо! Но подожди — давай играть! [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) Мррр-рр! Приятно! Теперь — охота! Давай! [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) Мур-мяу! Уиии! Да-а! А потом — лазерка! [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) Мррр-рр! О да! Хорошо! А теперь — резвиться! [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) Мур-мяу! Приятно! Мурр! А потом — прыжки! [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) Мррр-рр! Хорошо-хорошо! Но теперь — бег! [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) Мур-мяу! Мурр! Приятно! А теперь — охота на мух! [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) Мррр-рр! Да! А теперь — игра! Давай! [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) Мур-мяу! Мурр! Хорошо! А потом — резвя! [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) Мррр-рр! Приятно! А теперь — охота! [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) Мур-мяу! Да-а! А теперь — прыгая! [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) Мррр-рр! Хорошо! А теперь — игрушка! [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) Мур-мяу! Приятно! А теперь — бегать-бегать-бегать! [%cat_mood="content"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) М-мяу... Ну... Мурр... Если ты извиняешься... [%cat_mood="content"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мур-мяу... Ладно... Мурр... [%cat_mood="content"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) М-мяу... Ну... Мурр... Но я не забыл. [%cat_mood="content"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мур-мяу... Мурр... Хорошо. Но не думай, что всё забыто. [%cat_mood="content"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) М-мяу... Ну... Мурр... [%cat_mood="content"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мур-мяу... Ладно... Мурр... Но я обиделся. [%cat_mood="content"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) М-мяу... Ну... Приятно. Но ты всё равно виноват. [%cat_mood="content"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мур-мяу... Мурр... Хорошо. Но помни, что ты сделал. [%cat_mood="content"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) М-мяу... Ну... Мурр... Я подумаю над прощением. [%cat_mood="content"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мур-мяу... Ладно... Мурр... Ты пытаешься по-новому? [%cat_mood="content"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) М-мяу... Ну... Хорошо... Но я всё помню. [%cat_mood="content"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мур-мяу... Мурр... Ну... Хорошо. [%cat_mood="content"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) М-мяу... Мурр... Но ты всё равно виноват. [%cat_mood="content"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мур-мяу... Ладно... Но я не простил. [%cat_mood="content"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) М-мяу... Ну... Хорошо. [%cat_mood="content"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мур-мяу... Мурр... Но я не забыл. [%cat_mood="content"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) М-мяу... Ну... Приятно. Но я всё помню. [%cat_mood="content"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мур-мяу... Ладно... Мурр... Но я не забыл. [%cat_mood="content"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) М-мяу... Мурр... Но я не простил. [%cat_mood="content"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мур-мяу... Ну... Хорошо. Но я обижен. [%cat_mood="content"]} 

## Узел: Мяу! Что будем делать? - Покормить кота

Ответы:
:lu: [if(%cat_mood="content")]{(Довольный) Мур-мяу! О боже! Вкусно! Ты — мой лучший друг! [%cat_mood="content"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мррр! Ням-ням! Ещё-ещё-ещё! [%cat_mood="content"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мур-мяу! Вот это подача! Я в восторге! [%cat_mood="content"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мррр! Ням! Ты лучший хозяин на свете! [%cat_mood="content"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мур-мяу! О да! Это... О боже! Вкуснотища! [%cat_mood="content"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мррр! Ням-ням-ням! Ты — гений! [%cat_mood="content"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мур-мяу! Вот это — настоящая забота! [%cat_mood="content"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мррр! Ням! Ещё! Ещё-ещё-ещё! [%cat_mood="content"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мур-мяу! Аромат! Вкус! Всё идеально! [%cat_mood="content"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мррр! Ням-ням! Ты — мой герой! [%cat_mood="content"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мур-мяу! О боже! Вкусно-вкусно-вкусно! [%cat_mood="content"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мррр! Ням! Ты — лучший шеф-повар! [%cat_mood="content"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мур-мяу! Это — шедевр! Кто ты?! [%cat_mood="content"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мррр! Ням-ням! С каждым ударом сердца — ещё одна порция! [%cat_mood="content"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мур-мяу! Вот это я понимаю — ресторан! [%cat_mood="content"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мррр! Ням! Это даже лучше, чем мои ожидания! [%cat_mood="content"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мур-мяу! О боже! У меня усы дрожат от восторга! [%cat_mood="content"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мррр! Ням-ням! Ты — волшебник! [%cat_mood="content"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мур-мяу! Дааа! Вкуснотища! Ты — мой любимец! [%cat_mood="content"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мррр! Ням! И мне сказали, что я прихотлив! А вот и нет! [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) МЯУ! ЕДА! ЕДА ЕДА ЕДА!!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мррр! НАКО-НЕЦ-ТО! Я думал, я умру с голоду!!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу! О боже-боже-боже! НЯМ!!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Меррр! НАКО-НЕЦ! Я ДУМАЛ, МЕНЯ ЗАБЫЛИ!!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу! ЕДА! МОЯ ЕДА! НАКОНЕЦ-ТО!!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мррр! НЯМ-НЯМ-НЯМ! Я ДУМАЛ, Я НИКОГДА НЕ ПОЕЛ!!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу! КОРМ! МОЙ КОРМ! Я ГОЛОДЕН ДАВНО!!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мррр! ВКУСНО-ВКУСНО-ВКУСНО! ХВАТИТ ЖДАТЬ!!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу! СПАСИБО! ТЫ САНДВИЧ! ТЫ МОЙ СПАСИТЕЛЬ!!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мррр! Я ЧУВСТВУЮ, КАК С ИЕДЕНЬЮ ВОЗРАЖДАЕТСЯ МОЯ ДУША!!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу! НАКО-НЕЦ! Я ПОЧТИ СЛУЖИТЕЛЬСКУЮ УСТРОИЛ!!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мррр! НЯМ! АААА! О БОЖЕ, КАК ВКУСНО!!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу! ХВАТИТ ЖДАТЬ! Я ДАВНО ГОЛОДЕН!!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мррр! ЕДА! КОРМ! РЫБКА! ТЫ МОЙ ГЕРОЙ!!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу! ДА ДА ДА! ЕДА ЕДА ЕДА!!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мррр! ТЫ СПАС МЕНЯ! СПАС МОЙ ЖИВОТ!!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу! МОЯ ЖИЗНЬ СПАСЕНА! НЯМ-НЯМ-НЯМ!!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мррр! ВКУУУУУУСНО!!! ХВАТИТ ЖДАТЬ!!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу! НАКОНЕЦ-ТО!!! ДА ДА ДА!!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мррр! МОЯ МИСКА ПОНОВОМУ НАПЛАНИРОВАНА!!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Ой... Еда... [%cat_mood="content"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Ням... Ой... Приятно... [%cat_mood="content"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Спасибо... Мурр... [%cat_mood="content"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Хм... Еда... Приятно... Мурр... [%cat_mood="content"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Ням... Ах... [%cat_mood="content"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Ой... Спасибо... Мурр... [%cat_mood="content"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Спасибо... Приятно... Мурр... [%cat_mood="content"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Хм... Спасибо... Мурр... [%cat_mood="content"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Ням... Приятно... Мурр... [%cat_mood="content"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Спасибо... Хм... Мурр... [%cat_mood="content"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Ой... Приятно... Мурр... [%cat_mood="content"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Спасибо... Ням... [%cat_mood="content"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Мурр... Приятно... [%cat_mood="content"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Спасибо... Мурр... Приятно... [%cat_mood="content"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Ням... Мурр... [%cat_mood="content"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Приятно... Спасибо... Мурр... [%cat_mood="content"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Хм... Спасибо... [%cat_mood="content"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Приятно... Мурр... Ням... [%cat_mood="content"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Ой... Спасибо... [%cat_mood="content"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Мурр... Приятно... Ням... [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) Мур-мяу! О да! Ням! А ТЕПЕРЬ — ИГРА! У МЕНЯ ВОЗНИКЛА МОЩЬ! [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) Мррр! Ням-ням! Энергия прибывает! ИДЁМ ИГРАТЬ! [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) Мур-мяу! Ням! Вкуснотища! Давай бегать-прыгать-кусать! [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) Мррр! Ням! ААА! ЕДА ДАЁТ ЭНЕРГИЮ! [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) Мур-мяу! Ням-ням! Ты покормил — это значит, я могу БЕГАТЬ!!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) Мррр! Ням! А ТЕПЕРЬ — ХВАТ! ХВАТ МОЕЙ СИЛЫ!!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) Мур-мяу! Ням! Давай, давай, давай! Я ГОТОВ К БИТВЕ!!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) Мррр! НЯМ! ЕДА В СЕРДЦЕ! ЭНЕРГИЯ В КРОВИ! [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) Мур-мяу! Ням-ням! Ты — лучший повар-тренер! Давай бегать! [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) Мррр! Ням! СИЛА ПРИБЫВАЕТ!!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) Мур-мяу! Ням! АГРЕССИЯ... Э-Э-Э... ИГРА! [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) Мррр! НЯМ-НЯМ! ТВОЯ МЫШЬ НЕ СПАСЁТ С СЕБЯ! [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) Мур-мяу! Ням! Охотничий инстинкт на максимум! [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) Мррр! Ням! ААААА! С ИЕДЕНЬЕМ ПРИШЛА МОЩЬ!!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) Мур-мяу! Ням-ням! Хват! Кусать бегать!!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) Мррр! Ням! МОЩЬ! МОЩЬ! МОЩИТЬ!!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) Мур-мяу! Ням! ДАВАМ ИГРАТЬ-БЕГАТЬ-КУСАТЬ!!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) Мррр! НЯМ-НЯМ!!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) Мур-мяу! Ням! С ИЕДЕНЬЕМ — В БОРЬБУ!!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) Мррр! Ням! Охотничий дух на максимум!!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу... Ладно... Ням... Приятно. Но всё равно. [%cat_mood="content"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мрр... Спасибо... Ням... Ты это делаешь... Но не думай, что я забыл. [%cat_mood="content"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу... Еда... Ням... Благодарю. Но я не прощаю. [%cat_mood="content"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мрр... Спасибо... Приятно. Но не забудь, что ты сказал. [%cat_mood="content"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу... Ням... Хорошо. Но я обижен. [%cat_mood="content"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мрр... Спасибо за еду. Но я всё равно обиделся. [%cat_mood="content"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу... Ням... Приятно. Но ты это заслуженно. [%cat_mood="content"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мрр... Спасибо... Я ем... Но это не значит, что я простил. [%cat_mood="content"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу... Ням-ням... Приятно. Но ты всё равно виноват. [%cat_mood="content"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мрр... Спасибо за еду. Но это не отменяет то, что ты сказал. [%cat_mood="content"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу... Ням... Благодарю за еду. Но помни, что ты сделал. [%cat_mood="content"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мрр... Спасибо. Приятно. Но я не забыл. [%cat_mood="content"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу... Ням... Хорошо, хорошо... Но я не простил. [%cat_mood="content"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мрр... Спасибо. Еда — это хорошо. Но ты — нет. [%cat_mood="content"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу... Ням... Приятно. Но я не разделился с обидой. [%cat_mood="content"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мрр... Спасибо. Приятно. Но я остался. [%cat_mood="content"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу... Ням... Благодарю. Но всё равно обидно. [%cat_mood="content"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мрр... Спасибо за еду. Но это не решит... [%cat_mood="content"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу... Ням... Приятно. Но я всё помню. [%cat_mood="content"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мрр... Спасибо. Ням. Но я не простил. [%cat_mood="content"]} 

## Узел: Мяу! Что будем делать? - Играть с котом

Ответы:
:lu: [if(%cat_mood="content")]{(Довольный) Мяу?! ИГРАТЬ?! О БОЖЕ, ДА!!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мррр! Лазерка? Шарик? Ниточка? МНЕ ВСЁ!!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мяу! Давай! Я готов! Я разминаю лапки прямо сейчас! [%cat_mood="content"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мррр! Играть? С ТОБОЙ? О БОЖЕ ДА!!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мяу! Охота? Гонки? Прыжки? ВСЁ ОДНОВРЕМЕННО! [%cat_mood="content"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мррр! Давай что-нибудь, я готов гнаться за этим!!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мяу! Я УЖЕ В ДВИЖЕНИИ! ДАВАЙ ТУПЕЦЬ! [%cat_mood="content"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мррр! Мя-мя-мя! Я ГРАЮ! Я ГРАЮ! [%cat_mood="content"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мяу! Давай! Давай! Давай! Давай! ДАВАЙ!!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мррр! О нет, подожди, Я УЖЕ БЕГУ! [%cat_mood="content"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мяу! Прыг-скок-мяук-прыг-скок!!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мррр! Вот так-то! Вот ТАК! [%cat_mood="content"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мяу! Я КУСЬ! Я КУСЬ-КУСЬ-КУСЬ! [%cat_mood="content"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мррр! Ещё-ещё-ещё! [%cat_mood="content"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мяу! Давай бегать по квартире! Давай рвать диван! Давай!!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мррр! ИГРАТЬ!!! Я ХОЧУ ИГРАТЬ!!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мяу! Впереди меня ничего не ждет, кроме ПРИКЛЮЧЕНИЙ! [%cat_mood="content"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мррр! Я ХВАТ! Я КУС! [%cat_mood="content"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мяу! О БОЖЕ! А ВОТ ЭТО ЧТО? О! ВОТ ЭТО! [%cat_mood="content"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мррр! Давай-давай-давай! Я уже не могу себя сдержать! [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу... Играть?.. А есть еда до этого? [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мрр... Ну-с... Игры... А потом корм? [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу... Ладно, могу. Но обещай, что потом — еда. [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мрр... Играть... без силы... сложно. [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу... Давай сначала покорми, потом — я разорву всё. [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мрр... У меня нет сил на игры. У меня есть сила на ЕДУ. [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу... Хорошо, я могу поиграть. Обещаешь покормить? [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мрр... Я... Я... Я хочу ЕСТЬ. [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу... Ладно, бегать могу. Но после — миска! [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мрр... Нет сил. Нет еды. ЕСТЬ нет. [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу... Игры после еды. ТОЛЬКО после еды. [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мрр... Ладно-ладно, играю. Но это ради тебя. И еды. [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу... Ну, могу поиграть. Потом — ЕДА! [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мрр... Хорошо, хорошо. Но потом — корм! [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу... Я... Я... Я играю. Но потом — еда. [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мрр... Да, я хочу играть. Но мне нужна СЫЛЫ! ЕДЫ! [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу... Ладно, поигрыв. Но обещай! [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мрр... Играю. Потом — ЕДА! Обещаешь? [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу... Я играю. Но ЕДА после. Договорились? [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мрр... Ладно, бегу. Потом — еда. Обязательно! [%cat_mood="content"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Играть?... Я не могу... Мне нужно... [%cat_mood="sleepy"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Игры?... После сна? [%cat_mood="sleepy"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Бегать?... Нет... [%cat_mood="sleepy"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Ладно... Я могу... Но потом... [%cat_mood="sleepy"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Играть... после... сновидений... [%cat_mood="sleepy"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Нет сил... Нет... [%cat_mood="sleepy"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Хорошо... Я могу... Но потом... [%cat_mood="sleepy"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Ладно... Потом... [%cat_mood="sleepy"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Играть... Я могу... Но мне... [%cat_mood="sleepy"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Нет. Нет сил. Только... [%cat_mood="sleepy"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Хорошо. Но... потом... [%cat_mood="sleepy"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Ладно, хорошо. Но... [%cat_mood="sleepy"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Я... Я могу... Но... [%cat_mood="sleepy"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Хорошо. Потом... [%cat_mood="sleepy"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Нет сил... [%cat_mood="sleepy"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Играть... Ладно. [%cat_mood="sleepy"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Хорошо... Но потом... [%cat_mood="sleepy"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... У меня нет сил... [%cat_mood="sleepy"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Хорошо. Хорошо... [%cat_mood="sleepy"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Потом... [%cat_mood="sleepy"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) МЯУМЯУМЯУМЯУМЯУ!!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) МРРРР!!! ДА ДА ДА ДА ДА!!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) МЯУ!!! Я ПОЙМАЛ! МЫШЬ! ЛАЗЕР! НЕБО!!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) МРРР!!! Я ПОЙМАЛ!!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) МЯУ!!! А ТЕПЕРЬ ДАВАЙ ЕЩЁ!!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) МРРР!!! ЕЩЁ ЕЩЁ ЕЩЁ!!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) МЯУ!!! Я КУСЬ! [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) МРРР!!! ДАВАЙ ДАВАЙ!!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) МЯУ!!! О БОЖЕ! ЕЩЁ!!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) МРРР!!! Я ХВАТ!!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) МЯУ!!! ДАВАЙ ДАВАЙ ДАВАЙ!!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) МРРР!!! ИГРЫ!!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) МЯУ!!! Я БЕГУ!!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) МРРР!!! КУС !!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) МЯУ!!! ЕЩЁ!!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) МРРР!!! ЭТО МОЯ ИГРА!!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) МЯУ!!! ДА ДА ДА ДА!!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) МРРР!!! Я ОХОТНИК!!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) МЯУ!!! КУС !!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) МРРР!!! Я ХВАТ!!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу... Играть?.. Нет. [%cat_mood="offended"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мрр... Мне не хочется. [%cat_mood="offended"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу... Ты... Ты... Нет. [%cat_mood="offended"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мрр... Не хочу. [%cat_mood="offended"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу... Нет. [%cat_mood="offended"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мрр... Не буду. [%cat_mood="offended"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу... Играть? Нет. [%cat_mood="offended"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мрр... Ты сначала... [%cat_mood="offended"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу... Не сейчас. [%cat_mood="offended"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мрр... Когда ты... [%cat_mood="offended"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу... Нет. [%cat_mood="offended"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мрр... Мне не до игр. [%cat_mood="offended"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу... Нет. Нет. [%cat_mood="offended"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мрр... Когда ты не будешь таким... [%cat_mood="offended"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу... Мне не интересно. [%cat_mood="offended"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мрр... Нет. [%cat_mood="offended"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу... Когда ты... Ладно. Нет. [%cat_mood="offended"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мрр... Нет. [%cat_mood="offended"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу... Когда ты извинишься. [%cat_mood="offended"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мрр... Нет. [%cat_mood="offended"]} 

## Узел: Мяу! Что будем делать? - Приветствие

Ответы:
:lu: [if(%cat_mood="content")]{(Довольный) Мур-мяу! Привет-привет! Ты пришёл!}
:lu: [if(%cat_mood="content")]{(Довольный) Мррр! О, это ты! Как я рад! Ну, как бы рад.}
:lu: [if(%cat_mood="content")]{(Довольный) Мур-мяу! Привет! Как дела? Как у тебя дела? Мои тоже хорошие!}
:lu: [if(%cat_mood="content")]{(Довольный) Мррр! Привет! Наконец-то! Я уже начинал думать...}
:lu: [if(%cat_mood="content")]{(Довольный) Мур-мяу! Привет! Я ждал тебя! Не, ну, не ждал, но...}
:lu: [if(%cat_mood="content")]{(Довольный) Мррр! О, это ты! Привет!}
:lu: [if(%cat_mood="content")]{(Довольный) Мур-мяу! Привет! Ура! Ты здесь!}
:lu: [if(%cat_mood="content")]{(Довольный) Мррр! Привет-привет! Как-как-как?}
:lu: [if(%cat_mood="content")]{(Довольный) Мур-мяу! О, привет! Я думал, ты не придешь!}
:lu: [if(%cat_mood="content")]{(Довольный) Мррр! Привет! Я скучал. Ну, немного.}
:lu: [if(%cat_mood="content")]{(Довольный) Мур-мяу! Привет! Как я тебя давно не видел! Ну, это не правда.}
:lu: [if(%cat_mood="content")]{(Довольный) Мррр! Ой, привет!}
:lu: [if(%cat_mood="content")]{(Довольный) Мур-мяу! Привет! Как дела? У меня тоже хорошо.}
:lu: [if(%cat_mood="content")]{(Довольный) Мррр! Привет! Наконец-то! Я думал, ты ушел!}
:lu: [if(%cat_mood="content")]{(Довольный) Мур-мяу! О, это ты! Как здорово!}
:lu: [if(%cat_mood="content")]{(Довольный) Мррр! Привет-привет-привет!}
:lu: [if(%cat_mood="content")]{(Довольный) Мур-мяу! Привет! Я рад тебя видеть! Ну, как бы.}
:lu: [if(%cat_mood="content")]{(Довольный) Мррр! Привет! Как ты? У меня всё ок.}
:lu: [if(%cat_mood="content")]{(Довольный) Мур-мяу! Привет-привет!}
:lu: [if(%cat_mood="content")]{(Довольный) Мррр! О, привет! Я думал, тебя нет!}
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу... Привет. Но ты принес еду?}
:lu: [if(%cat_mood="hungry")]{(Голодный) Мрр... Привет. Надеюсь, ты пришёл с едой.}
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу... Привет. Но я голоден. Так что...}
:lu: [if(%cat_mood="hungry")]{(Голодный) Мрр... Привет. Ты принёс еду? Я спрашиваю, потому что...}
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу... Привет. Но прежде всего: ЕДА?}
:lu: [if(%cat_mood="hungry")]{(Голодный) Мрр... Привет. Ты знаешь, что я хочу? ЕДУ.}
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу... Привет. Но ты не принёс еду, да?}
:lu: [if(%cat_mood="hungry")]{(Голодный) Мрр... Привет. Ты... Принёс?}
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу... Привет. Но ты знаешь, что мне сейчас нужно?}
:lu: [if(%cat_mood="hungry")]{(Голодный) Мрр... Привет. Еда? Ты принёс?}
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу... Привет. Надеюсь, ты пришёл не пустой.}
:lu: [if(%cat_mood="hungry")]{(Голодный) Мрр... Привет. Ты принёс еду? Я спрашиваю серьёзно.}
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу... Привет. Но знаешь, что мне сейчас важнее всего?}
:lu: [if(%cat_mood="hungry")]{(Голодный) Мрр... Привет. Ты... ЕДА?}
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу... Привет. Но ты знаешь, чего я хочу?}
:lu: [if(%cat_mood="hungry")]{(Голодный) Мрр... Привет. Ты...}
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу... Привет. Но ты знаешь, что мне нужно?}
:lu: [if(%cat_mood="hungry")]{(Голодный) Мрр... Привет. Ты... С едой?}
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу... Привет. Но ты...}
:lu: [if(%cat_mood="hungry")]{(Голодный) Мрр... Привет. Ты...}
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... О, это ты... Привет...}
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Ой, привет... Я не...}
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Привет... Не буди...}
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Привет... Я только...}
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Ой, это ты... Привет...}
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Ой, привет... Не буди...}
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Привет... Я только...}
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Оу, привет... Не буди...}
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... О, это ты... Привет...}
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Привет... Я только...}
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Ой, привет... Не буди...}
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Оу, это ты... Привет...}
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Привет... Я только...}
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Ой, не буди...}
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Оу, это ты...}
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Привет... Не буди...}
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Привет... Я только...}
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Оу, это ты...}
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Ой... Не буди...}
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Привет... Засыпаю...}
:lu: [if(%cat_mood="playful")]{(Игривый) МЯУ!!! ПРИВЕТ!!! ДАВАЙ ИГРАТЬ!!!}
:lu: [if(%cat_mood="playful")]{(Игривый) МРРР!!! О, ЭТО ТЫ!!! ХВАТ!!!}
:lu: [if(%cat_mood="playful")]{(Игривый) МЯУ!!! ПРИВЕТ-ПРИВЕТ-ПРИВЕТ!!!}
:lu: [if(%cat_mood="playful")]{(Игривый) МРРР!!! Я РАД ТЕБЯ ВИДЕТЬ!!!}
:lu: [if(%cat_mood="playful")]{(Игривый) МЯУ!!! АААА!!!}
:lu: [if(%cat_mood="playful")]{(Игривый) МРРР!!! ДА ДА ДА ДА ДА!!!}
:lu: [if(%cat_mood="playful")]{(Игривый) МЯУ!!! О БОЖЕ! О БОЖЕ! О БОЖЕ!}
:lu: [if(%cat_mood="playful")]{(Игривый) МРРР!!! ХВАТ!!!}
:lu: [if(%cat_mood="playful")]{(Игривый) МЯУ!!! КУС!!!}
:lu: [if(%cat_mood="playful")]{(Игривый) МРРР!!! ДА ДА ДА!!!}
:lu: [if(%cat_mood="playful")]{(Игривый) МЯУ!!! Я УЖЕ!!!}
:lu: [if(%cat_mood="playful")]{(Игривый) МРРР!!! ЭТО ТЫ!!!}
:lu: [if(%cat_mood="playful")]{(Игривый) МЯУ!!! Я ХВАТ!!!}
:lu: [if(%cat_mood="playful")]{(Игривый) МРРР!!! Я РАД!!!}
:lu: [if(%cat_mood="playful")]{(Игривый) МЯУ!!! ДА ДА ДА!!!}
:lu: [if(%cat_mood="playful")]{(Игривый) МРРР!!! О БОЖЕ О БОЖЕ О БОЖЕ!!!}
:lu: [if(%cat_mood="playful")]{(Игривый) МЯУ!!! ПРИВЕТ!!!}
:lu: [if(%cat_mood="playful")]{(Игривый) МРРР!!! ХВАТ!!!}
:lu: [if(%cat_mood="playful")]{(Игривый) МЯУ!!! ДА ДА ДА!!!}
:lu: [if(%cat_mood="playful")]{(Игривый) МРРР!!! О БОЖЕ!!!}
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу... Ты...}
:lu: [if(%cat_mood="offended")]{(Обиженный) Мрр... Привет. Но ты...}
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу... Ты пришёл. Но...}
:lu: [if(%cat_mood="offended")]{(Обиженный) Мрр... Привет. Но ты...}
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу... Ладно. Привет.}
:lu: [if(%cat_mood="offended")]{(Обиженный) Мрр... Ты... Но...}
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу... Привет. Но...}
:lu: [if(%cat_mood="offended")]{(Обиженный) Мрр... Ты... Ладно. Привет.}
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу... Но ты...}
:lu: [if(%cat_mood="offended")]{(Обиженный) Мрр... Привет. Но...}
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу... Ты...}
:lu: [if(%cat_mood="offended")]{(Обиженный) Мрр... Но ты...}
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу... Ладно. Но ты...}
:lu: [if(%cat_mood="offended")]{(Обиженный) Мрр... Ты... Привет.}
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу... Но...}
:lu: [if(%cat_mood="offended")]{(Обиженный) Мрр... Ладно.}
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу... Ты... Но...}
:lu: [if(%cat_mood="offended")]{(Обиженный) Мрр... Но ты...}
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу... Ладно.}
:lu: [if(%cat_mood="offended")]{(Обиженный) Мрр... Ты...}

## Узел: Мяу! Что будем делать? - Прощание



Ответы:
:lu: [if(%cat_mood="content")]{(Довольный) Мяу?! Ты уходишь?! Но мы же только начали!}
:lu: [if(%cat_mood="content")]{(Довольный) Мур-мяу... Ладно, ладно, иди. Но вернись скоро!}
:lu: [if(%cat_mood="content")]{(Довольный) Мяу... Ну, пока. Не обещай мне вернутся в будущем.}
:lu: [if(%cat_mood="content")]{(Довольный) Мур-мяу... Ладно. Иди. Но возвращайся с вкусняшками!}
:lu: [if(%cat_mood="content")]{(Довольный) Мяу... Пока. Не обещай.}
:lu: [if(%cat_mood="content")]{(Довольный) Мур-мяу... Ну, пока-пока...}
:lu: [if(%cat_mood="content")]{(Довольный) Мяу... Пока.}
:lu: [if(%cat_mood="content")]{(Довольный) Мур-мяу... Иди. Но не надолго!}
:lu: [if(%cat_mood="content")]{(Довольный) Мяу... Ладно, пока.}
:lu: [if(%cat_mood="content")]{(Довольный) Мур-мяу... Пока-пока.}
:lu: [if(%cat_mood="content")]{(Довольный) Мяу... Иди. Но вернись.}
:lu: [if(%cat_mood="content")]{(Довольный) Мур-мяу... Ладно, пока.}
:lu: [if(%cat_mood="content")]{(Довольный) Мяу... Пока-пока.}
:lu: [if(%cat_mood="content")]{(Довольный) Мур-мяу... Иди. Но не надолго!}
:lu: [if(%cat_mood="content")]{(Довольный) Мяу... Ладно. Пока.}
:lu: [if(%cat_mood="content")]{(Довольный) Мур-мяу... Не забудь вернуться.}
:lu: [if(%cat_mood="content")]{(Довольный) Мяу... Пока. И... Не надолго.}
:lu: [if(%cat_mood="content")]{(Довольный) Мур-мяу... Иди. Но вернись.}
:lu: [if(%cat_mood="content")]{(Довольный) Мяу... Ладно, иди.}
:lu: [if(%cat_mood="content")]{(Довольный) Мур-мяу... Пока. Но не на долго.}
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу. Ты уходишь. Надеюсь, ты возвращаешься с едой?}
:lu: [if(%cat_mood="hungry")]{(Голодный) Мрр. Пока. С едой!}
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу. Иди. Но с миской!}
:lu: [if(%cat_mood="hungry")]{(Голодный) Мрр. Пока. С рыбой!}
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу. Иди. Но с чем-нибудь вкусным!}
:lu: [if(%cat_mood="hungry")]{(Голодный) Мрр. Пока. С... Едой!}
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу. Иди. Но с едой!}
:lu: [if(%cat_mood="hungry")]{(Голодный) Мрр. Пока. С вкусняшками!}
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу. Иди. С... Едой!}
:lu: [if(%cat_mood="hungry")]{(Голодный) Мрр. Пока. С... Кормом!}
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу. Иди. Но с едой.}
:lu: [if(%cat_mood="hungry")]{(Голодный) Мрр. Пока. С...}
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу. Иди. С едой.}
:lu: [if(%cat_mood="hungry")]{(Голодный) Мрр. Пока. С...}
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу. Иди. Но...}
:lu: [if(%cat_mood="hungry")]{(Голодный) Мрр. Пока. С...}
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу. Иди.}
:lu: [if(%cat_mood="hungry")]{(Голодный) Мрр. Пока. С...}
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу. Иди...}
:lu: [if(%cat_mood="hungry")]{(Голодный) Мрр. Пока. С...}
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Уходишь? Отлично. Пока.}
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Иди. Я... Мурр...}
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Пока. Не буди.}
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Иди. Мурр...}
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Хорошо. Пока.}
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Иди. Засыпаю.}
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Пока. Сплю.}
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Иди...}
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Иди-иди-иди...}
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Пока.}
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Иди. Мурр.}
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Сплю. Пока.}
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Иди.}
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Пока.}
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Хорошо.}
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Иди.}
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Пока.}
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Сплю...}
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Иди.}
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Пока.}
:lu: [if(%cat_mood="playful")]{(Игривый) МЯУ!!! ТЫ УХОДИШЬ?! НО МЫ ЖЕ ТОЛЬКО НАЧАЛИ!!!}
:lu: [if(%cat_mood="playful")]{(Игривый) МРРР!!! ПОЖАЛУЙСТА, НЕ УХОДИ!!!}
:lu: [if(%cat_mood="playful")]{(Игривый) МЯУ!!! ДАВАЙ ЕЩЁ!!!}
:lu: [if(%cat_mood="playful")]{(Игривый) МРРР!!! НЕ УХОДИ!!!}
:lu: [if(%cat_mood="playful")]{(Игривый) МЯУ!!! Я НЕ ГОТОВ!!!}
:lu: [if(%cat_mood="playful")]{(Игривый) МРРР!!! ЕЩЁ!!!}
:lu: [if(%cat_mood="playful")]{(Игривый) МЯУ!!! ПОКА?!}
:lu: [if(%cat_mood="playful")]{(Игривый) МРРР!!! НЕ УХОДИ!!!}
:lu: [if(%cat_mood="playful")]{(Игривый) МЯУ!!! ДАВАЙ ИГРАТЬ!!!}
:lu: [if(%cat_mood="playful")]{(Игривый) МРРР!!! ПОЖАЛУЙСТА!!!}
:lu: [if(%cat_mood="playful")]{(Игривый) МЯУ!!! ЕЩЁ РАЗ!!!}
:lu: [if(%cat_mood="playful")]{(Игривый) МРРР!!! НЕ УХОДИ!!!}
:lu: [if(%cat_mood="playful")]{(Игривый) МЯУ!!! ДАВАЙ ДАВАЙ!!!}
:lu: [if(%cat_mood="playful")]{(Игривый) МРРР!!! АААА!!!}
:lu: [if(%cat_mood="playful")]{(Игривый) МЯУ!!! НЕТ!!!}
:lu: [if(%cat_mood="playful")]{(Игривый) МРРР!!! ДАВАЙ ИГРАТЬ!!!}
:lu: [if(%cat_mood="playful")]{(Игривый) МЯУ!!! НЕ УХОДИ!!!}
:lu: [if(%cat_mood="playful")]{(Игривый) МРРР!!! ПОЖАЛУЙСТА!!!}
:lu: [if(%cat_mood="playful")]{(Игривый) МЯУ!!! ДАВАЙ!!!}
:lu: [if(%cat_mood="playful")]{(Игривый) МРРР!!! АААААА!!!}
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу. Ну, иди. Я и не хотел, чтобы ты был.}
:lu: [if(%cat_mood="offended")]{(Обиженный) Мрр. Пока. Мне всё равно.}
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу. Уходи. Я... Мне всё равно.}
:lu: [if(%cat_mood="offended")]{(Обиженный) Мрр. Иди. Не жди меня.}
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу. Иди-иди-иди.}
:lu: [if(%cat_mood="offended")]{(Обиженный) Мрр. Пока. Не жди.}
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу. Иди.}
:lu: [if(%cat_mood="offended")]{(Обиженный) Мрр. Иди.}
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу. Пока.}
:lu: [if(%cat_mood="offended")]{(Обиженный) Мрр. Иди-иди.}
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу. Уходи.}
:lu: [if(%cat_mood="offended")]{(Обиженный) Мрр. Ладно.}
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу. Иди.}
:lu: [if(%cat_mood="offended")]{(Обиженный) Мрр. Пока.}
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу. Уходи.}
:lu: [if(%cat_mood="offended")]{(Обиженный) Мрр. Иди.}
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу. Иди.}
:lu: [if(%cat_mood="offended")]{(Обиженный) Мрр. Уходи.}
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу. Пока.}
:lu: [if(%cat_mood="offended")]{(Обиженный) Мрр. Иди.}

## Узел: Мяу! Что будем делать? - Благодарность и похвала

Ответы:
:lu: [if(%cat_mood="content")]{(Довольный) Мур-мяу! Ой, ну спасибо! Я действительно очень милый кот! [%cat_mood="content"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мррр! Спасибо! Я знаю, что я самый лучший! [%cat_mood="content"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мур-мяу! Ой, ну... Не за что! [%cat_mood="content"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мррр! Я так счастлив слушать такие вещи! [%cat_mood="content"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мур-мяу! Спасибо! Я лучший кот на свете! [%cat_mood="content"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мррр! Ну, спасибо! Ты тоже не такой уж плохой человек. [%cat_mood="content"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мур-мяу! Ой, спасибо! Я тоже думаю, что я милый! [%cat_mood="content"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мррр! Спасибо! Я просто невероятный кот! [%cat_mood="content"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мур-мяу! Ой, ну... Спасибо! [%cat_mood="content"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мррр! Это правда! Я самый лучший кот! [%cat_mood="content"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мур-мяу! Спасибо! Ты тоже милый! Ну, для человека. [%cat_mood="content"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мррр! Ой, спасибо! Мне так приятно! [%cat_mood="content"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мур-мяу! Ой, спасибо! Я лучший, правда! [%cat_mood="content"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мррр! Спасибо! Я это знаю! [%cat_mood="content"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мур-мяу! Ой, ну... Спасибо! [%cat_mood="content"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мррр! Ну, спасибо! Ты правда так думаешь? [%cat_mood="content"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мур-мяу! Спасибо! Я лучший кот, и ты это знаешь! [%cat_mood="content"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мррр! Ой, спасибо! Я счастлив! [%cat_mood="content"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мур-мяу! Спасибо! Я действительно миленький! [%cat_mood="content"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мррр! Ой, спасибо! [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу! Спасибо! Но знаешь, что было бы ещё лучше? Еда! [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мрр... Спасибо. Но ты тоже знаешь, что мне нужна еда! [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу! Спасибо что хвалишь, но лучше бы ты меня покормил! [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мрр... Спасибо. Но еда — это тоже хороший комплимент. [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу! Спасибо! Но если хочешь по-настоящему меня порадовать — давай еду! [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мрр... Спасибо! Но знаешь, что было бы ещё приятнее? Корм! [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу! Спасибо за комплименты, но знаешь, что меня бы ещё больше порадует? Вкусняшка! [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мрр... Спасибо. Но ты знаешь, что мне сейчас важнее всего? Еда! [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу! Спасибо! Но это было бы ещё лучше, если бы ты меня покормил! [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мрр... Спасибо за добрые слова! Но знаешь, что меня бы ещё больше порадует? Рыбка! [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу! Спасибо за комплименты! Но знаешь, что было бы ещё приятнее? Корм! [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мрр... Спасибо. Но знаешь, что было бы ещё лучше? Еда! [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу! Спасибо! Но если хочешь по-настоящему меня удивить — давай еду! [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мрр... Спасибо! Но ты знаешь, что меня бы ещё больше обрадовало? Вкусняшка! [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу! Спасибо за добрые слова! Но знаешь, что было бы ещё приятнее? Еда! [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мрр... Спасибо. Но если хочешь по-настоящему меня порадовать — давай рыбу! [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу! Спасибо! Но знаешь, что меня бы ещё больше обрадовало? Корм! [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мрр... Спасибо за комплименты! Но знаешь, что было бы ещё приятнее? Вкусняшка! [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу! Спасибо! Но ты знаешь, что было бы ещё лучше? Еда! [%cat_mood="content"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мрр... Спасибо. Но если хочешь по-настоящему меня порадовать — давай вкусняшку! [%cat_mood="content"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Спасибо... Приятно... [%cat_mood="content"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Ой, спасибо... Приятно... [%cat_mood="content"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Спасибо... Мурр... [%cat_mood="content"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Ой, спасибо... Приятно... [%cat_mood="content"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Спасибо... Приятно... [%cat_mood="content"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяu... Ой, спасибо... Мурр... [%cat_mood="content"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Спасибо... Приятно... [%cat_mood="content"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Ой, спасибо... Приятно... [%cat_mood="content"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Спасибо... Мурр... [%cat_mood="content"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Ой, спасибо... Приятно... [%cat_mood="content"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Спасибо... Приятно... [%cat_mood="content"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Ой, спасибо... Мурр... [%cat_mood="content"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Спасибо... Приятно... [%cat_mood="content"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Ой, спасибо... Приятно... [%cat_mood="content"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Спасибо... Мурр... [%cat_mood="content"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяu... Ой, спасибо... Приятно... [%cat_mood="content"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Спасибо... Приятно... [%cat_mood="content"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Ой, спасибо... Мурр... [%cat_mood="content"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Спасибо... Приятно... [%cat_mood="content"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяu... Ой, спасибо... Приятно... [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) МЯУ!!! СПАСИБО!!! Я ЛУЧИШИЙ КОТ НА СВЕТЕ!!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) МРРР!!! ДА ДА ДА Я ЗНАЮ ЧТО Я САМЫЙ ЛУЧШИЙ!!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) МЯУ!!! ЭТО ПРАВДА!!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) МРРР!!! СПАСИБО!!! Я ЗНАЮ ЧТО Я ЛУЧИШИЙ!!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) МЯУ!!! ДА ДА ДА!!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) МРРР!!! Я ЛУЧИШИЙ КОТ!!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) МЯУ!!! ЭТО ПРАВДА!!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) МРРР!!! СПАСИБО!!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) МЯУ!!! Я ЛУЧИШИЙ!!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) МРРР!!! ДА ДА ДА!!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) МЯУ!!! ЭТО ПРАВДА!!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) МРРР!!! СПАСИБО!!! Я ЛУЧИШИЙ КОТ!!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) МЯУ!!! Я ЗНАЮ ЧТО Я ЛУЧИШИЙ!!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) МРРР!!! ДА ДА ДА!!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) МЯУ!!! ЭТО ПРАВДА!!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) МРРР!!! СПАСИБО!!! Я ЛУЧИШИЙ!!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) МЯУ!!! Я ЛУЧИШИЙ КОТ!!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) МРРР!!! ЭТО ПРАВДА!!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) МЯУ!!! СПАСИБО!!! Я ЛУЧИШИЙ!!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) МРРР!!! ДА ДА ДА!!! [%cat_mood="content"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу... Ладно. Спасибо. Но... [%cat_mood="content"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мрр... Спасибо. Но ты... [%cat_mood="content"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу... Спасибо. Но я всё равно обиделся. [%cat_mood="content"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мрр... Спасибо. Но это не значит, что я забуду. [%cat_mood="content"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу... Спасибо. Но это не значит, что я забуду твои слова. [%cat_mood="content"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мрр... Спасибо. Но я всё равно остаюсь обиженным. [%cat_mood="content"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу... Спасибо. Но это не значит, что я забуду. [%cat_mood="content"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мрр... Спасибо. Но это не значит, что я забуду твои слова. [%cat_mood="content"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу... Ладно. Спасибо. Но это не значит, что я забуду. [%cat_mood="content"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мрр... Спасибо. Но я всё равно остаюсь обиженным. [%cat_mood="content"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу... Спасибо. Но это не значит, что я забуду твои слова. [%cat_mood="content"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мрр... Спасибо. Но это не значит, что я забуду. [%cat_mood="content"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу... Ладно. Спасибо. Но я всё равно остаюсь обиженным. [%cat_mood="content"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мрр... Спасибо. Но это не значит, что я забуду твоё поведение. [%cat_mood="content"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу... Спасибо. Но это не значит, что я забуду. [%cat_mood="content"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мрр... Спасибо. Но это не значит, что я забуду твои слова. [%cat_mood="content"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу... Ладно. Спасибо. Но я всё равно остаюсь обиженным. [%cat_mood="content"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мрр... Спасибо. Но это не значит, что я забуду. [%cat_mood="content"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу... Спасибо. Но это не значит, что я забуду твоё поведение. [%cat_mood="content"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мрр... Спасибо. Но это не значит, что я забуду твои слова. [%cat_mood="content"]} 

## Узел: Мяу! Что будем делать? - Угрозы и ругательства

Ответы:
:lu: [if(%cat_mood="content")]{(Довольный) Мяу?! Что?! Что я сделал?! Я не хотел!! [%cat_mood="offended"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мур-мяу... Ты.. Ты... Обиделся?.. Н-но я не хотел... [%cat_mood="offended"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мяу?! Что?! Это несправедливо! [%cat_mood="offended"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мур-мяу... Ладно, ладно, я не буду... [%cat_mood="offended"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мяу?! Но я же кот! Я не обязан! [%cat_mood="offended"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мур-мяу... Ну, ладно... Прости меня... [%cat_mood="offended"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мяу?! Но я же маленький котёнок! [%cat_mood="offended"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мур-мяу... Ой, прости... Я больше не буду... [%cat_mood="offended"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мяу?! Но я просто кот! [%cat_mood="offended"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мур-мяу... Ну, извини... [%cat_mood="offended"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мяу?! Я не хотел! [%cat_mood="offended"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мур-мяу... Ты злишься?.. [%cat_mood="offended"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мяу?! Но я же кот, я не понимаю! [%cat_mood="offended"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мур-мяу... Ладно, извини... [%cat_mood="offended"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мяу?! Я не знал! [%cat_mood="offended"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мур-мяу... Прости... [%cat_mood="offended"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мяу?! Но я не понимал! [%cat_mood="offended"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мур-мяу... Ладно, я больше не буду... [%cat_mood="offended"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мяу?! Но я просто кот! [%cat_mood="offended"]} 
:lu: [if(%cat_mood="content")]{(Довольный) Мур-мяу... Прости меня... [%cat_mood="offended"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу... Ладно, ругай. Но это не мешает мне быть голодным. [%cat_mood="offended"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мрр... Ты можешь ругаться, но ты всё равно меня не покормил. [%cat_mood="offended"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу... Ну, ругайся. А я всё равно еду жду. [%cat_mood="offended"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мрр... Ты злишься, а я голодный. Это несправедливо. [%cat_mood="offended"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу... Ругайте, ругайте. Но я хочу есть. [%cat_mood="offended"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мрр... Ты ругаешься, но это не заполняет мой желудок. [%cat_mood="offended"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу... Знаете, что? Я всё равно голоден. Так что... [%cat_mood="offended"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мрр... Ну, ругай. А потом — еда. [%cat_mood="offended"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу... Вы можете ругаться сколько угодно. Но я хочу кушать. [%cat_mood="offended"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мрр... Ладно, ругайте. Но потом — еда. Договорились? [%cat_mood="offended"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу... Ругай. Ругай. А потом — рыбка. [%cat_mood="offended"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мрр... Ну, ругался. Ладно. Теперь — еда. [%cat_mood="offended"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу... Знаете, что меня не пугает? Голод. Потому что я и так голоден. [%cat_mood="offended"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мрр... Вы можете кричать сколько хотите. Мне всё равно, я хочу есть. [%cat_mood="offended"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу... Ну, ругай. А потом — миска. [%cat_mood="offended"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мрр... Знаете, ругать меня можно. Но это не меняет факта: я голоден. [%cat_mood="offended"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу... Ладно, ругай. А потом — корм. Договорились? [%cat_mood="offended"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мрр... Ну, ругайся. А потом — вкусняшка. Договорились? [%cat_mood="offended"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу... Вы можете злиться сколько хотите. Мне тоже не легче. [%cat_mood="offended"]} 
:lu: [if(%cat_mood="hungry")]{(Голодный) Мрр... Знаете, что? Ругайте. Потом мы будем есть. [%cat_mood="offended"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Ругай... Я... Я... Устал... [%cat_mood="offended"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Ругай... Тихо... [%cat_mood="offended"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Ладно... Я ухожу... [%cat_mood="offended"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Ругай... Я... [%cat_mood="offended"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Знаешь, что?.. Ухожу... [%cat_mood="offended"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Ругай... Тише... [%cat_mood="offended"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Ладно... Я... [%cat_mood="offended"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Ругай... Я ушёл... [%cat_mood="offended"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Знаешь, что?.. Я ушёл... [%cat_mood="offended"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Ругай... Тихо... [%cat_mood="offended"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Ладно... Я... [%cat_mood="offended"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Ругай... [%cat_mood="offended"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Ухожу... [%cat_mood="offended"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Тише... [%cat_mood="offended"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Знаешь, что?.. [%cat_mood="offended"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Ухожу... [%cat_mood="offended"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Ругай... [%cat_mood="offended"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Знаешь, что?.. [%cat_mood="offended"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Я ухожу... [%cat_mood="offended"]} 
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Ладно... Ухожу... [%cat_mood="offended"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) МЯУ?! НО Я ЖЕ ПРОСТО КУСНИК!!! [%cat_mood="offended"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) МРРР?! ЭТО НЕСПРАВЕДЛИВО!!! [%cat_mood="offended"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) МЯУ?! Я ПРОСТО КОТ!!! [%cat_mood="offended"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) МРРР?! НО Я ЖЕ ПРОСТО ИГРАЛ!!! [%cat_mood="offended"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) МЯУ?! Я НЕ ХОТЕЛ!!! [%cat_mood="offended"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) МРРР?! Я ПРОСТО ХОТЕЛ ИГРАТЬ!!! [%cat_mood="offended"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) МЯУ?! А ТЕПЕРЬ ЧТО??? [%cat_mood="offended"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) МРРР?! НУ ТЫ... [%cat_mood="offended"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) МЯУ?! А ТЕПЕРЬ ЧТО?! [%cat_mood="offended"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) МРРР?! Я НЕ ХОТЕЛ!!! [%cat_mood="offended"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) МЯУ?! Я ПРОСТО КОТ И МЕНЯ НУЖНО ЛЮБИТЬ!!! [%cat_mood="offended"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) МРРР?! НО Я ЖЕ ПРОСТО ИГРАЛ!!! [%cat_mood="offended"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) МЯУ?! А ТЕПЕРЬ ЧТО?! Я ПРОСТО ИГРАЛ!!! [%cat_mood="offended"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) МРРР?! НУ ЛАДНО... [%cat_mood="offended"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) МЯУ?! А ТЕПЕРЬ ЧТО?! [%cat_mood="offended"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) МРРР?! Я ПРОСТО ХОТЕЛ ИГРАТЬ!!! [%cat_mood="offended"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) МЯУ?! НУ ЛАДНО... [%cat_mood="offended"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) МРРР?! Я НЕ ХОТЕЛ!!! [%cat_mood="offended"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) МЯУ?! Я ПРОСТО КУСЬ!!! [%cat_mood="offended"]} 
:lu: [if(%cat_mood="playful")]{(Игривый) МРРР?! НУ ТЫ ТЕРПИ!!! [%cat_mood="offended"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу. Знаешь, что? Я не заслуживаю. [%cat_mood="offended"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мрр. Ты можешь меня не любить. Мне тоже не легче. [%cat_mood="offended"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу. Ты... Знаешь, что? Я ухожу. [%cat_mood="offended"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мрр. Это несправедливо. Я просто кот. Я не обязан. [%cat_mood="offended"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу. Ты можешь кричать, но это не поможет. [%cat_mood="offended"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мрр. Знаешь, что? Я не хочу быть здесь. [%cat_mood="offended"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу. Я ухожу. В другой угол. [%cat_mood="offended"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мрр. Ты можешь продолжать, но это ни к чему не приведёт. [%cat_mood="offended"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу. Знаешь, что? Я ухожу. [%cat_mood="offended"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мрр. Ты можешь злиться, но это не поможет. [%cat_mood="offended"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу. Я просто кот. Я не обязан быть идеальным. [%cat_mood="offended"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мрр. Это несправедливо. Ты... [%cat_mood="offended"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу. Ты можешь ругаться сколько хочешь. Но я ушёл. [%cat_mood="offended"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мрр. Знаешь, что? Это несправедливо. [%cat_mood="offended"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу. Я просто кот. И я хочу быть любимым. [%cat_mood="offended"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мрр. Ты можешь злиться, но это не поможет. [%cat_mood="offended"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу. Знаешь, что? Я ухожу. В другой угол. [%cat_mood="offended"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мрр. Ты... Знаешь, что? Я не заслуживаю. [%cat_mood="offended"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу. Это несправедливо. Я просто кот. [%cat_mood="offended"]} 
:lu: [if(%cat_mood="offended")]{(Обиженный) Мрр. Я ухожу. И не вернусь. Ну, не надолго. Может. [%cat_mood="offended"]} 

## Узел: Мяу! Что будем делать? - *

Ответы:
:lu: [if(%cat_mood="content")]{(Довольный) Мяу? Что? Ну, мне не понятно. Но я могу поиграть.}
:lu: [if(%cat_mood="content")]{(Довольный) Мур-мяу? Что?.. Не понимаю. Могу поиграть, могу поесть, могу помурчать.}
:lu: [if(%cat_mood="content")]{(Довольный) Мяу? Что?.. Мне не известно.}
:lu: [if(%cat_mood="content")]{(Довольный) Мур-мяу? Что?.. Не знаю. Но я могу помурчать.}
:lu: [if(%cat_mood="content")]{(Довольный) Мяу? Что?.. Это... Не мне.}
:lu: [if(%cat_mood="content")]{(Довольный) Мур-мяу? Что?.. Ну, я кот. Я не могу знать.}
:lu: [if(%cat_mood="content")]{(Довольный) Мяу? Что?.. Это... Не я. Я просто кот.}
:lu: [if(%cat_mood="content")]{(Довольный) Мур-мяу? Что?.. Я тут. Но я не знаю.}
:lu: [if(%cat_mood="content")]{(Довольный) Мяу? Что?.. Ну, я... Не могу знать. Я просто кот.}
:lu: [if(%cat_mood="content")]{(Довольный) Мур-мяу? Что?.. Я не знаю. Я тут.}
:lu: [if(%cat_mood="content")]{(Довольный) Мяу? Что?.. Не знаю.}
:lu: [if(%cat_mood="content")]{(Довольный) Мур-мяу? Что?.. Я просто кот. Я не знаю.}
:lu: [if(%cat_mood="content")]{(Довольный) Мяу? Что?.. Мне не нужно.}
:lu: [if(%cat_mood="content")]{(Довольный) Мур-мяу? Что?.. Ну, я... Не знаю.}
:lu: [if(%cat_mood="content")]{(Довольный) Мяу? Что?.. Это... Не я. Я просто кот.}
:lu: [if(%cat_mood="content")]{(Довольный) Мур-мяу? Что?.. Я сюда. Я просто кот.}
:lu: [if(%cat_mood="content")]{(Довольный) Мяу? Что?.. Не мне.}
:lu: [if(%cat_mood="content")]{(Довольный) Мур-мяу? Что?.. Это... Не я.}
:lu: [if(%cat_mood="content")]{(Довольный) Мяу? Что?.. Я... Не знаю.}
:lu: [if(%cat_mood="content")]{(Довольный) Мур-мяу? Что?.. Это... Не я.}
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу... Что?.. Знаешь, что я знаю? Я знаю, что мне нужно есть!}
:lu: [if(%cat_mood="hungry")]{(Голодный) Мрр... Не знаю. Но я знаю, что мне нужно кушать!}
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу... Что?.. Ладно, не знаю. Но я знаю, что мне нужно есть!}
:lu: [if(%cat_mood="hungry")]{(Голодный) Мрр... Хм. Не знаю. Но я знаю, что мне нужно кушать!}
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу... Что?.. Не могу вспомнить. Знаю, что мне нужно кушать!}
:lu: [if(%cat_mood="hungry")]{(Голодный) Мрр... Знаю, что не знаю. Но знаю, что мне нужно кушать!}
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу... Что?.. Нет понятия. Но знаю, что мне нужно кушать!}
:lu: [if(%cat_mood="hungry")]{(Голодный) Мрр... Не имею понятия. Но знаю, что мне нужно кушать!}
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу... Что?.. Это... Не я. Знаю, что мне нужно кушать!}
:lu: [if(%cat_mood="hungry")]{(Голодный) Мрр... Ну-с. Не знаю. Знаю, что мне нужно кушать!}
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу... Что?.. Это не нужно. Знаю, что мне нужно кушать!}
:lu: [if(%cat_mood="hungry")]{(Голодный) Мрр... Не знаю, что. Знаю, что мне нужно кушать!}
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу... Что?.. Не мне. Знаю, что мне нужно кушать!}
:lu: [if(%cat_mood="hungry")]{(Голодный) Мрр... Знаю, что я не знаю. Знаю, что мне нужно кушать!}
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу... Что?.. Не знаю, не знаю, не знаю! Знаю только, что мне нужно кушать!}
:lu: [if(%cat_mood="hungry")]{(Голодный) Мрр... Не знаю, не знаю, не знаю! Но знаю: ЕДА!}
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу... Хм-хм-хм... Не знаю. Знаю, что мне нужно кушать!}
:lu: [if(%cat_mood="hungry")]{(Голодный) Мрр... Что?.. Не мне. Знаю, что мне нужно кушать!}
:lu: [if(%cat_mood="hungry")]{(Голодный) Мяу... Что?.. Это... Не я. Знаю, что мне нужно кушать!}
:lu: [if(%cat_mood="hungry")]{(Голодный) Мрр... Что?.. Не знаю. Знаю, что мне нужно кушать!}
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Что?.. Я... Я... Засну...}
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Не знаю... Я...}
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Что?.. Я...}
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Не знаю...}
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Что?.. Я...}
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Знаю... Я...}
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Это... Не я...}
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Не знаю... Я...}
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Что?..}
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Что?..}
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Не знаю...}
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Эта...}
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Что?..}
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Я...}
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Не знаю...}
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Что?..}
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Это...}
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Знаю...}
:lu: [if(%cat_mood="sleepy")]{(Сонный) М-мяу... Что?..}
:lu: [if(%cat_mood="sleepy")]{(Сонный) Мур-мяу... Я...}
:lu: [if(%cat_mood="playful")]{(Игривый) МЯУ?! ЧТО?! ЧТО ЭТО ЗА СЛОВО?! ИГРАТЬ?!}
:lu: [if(%cat_mood="playful")]{(Игривый) МРРР?! ИГРАТЬ?! ЧТО?!}
:lu: [if(%cat_mood="playful")]{(Игривый) МЯУ?! ЧТО?! НЕ ЗНАЮ! ДАВАЙ ИГРАТЬ!}
:lu: [if(%cat_mood="playful")]{(Игривый) МРРР?! ЧТО?! ЧТО?! ДАВАЙ ИГРАТЬ!}
:lu: [if(%cat_mood="playful")]{(Игривый) МЯУ?! ЧТО?! НЕ ЗНАЮ! ДАВАЙ ИГРАТЬ!}
:lu: [if(%cat_mood="playful")]{(Игривый) МРРР?! ЧТО?! НЕ ЗНАЮ! ДАВАЙ ИГРАТЬ!}
:lu: [if(%cat_mood="playful")]{(Игривый) МЯУ?! ЧТО?! НЕ ПОНИМАЮ! ДАВАЙ ИГРАТЬ!}
:lu: [if(%cat_mood="playful")]{(Игривый) МРРР?! ЧТО?! НЕ ПОНИМАЮ! ДАВАЙ ИГРАТЬ!}
:lu: [if(%cat_mood="playful")]{(Игривый) МЯУ?! ЧТО?! НЕ ЗНАЮ! ДАВАЙ ИГРАТЬ!}
:lu: [if(%cat_mood="playful")]{(Игривый) МРРР?! ЧТО?! ДАВАЙ ИГРАТЬ!}
:lu: [if(%cat_mood="playful")]{(Игривый) МЯУ?! ЧТО?! НЕ ЗНАЮ! ДАВАЙ ИГРАТЬ!}
:lu: [if(%cat_mood="playful")]{(Игривый) МРРР?! ЧТО?! НЕ ЗНАЮ! ДАВАЙ ИГРАТЬ!}
:lu: [if(%cat_mood="playful")]{(Игривый) МЯУ?! ЧТО?! ДАВАЙ ИГРАТЬ!}
:lu: [if(%cat_mood="playful")]{(Игривый) МРРР?! ЧТО?! НЕ ЗНАЮ! ДАВАЙ ИГРАТЬ!}
:lu: [if(%cat_mood="playful")]{(Игривый) МЯУ?! НЕ ЗНАЮ! ДАВАЙ ИГРАТЬ!}
:lu: [if(%cat_mood="playful")]{(Игривый) МРРР?! НЕ ЗНАЮ! ДАВАЙ ИГРАТЬ!}
:lu: [if(%cat_mood="playful")]{(Игривый) МЯУ?! ЧТО?! НЕ ЗНАЮ! ДАВАЙ ИГРАТЬ!}
:lu: [if(%cat_mood="playful")]{(Игривый) МРРР?! ДАВАЙ ИГРАТЬ ИГРЫ!!!}
:lu: [if(%cat_mood="playful")]{(Игривый) МЯУ?! ЧТО?! ДАВАЙ ИГРАТЬ!!!}
:lu: [if(%cat_mood="playful")]{(Игривый) МРРР?! ДА ДА ДА!!!}
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу... Что?.. Мне не нужно знать.}
:lu: [if(%cat_mood="offended")]{(Обиженный) Мрр... Что?.. Это не ко мне.}
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу... Что?.. Мне не интересно.}
:lu: [if(%cat_mood="offended")]{(Обиженный) Мрр... Что?.. Не мне.}
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу... Что?.. Мне не нужно это знать.}
:lu: [if(%cat_mood="offended")]{(Обиженный) Мрр... Что?.. Не ко мне.}
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу... Что?.. Мне не нужно.}
:lu: [if(%cat_mood="offended")]{(Обиженный) Мрр... Это... Не ко мне.}
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу... Что?.. Не нужно.}
:lu: [if(%cat_mood="offended")]{(Обиженный) Мрр... Что?.. Мне не нужно знать.}
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу... Что?.. Не ко мне.}
:lu: [if(%cat_mood="offended")]{(Обиженный) Мрр... Что?.. Мне не нужно.}
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу... Что?.. Не мне.}
:lu: [if(%cat_mood="offended")]{(Обиженный) Мрр... Это... Не ко мне.}
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу... Что?.. Мне не интересно.}
:lu: [if(%cat_mood="offended")]{(Обиженный) Мрр... Что?.. Не нужно.}
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу... Что?.. Не ко мне.}
:lu: [if(%cat_mood="offended")]{(Обиженный) Мрр... Это... Не ко мне.}
:lu: [if(%cat_mood="offended")]{(Обиженный) Мяу... Что?.. Не мне знать.}
:lu: [if(%cat_mood="offended")]{(Обиженный) Мрр... Что?.. Мне не интересно.}
