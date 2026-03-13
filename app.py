import streamlit as st
import pandas as pd
import joblib
import time
import random

# Load trained model
model = joblib.load("iq_model.pkl")

st.title("🧠 Human Intelligence Predictor")

st.write("Answer the following questions")

# Timer state
if "start_time" not in st.session_state:
    st.session_state.start_time = None

# Function to start timer
def start_timer():
    if st.session_state.start_time is None:
        st.session_state.start_time = time.time()

# Questions
q1 = st.selectbox(
    "Q1: What comes next? 2,4,6,8",
    ["Select option", "10", "12", "14", "16"],
    on_change=start_timer
)

q2 = st.selectbox(
    "Q2: 5 + 7 = ?",
    ["Select option", "10", "11", "12", "13"],
    on_change=start_timer
)

q3 = st.selectbox(
    "Q3: Which is the largest?",
    ["Select option", "Dog", "Elephant", "Cat", "Mouse"],
    on_change=start_timer
)

q4 = st.selectbox(
    "Q4: What is 9 × 3 ?",
    ["Select option", "27", "21", "24", "18"],
    on_change=start_timer
)

q5 = st.selectbox(
    "Q5: Which planet do we live on?",
    ["Select option", "Mars", "Earth", "Venus", "Jupiter"],
    on_change=start_timer
)

# Stress level
stress = st.slider("Stress Level (1 = low, 10 = high)", 1, 10)

# Predict button
if st.button("Predict Intelligence"):

    if "Select option" in [q1, q2, q3, q4, q5]:
        st.warning("Please answer all questions")

    else:

        # Calculate time taken
        if st.session_state.start_time is not None:
            time_taken = int(time.time() - st.session_state.start_time)
        else:
            time_taken = 0

        score = 0

        if q1 == "10":
            score += 1
        if q2 == "12":
            score += 1
        if q3 == "Elephant":
            score += 1
        if q4 == "27":
            score += 1
        if q5 == "Earth":
            score += 1

        # Prepare input for model
        input_data = pd.DataFrame(
            [[score, stress, time_taken]],
            columns=["Score", "Stress", "Time"]
        )

        prediction = model.predict(input_data)

        st.subheader("Result")

        st.success(f"Predicted Intelligence: {prediction[0]}")

        advice = [
            "Take deep breaths to reduce stress.",
            "Try meditation for 5 minutes.",
            "Go for a short walk.",
            "Listen to calming music.",
            "Drink water and relax your mind."
        ]

        st.info(random.choice(advice))

        st.write("Score:", score, "/5")
        st.write("Time Taken:", time_taken, "seconds")

# Restart test button
if st.button("Restart Test"):
    st.session_state.start_time = None
    st.experimental_rerun()
