def coping_plan(mood):
    plans = {
        "Severe Distress": [
            "Reach out to someone you trust today",
            "Practice guided breathing",
            "Seek professional counseling"
        ],
        "Depression": [
            "Maintain a routine",
            "Go for short walks",
            "Write down your thoughts"
        ],
        "Anxiety": [
            "Try box breathing",
            "Limit caffeine",
            "Grounding exercises"
        ],
        "Normal": [
            "Maintain sleep schedule",
            "Exercise regularly",
            "Practice gratitude"
        ]
    }
    return plans.get(mood, [])
