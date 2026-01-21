def summarize_mood(df):
    if df.empty:
        return "No data available"

    counts = df["mood"].value_counts()

    if counts.get("Severe Distress", 0) > 2:
        return "High emotional risk detected this period"
    elif counts.get("Normal", 0) > counts.sum() * 0.6:
        return "Overall stable mental health"
    else:
        return "Mixed emotional pattern observed"
