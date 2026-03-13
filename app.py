import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import time

# Load dataset
data = pd.read_csv("dataset.csv")

X = data[["Q1","Q2","Q3","Q4","Q5","Time"]]
y = data["Intelligence"]

# Train model
model = DecisionTreeClassifier()
model.fit(X,y)

st.title("🧠 AI Intelligence Predictor")

st.write("Answer the questions below")

start_time = time.time()

q1 = st.radio("1. What comes next? 2,4,8,16 ?", ["18","24","32","30"])
q2 = st.radio("2. 15 × 4 + 10 ?", ["70","60","50","80"])
q3 = st.radio("3. What was the third digit of 48291 ?", ["4","8","2","9"])
q4 = st.radio("4. Which number is largest?", ["12","25","19","31"])
q5 = st.radio("5. What is 9 × 9 ?", ["72","81","99","69"])

if st.button("Predict Intelligence"):

    end_time = time.time()
    time_taken = int(end_time-start_time)

    a1 = 1 if q1=="32" else 0
    a2 = 1 if q2=="70" else 0
    a3 = 1 if q3=="2" else 0
    a4 = 1 if q4=="31" else 0
    a5 = 1 if q5=="81" else 0

    prediction = model.predict([[a1,a2,a3,a4,a5,time_taken]])

    st.write("Time Taken:",time_taken,"seconds")
    st.success("Predicted Intelligence Level: "+prediction[0])
