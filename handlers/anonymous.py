anonymous_orders = {}

def start_anonymous_request(bot, message):
    user_id = message.chat.id
    anonymous_orders[user_id] = {}
    bot.send_message(user_id, "Что вы хотите заказать? Опишите проблему или услугу.")

def handle_anonymous_message(bot, message):
    user_id = message.chat.id
    order_text = message.text
    anonymous_orders[user_id]["text"] = order_text

    # Имитация рассылки заявки мастерам (в реальности — фильтрация по гео/категории)
    fake_masters = [123456789]  # сюда ID мастеров
    for master_id in fake_masters:
        bot.send_message(master_id, f"Новая анонимная заявка:

{order_text}

Отправитель скрыт.")

    bot.send_message(user_id, "Ваша заявка отправлена мастерам анонимно!")
    anonymous_orders.pop(user_id, None)
