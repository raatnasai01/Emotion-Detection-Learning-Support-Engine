"""
==========================================================
MODEL LOADER
Emotion Detection & Learning Support Engine
==========================================================
"""

import os
import pickle
import tensorflow as tf

from transformers import (
    BertTokenizer,
    BertForSequenceClassification,
)

# ------------------------------------------------------
# PROJECT PATHS
# ------------------------------------------------------

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODELS_DIR = os.path.join(ROOT_DIR, "models")
PREPROCESSING_DIR = os.path.join(ROOT_DIR, "preprocessing")

# ------------------------------------------------------
# CACHE
# ------------------------------------------------------

_cached_models = None


def load_models():
    global _cached_models

    if _cached_models is not None:
        return _cached_models

    print("Loading models... (This happens only once)")

    # -----------------------------
    # BERT
    # -----------------------------

    bert_tokenizer = BertTokenizer.from_pretrained(
        os.path.join(MODELS_DIR, "bert")
    )

    bert_model = BertForSequenceClassification.from_pretrained(
        os.path.join(MODELS_DIR, "bert")
    )

    # -----------------------------
    # BiLSTM
    # -----------------------------

    bilstm_model = tf.keras.models.load_model(
        os.path.join(
            MODELS_DIR,
            "bilstm",
            "bilstm_best_model.keras"
        ),
        compile=False
    )

    # -----------------------------
    # Tokenizer
    # -----------------------------

    with open(
        os.path.join(
            PREPROCESSING_DIR,
            "tokenizer.pkl"
        ),
        "rb"
    ) as f:

        keras_tokenizer = pickle.load(f)

    # -----------------------------
    # Label Encoder
    # -----------------------------

    with open(
        os.path.join(
            PREPROCESSING_DIR,
            "label_encoder.pkl"
        ),
        "rb"
    ) as f:

        label_encoder = pickle.load(f)

    _cached_models = {

        "bert_model": bert_model,
        "bert_tokenizer": bert_tokenizer,
        "bilstm_model": bilstm_model,
        "keras_tokenizer": keras_tokenizer,
        "label_encoder": label_encoder

    }

    return _cached_models