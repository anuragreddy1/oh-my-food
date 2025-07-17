# app/nutrition.py
from app.nutrition_data import nutrition_db

def get_nutrition(label):
    return nutrition_db.get(label.lower(), {
        "calories": 0,
        "protein": 0,
        "carbs": 0,
        "fat": 0
    })
