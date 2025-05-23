import json
import os

DATA_FILE = "usta_superbot_x/data/masters.json"
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump([], f)

registration_state = {}

def start_registration(bot, message):
    user_id = message.chat.id
    registration_state[user_id] = {}
    bot.send_message(user_id, "Введите ваше имя:")

def handle_registration(bot, message):
    user_id = message.chat.id
    state = registration_state.get(user_id, {})

    if "name" not in state:
        state["name"] = message.text
        bot.send_message(user_id, "Какая у вас профессия? (например, электрик)")
    elif "profession" not in state:
        state["profession"] = message.text
        bot.send_message(user_id, "Сколько лет вы работаете по профессии?")
    elif "experience" not in state:
        state["experience"] = message.text
        bot.send_message(user_id, "На каких языках вы работаете? (русский, узбекский и т.д.)")
    elif "languages" not in state:
        state["languages"] = message.text
        bot.send_message(user_id, "Отправьте ваше местоположение (включите геолокацию)")
    elif "location" not in state:
        bot.send_message(user_id, "Ожидаю ваше местоположение...")
    registration_state[user_id] = state

def handle_location(bot, message):
    user_id = message.chat.id
    state = registration_state.get(user_id, {})
    if "location" not in state:
        state["location"] = {
            "lat": message.location.latitude,
            "lon": message.location.longitude
        }
        # Сохраняем мастера
        with open(DATA_FILE, "r") as f:
            masters = json.load(f)
        masters.append(state)
        with open(DATA_FILE, "w") as f:
            json.dump(masters, f, ensure_ascii=False, indent=2)
        bot.send_message(user_id, "Регистрация завершена! Вы добавлены в список мастеров.")
        registration_state.pop(user_id, None)
