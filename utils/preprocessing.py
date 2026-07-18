"""
==========================================================
TEXT PREPROCESSING
Emotion Detection & Learning Support Engine
==========================================================
"""

import re


def clean_text(text: str) -> str:
    """
    Clean input text before prediction.
    """

    # Lowercase
    text = text.lower()

    # Remove URLs
    text = re.sub(r"http\S+", "", text)

    # Remove HTML tags
    text = re.sub(r"<.*?>", "", text)

    # Keep only letters, numbers and apostrophes
    text = re.sub(r"[^a-zA-Z0-9\s']", " ", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text