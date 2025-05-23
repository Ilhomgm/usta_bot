import json

def analyze_review_sentiment(text):
    negative_keywords = ["ужасно", "плохо", "недоволен", "проблема", "опоздал", "грязно", "некачественно"]
    positive_keywords = ["отлично", "быстро", "профессионал", "супер", "хорошо", "рекомендую", "доволен"]

    score = 0
    for word in positive_keywords:
        if word in text.lower():
            score += 1
    for word in negative_keywords:
        if word in text.lower():
            score -= 1
    return "положительный" if score > 0 else "негативный" if score < 0 else "нейтральный"

def get_reviews_by_tone(tone="положительный"):
    with open("data/reviews.json", "r") as f:
        reviews = json.load(f)
    return [r for r in reviews if analyze_review_sentiment(r["text"]) == tone]
