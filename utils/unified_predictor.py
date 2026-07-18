"""
==========================================================
UNIFIED PREDICTOR
Emotion Detection & Learning Support Engine
==========================================================
"""

from utils.bilstm_predictor import bilstm_predict
from utils.bert_predictor import bert_predict
from utils.keyword_enhancer import detect_keywords


# ---------------------------------------------------------
# Configuration
# ---------------------------------------------------------

KEYWORD_WEIGHT = 0.03      # Small boost from keywords
SECONDARY_THRESHOLD = 0.15 # Minimum confidence for secondary emotion


# ---------------------------------------------------------
# Unified Prediction
# ---------------------------------------------------------

def unified_predict(text):

    # -----------------------------------------------------
    # Keyword Detection
    # -----------------------------------------------------

    keyword_scores = detect_keywords(text)

    # -----------------------------------------------------
    # BiLSTM Prediction
    # -----------------------------------------------------

    bilstm_scores = bilstm_predict(text)

    # -----------------------------------------------------
    # BERT Prediction
    # -----------------------------------------------------

    bert_scores = bert_predict(text)

    # -----------------------------------------------------
    # Keyword Adjustment
    # -----------------------------------------------------

    adjusted_scores = bert_scores.copy()

    for emotion in adjusted_scores:

        adjusted_scores[emotion] += (
            keyword_scores[emotion] * KEYWORD_WEIGHT
        )

    # -----------------------------------------------------
    # Normalize Scores
    # -----------------------------------------------------

    total = sum(adjusted_scores.values())

    if total > 0:

        for emotion in adjusted_scores:

            adjusted_scores[emotion] /= total

    # -----------------------------------------------------
    # Primary Emotion
    # -----------------------------------------------------

    primary_emotion = max(
        adjusted_scores,
        key=adjusted_scores.get
    )

    primary_confidence = adjusted_scores[primary_emotion]

    # -----------------------------------------------------
    # Secondary Emotion
    # -----------------------------------------------------

    sorted_scores = sorted(
        adjusted_scores.items(),
        key=lambda x: x[1],
        reverse=True
    )

    secondary_emotion = None
    secondary_confidence = 0

    if len(sorted_scores) > 1:

        emotion, confidence = sorted_scores[1]

        if confidence >= SECONDARY_THRESHOLD:

            secondary_emotion = emotion
            secondary_confidence = confidence

    # -----------------------------------------------------
    # Final Result
    # -----------------------------------------------------

    return {

        "primary_emotion": primary_emotion,
        "primary_confidence": primary_confidence,

        "secondary_emotion": secondary_emotion,
        "secondary_confidence": secondary_confidence,

        "keyword_scores": keyword_scores,

        "bert_scores": adjusted_scores,

        "bilstm_scores": bilstm_scores

    }