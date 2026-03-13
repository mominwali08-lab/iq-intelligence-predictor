import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset
data = pd.read_csv("dataset.csv")

# Create Score column
data["Score"] = data["Q1"] + data["Q2"] + data["Q3"] + data["Q4"] + data["Q5"]

# Features and target
X = data[["Score", "Stress", "Time"]]
y = data["Intelligence"]

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Save model
joblib.dump(model, "iq_model.pkl")

print("Model trained successfully and saved as iq_model.pkl")