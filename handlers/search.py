# handlers/search.py

import telebot
from telebot import types
from utils.database import load_data
from utils.language_manager import translate

def init(bot: telebot.TeleBot):
    @bot.message_handler(func=lambda message: message.text and translate("main_menu_find", message.from_user.id) in message.text)
    def show_search_menu(message):
        user_id = message.from_user.id
        bot.send_message(message.chat.id, translate("ask_search_category", user_id))
        bot.register_next_step_handler(message, search_by_category)

    def search_by_category(message):
        user_id = message.from_user.id
        category = message.text.lower()
        masters = load_data("data/masters.json")
        results = [m for m in masters if category in m.get("profession", "").lower()]

        if not results:
            bot.send_message(message.chat.id, translate("no_masters_found", user_id))
            return

        sorted_results = sorted(results, key=lambda x: x.get("rating", 0), reverse=True)
        for m in sorted_results[:5]:  # показываем до 5 мастеров
            text = f"👨‍🔧 {m['name']}\n🛠 {m['profession']}\n📍 {m['location']}\n📞 {m['phone']}\n⭐ {m['rating']} ⭐"
            bot.send_message(message.chat.id, text)
