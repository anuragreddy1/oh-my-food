# app/suggester.py
def suggest_next_meal(summary):
    if summary["protein"] < 40:
        return "Try a protein-rich meal next: Grilled Chicken, Paneer, or Eggs."
    elif summary["carbs"] > 200:
        return "Reduce carbs next meal. Try a low-carb salad or boiled eggs."
    elif summary["calories"] > 1800:
        return "You're nearing your daily calorie limit. Eat something light."
    else:
        return "You're on track. Continue with a balanced meal."
