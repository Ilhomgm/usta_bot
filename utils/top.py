import json
from collections import Counter

def top_masters(limit=3):
    with open("data/reviews.json", "r") as f:
        reviews = json.load(f)

    counter = Counter()
    for r in reviews:
        counter[r["author"]] += 1

    return counter.most_common(limit)
