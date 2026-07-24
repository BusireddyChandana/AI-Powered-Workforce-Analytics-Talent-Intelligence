import pickle
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(BASE_DIR, "models", "attrition_model.pkl")
SCALER_PATH = os.path.join(BASE_DIR, "models", "scaler.pkl")
FEATURES_PATH = os.path.join(BASE_DIR, "models", "features.pkl")


with open(MODEL_PATH, "rb") as file:
    model = pickle.load(file)

with open(SCALER_PATH, "rb") as file:
    scaler = pickle.load(file)

with open(FEATURES_PATH, "rb") as file:
    features = pickle.load(file)


print("Model loaded successfully")