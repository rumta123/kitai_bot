# https://t.me/GooseChooseBot
import telebot
from telebot import types
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import re
import logging

# Замените 'YOUR_BOT_TOKEN' на ваш реальный токен бота
TOKEN = '6695892448:AAEzb5VJX26xWpFrFOt_2BJOCAMDL5wBC7E'


# Замените 'ID_Roger_ver' на идентификатор чата для пользователя @Roger_ver
your_chat_id = -1002119142548

# Состояния для отслеживания шагов
states = {}
global_result = None
global_persent =None
global_link = None
global_photo = None
global_size = None
global_category = None
global_price = None
global_photo = None
bot = telebot.TeleBot(TOKEN)
user_info = {}

# Callback-команды
CALCULATOR_COMMAND = 'calculator'
CHOOSE_CATEGORY_COMMAND = 'choose_category'
CHOOSE_KATEGORY_COMMAND = 'chose_kategory'

@bot.message_handler(commands=['start'])
def start_handler(message):
    # Replace 'https://t.me/buy_from_east/429' with your actual link
    link = "[здесь](https://t.me/buy_from_east/429)"


    # Create ReplyKeyboardMarkup with one button and set resize_keyboard to True
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    # Add buttons in two rows
    buttons = [
        [InlineKeyboardButton("👟 Наличие в Москве 👜"), InlineKeyboardButton("🛍️Оформить заказ", callback_data='order')],
        [InlineKeyboardButton("ℹ️ FAQ", callback_data='faq'), InlineKeyboardButton("💴 Калькулятор цен", callback_data=CALCULATOR_COMMAND)],
    ]

    # Add buttons to the keyboard
    keyboard.add(*[button for row in buttons for button in row])

    # Create Markdown-formatted message
    
    markdown_message = (
        f"Добро пожаловать, **{message.from_user.first_name}** в бот магазина **GooseChoose!** 😉\n"
        f"Этот бот поможет Вам выкупить товары с **ЛЮБЫХ** китайских площадок, например:\n"
        "1️⃣ POIZON (DEWU)\n2️⃣ Taobao.com\n3️⃣ Tmall и другие.\n\n"
        f"Также, у нас есть **кроссовки и сумки в наличии** в Москве. "
        
        "**Внимание!** Все расчеты и прием заказа осуществляются **только в боте или у менеджера **[goosechooseshop](https://t.me/GooseChooseShop)"
    )

    # Send Markdown message with keyboard
    bot.send_message(
        message.chat.id,
        markdown_message,
        parse_mode="Markdown",  # Specify that Markdown formatting is used
        reply_markup=keyboard,
    )

@bot.message_handler(func=lambda message: message.text == '👟 Наличие в Москве 👜')
def faq_handler(message):
    try:
    # Handle the "ℹ️ FAQ" button
        faq_text = (
            "Ознакомиться с каталогом Вы можете [здесь](https://t.me/buy_from_east/429)"
            
        )
        
        

        # Send the FAQ message with hyperlinks
        bot.send_message(
            message.chat.id,
            faq_text,
            parse_mode="Markdown",
        )
    except Exception as e:
        print(f"Error in faq_order_callback: {e}")



# кнопка faq
@bot.message_handler(func=lambda message: message.text == 'ℹ️ FAQ')
def faq_handler(message):
    try:
    # Handle the "ℹ️ FAQ" button
        faq_text = (
            "💻 Связь с администратором:[GooseChooseShop](https://t.me/GooseChooseShop) ℹ️\n \n"
            "- Как оформить заказ? [Инструкция](https://teletype.in/@goosechoose/lnnmnLOfUtE)\n"
            "- Как рассчитать стоимость заказа? [Инструкция](https://teletype.in/@goosechoose/Ua6HLvPolDx)\n"
            "- Как скачать и зарегистрироваться в Poizon? [Инструкция](https://teletype.in/@goosechoose/v4EwmwMRLlm)\n \n"
            "- Доставка: [Информация](https://teletype.in/@goosechoose/H8w4oQDHCF1)\n \n"
            "-  [Отзывы:](https://t.me/goose_choose_feedback) -\n \n"
            "  Скачать Poizon ✅\n \n" 
            "- [Для IOS](https://apps.apple.com/ru/app/%E5%BE%97%E7%89%A9-%E6%9C%89%E6%AF%92%E7%9A%84%E8%BF%90%E5%8A%A8-%E6%BD%AE%E6%B5%81-%E5%A5%BD%E7%89%A9/id1012871328)  \n \n"
            "- [Для Android](https://m.anxinapk.com/rj/12201303.html) \n \n" 
        )
        
        # Creating InlineKeyboardMarkup for the "FAQ" message
        keyboard = InlineKeyboardMarkup(row_width=1)
        keyboard.add(
            InlineKeyboardButton("Написать", url='https://t.me/GooseChooseShop '),
            
        )

        # Send the FAQ message with hyperlinks
        bot.send_message(
            message.chat.id,
            faq_text,
            reply_markup=keyboard,
            parse_mode="Markdown",
        )
    except Exception as e:
        print(f"Error in faq_order_callback: {e}")



@bot.callback_query_handler(func=lambda call: call.data == 'order')
def order_handler(call):
    try:
        logging.debug("Debugging information")
        keyboard = InlineKeyboardMarkup(row_width=2)
        keyboard.add(
            InlineKeyboardButton("Продолжить", callback_data='continue_order1'),
            InlineKeyboardButton("Закрыть", callback_data='close_order')
        )
        link = "<a href='https://teletype.in/@goosechoose/lnnmnLOfUtE'>инструкцией</a>"

        bot.send_message(
        call.message.chat.id,
        f"Перед покупкой товара, <b>ознакомьтесь с {link} по Poizon</b>\n"
        "Если уже знакомы, пожалуйста, нажмите продолжить 👉",
        parse_mode="HTML",
        reply_markup=keyboard,
    )
    except Exception as e:
        print(f"Error in oformit_order_callback: {e}")

# по имени отработка 
@bot.message_handler(func=lambda message: message.text == '🛍️Оформить заказ')
def order_button_handler(message):
    try:
        logging.debug("Debugging information")
        keyboard = InlineKeyboardMarkup(row_width=2)
        keyboard.add(
            InlineKeyboardButton("Продолжить", callback_data='continue_order1'),
            InlineKeyboardButton("Закрыть", callback_data='close_order')
        )
        link = "<a href='https://teletype.in/@goosechoose/lnnmnLOfUtE'>Ознакомится</a>"

        bot.send_message(
            message.chat.id,
            "Перед добавлением товара, ознакомьтесь с инструкцией\n"
            f"{link}\n",
            parse_mode="HTML",
            reply_markup=keyboard,
        )
    except Exception as e:
        print(f"Error in order_button_handler: {e}")

# @bot.callback_query_handler(func=lambda call: call.data == 'close_order')
# def order_handler(call):
#     try:
#         link = "[здесь](https://t.me/buy_from_east/429)"
#         link1 = "[goosechooseshop](https://t.me/GooseChooseShop)"

#         # Create ReplyKeyboardMarkup with one button and set resize_keyboard to True
#         keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

#         # Add buttons in two rows
#         buttons = [
#             [InlineKeyboardButton("👟 Наличие в Москве 👜", url='https://t.me/buy_from_east/429'), InlineKeyboardButton("🛍️Оформить заказ", callback_data='order')],
#             [InlineKeyboardButton("ℹ️ FAQ", callback_data='faq'), InlineKeyboardButton("💴 Калькулятор цен", callback_data=CALCULATOR_COMMAND)],
#         ]

#         # Add buttons to the keyboard
#         keyboard.add(*[button for row in buttons for button in row])

#         # Create Markdown-formatted message
#         markdown_message = (
#             f"Добро пожаловать, {message.from_user.first_name} в бот магазина GooseChoose! 😉\n"
#             f"Этот бот поможет Вам выкупить товары с ЛЮБЫХ китайских площадок, например:\n"
#             "1️⃣ POIZON (DEWU)\n 2️⃣ Taobao.com\n 3️⃣ Tmall и другие.\n\n"
#             f"Также, у нас есть кроссовки и сумки в наличии в Москве. "
#             f"Ознакомиться с каталогом Вы можете {link}\n"
#             "**Внимание!** Все расчеты и прием заказа осуществляются **только в боте или у менеджера** {link1}"
#         )

#         # Send Markdown message with keyboard
#         bot.send_message(
#             markdown_message,
#             parse_mode="Markdown",  # Specify that Markdown formatting is used
#             reply_markup=keyboard,
#         )
       
#     except Exception as e:
#             print(f"Error in order_button_handler: {e}")

@bot.callback_query_handler(func=lambda call: call.data == 'close_order')
def close_button_handler(callback_query):
    try:
        print("ghgdjhgfdhjg")
        link = "[здесь](https://t.me/buy_from_east/429)"
        link1 = "[goosechooseshop](https://t.me/GooseChooseShop)"
       
        # Create ReplyKeyboardMarkup with one button and set resize_keyboard to True
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

        # Add buttons in two rows
        buttons = [
            [InlineKeyboardButton("👟 Наличие в Москве 👜", url='https://t.me/buy_from_east/429'), InlineKeyboardButton("🛍️Оформить заказ", callback_data='order')],
            [InlineKeyboardButton("ℹ️ FAQ", callback_data='faq'), InlineKeyboardButton("💴 Калькулятор цен", callback_data=CALCULATOR_COMMAND)],
        ]

        # Add buttons to the keyboard
        keyboard.add(*[button for row in buttons for button in row])

        # Create Markdown-formatted message
        markdown_message = (
            f"Добро пожаловать, {callback_query.from_user.first_name} в бот магазина GooseChoose! 😉\n"
            f"Этот бот поможет Вам выкупить товары с ЛЮБЫХ китайских площадок, например:\n"
            "1️⃣ POIZON (DEWU)\n 2️⃣ Taobao.com\n 3️⃣ Tmall и другие.\n\n"
            f"Также, у нас есть кроссовки и сумки в наличии в Москве. "
            f"Ознакомиться с каталогом Вы можете {link}\n"
            "**Внимание!** Все расчеты и прием заказа осуществляются **только в боте или у менеджера** {link1}"
        )

        # Send Markdown message with keyboard
        bot.send_message(
            callback_query.message.chat.id,
            markdown_message,
            parse_mode="Markdown",  # Specify that Markdown formatting is used
            reply_markup=keyboard,
        )
       
    except Exception as e:
        print(f"Error in close_button_handler: {e}")

        
# @bot.message_handler(func=lambda message: message.text == 'Закрыть')
# def order_button_handler(message):
#     try:
#         link = "[здесь](https://t.me/buy_from_east/429)"
#         link1 = "[goosechooseshop](https://t.me/GooseChooseShop)"

#         # Create ReplyKeyboardMarkup with one button and set resize_keyboard to True
#         keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

#         # Add buttons in two rows
#         buttons = [
#             [InlineKeyboardButton("👟 Наличие в Москве 👜", url='https://t.me/buy_from_east/429'), InlineKeyboardButton("🛍️Оформить заказ", callback_data='order')],
#             [InlineKeyboardButton("ℹ️ FAQ", callback_data='faq'), InlineKeyboardButton("💴 Калькулятор цен", callback_data=CALCULATOR_COMMAND)],
#         ]

#         # Add buttons to the keyboard
#         keyboard.add(*[button for row in buttons for button in row])

#         # Create Markdown-formatted message
#         markdown_message = (
#             f"Добро пожаловать, {message.from_user.first_name} в бот магазина GooseChoose! 😉\n"
#             f"Этот бот поможет Вам выкупить товары с ЛЮБЫХ китайских площадок, например:\n"
#             "1️⃣ POIZON (DEWU)\n 2️⃣ Taobao.com\n 3️⃣ Tmall и другие.\n\n"
#             f"Также, у нас есть кроссовки и сумки в наличии в Москве. "
#             f"Ознакомиться с каталогом Вы можете {link}\n"
#             "**Внимание!** Все расчеты и прием заказа осуществляются **только в боте или у менеджера** {link1}"
#         )

#         # Send Markdown message with keyboard
#         bot.send_message(
#             message.chat.id,
#             markdown_message,
#             parse_mode="Markdown",  # Specify that Markdown formatting is used
#             reply_markup=keyboard,
#         )
       
#     except Exception as e:
#         print(f"Error in order_button_handler: {e}")
# # # продолжить для кнопки заказа

@bot.callback_query_handler(func=lambda call: call.data == 'continue_order1')
def continue_order1_callback(call):
    try:
        keyboard = InlineKeyboardMarkup(row_width=1)
        categories = ["Обувь", "Футболки шорты", "Штаны/верхняя одежда", "Сумки", "Духи/часы", "Носки/Нижнее белье"]
        buttons = [InlineKeyboardButton(f"{kategory} ({index + 1})", callback_data=f"kategory_{index + 1}") for index, kategory in enumerate(categories)]
        keyboard.add(*buttons)

        bot.send_message(
            call.message.chat.id,
            "К какой категории относится товар?",
            reply_markup=keyboard,
        )
    except Exception as e:
        print(f"Error in continue_order1_callback: {e}")


@bot.callback_query_handler(func=lambda call: call.data.startswith('kategory_'))
def choose_category_callback(call):
    try:
        # Extracting the selected category number
        category_number = int(call.data.split('_')[1])

        # Update the user's state to indicate the chosen category
        states[call.from_user.id] = f"{CHOOSE_CATEGORY_COMMAND}_{category_number}"

        # Now, ask the user to input the price
        bot.send_message(call.message.chat.id, "Введите цену товара в ¥:")
    except Exception as e:
        print(f"Error in choose_category_callback: {e}")



@bot.message_handler(func=lambda message: states.get(message.from_user.id, '').startswith(f'{CHOOSE_CATEGORY_COMMAND}_'))
def handle_price_input(message):
    try:
        global global_category
        global global_result
        global global_persent
        global global_price
        print("Handling price input...")
        print(f"Message text: {message.text}")
        print(f"Current state for user {message.from_user.id}: {states}")

        # Extracting the state for the user
        user_state = states.get(message.from_user.id)

        # Check if the state has the expected format
        if not user_state.startswith(f"{CHOOSE_CATEGORY_COMMAND}_"):
            raise ValueError("Invalid state format")

        # Convert the input to an integer
        price = float(message.text.replace(" ", ""))

        # Ensure that the input is a non-negative number
        if price < 0:
            raise ValueError("Negative number not allowed")

        if price.is_integer():
            price = int(price)

        category_match = re.match(rf"{CHOOSE_CATEGORY_COMMAND}_(\d+)", user_state)
        if not category_match:
            raise ValueError("Invalid state format - category number not found")

        category_number = int(category_match.group(1))

        category_mapping = {
            1: "Обувь",
            2: "Футболки/шорты",
            3: "Штаны/верхняя одежда",
            4: "Сумки",
            5: "Духи/часы",
            6: "Носки/Нижнее белье",
        }
        selected_category = category_mapping.get(category_number, "Неизвестно")
        global_category = selected_category
        print(f"Selected category: {selected_category}")

        # Defining parameters for the formula based on the category
        if selected_category == "Обувь":
            print(f"категория {selected_category}")
            formula_params = [800, 1100, 999]
        elif selected_category == "Футболки/шорты":
            print(f"категория {selected_category}")
            formula_params = [450, 400, 999]
        elif selected_category == "Штаны/верхняя одежда":
            print(f"категория {selected_category}")
            formula_params = [850, 950, 999]
        elif selected_category == "Сумки":
            print(f"категория {selected_category}")
            formula_params = [500, 700, 999]
        elif selected_category == "Духи/часы":
            print(f"категория {selected_category}")
            formula_params = [400, 500, 999]
        else:
            formula_params = [300, 400, 999]  # Replace with parameters for other categories

        result = (price + (price / 100) * 5) * 13.7 + sum(formula_params)
        global_price =price
        rounded_result = round(result, 1)
        global_result = rounded_result
        procent = round((price / 100) * 5, 1)
        global_persent = procent

         # Ask the user to send a link to the product
        bot.send_message(
            message.chat.id,
            "Теперь отправьте мне ссылку на товар:",
        )

        # Update the user state to indicate that you're waiting for a link
        states[message.from_user.id] = 'waiting_for_link'

        # bot.send_message(your_chat_id, text="your_message_text", parse_mode="HTML")
        # keyboard = InlineKeyboardMarkup(row_width=1)
        # keyboard.add(
        #     InlineKeyboardButton("Оформить заказ", callback_data='oformit_order'),
        # )

        # bot.send_message(
        #     message.chat.id,
        #     f"<b>📊 Результат:</b>\n"
        #     f"{message.text} ¥ = {rounded_result} ₽\n\n"
        #     f"<b>🧮 Формула для выбранной категории:</b>\n"
        #     f"{selected_category}:\n"
        #     f"{message.text} +{procent})*13.7 + (800 + 1100 + 999) = {rounded_result} ₽ \n"
        #     f"(Цена + 5%) * курс + (доставка по Китаю + Китай-Москва со страховкой + комиссия сервиса) 😎\n\n"
        #     f"<b>Готов оформить заказ или задать вопрос?</b> 😎\n"
        #     f"Тебе сюда: @GooseChooseShop\n\n"
        #     "Для оформления заказа отправь фотографию товара, ссылку и свой размер менеджеру 🤩\n\n"
        #     "‼️ Все заказы оформляются только через @GooseChooseShop ‼️",
        #     parse_mode="HTML",
        #     reply_markup=keyboard,
        # )
        # bot.send_message(
        #     your_chat_id,
        #     f"<b>📊 Результат для пользователя @{message.from_user.username}:</b>\n"
        #     f"{message.text} ¥ = {rounded_result} ₽\n\n"
        #     f"<b>🧮 Формула для выбранной категории:</b>\n"
        #     f"{selected_category}:\n"
        #     f"{message.text} +{procent})*13.7 + (800 + 1100 + 999) = {rounded_result} ₽ \n"
        #     f"(Цена + 5%) * курс + (доставка по Китаю + Китай-Москва со страховкой + комиссия сервиса) 😎\n\n"
        #     f"<b>Готов оформить заказ или задать вопрос?</b> 😎\n"
        #     f"Тебе сюда: @GooseChooseShop\n\n"
        #     "Для оформления заказа отправь фотографию товара, ссылку и свой размер менеджеру 🤩\n\n"
        #     "‼️ Все заказы оформляются только через @GooseChooseShop ‼️",
        #     parse_mode="HTML"
        # )

    except ValueError as e:
        print(f"Error: {e}")
        # If the input is not a valid number, send an error message
        bot.send_message(message.chat.id, "Пожалуйста, введите корректное числовое значение.")


@bot.message_handler(func=lambda message: states.get(message.from_user.id) == 'waiting_for_link')
def handle_link_input(message):
    global global_link
    try:
        
        # Extract link from the message text using regular expression
        link_pattern = re.compile(r'https?://\S+|www\.\S+')
        match = link_pattern.search(message.text)

      
        if match:
            # Get the matched link
            product_link = match.group()
            global_link = product_link
            # Process the product link as needed
            print("global_link")
            # For now, just send a confirmation message
            bot.send_message(
                message.chat.id,
                f"Спасибо! 📏 Отправьте мне размер товара ",
            )

            # Clearing the user state
            states[message.from_user.id] = 'waiting_for_size'
        else:
            bot.send_message(
                message.chat.id,
                "Пожалуйста, введите корректную ссылку на товар.",
            )

    except Exception as e:
        print(f"Error in handle_link_input: {e}")
        # If there's an error, handle it appropriately (e.g., log it) without sending an error message to the user
        # You can customize this part based on your needs
        pass



@bot.message_handler(func=lambda message: states.get(message.from_user.id) == 'waiting_for_size')
def handle_size_input(message):
    global global_size
    try:
        
        # Extract the size from the message text
        global_size = message.text

        # Store the size in the dictionary
        user_info[message.from_user.id] = {'size': global_size}

        # Process the size as needed
        # For now, you can include it in the final message
        bot.send_message(
            message.chat.id,
            f"Спасибо за размер! Товар с размером {global_size} успешно добавлен. Отправьте фото"
        )

        # You can continue with the rest of your logic here

        # Clear the user state
        states[message.from_user.id] = 'waiting_for_photo'

    except Exception as e:
        print(f"Error in handle_size_input: {e}")
        # Handle errors as needed
        pass


@bot.message_handler(func=lambda message: states.get(message.from_user.id) == 'waiting_for_photo', content_types=['photo'])
def handle_photo_input(message):
    global global_result
    global global_category
    global global_persent
    global global_link
    global global_price
    global global_photo
    global global_size
    try:
        print("{global_category}")
        # Assuming you want to process the first photo sent by the user
        photo_file_id = message.photo[0].file_id

        global_photo = photo_file_id

        # Process the photo file ID as needed
        # For now, just send a confirmation message with the photo
       
        keyboard = InlineKeyboardMarkup(row_width=1)
        keyboard.add(
            InlineKeyboardButton("Продолжить", callback_data='prodoljit'),
            
        )
        bot.send_photo(
            your_chat_id,
            global_photo,
            caption=f"Фото с выбранным товаром"
        )

        bot.send_message(
            
            message.chat.id,
            global_link
            
        )
        bot.send_message(
            
            message.chat.id,
            f"<b>📊 Результат:</b>\n"
            f"{global_price} ¥ = {global_result} ₽\n\n || размер {global_size}\n\n"
             f"ℹ️ <b>Итоговая сумма включает:</b>\n"
            f"- Выкуп товара\n"
            f"- Комиссию\n"
            f"- Доставку по Китаю\n"
            f"- Доставку Китай - Москва\n"
            f"- Страховку \n\n"
            f"🧮 <b>Формула для выбранной категории:</b>\n"
            f"{global_category}:\n"
            f"({global_price} +{global_persent})*13.7 + (800 + 1100 + 999) = {global_result} ₽ \n"
            f"(Цена + 5%) * курс + (доставка по Китаю + Китай-Москва + комиссия сервиса) 😎\n\n"
            f"Готов оформить заказ или задать вопрос? 😎\n"
            f"Тебе сюда: @GooseChooseShop\n\n"
            "Для оформления заказа отправь фотографию товара, ссылку и свой размер менеджеру 🤩\n\n"
            "‼️ Все заказы оформляются только через @GooseChooseShop ‼️",
            parse_mode="HTML",
            reply_markup=keyboard,
        )

      


        # Clearing the user state
        states[message.from_user.id] = 'waiting_for_price_in_yen'
    except Exception as e:
        print(f"Error in handle_photo_input: {e}")
        # If there's an error, handle it appropriately (e.g., log it) without sending an error message to the user
        # You can customize this part based on your needs
        pass

@bot.callback_query_handler(func=lambda call: call.data == 'prodoljit')
def handle_continue_callback(call):
    try:
        user_id = call.from_user.id

        # Send a message asking for the Full Name (FIO)
        bot.send_message(user_id, "👤 Отправьте мне Ваше ФИО")

        # Update user state to 'waiting_for_fio'
        states[user_id] = 'waiting_for_fio'

    except Exception as e:
        print(f"Error in handle_continue_callback: {e}")
        # Handle errors as needed
        pass

# Add a new state for handling FIO input
@bot.message_handler(func=lambda message: states.get(message.from_user.id) == 'waiting_for_fio')
def handle_fio_input(message):
    try:
        # Assume FIO is sent as a single message
        fio = message.text

        # Process FIO as needed
        # For example, store it in user_info dictionary
        user_info[message.from_user.id]['fio'] = fio

        # Send a message asking for the phone number
        bot.send_message(
            message.chat.id,
            "📲 Отправьте мне Ваш номер телефона без знака +",
        )


        # Update user state to 'waiting_for_phone'
        states[message.from_user.id] = 'waiting_for_phone'

    except Exception as e:
        print(f"Error in handle_fio_input: {e}")
        # Handle errors as needed
        pass

# Add a new state for handling phone input
@bot.message_handler(func=lambda message: states.get(message.from_user.id) == 'waiting_for_phone')
def handle_phone_input(message):
    global global_result
    global global_category
    global global_persent
    global global_link
    global global_price
    global global_photo
    try:
        # Assume the phone number is sent as a single message
        phone_number = message.text

        # Process the phone number as needed
        # For example, store it in user_info dictionary
        user_info[message.from_user.id]['phone'] = phone_number

        # Send a confirmation message
        bot.send_message(
            message.chat.id,
            "✅ Ваш заказ принят и отправлен администратору @GooseChooseShop. Ожидайте, пожалуйста, обратную связь.",
        )

        # Send the collected information to the manager/administrator
      
        user_data = user_info[message.from_user.id]
        bot.send_message(
            your_chat_id,
            f"Новый заказ от пользователя @{message.from_user.username}:\n \n"
            f"{global_link} "
            f"{global_price} ¥  "
    
            f"{global_result} Р \n \n"

            f"ФИО: {user_data['fio']}\n \n"
            f"Номер телефона: {user_data['phone']}"
            
            # Add more details as needed
        )

        # If you want to offer the option to add another item, you can include that here
        bot.send_message(
            message.chat.id,
            "Если Вы хотите добавить еще один товар, просто перезапустите бота. Если хотите удалить товар, пожалуйста, сообщите об этом @GooseChooseShop",
        )

        # Clear the state
        states.pop(message.from_user.id, None)

    except Exception as e:
        print(f"Error in handle_phone_input: {e}")
        # Handle errors as needed
        pass




class PriceCalculator:
    def __init__(self, bot, states):
        self.bot = bot
        self.states = states
        self.global_result = None
        self.global_category = None

    def send_category_selection_message(self, chat_id):
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        categories = ["Обувь", "Футболки/шорты", "Штаны/верхняя одежда", "Сумки", "Духи/часы", "Носки/Нижнее белье"]
        buttons = [types.InlineKeyboardButton(f"{category} ({index + 1})", callback_data=f"category_{index + 1}") for index, category in enumerate(categories)]
        keyboard.add(*buttons)

        self.bot.send_message(
            chat_id,
            "К какой категории относится товар?",
            reply_markup=keyboard,
        )

    def handle_category_selection(self, call):
        category_number = int(call.data.split("_")[1])
        print("blabla")
        category_mapping = {
            1: "Обувь",
            2: "Футболки/шорты",
            3: "Штаны/верхняя одежда",
            4: "Сумки",
            5: "Духи/часы",
            6: "Носки/Нижнее белье",
        }
        selected_category = category_mapping.get(category_number, "Неизвестно")

        # Инициализация состояния для пользователя
        self.states[call.from_user.id] = f"CHOOSE_CATEGORY_{category_number}"
        print(f"Updated state for user {call.from_user.id}: {self.states}")
        # Отправка изображения
        image_path = f"images/{re.sub('[^A-Za-z0-9А-Яа-я]+', '_', selected_category.lower())}.jpg"
        self.global_category =  selected_category
        with open(image_path, "rb") as photo:
            self.bot.send_photo(
                call.message.chat.id,
                photo,
                caption=f"Выбрана категория: {selected_category}\n 💰 Отправьте мне цену за позицию в ¥ для расчёта",
            )

    def handle_price_input(self, message):
        try:
            print("Handling price input...")
            print(f"Message text: {message.text}")
            print(f"Current state for user {message.from_user.id}: {self.states}")

            # Extracting the state for the user
            user_state = self.states.get(message.from_user.id)

            # Check if the state has the expected format
            if not user_state.startswith("CHOOSE_CATEGORY_"):
                raise ValueError("Invalid state format")

            # Convert the input to a float
            price = float(message.text.replace(" ", ""))
            
            # Ensure that the input is a non-negative number
            if price < 0:
                raise ValueError("Negative number not allowed")

            category_match = re.match(r"CHOOSE_CATEGORY_(\d+)", user_state)
            if not category_match:
                raise ValueError("Invalid state format - category number not found")

            category_number = int(category_match.group(1))

            # Defining parameters for the formula based on the category
            formula_params = {
                1: "Обувь",
                2: "Футболки шорты",
                3: "Штаны/верхняя одежда",
                4: "Сумки",
                5: "Духи/часы",
                6: "Носки/Нижнее белье"
            }

            selected_category = formula_params.get(category_number, "Неизвестно")
            print(f"Selected category: {selected_category}")

            if selected_category == "Обувь":
                formula_params = [800, 1100, 999]
            elif selected_category == "Футболки/шорты":
                formula_params = [450, 400, 999]
            elif selected_category == "Штаны/верхняя одежда":
                formula_params = [850, 950, 999]
            elif selected_category == "Сумки":
                formula_params = [500, 700, 999]
            elif selected_category == "Духи/часы":
                formula_params = [400, 500, 999]
            elif selected_category == "Носки/Нижнее белье":
                formula_params = [300, 400, 999]
            else:
                formula_params = [0, 0, 0]  # Replace with parameters for other categories

            # Assuming price is the input value provided by the user
            procent = round((price / 100) * 5 , 1)

            # Formula calculation
            result = (price + procent) * 13.7 + sum(formula_params)
            rounded_result = round(result, 1)

            # Display the result
            formatted_result = f"<b>📊 Результат для пользователя @{message.from_user.username}:</b>\n\n" \
                            f" {message.text} ¥ = {rounded_result} ₽\n\n" \
                            f"<b>🧮 Формула для выбранной категории:</b>\n" \
                            f"{selected_category}:\n" \
                            f"({message.text} + {procent})*13.7 + {formula_params[0]} + {formula_params[1]} + {formula_params[2]} = {rounded_result} ₽ \n" \
                            f"(Цена + 5%) * курс + (доставка по Китаю + Китай-Москва со страховкой + комиссия сервиса) 😎\n\n" \
                            f"<b>Готов оформить заказ или задать вопрос?</b> 😎\n" \
                            f"Тебе сюда: @GooseChooseShop\n\n" \
                            "Для оформления заказа отправь фотографию товара, ссылку и свой размер менеджеру 🤩\n\n" \
                            "‼️ Все заказы оформляются только через @GooseChooseShop ‼️"

            keyboard = InlineKeyboardMarkup(row_width=1)
            keyboard.add(
                InlineKeyboardButton("🛍️Оформить заказ", callback_data='order'),
            )

            self.bot.send_message(
                message.chat.id,
                formatted_result,
                parse_mode="HTML",
                reply_markup=keyboard,
)
            self.bot.send_message(
                your_chat_id,
                formatted_result,
                parse_mode="HTML",
                
)

        except ValueError as e:
            print(f"Error: {e}")
            # If the input is not a valid number, send an error message
            self.bot.send_message(message.chat.id, f"Пожалуйста, введите корректное числовое значение. {e}")



# Create an instance of PriceCalculator
price_calculator = PriceCalculator(bot, states)

# Handlers
@bot.message_handler(func=lambda message: message.text == "💴 Калькулятор цен")
def calculator_handler(message):
    price_calculator.send_category_selection_message(message.chat.id)

@bot.callback_query_handler(func=lambda call: call.data.startswith("category_"))
def category_handler(call):
    price_calculator.handle_category_selection(call)

@bot.message_handler(func=lambda message: states.get(message.from_user.id, "").startswith('CHOOSE_CATEGORY'))
def handle_price_input(message):
    price_calculator.handle_price_input(message)

# Run the bot
bot.polling(none_stop=True)

if __name__ == "__main__":
    bot.polling(none_stop=True)