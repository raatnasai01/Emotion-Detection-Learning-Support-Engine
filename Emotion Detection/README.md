# 🎓 Emotion Detection & Learning Support Engine

An AI-powered educational support system that detects a student's learning emotion from text and provides personalized learning guidance using Google's Gemini AI.

---

## 📌 Project Overview

The Emotion Detection & Learning Support Engine is designed to help students by identifying their emotional state during learning and generating supportive, field-specific responses.

The system combines Deep Learning, Natural Language Processing (NLP), and Generative AI to deliver personalized learning assistance.

---

## ✨ Features

- 😊 Emotion Detection from text
- 🧠 BiLSTM Emotion Classification
- 🤖 BERT Emotion Classification
- 🔍 Keyword-Based Emotion Enhancement
- 🎯 Hybrid Emotion Prediction
- ✨ Gemini AI Learning Mentor
- 📜 Prediction History
- 📊 Analytics Dashboard
- 💾 CSV Logging
- 🌐 Multi-page Streamlit Application

---

## 📚 Emotion Classes

- 😐 Bored
- 😎 Confident
- 😕 Confused
- 🤔 Curious
- 😣 Frustrated

---

## 🛠 Technologies Used

- Python
- Streamlit
- TensorFlow / Keras
- Hugging Face Transformers (BERT)
- Google Gemini API
- Pandas
- Plotly
- Scikit-learn
- NumPy

---

## 📂 Project Structure

```text
Emotion-Detection-Learning-Support-Engine/
│
├── app.py
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
│
├── data/
├── models/
├── pages/
├── preprocessing/
├── utils/
├── notebooks/
└── screenshots/
```

---

## ⚙ Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/Emotion-Detection-Learning-Support-Engine.git
```

### Move into the project

```bash
cd Emotion-Detection-Learning-Support-Engine
```

### Create a virtual environment

```bash
python -m venv .venv
```

### Activate it

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Configure API Key

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_api_key_here
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 📸 Application Pages

- 🏠 Home
- 📜 History
- 📊 Analytics
- ℹ️ About

---

## 📊 AI Workflow

```text
Student Input
      │
      ▼
Text Preprocessing
      │
      ▼
Keyword Enhancement
      │
      ▼
BiLSTM Prediction
      │
      ▼
BERT Prediction
      │
      ▼
Hybrid Emotion Prediction
      │
      ▼
Prompt Builder
      │
      ▼
Gemini AI
      │
      ▼
Learning Support Response
```

---

## 🚀 Future Enhancements

- Speech Emotion Recognition
- Multilingual Emotion Detection
- Teacher Dashboard
- Student Progress Tracking
- Mobile Application
- Cloud Deployment

---

## 👨‍💻 Developer

**Bandaru Raatna Sai**

B.Tech – Artificial Intelligence & Machine Learning

---

## 📜 License

This project is developed for educational and research purposes.