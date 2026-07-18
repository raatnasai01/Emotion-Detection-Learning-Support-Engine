"""
==========================================================
RESPONSE MANAGER
==========================================================
"""

from utils.prompt_builder import build_prompt
from utils.gemini_service import generate_response


def regenerate_response(
    field,
    problem,
    emotion,
    confidence,
):
    """
    Generate a fresh Gemini response whenever
    the input changes.
    """

    prompt = build_prompt(
        field,
        problem,
        emotion,
        confidence
    )

    response = generate_response(
        prompt,
        emotion
    )

    return response