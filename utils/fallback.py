"""
==========================================================
FALLBACK RESPONSES
==========================================================
"""

FALLBACK_RESPONSES = {

    "Bored":
        "It seems you're feeling bored. Try changing your study environment, taking a short break, or working on a hands-on activity to regain focus.",

    "Confident":
        "You're doing well! Keep building on your confidence by practicing more challenging problems and helping others learn.",

    "Confused":
        "It's okay to feel confused. Break the topic into smaller parts, review the fundamentals, and ask questions whenever you're stuck.",

    "Curious":
        "Your curiosity is a strength. Explore additional tutorials, articles, or small projects to deepen your understanding.",

    "Frustrated":
        "Feeling frustrated is completely normal. Take a short break, revisit the concept step by step, and remember that progress comes with practice."
}


def get_fallback_response(emotion):
    return FALLBACK_RESPONSES.get(
        emotion,
        "Keep learning and stay positive!"
    )