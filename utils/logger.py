import os
import pandas as pd
from datetime import datetime
from pandas.errors import EmptyDataError

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT_DIR, "data")
LOG_FILE = os.path.join(DATA_DIR, "emotion_logs.csv")


def log_prediction(text, prediction):

    os.makedirs(DATA_DIR, exist_ok=True)

    row = {
        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Input_Text": text,
        "Primary_Emotion": prediction["primary_emotion"],
        "Primary_Confidence": round(prediction["primary_confidence"] * 100, 2),
        "Secondary_Emotion": prediction["secondary_emotion"],
        "Secondary_Confidence": round(prediction["secondary_confidence"] * 100, 2),
    }

    try:
        df = pd.read_csv(LOG_FILE)
    except (FileNotFoundError, EmptyDataError):
        df = pd.DataFrame()

    df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)
    df.to_csv(LOG_FILE, index=False)

    print("✅ Prediction saved to emotion_logs.csv")