from google import genai
from google.genai.errors import ClientError

client = genai.Client(api_key="AIzaSyA9yz7OLoSgt99r1Wj7T_4ynKRw2WYPtWI")

def generate_response(command, mood=None):
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=[
                {
                    "role": "user",
                    "parts": [
                        {"text": "You are a compassionate mental health companion for students."}
                    ]
                },
                {
                    "role": "user",
                    "parts": [{"text": command}]
                }
            ]
        )
        return response.text

    except ClientError:
        # 🔹 FALLBACK RESPONSE (LOCAL, SAFE)
        fallback = {
            "Normal": "You seem to be doing well. Keep taking care of yourself and maintain healthy routines.",
            "Anxiety": "It’s okay to feel anxious sometimes. Try slow breathing and grounding exercises.",
            "Depression": "I’m really glad you shared this. Small steps matter. You’re not alone.",
            "Severe Distress": (
                "I’m really sorry you’re feeling this way. "
                "Please consider reaching out to a trusted person or a mental health professional."
            )
        }

        return fallback.get(
            mood,
            "Thank you for sharing. Take a moment to breathe and be kind to yourself."
        )
