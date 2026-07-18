import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="Prediction History",
    page_icon="📜",
    layout="wide"
)

st.title("📜 Prediction History")

LOG_FILE = "data\emotion_logs.csv"

if os.path.exists(LOG_FILE):

    df = pd.read_csv(LOG_FILE)

    if len(df) == 0:
        st.info("No predictions available.")

    else:

        st.success(f"Total Predictions : {len(df)}")

        st.dataframe(
            df,
            use_container_width=True
        )

        csv = df.to_csv(index=False)

        st.download_button(
            "📥 Download History",
            csv,
            "emotion_history.csv",
            "text/csv"
        )

else:

    st.warning("emotion_logs.csv not found.")