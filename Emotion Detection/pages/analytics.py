import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(
    page_title="Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Emotion Analytics Dashboard")

LOG_FILE = "data\emotion_logs.csv"   # Change if your CSV is inside data/

if os.path.exists(LOG_FILE):

    df = pd.read_csv(LOG_FILE)

    if df.empty:
        st.warning("No prediction history available.")

    else:

        # ==========================
        # Summary Cards
        # ==========================

        st.header("📈 Summary")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Total Predictions",
                len(df)
            )

        with col2:
            top_emotion = df["Primary_Emotion"].mode()[0]
            st.metric(
                "Most Common Emotion",
                top_emotion
            )

        st.divider()

        # ==========================
        # Emotion Distribution
        # ==========================

        st.header("😊 Emotion Distribution")

        emotion_counts = df["Primary_Emotion"].value_counts()

        fig1 = px.bar(
            x=emotion_counts.index,
            y=emotion_counts.values,
            labels={
                "x": "Emotion",
                "y": "Count"
            },
            text=emotion_counts.values,
            title="Primary Emotion Frequency"
        )

        st.plotly_chart(
            fig1,
            use_container_width=True
        )

        st.divider()

        # ==========================
        # Pie Chart
        # ==========================

        st.header("🥧 Emotion Percentage")

        fig2 = px.pie(
            values=emotion_counts.values,
            names=emotion_counts.index,
            title="Emotion Distribution"
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

        st.divider()

        # ==========================
        # Confidence Histogram
        # ==========================

        st.header("🎯 Confidence Distribution")

        fig3 = px.histogram(
            df,
            x="Primary_Confidence",
            nbins=10,
            title="Prediction Confidence"
        )

        st.plotly_chart(
            fig3,
            use_container_width=True
        )

        st.divider()

        # ==========================
        # Recent Predictions
        # ==========================

        st.header("📋 Recent Predictions")

        st.dataframe(
            df.tail(10),
            use_container_width=True
        )

else:

    st.error("emotion_logs.csv not found.")