"""
==========================================================
BiLSTM PREDICTOR
==========================================================
"""

import numpy as np

from tensorflow.keras.preprocessing.sequence import pad_sequences

from utils.model_loader import load_models
from utils.preprocessing import clean_text


models = load_models()

bilstm_model = models["bilstm_model"]
tokenizer = models["keras_tokenizer"]
label_encoder = models["label_encoder"]


MAX_LEN = 80


def bilstm_predict(text):

    # Clean text
    text = clean_text(text)

    # Convert to sequence
    sequence = tokenizer.texts_to_sequences([text])

    # Pad
    padded = pad_sequences(
        sequence,
        maxlen=MAX_LEN,
        padding="post"
    )

    # Predict
    probabilities = bilstm_model.predict(
        padded,
        verbose=0
    )[0]

    # Convert to dictionary
    results = {}

    for emotion, probability in zip(
        label_encoder.classes_,
        probabilities
    ):
        results[emotion] = float(probability)

    return results