"""
==========================================================
GEMINI SERVICE
Emotion Detection & Learning Support Engine
==========================================================
"""

import os
from dotenv import load_dotenv
import google.generativeai as genai

# ------------------------------------------------------
# LOAD ENVIRONMENT VARIABLES
# ------------------------------------------------------

load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    raise ValueError("GOOGLE_API_KEY not found in .env file")

# ------------------------------------------------------
# CONFIGURE GEMINI
# ------------------------------------------------------

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

# ------------------------------------------------------
# GENERATE RESPONSE
# ------------------------------------------------------

def generate_response(prompt):

    response = model.generate_content(prompt)

    return response.text

from utils.fallback import get_fallback_response

def generate_response(prompt, emotion):

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception:
        return get_fallback_response(emotion)