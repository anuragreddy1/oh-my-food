# test.py

import os
import sys

# If running from root, add the app folder to path
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from app.classifier import classify_food_image

# Path to your test image
image_path = "calorie-ai-app/test_images/biriyani.jpg"

# Classify
result = classify_food_image(image_path)
print(f"Predicted class: {result}")
