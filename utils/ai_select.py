import json

def ai_select_best_master(query, min_experience=2):
    with open("usta_superbot_x/data/masters.json", "r") as f:
        masters = json.load(f)

    candidates = []
    for m in masters:
        profession = m.get("profession", "").lower()
        experience = int(m.get("experience", "0").split()[0])
        if query.lower() in profession and experience >= min_experience:
            candidates.append((experience, m))

    if not candidates:
        return None
    # Выбираем самого опытного
    candidates.sort(reverse=True)
    return candidates[0][1]
