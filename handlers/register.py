# handlers/register.py

import telebot
from telebot import types
from utils.database import load_data, save_data
from utils.language_manager import translate

def init(bot: telebot.TeleBot):
    @bot.message_handler(func=lambda message: message.text and translate("main_menu_become", message.from_user.id) in message.text)
    def register_start(message):
        user_id = message.from_user.id
        bot.send_message(message.chat.id, translate("ask_name", user_id))
        bot.register_next_step_handler(message, step_get_name)

    def step_get_name(message):
        user_id = message.from_user.id
        master = {
            "id": user_id,
            "name": message.text
        }
        bot.send_message(message.chat.id, translate("ask_profession", user_id))
        bot.register_next_step_handler(message, step_get_category, master)

    def step_get_category(message, master):
        user_id = message.from_user.id
        master["profession"] = message.text
        bot.send_message(message.chat.id, translate("ask_location", user_id))
        bot.register_next_step_handler(message, step_get_location, master)

    def step_get_location(message, master):
        user_id = message.from_user.id
        master["location"] = message.text
        bot.send_message(message.chat.id, translate("ask_phone", user_id))
        bot.register_next_step_handler(message, step_get_phone, master)

    def step_get_phone(message, master):
        user_id = message.from_user.id
        master["phone"] = message.text
        master["rating"] = 0
        master["verified"] = False
        master["gallery"] = []

        bot.send_message(message.chat.id, translate("ask_photos", user_id))
        bot.register_next_step_handler(message, step_get_photos, master)

    def step_get_photos(message, master):
        user_id = message.from_user.id
        if message.photo:
            photo_id = message.photo[-1].file_id
            master["gallery"].append(photo_id)
            bot.send_message(message.chat.id, translate("ask_more_photos", user_id))
            bot.register_next_step_handler(message, step_get_photos, master)
        else:
            all_masters = load_data("data/masters.json")
            all_masters.append(master)
            save_data("data/masters.json", all_masters)
            bot.send_message(message.chat.id, translate("register_success", user_id))
