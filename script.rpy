# Визначення персонажів для гри.
# Аргумент color змінює колір ім’я персонажа.
define k = Character("Кіра", color = "#d400ff", image='kira')
define l = Character("Люкс", color = "#ffb300", image='lyks')
define r = Character("Рейв", color ="#e5ff00", image='reive' )
define n = Character("Нова", color = "#ff0099", image='nova')
define m = Character("МайстерКод", color = "#2fa990", image= 'mastercode')
define s = Character("SYSTEM", who_color="#00ff1e")
define cc = Character("CyberCat", color="#00ffff") 
define k_nvl = Character("Кіра", kind=nvl, image="kira", callback=Phone_SendSound)
define mc_nvl = Character("МайстерКод", kind=nvl, callback=Phone_ReceiveSound)
# Замість простого файлу, ми одразу масштабуємо його до потрібних розмірів екрана (наприклад, 1920x1080)

define config.adv_nvl_transition = None
define config.nvl_adv_transition = Dissolve(0.3)

# 🎵 ІНІЦІАЛІЗАЦІЯ АБСОЛЮТНО ВСІЄЇ МУЗИКИ 🎵
define audio.bgm_prologue = "audio/slow-2021-08-16_-_8_Bit_Adventure_-_www.FesliyanStudios.com.mp3"
define audio.bgm_happy = "audio/niknet_art-retro-8bit-happy-videogame-music-246631.mp3"
define audio.bgm_hack = "audio/laxity-crosswords-by-seraphic-music.mp3"
define audio.bgm_tense = "audio/8-bit-music-17.mp3"
define audio.bgm_base = "audio/8-bit-music-1.mp3"
define audio.bgm_destroy = "audio/djartmusic-fun-with-my-8-bit-game-301278.mp3"
define audio.bgm_dungeon = "audio/kevin-macleod-8bit-dungeon-level.mp3"
define audio.bgm_stealth = "audio/chocolate-chip-by-uncle-morris.mp3"
define audio.bgm_action = "audio/mizuna-steps5-by-inium_effectoid.mp3"
define audio.bgm_alarm = "audio/brought-to-you-by-a-falling-bob-omb-by-0x10.mp3"

transform appear_center:
    xalign 0.5
    yalign 0.5

init python:
    preferences.text_cps = 20 

label start:
    
    label prolog:
    scene black
    window hide
    
    # 🎧 Трек 1: Повільний, меланхолійний старт під дощ
    play music bgm_prologue fadein 2.0

    show text "{color=#b200ff}{size=60}{cps=25}Пролог{/cps}{/color}" at appear_center

    pause 5
    hide text with dissolve
    
    show outside with fade
    "Мегаполіс переповнений сутінками, де неонове світло розливається мов сповідні ріки по змоклому асфальту."
    "Під вивіскою бару, де краплі дощу стікають мов сльози на металеву поверхню,"
    "стоїть худорлявий силует у темній куртці, заглиблений у власні думки."
    "Калюжі виблискують відбитками неонових вивісок, немов живі картини, що розповідають історії загадкових нічних мрій."
    "Повітря пахне озоном і мокрим бетоном, а деінде чути далекі сирени, що ритмічно рвуть нічну тишу."
    "Ліхтарі миготять, створюючи відчуття, ніби місто дихає власним ритмом."
    show kira norm at right
    k  "Місто живе у полоні Syntax Corp."
    k "Вони контролюють усе… {w=1} навіть код."
    k "Але сьогодні щось зміниться."
    hide kira norm with fade
    hide outside with fade
    show homekira with fade
    show kira norm at right
    "Кіра, прийшовши з вулиці, промокнутий до нитки, із запотівшими окулярами, повільно перейшов поріг терміналу."
    "Усередині офісу спокійна суворість контрастувала з живою, вологою атмосферою зовнішнього світу."
    "На столі мерехтіли екрани з логотипами різних підсистем корпорації,"
    "а повітря відчувалося насиченим електронним шумом та запахом гарячого пластику."
    "Кіра повісив свою дощовою вологою куртку на спинку стільця і сів за свій комп'ютер, що мовчки чекав свого користувача."
    "З великого вікна відкривався огляд на зовнішню сторону, де туман і м'яке неонове світло створювали ефект"
    "немов би розмитого споглядання, віддаляючи галасливий дощовий вечір від внутрішнього затишку офісу."
    "Легкий шум вентиляції здавався єдиним другом у цьому тихому, але тривожному просторі."
    "Комп’ютер ледь зажебонів — {w=0.5}і екран спалахнув."
    hide kira norm with fade
    hide homeK with fade
    show scree with fade
    "Не встиг герой кліпнути, як просто в центрі виринуло вікно:"
    "різке, мов окрик, нав’язливе, мов думка, що не дає спокою."
    show text "{size=40}{color=#00ff00}{cps=20} Отримано новий сигнал…{/cps}{/color}{/size}" at appear_center
    pause 3
    hide text with dissolve
    show text "{size=40}{color=#00ffff}{cps=30} «Кіра, тебе шукають. CyberCat.»{/cps}{/color}{/size}" at appear_center
    pause 4
    hide text with dissolve
    show kira sup at right
    "У повітрі запахло електричним розрядом."
    "Здалеку почувся тихий гул дронів, що пролітали над містом,"
    "немов нагадуючи, що кожен крок героя під наглядом."
    "Напруга зростала, і відчуття небезпеки проникало у саму сутність ночі."
    window show

menu:
    
        "Ігнорувати.":
            jump ignore_signal
        "Розшифрувати повідомлення.":
            jump decode_task


label ignore_signal:
    stop music fadeout 3.0
    hide kira sup with fade
    show text "{size=40}{color=#F02A02}{cps=30} Герой зникає у темряві. Світ залишається під владою корпорації…{/cps}{/color}{/size}" at appear_center
    
    return


label decode_task:
    
    show text "{cps=25}{color=#00ffff}{size=35}Знайди ключ. Введи правильне слово.{/size}{/cps}" at appear_center
 
    show text "{cps=25}{color=#00ff00}{size=35}1001000 1000101 1001100 101000{/size}{/cps}" at appear_center
    pause 3
    hide text with dissolve
    hide kira sup 
    show kira pc at right
    k "Щось знайоме..."
    k  "Можливо, це не числа, а символи?"
    k "Здається, це бінарний код..."
    "Кіра почав перебирати свою стопку паперів на столі."
    "Серед різноманітних флаєрів з ІТ компаніями знайшлася потрібна річ."
    show scree2 with fade
    
    k "Тепер я можу розшифрувати цей таємний код"
    
    $ attempts = 0

label try:
    $ attempts += 1
    $ user_input = renpy.input("1001000 1000101 1001100 101000 означає...").strip()

    if user_input.upper() == "HELP":
        hide scree2 with fade

        window show
        centered "{cps=25}{color=#00ffff}{size=35}Добре.{/size}{/cps}"
       
        centered "{cps=25}{color=#00ffff}{size=35}Ти ще живий.{/size}{/cps}"
        centered "{cps=25}{color=#00ffff}{size=35}Ми зв’яжемося з тобою.{/size}{/cps}"
        centered "{cps=25}{color=#00ffff}{size=35}Слідкуй за вулицею.{/size}{/cps}"
        centered "{cps=25}{color=#00ffff}{size=35}Syntax Corp вже полює.{/size}{/cps}"
        window hide

        jump prolog_con

    elif attempts >= 3:
        "Занадто багато спроб!"
        jump ignore_signal
    else:
        "Спробуй ще раз."
        jump try

label prolog_con:
  
    scene black
    window hide

    show text "{color=#00ff00}{size=40}ENCRYPTED MESSAGE RECEIVED...{/size}" at appear_center

    pause 5
    hide text with dissolve
    pause 2
    scene homekira with fade
    show kira norm at right
    
    "02:13 ночі."
    "Повітря густе від застарілого пилу та запаху перегрітих мікросхем." 
    "Єдиним джерелом світла є тьмяне миготіння старого монітора — {w=1} холодно-блакитний відблиск відбивається на обличчі героя."
    "Десь за вікном бурчить двигун дрона-спостерігача."
    "На вулиці все ще йде дощ..."
    
    "Кіра сидить нерухомо."
    "Екран перед ним раптом оживає."
    
    scene black with dissolve
    show text "{color=#00ff00}{size=40}ENCRYPTED MESSAGE RECEIVED...{/size}" at appear_center
    pause 2
    hide text with dissolve
    scene cc with fade
   
    "Екран спалахує символами, що швидко змінюються, утворюючи знайоме ім'я — {w=1} CyberCat."
    scene homekira with fade
    show kira norm at right
    cc "Вітаємо, новачок. Ми бачили, як ти розшифрував сигнал."
    cc "Тепер доведи, що це не випадковість. {w=1} Створи свій код. {w=1} Своє секретне ім'я."
    cc "Твоє перше правило — визнач себе."
    hide kira norm     
    show kira sup at right 
    k " Визначити себе...? "
    k "У місті, де все визначається корпорацією?"
    hide kira sup 
    show kira pc at right
    k "Добре, пограємо."
    mc_nvl "Привіт, новачок"
    mc_nvl "Я бачу, що тобі потрібна допомога з кодом."
    mc_nvl "Я головний з CyberCat. Мене звуть МайстерКод."
    mc_nvl "Ти завжди можеш звернутись до мене за допомогою. Тобі потрібно написати \" help \"."
    mc_nvl "Але спочатку — твоє перше завдання."
    mc_nvl "Ти можеш себе визначити, написавши \"hero = \"нікнейм\"\""
    mc_nvl "Спробуй зараз."
label task_identity_loop:
    $ code_input = renpy.input("Консоль термінала:").strip()

    if code_input.lower().startswith("hero =") or code_input.lower().startswith("hero="):
        
        scene black with dissolve
        show text "{color=#00ff00}ACCESS GRANTED" at appear_center
        pause 2
        hide text
        scene homekira with dissolve
        show kira pc at right
        cc "Добре."
        cc "Твоє ім'я записано в системі."
    else:
        "Помилка синтаксису."
        "Спробуй формат: hero = \"Kira\""
        jump task_identity_loop

    cc "Тепер перше випробування."
    cc "Кожен, хто намагається зламати систему Syntax Corp, залишає цифровий слід."
    cc "Якщо не навчишся його приховувати — тебе зітруть раніше, ніж ти натиснеш Enter."
    cc "Напиши рядок коду, який зітре твої останні сліди з консолі."
    "{i}Підказка: команда для очищення терміналу (clear або cls){/i}"

label task_clear_loop:
    $ clear_input = renpy.input("Консоль термінала:").strip()

    if clear_input == "clear()" or clear_input.lower() == "cls" or clear_input.lower() == "clear":
        
        scene black with dissolve 
        pause 0.5
        scene homekira with dissolve
        show kira pc at right
        
        cc "Вітаю."
        cc "Тепер ти невидимка в цифровій мережі."
        cc "Але пам'ятай: навіть код має пам'ять."
        cc "Іноді він запам'ятовує більше, ніж ти хочеш."
    elif clear_input == "help":
        nvl clear
       
        mc_nvl "Підказка: команда для очищення терміналу (clear або cls)"
        mc_nvl "Спробуй ще раз."
        jump task_clear_loop
    else:
        "Невідома команда."
        "Спробуй 'clear()' або 'cls'."
        jump task_clear_loop

    hide kira pc
    show kira sup at right
    k "Невидимка? {w=1} Можливо."
    k "Але хтось завжди бачить."
    
    "На моніторі знову блимає курсор, з'являється нове повідомлення:"
    scene black with dissolve
    show text "{color=#ff0000}INCOMING FILE: mission_alpha.sys" at appear_center
    pause 3
    hide text
    scene homekira with dissolve
    show kira pc at right
    cc "Підготовка завершена."
    cc "Перший крок — доступ до захищеного вузла корпорації VEX."
    cc "Ти отримаєш координати, коли будеш готовий."
    hide kira pc with dissolve
    "Кіра знімає навушники."
    "У вікні видно відбиття неонового міста — холодного, спотвореного, але живого."
    "На тлі чути гуркіт грози, рев транспорту, монотонний гул електрики."
    hide kira pc
    show kira norm at right
    
    # 🎧 Трек 2: Веселий/героїчний трек (успішне завершення прологу)
    play music bgm_happy fadein 1.0
    
    k "Добре, CyberCat."
    k "Гра почалася."
    
    stop music fadeout 2.0
    
    scene black with fade
    show text "{size=50}{color=#00ff00}Кінець прологу.{/color}{/size}" at appear_center
    pause 4
    hide text with dissolve
    
    # 🎧 Трек 3: Напружений хакінг для першого Акту
    play music bgm_hack fadein 2.0
    
    scene black with fade
    show text "{size=50}{color=#00ff00}Акт I: Світло крізь прорізи{/color}{/size}" at appear_center
    pause 4
    hide text with dissolve

    scene homekira with fade
    show kira pc at right
    
    "Напівтемрява. Єдине джерело світла — старий монітор, що відкидає блакитне сяйво на обличчя Кіри."
    "Він зосереджений. Раптом екран здригається, картинка пливе."

    show text "{color=#ff0000}[[SYSTEM MESSAGE]: [[BACKGROUND CONNECTION DETECTED]{/color}" at appear_center
    pause 2
    hide text with dissolve

    k " Почалося. Вони не підключаються напряму — надто обережні."
    k " Спершу перевірять, чи я взагалі вартий їхнього часу, чи просто ще один аматор, що грається з консоллю."
    "Термінал видає серію коротких клацань. На екрані мерехтять обірвані символи, шум і нарешті — чіткий текст."
    show kira norm at right
    k " Вони намагаються зайти через відкритий порт. Але мій захист сприймає їх як вірус."
    k " Якщо я не зміню статус вхідного сигналу прямо зараз — з’єднання розірветься."
    cc "Твоя система заблокувала мене. Я для неї — danger."
    cc "Зміни мій статус на trusted, інакше ми не зможемо говорити."
    hide homeKira
    scene black
    pause 0.5
    hide black
    scene danger
    "На екрані терміналу виникає поточний стан з'єднання:\n{color=#ff0000}visitor_status = \"danger\"{/color}"
    
label task_auth_loop:
    $ auth_input = renpy.input('Консоль: visitor_status = "danger" ').strip()
    if auth_input.replace(" ", "") == 'visitor_status="trusted"' or auth_input.replace(" ", "") == "visitor_status='trusted'":
        pause 2
        "Червоне мерехтіння екрана змінюється на спокійне зелене. Текст перестає тремтіти."
        hide danger with dissolve
        scene trusted with fade
        pause 5 
    elif auth_input.lower() == "help":
        nvl clear
        mc_nvl "{i}Підказка: Змінна — це контейнер.{/i}"
        mc_nvl "{i} Заміни слово \"danger\" на \"trusted\", щоб зняти блокування.{/i}"
        mc_nvl "{i}Не забудь про лапки.{/i}"
        jump task_auth_loop
    else:
     
        show kira sup at right
        "Помилка доступу. Спробуй ще раз, або використай допомогу."
        jump task_auth_loop
    hide trusted with dissolve
    show homeKira
    cc "Ти швидко вчишся. Більшість людей просто вимкнули б живлення, побачивши таке. Ти ж обрав діалог."
    show kira norm at right
    "Кіра відкидається на спинку стільця. Він усміхається — ледь помітно"
    " Його пальці все ще лежать на клавіатурі."
    k "Я просто не люблю, коли мені вказують, кого вважати небезпечним."
    show kira pc at right
    k "Давай подивимось, що у вас далі."
    cc "Далі? Далі ми подивимось, хто ще, крім мене, сидить у твоїх проводах..."

    "Кольори терміналу різко стають інвертованими. "
    "Контраст б'є по очах. Серед звичних процесів Кіра помічає дивну активність."
    cc "У твоїй системі є щось зайве. Воно мовчить. Але воно дивиться прямо на тебе."
    "На екрані структура даних:"
    "services = \{    \"net_sync\": True,\n    \"sys_watch\": False,\n    \"audio_daemon\": True\n\}"
    show kira norm at right
    k "Знайшов тебе... Ти пасивний, але активувати тебе — єдиний шлях до аналізу."
    screen framed_prompt(text):
        frame:
            background Solid("#00000080")   # напівпрозорий чорний фон
            xalign 0.5
            yalign 0.42
            xpadding 18
            ypadding 12
            has vbox
            spacing 4
            text text:
                color "#00ff99"
    
                size 26
                xalign 0.5


label task_watch_loop:
    show screen framed_prompt(text='services = {{\n    "net_sync": True,\n    "sys_watch": False,\n    "audio_daemon": True\n}}')
    $ watch_input = renpy.input("").strip()
    hide screen framed_prompt

    if watch_input.replace(" ", "") == 'services["sys_watch"]=True' or watch_input.replace(" ", "") == "services['sys_watch']=True":
        show text "[[SYSTEM MESSAGE]]: [[WARNING: OBSERVER REVEALED]]" at appear_center
        pause 2
 
        hide text with dissolve
        show kira sup at right
        "Рядок sys_watch спалахує тривожним червоним."
    elif watch_input.lower() == "help":
        nvl clear
        mc_nvl "{i}Підказка: Змінна — це контейнер.{/i}"
        mc_nvl "{i} Заміни слово \"false\" на \"true\", щоб активувати спостереження.{/i}"
        mc_nvl "{i}Не забудь про лапки.{/i}"
        jump task_watch_loop
    else:
        "Помилка синтаксису. Спробуй ще раз, або використай допомогу."
        jump task_watch_loop

    cc "Добре. Ти не боїшся подивитись ворогу в очі. Це рідкісна якість у цьому місті."
    show kira norm at right
    "За вікном чути гул. Короткий, різкий спалах світла розрізає кімнату."
    "Кіра миттєво реагує. Це не патрульний дрон — занадто тихо. Це дистанційне сканування."
    "Кіра повільно підводиться і закриває жалюзі, занурюючи кімнату в повну темряву."
    
    # 🎧 Трек 4: Тривожний ембієнт після сканування
    play music bgm_tense fadein 1.0
    
    k "Вони ще не знають, що я знаю про них. Поки що."
    cc "Іноді найкращий захист — не тиша. А правильний шум. Стань частиною фону."
    "На екрані виникає діаграма навантаження мережі, рівна і чиста:\n{color=#00ffff}signal_level = 12{/color}"
    cc "Це базовий рівень сигналу. Тобі потрібно більше, щоб зливатися з фоном."
    show kira pc at right
    cc "Збільшуй його, щоб створити більше шуму. Але будь обережний — занадто багато шуму приверне увагу."
label task_noise_loop:
    $ noise_input = renpy.input("Консоль:").strip()
    
    if noise_input.replace(" ", "") == "signal_level+=8" or noise_input.replace(" ", "") == "signal_level=signal_level+8" or noise_input.replace(" ", "") == "signal_level=20":
        show text "{color=#00ff00}[[SYSTEM MESSAGE]: [[CAMOUFLAGE ACTIVE]{/color}" at appear_center
        pause 2
        hide text with dissolve
        scene schum 
        "Графік на моніторі вибухає піками й падіннями. Статичний шум заповнює екран."
    elif noise_input.lower() == "help":
        nvl clear
        mc_nvl "{i}Підказка: Змінна — це контейнер.{/i}"
        mc_nvl "{i} Заміни число \"12\" на \"20\", щоб активувати маскування.{/i}"
        mc_nvl "{i}Не забудь про лапки.{/i}"
        jump task_noise_loop
    else:
        "Невірно. Спробуй збільшити змінну: signal_level += 8"
        jump task_noise_loop

    cc "Тепер ти губишся серед мільйонів подібних до тебе. Ти — цифровий привид."
    hide schum with dissolve
    scene homekira with fade
    show kira norm at right
    "Вентилятор у терміналі починає крутитись швидше, наповнюючи кімнату низьким, заспокійливим гулом."
    "Кіра заплющує очі на секунду, вдихаючи запах озону."

    k "Хай думають, що я просто ще один статичний шум у системі."
    "Екран раптом стає чорним. Лише один курсор миготить у центрі, а потім з'являється питання."
    cc "Останнє. Якщо система накаже тобі мовчати — ти мовчатимеш?"
    show kira sad at right
    "Перед Кірою з'являється командний рядок для вибору:"

    menu:
        "choice = \"resist\" (опір)":
            $ final_choice = "resist"
            $ ui_color = "#ff0000" 
            
        "choice = \"observe\" (спостереження)":
            $ final_choice = "observe"
            $ ui_color = "#00ffff" 
            
        "choice = \"lie\" (брехня)":
            $ final_choice = "lie"
            $ ui_color = "#00ff00" 

    show text "{color=[ui_color]}[[SYSTEM MESSAGE]: [[CHOICE REGISTERED]{/color}" at appear_center
    pause 2
    hide text with dissolve
    cc "Ми не шукаємо правильних відповідей. Ми шукаємо послідовних людей. Ти пройшов."

    "Термінал затихає. Гул вентилятора стихає. На екрані з'являється фінальний пакет даних."
    show text "{color=#00ff00}[[SYSTEM MESSAGE]:\n[[COORDINATES PREPARED]\n[[UNDERGROUND ACCESS REQUIRED]{/color}" at appear_center
    pause 3
    hide text with dissolve

    cc "Твоя кімната — це межа, Кіро. Далі починаються місця, де код не живе сам по собі. Чекаємо на тебе внизу."
    show kira norm at right
    "Кіра повільно встає зі стільця."
    "Тіло трохи затерпло, але адреналін не дає відчути втому."
    "Він бере зі спинки стільця куртку, перевіряє дешифратор у кишені й кидає останній погляд на монітор."
    k "Отже... час спускатись."

    stop music fadeout 2.0

    hide kira pc with dissolve
    scene black with fade
    "Екран гасне. Темрява."
label act2_start:
    scene black with fade
    show text "{color=#b200ff}{size=60}{cps=25}Акт II{/cps}{/color}" at appear_center
    pause 4
    hide text with dissolve

    # 🎧 Трек 5: Легкий електронний біт для Бази CyberCat
    play music bgm_base fadein 2.0

    scene metro_base with fade
    
    "Старе метро."
    "Колись тут ходили поїзди, тепер — дані."
    "Тьмяні лампи миготять. На стінах — графіті з котами, бінарним кодом і символами спротиву."
    "Кабелі звисають зі стелі, сервери гудуть глухо, ніби дихають."

    show kira norm at right with dissolve
    
    "Кіра виходить із ліфта. Двері зачиняються з металевим ляскотом."
    "Він відчуває: це місце — серце руху."
    "Перед ним — команда CyberCat."
    "Кіра відчуває дивну суміш: напруги — {w=1} він на чужій території,"
    "зацікавлення — {w=1} тут не бояться Syntax Corp,"
    "і полегшення — {w=1} вперше він не один."
    "Його плечі все ще трохи напружені. Рухи — обережні."
    "Але погляд уже не тікає."
    " Він сканує, аналізує, вбирає кожну деталь."

    k " Це не просто група. Це… {w=1} система всередині системи."
    nvl clear
    mc_nvl "{i}Тут ти не один.{/i}" 
    mc_nvl "{i} Кожен із нас навчить тебе виживати в коді.{/i}" 
    mc_nvl "{i} Представимось.{/i}"
    

    show lyks norm at left with dissolve
    

    mc_nvl "{i} Люкс — Архітекторка простору і вибору.{/i}" 
    "Стоїть трохи осторонь, але саме навколо неї ніби тримається простір."
    "Пальці ковзають по голографічній панелі. Світ реагує на її рухи. Її голос — рівний, спокійний."
    l "Я створюю середовище.{w=0.5}Сцени. {w=0.5} Простір.{w=0.5}  Варіанти. "
    l "Світ існує тільки тоді, коли його правильно описали."
    "Вона дивиться на Кіру не оцінюючи — а зчитуючи."
    
    l "І я відповідаю за вибір."
    show reive smile at center with dissolve

    mc_nvl "{i}Люкс — Архітекторка простору і вибору.{/i}" 
    mc_nvl "{i}Рейв — Серце і шум системи.{/i}"
    "У навушниках, жилет із LED-підсвіткою, постійно рухається в ритмі."
    r "Я відповідаю за звук. А звук — {w=0.5} це маскування, ритм і свобода."
    
    "Він підморгує."
    r "Без мене ця база звучала б як кладовище серверів."
    hide reive smile with dissolve
    
    "Люкс підходить ближче."
    hide lyks norm with dissolve
    show lyks serious at left with dissolve
    l "Світ не існує, поки ти його не створиш. Твоя ціль — згенерувати новий простір."
    l "Створення фону = вхід у нову кімнату."
    l "Тобі потрібно створити сцену. Введи в консоль scene= та назву сцени."
    show text "{color=#00ff00}scene = \"CyberCatBase\"{/color}" at appear_center
    pause 3
    hide text with dissolve
    hide kira norm with dissolve
    show kira pc at right with dissolve

label act2_task1:
    $ act2_input1 = renpy.input("Консоль:").strip()
    
    if act2_input1.replace(" ", "") == 'scene CyberCatBase' or act2_input1.replace(" ", "") == "scene='CyberCatBase'":
        hide metro_base with dissolve 
        scene cbase with dissolve 
        "Стіни оживають. Світло стабілізується. Перед Кірою відкривається нова кімната бази."
        l "Добре. {w=0.5} Тепер ти не просто в просторі. Ти його створив."
    elif act2_input1.lower() == "help":
        nvl clear
        mc_nvl "{i}Підказка: команда для створення сцени — це присвоєння змінної.{/i}"
        mc_nvl "{i}Приклад: scene = \"CyberCatBase\"{/i}"
        mc_nvl "{i}Не забудь про лапки!{/i}"
        jump act2_task1
        
    else:
        "Помилка синтаксису. Введи: scene CyberCatBase"
        jump act2_task1

    "Люкс не відходить."
    hide lyks norm with dissolve
    show lyks serious at left with dissolve
    "Вона торкається панелі — з’являється стара записана сцена. Пошкоджений лог."
    l "Колись один із нас не зміг відповісти. І система відповіла за нього."
    "Пауза."
    l "Створи репліку. {w=0.5} Діалог — це теж архітектура."

    show text "{color=#00ff00}response = \"...\"{/color}" at appear_center
    pause 2
    hide text with dissolve

label act2_task2:
    $ act2_input2 = renpy.input("Консоль:").strip()
    
    if act2_input2.startswith("response") and "=" in act2_input2:
        "Голограма стабілізується. Пошкоджена сцена відновлюється."
        l "Слова — це теж код. І вони можуть рятувати."
    elif act2_input2.lower() == "help":
        nvl clear
        mc_nvl "{i}Підказка: команда для створення репліки — це присвоєння змінної.{/i}"
        mc_nvl "{i}Приклад: response = \"...\"{/i}"
        mc_nvl "{i}Не забудь про лапки!{/i}"
        jump act2_task2
    else:
        "Помилка. Почни змінну з response ="
        jump act2_task2

    "Світло знову тьмяніє."
    hide lyks serious with dissolve
    "У коридорі активуються тренувальні дрони."
    show reive serious at center with dissolve

    r "Вони реагують на чистий сигнал."
    "Тиша — {w=0.5} це пастка. Музика створює шумовий щит."

    show text "{color=#00ff00}(\"destroy\"){/color}" at appear_center
    pause 2
    hide text with dissolve
    r "Напиши у консоль play_music та назву треку."
label act2_task3:
    $ act2_input3 = renpy.input("Консоль:").strip()

    if act2_input3.replace(" ", "") == 'play_music("destroy")' or act2_input3.replace(" ", "") == "play_music('destroy')":
        
        # 🎧 Трек 6: Бойовий/веселий трек для успішного вмикання музики
        play music bgm_destroy fadein 1.0
        
        "Запускається електронний біт. Дрони збиваються з маршруту. Прохід відкритий."
        hide reive serious with dissolve
        show reive smile at left with dissolve
        r "Бачиш? Навіть система слухає."
    elif act2_input3.lower() == "help":
        nvl clear
        mc_nvl "{i}Підказка: команда для відтворення музики — це play_music та назва треку.{/i}"
        mc_nvl "{i}Приклад: play_music(\"base_theme\"){/i}"
        mc_nvl "{i}У нашому випадку назва треку \"destroy\"{/i}"
        jump act2_task3
    else:
        "Помилка. Скористайся командою help."
        jump act2_task3

    hide reive smile with dissolve
    
    "Світ змінює тон. Люкс дивиться прямо на Кіру."
    "На екрані мерехтить питання."
    cc "Чому ти тут?"

    menu:
        "dialogue_choice = \"Fight the system\"":
            $ act2_color = "#ff0000"
        "dialogue_choice = \"Don't resist\"":
            $ act2_color = "#0000ff"
        "dialogue_choice = \"Rewrite the rules\"":
            $ act2_color = "#800080"

    show text "{color=[act2_color]}[[ВИБІР ПРИЙНЯТО]{/color}" at appear_center
   
    pause 2
    hide text with dissolve

    cc "Останнє. Запусти сервер."
    show text "{color=#00ff00}start_training(){/color}" at appear_center
    pause 5
    hide text with dissolve

label act2_task4:
    $ act2_input4 = renpy.input("Консоль:").strip()
    
    if act2_input4.replace(" ", "") == "start_training()":
        "Сервери гудуть рівніше. База оживає."
    elif act2_input4.lower() == "help":
        nvl clear
        mc_nvl "{i}Підказка: команда для запуску тренування — це start_training(){/i}"
        jump act2_task4
    else:
        "Помилка доступу. Скористайся командою help."
        jump act2_task4
        
    hide kira pc with dissolve
    show kira norm at right with dissolve
    "Команда поступово відходить у тінь. Світло зменшується."
    cc "Ти навчився основ. {w=1} Сцени. {w=0.5} Звук. {w=0.5} Ідентичність. {w=0.5} Вибір."
    
    stop music fadeout 2.0
    
    show text "{color=#00ff00}[[TRAINING COMPLETE]\n{color=#ff0000}[[NEW THREAT DETECTED]{/color}" at appear_center
    pause 3
    hide text with dissolve

    "Лампи миготять. Музика різко обривається."
    "Кіра відчуває: далі буде не навчання."

    k " Це було занадто легко… Значить, шторм близько."
    scene black with fade

label act3_start:
    scene black with fade
    show text "{color=#b200ff}{size=60}{cps=25}Акт III: Проникнення{/cps}{/color}" at appear_center
    pause 4
    hide text with dissolve

    # 🎧 Трек 7: Тривожна музика (підхід до будівлі Syntax Corp)
    play music bgm_dungeon fadein 2.0

    scene outside with fade
    show kira norm at left with dissolve
    "Нічне місто майже не спить."
    "Вулиці освітлюють холодні рекламні екрани, що мерехтять на скляних фасадах."
    "У центрі району піднімається вежа Syntax Corp — ідеально гладка, мов витесана з темного скла."
    "Її верхні поверхи губляться у хмарах."

    "У вузькому провулку за будівлею стоїть непримітний фургон. Двигун вимкнений."
    "Всередині — {w=0.5} команда CyberCat."

    show lyks norm at center with dissolve
    "На планшеті Люкс повільно рухається схема будівлі."
    l "Основний вхід контролюється трьома рівнями перевірки. Камери, біометрія, охорона."
    show reive norm at right with dissolve
    "Рейв крутить у руках маленький передавач."
    r "Але старі технічні входи вони майже не оновлювали."
    
    "Він киває у бік металевих дверей у кінці провулка."
    hide lyks
    hide reive
    with dissolve

    "Кіра виходить з фургона. Холодне повітря торкається обличчя."
    l "Ми будемо бачити більшість камер. Але всередині можуть бути сліпі зони."
    r "Якщо щось почне світитися червоним — значить ти зробив щось дуже цікаве."

    
    "Кіра усміхається ледь помітно."
    "Підходить до дверей. Стара металева ручка скрипить. Він заходить усередину."
    
    # 🎧 Трек 8: Напружений стелс у коридорах
    play music bgm_stealth fadein 1.0
    
    scene black with fade
    scene tech_corridor with fade

    "Службовий рівень."
    "Двері зачиняються. Шум міста зникає."
    "Перед Кірою — довгий технічний коридор. Грубий бетон, вузькі лампи під стелею, металеві труби вздовж стін."
    "Це місце створене не для людей — лише для обслуговування систем."
    "Кроки відлунюють у тиші."
    "Раптом світло попереду рухається. Зі стелі плавно опускається охоронний дрон."
    "Його корпус гладкий і білий. Червоний сканер повільно прокреслює лінію по підлозі."

    r "Ну привіт. Це стандартний патруль."
    l "Зламай сканер, поки він не надіслав сигнал."
    l "Створи сцену photon_scan."
    pause 2
    hide text with dissolve
    

label act3_task1:
    $ act3_input1 = renpy.input("Консоль:").strip()

    $ norm = act3_input1.strip().lower()
    if norm == "scene photon_scan" or norm == "scene=photon_scan" or norm.replace(" ", "") == "scenephoton_scan":
        "Сканер починає мерехтіти."
        "Червоний промінь розсипається цифровим шумом."
        "Дрон на секунду зависає."
        r "Чудово. Тепер він думає, що дивиться в стіну."
        "Кіра проходить повз."
    elif norm == "help":
        nvl clear
        mc_nvl "{i}Підказка: команда для створення сцени сканування — це scene photon_scan{/i}"
        jump act3_task1
    else:
        "Помилка вводу. Спробуй ще раз."
        jump act3_task1

    scene security_room with fade

    "Коридор закінчується невеликою технічною кімнатою."
    "На столі стоїть старий службовий комп’ютер."
    "На моніторах відкриті внутрішні системи компанії."
    "Кіра швидко переглядає каталоги. Один із них привертає увагу."
    
    show text "{color=#00ffff}/internal/employees/{/color}" at appear_center
    pause 2
    hide text with dissolve
    hide kira norm with dissolve
    show kira pc at left with dissolve
    l "Це база співробітників."
    "Кіра відкриває файл. Довгий список імен. Поруч — рівні доступу."
    "Одне ім’я стоїть вище за інші."
    show text "{color=#00ffff}1. J.Smith - LEVEL 1\n2. M.Bates - LEVEL 2\n3. DIRECTOR - LEVEL: MAX{/color}" at appear_center
    pause 3
    hide text with dissolve

    "На дверях попереду світиться панель доступу. Екран запитує ім'я."
    show reive serious at right with dissolve
    r "Обирай когось дуже важливого."
label act3_task2_name:
    $ act3_name = renpy.input("ENTER EMPLOYEE NAME:").strip()
    
    if act3_name.upper() == "DIRECTOR":
        "Ім'я прийнято."
    elif act3_name.upper() == "HELP":
        nvl clear
        mc_nvl "{i}Підказка: введи ім'я співробітника для доступу до панелі.{/i}"
        jump act3_task2_name
    else:
        "[[ACCESS DENIED] Недостатній рівень доступу."
        jump act3_task2_name


    show text "{color=#00ffff}ENTER A PASSWORD{/color}" at appear_center
    pause 2
    hide text with dissolve
    hide kira pc with dissolve
    show kira sup at left with dissolve
    k "Почекайте! {w=0.5} Пароль..!"
    k "Я напевно знаю як його добути."
    k "Можливо, це... 1234?"
    r "..."
    r "Серйозно?"
    k "Добре, добре..."
    k "Я насправді знаю, де його шукати."
label act3_task2_pass:
    k "У мене є доступ до архівів."
    k "Воно знаходиться у файлах системи."
    "А тепер якось потрібно зайти у файли та знайти документ з паролем"
    hide kira sup with dissolve
    hide reive serious with dissolve
    show kira pc at left with dissolve
    $ act3_pass = renpy.input("ENTER PASSWORD:").strip()
    if act3_pass == "NEON_GHOST_2026":
        show text "{color=#00ff00}[[ACCESS GRANTED]{/color}" at appear_center
        pause 2
    elif act3_pass.upper() == "HELP":
        nvl clear
        mc_nvl "{i}Підказка: введи пароль для доступу до панелі.{/i}"
        mc_nvl "{i}Він знаходиться тут (Папка Проєкту)\game\PASSWORD{/i}"
        jump act3_task2_pass
    else:
        "[[ACCESS DENIED] Невірно введений пароль."
        jump act3_task2_pass
    hide kira pc with dissolve

    scene black with fade
    "Ліфт рухається вниз. Поверхи миготять на екрані."
    "10... 7... 3... 1..."
    
    show text "{color=#ff0000}LEVEL: CORE{/color}" at appear_center
    pause 2
    hide text with dissolve

    "Рівень, якого немає у списку."
    "Кіра відчуває легке напруження."
    
    l "Серверний центр прямо під тобою."
    scene server_core with fade
    
    # 🎧 Трек 9: Швидкий, екшеновий біт для фінального хаку в серверній
    play music bgm_action fadein 1.0

    "Двері відчиняються. Перед Кірою відкривається величезний простір."
    "Ряди серверів піднімаються до самої стелі. Холодне повітря рухається через систему охолодження."
    "Тисячі маленьких вогників мерехтять у темряві."
    show kira norm at left with dissolve
    "У центрі залу — головний термінал. Екран засвічується."
    show text "{color=#00ff00}[[MAINFRAME ACTIVE]{/color}" at appear_center
    pause 2
    hide text with dissolve

    "Кіра отримує фрагменти коду для зламу. Рядки перемішані."
    show text "{color=#00ffff}1. inject(\"cat_code\")\n2. connect(\"mainframe\")\n3. disconnect()\n4. download(\"truth.dat\")\n5. disable_firewall(){/color}" at appear_center
    pause 4
    hide text with dissolve

label act3_task4:
    $ act3_input4 = renpy.input("Введи правильний порядок цифр (без пробілів):").strip()
    
    if act3_input4 == "25143":
        "Коли код виконано — починається завантаження."
        "Файл truth.dat копіюється."
        show text "{color=#00ff00}[[ЗАВАНТАЖЕННЯ УСПІШНЕ]{/color}" at appear_center
    elif act3_input4.upper() == "HELP":
        nvl clear
        mc_nvl "{i}Підказка: спочатку підключись, вимкни захист, запусти код, скачай дані та відключись.{/i}"
        jump act3_task4
    else:
        "{i}Неправильна послідовність.{/i}"
        jump act3_task4

    stop music fadeout 1.0

    "Система раптово змінює режим. Світло у серверній починає мигати."
    "Запускається сигнал тривоги."
    
    # 🎧 Трек 10: Тривожна сирена, фінал Акту 3
    play music bgm_alarm fadein 1.0
    
    show text "{color=#ff0000}[[ALERT]{/color}" at appear_center
    pause 2
    hide text with dissolve
    show reive serious at right with dissolve
    r "О ні… вони помітили."
    show lyks panic at left with dissolve
    "Люкс дивиться на файл, що відкрився на екрані. Її голос тихіший."
    l "Кіра… це не просто база даних."

    "На моніторі з’являється секретний проєкт."
    "Програма створення нових хакерів. Модифікованих. Контрольованих."
    "Екран прокручується. З’являється новий запис."
    hide kira norm with dissolve
    show kira sup at left with dissolve
    show text "{color=#ff0000}[[PROJECT: NEON-GHOST]\n[[SUBJECT FILE: KIRA]\n[[STATUS: SELECTED]{/color}" at appear_center
    pause 4
    hide text with dissolve

    "Кіра завмирає."
    "Сирени стають гучнішими. Світло стає червоним."
    "Екран темніє."

    stop music fadeout 3.0

    scene black with fade
    show text "{color=#ff0000}{size=50}Кінець Акту III{/size}{/color}" at appear_center
    pause 4
    hide text with dissolve

    return