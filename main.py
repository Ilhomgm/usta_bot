import telebot
from telebot import types
import os
import json
from handlers import register
from utils import semantic

# Безопасное получение токена из переменной окружения
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
if not TELEGRAM_TOKEN:
    raise ValueError("Токен Telegram не найден! Убедитесь, что TELEGRAM_TOKEN установлен в переменных среды.")

bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🔍 Найти мастера", "➕ Стать мастером")
    markup.add("🗺️ Карта мастеров", "⚙️ Настройки")
    bot.send_message(message.chat.id, "Добро пожаловать в USTA SuperBot X!", reply_markup=markup)

@bot.message_handler(func=lambda m: True)
def handle_text(message):
    intent = semantic.semantic_match(message.text)
    if "мастер" in message.text.lower():
        bot.send_message(message.chat.id, f"Ищу подходящего мастера по запросу: {intent}")
    elif "стать мастером" in message.text.lower():
        register.start_registration(bot, message)
    else:
        bot.send_message(message.chat.id, "Пожалуйста, выберите действие из меню или напишите подробнее.")

print("Бот запущен...")
bot.polling()
