import telebot
from telebot import types
import os

# Импорт модуля перевода
from utils.language_manager import translate, detect_language, set_user_language

# Инициализация бота
BOT_TOKEN = os.getenv("BOT_TOKEN", "ВСТАВЬ_СВОЙ_ТОКЕН")
bot = telebot.TeleBot(BOT_TOKEN)

# Главное меню с переводом
def main_menu(user_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add(
        translate("main_menu_find", user_id),
        translate("main_menu_become", user_id),
        translate("main_menu_map", user_id),
        translate("main_menu_reviews", user_id),
        translate("main_menu_settings", user_id)
    )
    return markup

# Команда /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id

    # Определяем язык пользователя по сообщению и сохраняем
    detected_lang = detect_language(message.text or message.from_user.first_name)
    set_user_language(user_id, detected_lang)

    welcome_text = "Welcome to USTA Superbot!"  # Можно тоже перевести, если хочешь
    bot.send_message(message.chat.id, welcome_text, reply_markup=main_menu(user_id))


# Запуск
if __name__ == "__main__":
    print("USTA Superbot is running...")
    bot.infinity_polling()
