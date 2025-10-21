# У цьому файлі міститься сценарій гри.

# Визначення персонажів для гри.
# Аргумент color змінює колір ім’я персонажа.

define k = Character("Кіра")
define l = Character("Люкс")
define r = Character("Рейв")
define n = Character("Нова")
define m = Character("МайстерКод")

transform pulsing_text:
    zoom 1.0
    linear 1.0 zoom 1.05
    linear 1.0 zoom 1.0
    repeat


label start:



screen fullscreen_pulsing_text(message):
    
    modal True

    
    text message:
        
        xalign 0.5
        yalign 0.5

        
        at pulsing_text

        # Стиль тексту (можете змінити на свій смак)
        size 100                # Розмір шрифту
        color "#9a0ced"         # Колір тексту (золотий)
        font "mini_pixel-7.ttf"   # Шрифт (переконайтесь, що він є у вашій грі)
        outlines [(5, "#510581", 0, 0)] # Чорна обводка для кращого контрасту


# 3. Приклад використання у грі
label prolog:
    # Для ефектності почнемо з чорного екрану
    scene black
    with fade

    "Зараз з'явиться пульсуючий напис..."

    # Показуємо наш екран, передаючи йому потрібний текст
    show screen fullscreen_pulsing_text("Увага!")

    # Ставимо гру на паузу на 4 секунди, щоб гравець побачив анімацію
    pause 4.0

    # Ховаємо екран, щоб продовжити гру
    hide screen fullscreen_pulsing_text
    with dissolve

    "Анімація завершилась. Гра продовжується."

    

    scene bg room

   
    show eileen happy

  
    k "Ви створили нову гру Ren'Py."

    k "Додавши сюжет, зображення та музику, ви зможете оприлюднити її світові!"

    

    return
