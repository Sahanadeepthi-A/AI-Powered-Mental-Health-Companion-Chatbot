import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
import numpy as np
import shap

# Load processed data
df = pd.read_csv("data/processed/training_data.csv")

# -------- TEXT CLEANING --------
df["text"] = df["text"].astype(str).str.strip()
df = df[df["text"].notna()]
df = df[df["text"] != ""]

print("Dataset size after cleaning:", df.shape)

X = df["text"]
y = df["label"]

# Encode labels
le = LabelEncoder()
y_enc = le.fit_transform(y)

# Vectorizer
vectorizer = TfidfVectorizer(
    max_features=8000,
    ngram_range=(1, 2),
    stop_words="english"
)

X_vec = vectorizer.fit_transform(X)

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X_vec, y_enc, test_size=0.2, random_state=42, stratify=y_enc
)

# Model
model = XGBClassifier(
    n_estimators=200,
    max_depth=6,
    learning_rate=0.1,
    subsample=0.8,
    colsample_bytree=0.8,
    eval_metric="mlogloss"
)

model.fit(X_train, y_train)

# 🔹 SHAP FIX: initialize WITHOUT sparse background
explainer = shap.TreeExplainer(model)

# Save artifacts
joblib.dump(model, "model/sentiment_model.pkl")
joblib.dump(vectorizer, "model/vectorizer.pkl")
joblib.dump(le, "model/label_encoder.pkl")
joblib.dump(explainer, "model/shap_explainer.pkl")

print("✅ Model training completed successfully")
