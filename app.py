import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import random

# Load dataset
data = pd.read_csv("dataset.csv")

X = data[["Q1","Q2","Q3","Q4","Q5","Stress"]]
y = data["Intelligence"]

# Train model
model = DecisionTreeClassifier()
model.fit(X,y)

st.title("🧠 AI Intelligence Predictor")

st.write("Answer all questions")

q1 = st.radio("1. What comes next? 2,4,8,16 ?", 
              ["Select an option","18","24","32","30"], index=0)

q2 = st.radio("2. 15 × 4 + 10 ?", 
              ["Select an option","70","60","50","80"], index=0)

q3 = st.radio("3. What was the third digit of 48291 ?", 
              ["Select an option","4","8","2","9"], index=0)

q4 = st.radio("4. Which number is largest?", 
              ["Select an option","12","25","19","31"], index=0)

q5 = st.radio("5. What is 9 × 9 ?", 
              ["Select an option","72","81","99","69"], index=0)

stress = st.slider("Select Your Stress Level",1,10)

if st.button("Predict Intelligence"):

    if "Select an option" in [q1,q2,q3,q4,q5]:
        st.warning("Please answer all questions")
    else:

        a1 = 1 if q1=="32" else 0
        a2 = 1 if q2=="70" else 0
        a3 = 1 if q3=="2" else 0
        a4 = 1 if q4=="31" else 0
        a5 = 1 if q5=="81" else 0

        prediction = model.predict([[a1,a2,a3,a4,a5,stress]])

        st.success("Predicted Intelligence Level: "+prediction[0])

        tips = [
            "Take a 5 minute deep breathing break.",
            "Go for a short walk to refresh your mind.",
            "Drink water and relax your eyes.",
            "Listen to calm music for a few minutes.",
            "Try meditation for 3 minutes.",
            "Stretch your body and relax your shoulders.",
            "Step away from screens for a short break.",
            "Write your thoughts in a notebook."
        ]

        st.info("Stress Advice: " + random.choice(tips))