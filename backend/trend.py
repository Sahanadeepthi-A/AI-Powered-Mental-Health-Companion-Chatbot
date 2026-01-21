def detect_trend(df):
    if len(df) < 5:
        return "Insufficient data"

    recent = df["mood"].tail(5).tolist()

    if recent.count("Severe Distress") >= 3:
        return "Worsening"
    elif recent.count("Normal") >= 3:
        return "Improving"
    else:
        return "Stable"
