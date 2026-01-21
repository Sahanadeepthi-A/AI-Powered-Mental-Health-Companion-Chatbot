import joblib
import joblib
import numpy as np

explainer = joblib.load("model/shap_explainer.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")
label_encoder = joblib.load("model/label_encoder.pkl")

def explain(text, predicted_label):
    vec = vectorizer.transform([text])
    vec_dense = vec.toarray()

    shap_values = explainer(vec_dense)

    # Get class index for the predicted label
    class_index = list(label_encoder.classes_).index(predicted_label)

    # Extract SHAP values for that class
    shap_for_class = shap_values[..., class_index]

    return shap_for_class, vec_dense
