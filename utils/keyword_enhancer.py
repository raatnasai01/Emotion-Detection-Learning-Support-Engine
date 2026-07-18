"""
==========================================================
KEYWORD ENHANCEMENT
Emotion Detection & Learning Support Engine
==========================================================
"""

# -----------------------------
# Common spelling corrections
# -----------------------------

SPELLING = {

    "frustated": "frustrated",
    "understd": "understand",
    "understnd": "understand",
    "dont": "don't",
    "cant": "can't",
    "ml": "machine learning",
    "ai": "artificial intelligence"

}


# -----------------------------
# Emotion Keywords
# -----------------------------

KEYWORDS = {

    "Bored": [
        "boring",
        "bored",
        "sleepy",
        "tired",
        "dull",
        "uninterested",
        "no interest",
        "not interested"
    ],

    "Confident": [
        "He understood",
        "she understood",
        "I understood",
        "easy",
        "solved",
        "done",
        "completed",
        "confident",
        "happy",
        "great",
        "excellent",
        "good",
        "finally understood"
    ],

    "Confused": [
        "confused",
        "don't understand",
        "cannot understand",
        "can't understand",
        "not understand",
        "unclear",
        "doubt",
        "stuck",
        "difficult",
        "hard",
        "problem",
        "help"
    ],

    "Curious": [
        "why",
        "how",
        "curious",
        "wonder",
        "interested",
        "learn",
        "explore",
        "know more"
    ],

    "Frustrated": [
        "fail",
        "failed",
        "frustrated",
        "stress",
        "stressed",
        "angry",
        "annoyed",
        "upset",
        "hate",
        "fed up",
        "irritated",
        "giving up"
    ]
}


# -----------------------------
# Keyword Detection
# -----------------------------

def detect_keywords(text):

    text = text.lower()

    # Apply spelling corrections
    for wrong, correct in SPELLING.items():
        text = text.replace(wrong, correct)

    scores = {emotion: 0 for emotion in KEYWORDS}

    for emotion, words in KEYWORDS.items():

        for word in words:

            if word in text:
                scores[emotion] += 1

    return scores