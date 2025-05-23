import json
from math import radians, cos, sin, sqrt, atan2

def is_nearby(loc1, loc2, radius_km=5):
    # Вычисление расстояния между двумя координатами (Haversine)
    R = 6371  # радиус Земли в км
    lat1, lon1 = radians(loc1["lat"]), radians(loc1["lon"])
    lat2, lon2 = radians(loc2["lat"]), radians(loc2["lon"])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c <= radius_km

def notify_nearby_masters(bot, user_location, order_text):
    with open("usta_superbot_x/data/masters.json", "r") as f:
        masters = json.load(f)

    for master in masters:
        if "location" in master and is_nearby(user_location, master["location"]):
            text = f"Поступил новый заказ рядом с вами!

Описание: {order_text}"
            # Пример: master['id'] можно заменить на master.get("tg_id", 123456)
            bot.send_message(master.get("tg_id", 123456), text)
