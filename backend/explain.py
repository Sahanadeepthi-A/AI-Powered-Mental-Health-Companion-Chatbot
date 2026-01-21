import os
import joblib
import numpy as np

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

EXPLAINER_PATH = os.path.join(BASE_DIR, "model", "shap_explainer.pkl")
VECTORIZER_PATH = os.path.join(BASE_DIR, "model", "vectorizer.pkl")
ENCODER_PATH = os.path.join(BASE_DIR, "model", "label_encoder.pkl")

explainer = joblib.load(EXPLAINER_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)
label_encoder = joblib.load(ENCODER_PATH)

def explain(text, predicted_label):
    vec = vectorizer.transform([text])
    vec_dense = vec.toarray()

    shap_values = explainer(vec_dense)
    class_index = list(label_encoder.classes_).index(predicted_label)

    shap_for_class = shap_values[..., class_index]
    return shap_for_class

