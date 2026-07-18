
import streamlit as st
import plotly.express as px
import pandas as pd
from utils.ai_mentor import get_learning_support

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="Emotion Detection & Learning Support Engine",
    page_icon="🎓",
    layout="wide"
)

# ==========================================================
# TITLE
# ==========================================================

st.title("🎓 Emotion Detection & Learning Support Engine")

st.markdown(
"""
Analyze a student's learning emotion and receive personalized
AI-powered learning support.
"""
)

# ==========================================================
# SIDEBAR
# ==========================================================

st.sidebar.success("✅ AI Models Loaded")

st.sidebar.markdown("""
### Models

- 🤖 BERT
- 🧠 BiLSTM
- ✨ Gemini AI

### Features

- Emotion Detection
- AI Learning Support
- Keyword Analysis
- Prediction History
""")

# ==========================================================
# INPUT SECTION
# ==========================================================

st.header("📝 Student Input")

field = st.selectbox(
    "Select Learning Field",
    [
        "Machine Learning",
        "Deep Learning",
        "Data Structures",
        "Algorithms",
        "Python",
        "Java",
        "Database",
        "Operating Systems",
        "Computer Networks",
        "Artificial Intelligence",
        "Other"
    ]
)

problem = st.text_area(
    "Describe your learning problem",
    height=180,
    placeholder="Example: I am frustrated because I don't understand recursion..."
)

analyze = st.button(
    "🚀 Analyze Emotion",
    use_container_width=True
)

# ==========================================================
# ANALYSIS
# ==========================================================

if analyze:

    if problem.strip() == "":

        st.warning("⚠ Please describe your learning problem.")

    else:

        with st.spinner("Analyzing your learning emotion..."):

            result = get_learning_support(
                field=field,
                problem=problem
            )

        prediction = result["prediction"]
        response = result["response"]

        st.success("✅ Analysis Complete!")

        from datetime import datetime
        st.caption(
        f"Prediction Time: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}"
        )

        st.divider()

        # ======================================================
        # EMOTION ANALYSIS
        # ======================================================

        st.header("📊 Emotion Analysis")

        col1, col2 = st.columns(2)

        with col1:

            st.success(
                f"😊 Primary Emotion: **{prediction['primary_emotion']}**"
            )

            st.progress(
                float(prediction["primary_confidence"])
            )

            st.write(
                f"Confidence: **{prediction['primary_confidence']*100:.2f}%**"
            )

        with col2:

            if prediction["secondary_emotion"]:

                st.info(
                    f"""
🧠 **Secondary Emotion**

{prediction['secondary_emotion']}

Confidence:
{prediction['secondary_confidence']*100:.2f}%
"""
                )

            else:

                st.info(
                    "🧠 No strong secondary emotion detected."
                )

        st.divider()

        # ======================================================
        # KEYWORD ANALYSIS
        # ======================================================

        st.header("🔍 Keyword Analysis")

        found = False

        for emotion, score in prediction["keyword_scores"].items():

            if score > 0:

                found = True

                st.write(f"### {emotion}")

                st.progress(
                    min(score / 5, 1.0)
                )

                st.caption(
                    f"Matched Keywords : {score}"
                )

        if not found:

            st.info(
                "No emotion keywords detected."
            )

        st.divider()

        # ======================================================
        # AI RESPONSE
        # ======================================================

        st.header("🤖 AI Learning Support")

        with st.expander(
            "View AI Mentor Response",
            expanded=True
        ):

            st.success(response)

        st.divider()

        # ======================================================
        # RAW MODEL SCORES
        # ======================================================

        # ======================================================
        # MODEL VISUALIZATION
        # ======================================================

        with st.expander("📈 Model Confidence Charts", expanded=False):

            st.subheader("🤖 BERT Emotion Confidence")

            bert_df = pd.DataFrame({
                "Emotion": list(prediction["bert_scores"].keys()),
                "Confidence": [
                    score * 100
                for score in prediction["bert_scores"].values()
                ]
            })

            fig1 = px.bar(
                bert_df,
                x="Emotion",
                y="Confidence",
                text_auto=".1f",
                title="BERT Emotion Scores"
            )

            fig1.update_traces(texttemplate="%{text:.1f}%")

            st.plotly_chart(fig1, use_container_width=True)

            st.divider()

            st.subheader("🧠 BiLSTM Emotion Confidence")

            bilstm_df = pd.DataFrame({
                "Emotion": list(prediction["bilstm_scores"].keys()),
                "Confidence": [
                    score * 100
                    for score in prediction["bilstm_scores"].values()
                ]
            })

            fig2 = px.bar(
                bilstm_df,
                x="Emotion",
                y="Confidence",
                text="Confidence",
                title="BiLSTM Emotion Scores"
            )

            fig2.update_traces(texttemplate="%{text:.1f}%")

            st.plotly_chart(fig2, use_container_width=True)

            st.divider()

st.markdown(
"""
<center>

Developed using

🧠 BiLSTM |
🤖 BERT |
✨ Gemini AI |
🎓 Streamlit

</center>
""",
unsafe_allow_html=True
)