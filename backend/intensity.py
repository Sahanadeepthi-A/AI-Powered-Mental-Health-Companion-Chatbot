def emotion_intensity(mood, confidence):
    base = {
        "Normal": 20,
        "Anxiety": 50,
        "Depression": 70,
        "Severe Distress": 90
    }.get(mood, 30)

    return min(100, int(base * confidence))
