import json
from collections import defaultdict
from random import randint

def fake_activity_stats():
    days = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]
    stats = {day: randint(1, 10) for day in days}
    return stats
