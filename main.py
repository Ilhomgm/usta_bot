import telebot
import os

# Импорт переводчика и определения языка
from utils.language_manager import translate, detect_language, set_user_language

# Импорт обработчиков
from handlers import register, search
# В будущем можно добавлять:
# from handlers import market, ai, gallery, settings, reviews

# Инициализация бота
BOT_TOKEN = os.getenv("BOT_TOKEN", "ВСТАВЬ_СВОЙ_ТОКЕН_ЗДЕСЬ")
bot = telebot.TeleBot(BOT_TOKEN)

# Главное меню
def main_menu(user_id):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add(
        translate("main_menu_find", user_id),
        translate("main_menu_become", user_id),
        translate("main_menu_map", user_id),
        translate("main_menu_reviews", user_id),
        translate("main_menu_settings", user_id)
    )
    return markup

# Обработчик /start
@bot.message_handler(commands=["start"])
def send_welcome(message):
    user_id = message.from_user.id
    guessed_lang = detect_language(message.text or message.from_user.first_name)
    set_user_language(user_id, guessed_lang)

    bot.send_message(
        message.chat.id,
        "Welcome to USTA Superbot!",
        reply_markup=main_menu(user_id)
    )

# Инициализация всех активных модулей
register.init(bot)
search.init(bot)
# В будущем:
# market.init(bot)
# ai.init(bot)
# settings.init(bot)
# gallery.init(bot)

# Запуск бота
if __name__ == "__main__":
    print("USTA Superbot is running...")
    bot.infinity_polling()
