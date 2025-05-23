from telebot import types
import json

def show_profession_filter(bot, chat_id):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Электрик", callback_data="filter_электрик"))
    markup.add(types.InlineKeyboardButton("Сантехник", callback_data="filter_сантехник"))
    markup.add(types.InlineKeyboardButton("Автомастер", callback_data="filter_автомастер"))
    markup.add(types.InlineKeyboardButton("Строитель", callback_data="filter_строитель"))
    bot.send_message(chat_id, "Выберите профессию для фильтрации мастеров:", reply_markup=markup)

def handle_filter_callback(bot, call):
    profession = call.data.replace("filter_", "")
    with open("usta_superbot_x/data/masters.json", "r") as f:
        masters = json.load(f)
    filtered = [m for m in masters if profession.lower() in m.get("profession", "").lower()]
    if not filtered:
        bot.send_message(call.message.chat.id, f"Мастеров по профессии '{profession}' пока нет.")
        return
    for m in filtered:
        text = f"👤 {m['name']}
🛠️ {m['profession']}
📅 Стаж: {m['experience']}
🗣️ Языки: {m['languages']}"
        bot.send_message(call.message.chat.id, text)
