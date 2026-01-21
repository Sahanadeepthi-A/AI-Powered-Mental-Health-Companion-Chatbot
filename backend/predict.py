import os
import joblib
import sqlite3

# Get project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(BASE_DIR, "model", "sentiment_model.pkl")
VECTORIZER_PATH = os.path.join(BASE_DIR, "model", "vectorizer.pkl")
ENCODER_PATH = os.path.join(BASE_DIR, "model", "label_encoder.pkl")
DB_PATH = os.path.join(BASE_DIR, "database", "app.db")

# Load artifacts
model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)
label_encoder = joblib.load(ENCODER_PATH)

def predict_with_confidence(text):
    vec = vectorizer.transform([text])
    probs = model.predict_proba(vec)[0]
    idx = probs.argmax()
    return label_encoder.inverse_transform([idx])[0], float(probs[idx])

def save_chat(user_id, text, mood):
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute(
        "INSERT INTO chats (user_id, message, mood) VALUES (?, ?, ?)",
        (user_id, text, mood)
    )
    conn.commit()
    conn.close()
