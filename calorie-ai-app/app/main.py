# app/main.py
from app.classifier import classify_food_image
from app.nutrition import get_nutrition
from app.tracker import add_food, get_today_summary
from app.suggester import suggest_next_meal

image_path = "test_images/biryani.jpg"
label = classify_food_image(image_path)
nutrition = get_nutrition(label)

add_food(label, nutrition)
summary = get_today_summary()

print(f"🧠 You just ate: {label.title()}")
print(f"🔥 Nutrition: {nutrition}")
print(f"📊 Daily Summary: {summary}")
print(f"🤖 Suggestion: {suggest_next_meal(summary)}")
