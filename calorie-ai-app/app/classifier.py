# classifier.py
import torch
from transformers import AutoFeatureExtractor, AutoModelForImageClassification
from PIL import Image
from torchvision import transforms
import os

MODEL_NAME = "google/vit-base-patch16-224"
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

feature_extractor = AutoFeatureExtractor.from_pretrained(MODEL_NAME)
model = AutoModelForImageClassification.from_pretrained(MODEL_NAME).to(device)
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=feature_extractor.image_mean, std=feature_extractor.image_std),
])

def classify_food_image(image_path):
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found at path: {image_path}")

    image = Image.open(image_path).convert("RGB")
    image_tensor = transform(image).unsqueeze(0).to(device)

    model.eval()
    with torch.no_grad():
        outputs = model(image_tensor)
        logits = outputs.logits
        predicted_class = torch.argmax(logits, dim=1).item()
        label = model.config.id2label[predicted_class]

    return label.lower()
 