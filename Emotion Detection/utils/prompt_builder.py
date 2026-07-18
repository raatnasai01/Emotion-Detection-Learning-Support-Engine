"""
==========================================================
PROMPT BUILDER
==========================================================
"""


def build_prompt(field,
                 problem,
                 emotion,
                 confidence):

    prompt = f"""
You are an empathetic AI learning mentor.

Student Field:
{field}

Student Problem:
{problem}

Detected Emotion:
{emotion}

Confidence:
{confidence:.2f}%

Instructions:

1. Acknowledge the student's emotional state.
2. Respond with empathy.
3. Give advice specific to the student's field.
4. Suggest practical next steps.
5. Keep the response positive and motivating.
6. Keep the response under 200 words.
"""

    return prompt