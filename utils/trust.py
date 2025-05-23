import json

def calculate_trust_rating():
    with open("data/profile.json", "r") as pf:
        profile = json.load(pf)
    with open("data/reviews.json", "r") as rf:
        reviews = json.load(rf)

    stars_total = sum(r["stars"] for r in reviews)
    review_count = len(reviews)
    experience_years = int(profile["experience"].split()[0])

    trust = (stars_total / review_count if review_count else 5) * 10 + experience_years * 2
    return min(100, round(trust, 2))  # максимум 100
