import joblib
import sqlite3

model = joblib.load("model/sentiment_model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")
le = joblib.load("model/label_encoder.pkl")

def predict_with_confidence(text):
    vec = vectorizer.transform([text])
    probs = model.predict_proba(vec)[0]
    idx = probs.argmax()
    return le.inverse_transform([idx])[0], float(probs[idx])

def save_chat(user_id, text, mood):
    conn = sqlite3.connect("database/app.db")
    c = conn.cursor()
    c.execute(
        "INSERT INTO chats (user_id, message, mood) VALUES (?, ?, ?)",
        (user_id, text, mood)
    )
    conn.commit()
    conn.close()
