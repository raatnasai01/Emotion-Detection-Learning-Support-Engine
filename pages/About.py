import streamlit as st

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

st.title("ℹ️ About the Project")

st.markdown("""
# 🎓 Emotion Detection & Learning Support Engine

An AI-powered educational support system that detects a student's emotional state from learning-related text and generates personalized learning guidance.

---

## 🎯 Project Objective

To identify students' learning emotions using Artificial Intelligence and provide personalized learning support using Google's Gemini AI.

---

## ✨ Features

- 😊 Emotion Detection
- 🤖 BERT Emotion Classification
- 🧠 BiLSTM Emotion Classification
- 🔍 Keyword Enhancement
- 🎯 Hybrid Emotion Prediction
- ✨ Gemini AI Mentor
- 📜 Prediction History
- 📊 Analytics Dashboard
- 💾 CSV Logging

---

## 🤖 AI Models Used

### 🧠 BiLSTM
- TensorFlow / Keras
- Student domain adaptation
- 5 Emotion Classes

### 🤖 BERT
- Hugging Face Transformers
- Fine-tuned for emotion classification
- Weighted prediction

---

## 📚 Emotion Classes

- 😐 Bored
- 😎 Confident
- 😕 Confused
- 🤔 Curious
- 😣 Frustrated

---

## 🛠 Technologies

- Python
- Streamlit
- TensorFlow
- Hugging Face Transformers
- Pandas
- Plotly
- Google Gemini API

---

## 📂 Dataset

Training data consists of multiple emotion datasets combined and cleaned for educational emotion detection.

---

## 🚀 Future Enhancements

- Speech Emotion Detection
- Voice-based Student Assistant
- Multilingual Emotion Detection
- Student Performance Analytics
- Teacher Dashboard
- Mobile Application

---

## 👨‍💻 Developer

**Bandaru Raatna Sai**

B.Tech – Artificial Intelligence & Machine Learning

Emotion Detection & Learning Support Engine

2026
""")