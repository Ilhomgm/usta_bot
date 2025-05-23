def semantic_match(user_input):
    input_lower = user_input.lower()

    # Категории: профессии и товары
    categories = {
        "электрик": ["лампочка", "проводка", "розетка", "электрик", "свет"],
        "сантехник": ["труба", "кран", "сантехник", "течь", "слив", "унитаз"],
        "мастер по кондиционерам": ["кондиционер", "сплит", "охлаждение"],
        "автомастер": ["машина", "авто", "двигатель", "шиномонтаж", "ремонт авто"],
        "строитель": ["кирпич", "цемент", "ремонт", "штукатурка", "строитель"],
        "продажа генераторов": ["генератор", "продаю генератор", "нужен генератор"],
        "продукты / еда": ["картошка", "сено", "курица", "яйца", "продукты", "мясо", "фрукты", "овощи"],
        "услуги": ["уборка", "няня", "курьер", "репетитор", "мастер", "услуга"]
    }

    # Узбекская поддержка (упрощённая)
    uz_categories = {
        "elektrik": ["chiroq", "elektr", "rozetka", "svet", "ustasi"],
        "santexnik": ["truba", "kran", "suv", "santexnik", "unitaz"],
        "konditsioner usta": ["konditsioner", "split", "sovutish"],
        "avto usta": ["mashina", "dvigatel", "avto", "remont mashina"],
        "quruvchi": ["g'isht", "sement", "ta'mirlash", "usta", "quruvchi"],
        "generator sotuvchisi": ["generator", "sotaman generator", "kerak generator"],
        "mahsulotlar": ["kartoshka", "jo'xori", "tovuq", "tuxum", "meva", "sabzavot"],
        "xizmatlar": ["tozalash", "enaga", "yetkazish", "usta", "xizmat"]
    }

    # Анализ на русском
    for category, keywords in categories.items():
        if any(word in input_lower for word in keywords):
            return category

    # Анализ на узбекском
    for category, keywords in uz_categories.items():
        if any(word in input_lower for word in keywords):
            return category

    return "универсальный мастер"
