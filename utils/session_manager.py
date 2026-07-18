"""
==========================================================
SESSION MANAGER
==========================================================
"""

session_history = []


def add_to_history(field,
                   problem,
                   emotion,
                   confidence,
                   response):

    session_history.append({

        "field": field,

        "problem": problem,

        "emotion": emotion,

        "confidence": round(confidence * 100, 2),

        "response": response

    })


def get_history():

    return session_history