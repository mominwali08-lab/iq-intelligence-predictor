import streamlit as st
import pandas as pd
import joblib
import time
import random

# Load trained model
model = joblib.load("iq_model.pkl")

st.title("🧠 Human Intelligence Predictor")

st.write("Answer the following questions")

start_time = time.time()

# Questions
q1 = st.selectbox(
    "Q1: What comes next? 2,4,6,8",
    ["Select option", "10", "12", "14", "16"]
)

q2 = st.selectbox(
    "Q2: 5 + 7 = ?",
    ["Select option", "10", "11", "12", "13"]
)

q3 = st.selectbox(
    "Q3: Which is the largest?",
    ["Select option", "Dog", "Elephant", "Cat", "Mouse"]
)

q4 = st.selectbox(
    "Q4: What is 9 × 3 ?",
    ["Select option", "27", "21", "24", "18"]
)

q5 = st.selectbox(
    "Q5: Which planet do we live on?",
    ["Select option", "Mars", "Earth", "Venus", "Jupiter"]
)

stress = st.slider("Stress Level (1 = low, 10 = high)",1,10)

if st.button("Predict Intelligence"):

    if "Select option" in [q1,q2,q3,q4,q5]:
        st.warning("Please answer all questions")
    else:

        end_time = time.time()
        time_taken = int(end_time - start_time)

        score = 0

        if q1 == "10":
            score +=1
        if q2 == "12":
            score +=1
        if q3 == "Elephant":
            score +=1
        if q4 == "27":
            score +=1
        if q5 == "Earth":
            score +=1

        input_data = pd.DataFrame([[score,stress,time_taken]],
            columns=["Score","Stress","Time"])

        prediction = model.predict(input_data)

        st.subheader("Result")
        st.success(f"Predicted Intelligence: {prediction[0]}")

        advice = [
            "Take deep breaths to reduce stress.",
            "Try meditation for 5 minutes.",
            "Go for a short walk.",
            "Listen to relaxing music.",
            "Drink water and relax your mind."
        ]

        st.info(random.choice(advice))

        st.write("Score:",score,"/5")
        st.write("Time Taken:",time_taken,"seconds")