# app/tracker.py
day_log = []

def add_food(label, nutrition):
    entry = {
        "label": label,
        "calories": nutrition["calories"],
        "protein": nutrition["protein"],
        "carbs": nutrition["carbs"],
        "fat": nutrition["fat"]
    }
    day_log.append(entry)

def get_today_summary():
    total = {"calories": 0, "protein": 0, "carbs": 0, "fat": 0}
    for entry in day_log:
        for key in total:
            total[key] += entry[key]
    return total
