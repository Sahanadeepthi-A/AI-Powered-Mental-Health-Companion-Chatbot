def calculate_risk(mood):
    """
    Returns a risk score (0–100) based on predicted mental state.
    This is NOT a diagnosis, only a severity indicator.
    """
    risk_map = {
        "Normal": 20,
        "Anxiety": 50,
        "Depression": 70,
        "Severe Distress": 90
    }

    return risk_map.get(mood, 30)
