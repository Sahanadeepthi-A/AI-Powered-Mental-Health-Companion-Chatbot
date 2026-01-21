def safety_filter(text):
    blocked = ["suicide", "self harm", "kill myself"]
    return not any(b in text.lower() for b in blocked)
