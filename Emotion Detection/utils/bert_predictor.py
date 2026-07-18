"""
==========================================================
BERT PREDICTOR
Emotion Detection & Learning Support Engine
==========================================================
"""

import torch
import numpy as np

from utils.model_loader import load_models
from utils.preprocessing import clean_text

# ------------------------------------------------------
# LOAD MODELS
# ------------------------------------------------------

models = load_models()

bert_model = models["bert_model"]
bert_tokenizer = models["bert_tokenizer"]
label_encoder = models["label_encoder"]

# ------------------------------------------------------
# CLASS WEIGHTS (SkillWallet)
# ------------------------------------------------------

CLASS_WEIGHTS = {
    "Bored": 1.2,
    "Confident": 1.8,
    "Confused": 0.6,
    "Curious": 1.0,
    "Frustrated": 1.4,
}


# ------------------------------------------------------
# PREDICT FUNCTION
# ------------------------------------------------------

def bert_predict(text):

    text = clean_text(text)

    inputs = bert_tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=80
    )

    with torch.no_grad():
        outputs = bert_model(**inputs)

    logits = outputs.logits

    probabilities = torch.softmax(logits, dim=1).numpy()[0]

    weighted_probs = []

    for emotion, probability in zip(label_encoder.classes_, probabilities):

        weighted_probs.append(
            probability * CLASS_WEIGHTS[emotion]
        )

    weighted_probs = np.array(weighted_probs)

    weighted_probs = weighted_probs / weighted_probs.sum()

    results = {}

    for emotion, probability in zip(
        label_encoder.classes_,
        weighted_probs
    ):

        results[emotion] = float(probability)

    return results