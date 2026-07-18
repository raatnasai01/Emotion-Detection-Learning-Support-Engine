"""
==========================================================
AI MENTOR SERVICE
Emotion Detection & Learning Support Engine
==========================================================
"""

from utils.unified_predictor import unified_predict
from utils.prompt_builder import build_prompt
from utils.gemini_service import generate_response
from utils.session_manager import add_to_history
from utils.logger import log_prediction


def get_learning_support(field, problem):

    # --------------------------------------------------
    # Emotion Detection
    # --------------------------------------------------

    prediction = unified_predict(problem)

    emotion = prediction["primary_emotion"]
    confidence = prediction["primary_confidence"] * 100

    # --------------------------------------------------
    # Prompt
    # --------------------------------------------------

    prompt = build_prompt(
        field,
        problem,
        emotion,
        confidence
    )

    # --------------------------------------------------
    # Gemini
    # --------------------------------------------------

    response = generate_response(
        prompt,
        emotion
    )

    # --------------------------------------------------
    # Session History
    # --------------------------------------------------

    add_to_history(
        field,
        problem,
        emotion,
        prediction["primary_confidence"],
        response
    )

    # --------------------------------------------------
    # CSV Logging
    # --------------------------------------------------

    log_prediction(
        problem,
        prediction
    )

    # --------------------------------------------------
    # Final Result
    # --------------------------------------------------

    return {
        "prediction": prediction,
        "response": response
    }