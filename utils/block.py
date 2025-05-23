import json

def get_blocked_masters(threshold=2):
    with open("data/reviews.json", "r") as f:
        reviews = json.load(f)

    negative_words = ["ужасно", "плохо", "грязно", "некачественно", "опоздал", "обман", "хамство"]
    negative_count = {}

    for review in reviews:
        author = review["author"]
        if any(word in review["text"].lower() for word in negative_words):
            negative_count[author] = negative_count.get(author, 0) + 1

    blocked = [name for name, count in negative_count.items() if count >= threshold]
    return blocked
