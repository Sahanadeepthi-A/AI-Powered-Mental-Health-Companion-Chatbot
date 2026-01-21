import os
os.environ["STREAMLIT_SERVER_HEADLESS"] = "true"

import streamlit as st
import matplotlib.pyplot as plt
import shap

from backend.auth import create_tables, signup, login
from backend.predict import predict_with_confidence, save_chat
from backend.risk_score import calculate_risk
from backend.analytics import get_user_chats
from backend.trend import detect_trend
from backend.coping_plan import coping_plan
from backend.explain import explain
from backend.safety import safety_filter
from chatbot.gemini_chat import generate_response

# ------------------ APP SETUP ------------------
create_tables()
st.set_page_config(page_title="Mental Health Companion")

if "user" not in st.session_state:
    st.session_state.user = None

# ------------------ AUTH ------------------
if st.session_state.user is None:
    st.title("Login / Signup")

    mode = st.selectbox("Select", ["Login", "Signup"])
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button(mode):
        if mode == "Signup":
            if signup(username, password):
                st.success("Account created. Please login.")
            else:
                st.error("Username already exists")
        else:
            user = login(username, password)
            if user:
                st.session_state.user = user
            else:
                st.error("Invalid credentials")

# ------------------ MAIN APP ------------------
else:
    st.title("🧠 AI Mental Health Companion")

    user_input = st.text_area("How are you feeling today?")

    if st.button("Analyze"):
        # ---------- SAFETY ----------
        if not safety_filter(user_input):
            st.error("We cannot assist with self-harm related content. Please seek professional help immediately.")
            st.stop()

        # ---------- ML PREDICTION ----------
        mood, confidence = predict_with_confidence(user_input)
        risk = calculate_risk(mood)

        save_chat(st.session_state.user[0], user_input, mood)

        st.subheader("Detected Emotional State")
        st.success(mood)
        st.write(f"Prediction confidence: {round(confidence * 100, 2)}%")
        st.progress(risk)

        from backend.intensity import emotion_intensity
        intensity = emotion_intensity(mood, confidence)
        st.subheader("🔥 Emotional Intensity Score")
        st.progress(intensity)
        st.caption("Scale: 0 (calm) to 100 (very intense)")


        # ---------- COPING PLAN ----------
        st.subheader("🧩 Personalized Coping Plan")
        for tip in coping_plan(mood):
            st.write("•", tip)

        # ---------- AI RESPONSE ----------
        st.subheader("AI Companion Response")
        st.write(
        generate_response(
                f"User feels {mood}. Respond empathetically.",
                mood=mood
                )
        )

        # ---------- SHAP EXPLANATION ----------
        st.subheader("🔍 Why this prediction?")
        shap_values, features = explain(user_input, mood)
        import matplotlib.pyplot as plt
        shap.plots.bar(shap_values, show=False)
        st.pyplot(plt.gcf())
        plt.clf()

        from backend.reports import get_user_report
        from backend.summary import summarize_mood

        st.subheader("📅 Weekly Mental Health Report")

        report_df = get_user_report(st.session_state.user[0], days=7)

        if not report_df.empty:
            st.write("Mood distribution (last 7 days):")
            st.bar_chart(report_df["mood"].value_counts())

            summary = summarize_mood(report_df)
            st.info(summary)
        else:
            st.info("Not enough data for weekly report yet.")

        from backend.trend import detect_trend
        trend = detect_trend(report_df)
        st.subheader("📈 Emotional Trend")
        st.success(trend)

        # ---------- ANALYTICS ----------
        df = get_user_chats(st.session_state.user[0])
        if not df.empty:
            st.subheader("📊 Mental Health Trend")
            st.info(detect_trend(df))
            df["mood"].value_counts().plot(kind="bar")
            st.pyplot(plt.gcf())
            
        
