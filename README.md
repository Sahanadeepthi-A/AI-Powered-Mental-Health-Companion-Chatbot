🧠 AI-Powered Mental Health Companion Chatbot

An end-to-end AI/ML-based mental health support system that analyzes user-written text to detect emotional states, explains predictions using Explainable AI (SHAP), and provides ethical, supportive guidance through a conversational interface.

This project is designed with responsible AI principles, where machine learning models make all decisions, and large language models are used only for empathetic responses, never for diagnosis or prediction.

📌 Problem Statement

Students often experience stress, anxiety, and emotional distress but hesitate to approach professional counselors due to stigma, lack of access, or fear of judgment.

This project aims to:

Provide a safe, private AI companion

Detect emotional states from free-text input

Explain predictions transparently

Offer supportive coping strategies

Handle high-risk cases responsibly

🎯 Objectives

Build a real NLP-based ML classifier using Kaggle data

Ensure explainability using SHAP

Avoid LLM hallucinations in decision-making

Implement ethical safeguards and graceful API failure handling

Deliver a full-stack, deployable AI web application

🗂️ Dataset

Source: Kaggle – Mental Health Sentiment Dataset
https://www.kaggle.com/datasets/suchintikasarkar/sentiment-analysis-for-mental-health

Dataset Features:

statement – user-written text

status – mental health category

Label Mapping Used in This Project:

Normal → Normal

Anxiety / Stress → Anxiety

Depression → Depression

Suicidal → Severe Distress

This dataset enables real NLP-based sentiment classification, not rule-based logic.

🧠 System Architecture
User Input (Text / Voice)
        ↓
Text Cleaning & Preprocessing
        ↓
TF-IDF Vectorization
        ↓
XGBoost Multi-Class Classifier
        ↓
Prediction + Confidence Score
        ↓
SHAP Explainability
        ↓
Risk Scoring & Coping Plan
        ↓
Optional LLM Empathetic Response

🛠️ Tech Stack
Backend / Machine Learning

Python

Pandas, NumPy

Scikit-learn

XGBoost

SHAP (Explainable AI)

Frontend

Streamlit

Database

SQLite

AI Assistant (Optional)

Google Gemini API
(fallback responses included if quota is exceeded)

✨ Key Features
🔹 Machine Learning Core

Multi-class emotion classification

Confidence score for predictions

Trained on real Kaggle text data

No rule-based or hard-coded decisions

🔹 Explainable AI

SHAP bar plots explaining predictions

Class-specific explanations for multi-class model

Transparent and interpretable outputs

🔹 Ethical AI Design

No medical diagnosis

Safety filter for self-harm content

Crisis escalation messaging

Clear separation of ML vs LLM responsibilities

🔹 Analytics & Reports

Chat history stored securely

Weekly emotional summary

Trend detection (Improving / Stable / Worsening)

Emotional intensity score (0–100)

🔹 Robust Engineering

Authentication system

SQLite database

Graceful handling of API failures

LLM fallback responses

Production-style error handling

📁 Project Structure
mental_health_companion_chatbot/
│
├── app.py
├── requirements.txt
│
├── data/
│   ├── raw/
│   └── processed/
│
├── model/
│   ├── sentiment_model.pkl
│   ├── vectorizer.pkl
│   ├── label_encoder.pkl
│   └── shap_explainer.pkl
│
├── backend/
│   ├── auth.py
│   ├── predict.py
│   ├── risk_score.py
│   ├── analytics.py
│   ├── reports.py
│   ├── trend.py
│   ├── intensity.py
│   ├── explain.py
│   └── safety.py
│
└── chatbot/
    └── gemini_chat.py

🚀 How to Run Locally
1️⃣ Install Dependencies
pip install -r requirements.txt

2️⃣ Preprocess Data
python backend/data_preprocessing.py

3️⃣ Train Model
python backend/train_model.py

4️⃣ Run Application
streamlit run app.py

🌐 Deployment

This application is deployable on Hugging Face Spaces using Streamlit.

Deployment highlights:

No Docker required

Supports ML models and SQLite

Gemini API key managed via environment secrets

Works even without LLM access due to fallback logic

🧪 Sample Output

Detected Emotional State: Normal

Prediction Confidence: 80%+

Coping Plan: Sleep, exercise, gratitude

Explainability: SHAP feature importance plot

Response: Ethical, non-diagnostic guidance

⚠️ Ethical Disclaimer

This project does not diagnose mental illness

It is not a replacement for professional care

High-risk cases prompt external support suggestions

Built strictly for educational and research purposes

📉 Limitations

Text-only analysis

Dependent on dataset quality

LLM responses limited by API quotas

Not a clinical or therapeutic system

🔮 Future Enhancements

Counselor dashboard

Voice emotion analysis

Mobile application

Privacy-preserving learning

Research-grade evaluation metrics
