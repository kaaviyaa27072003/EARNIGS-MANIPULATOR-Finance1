import pickle
from pathlib import Path
import numpy as np
import streamlit as st

model_path = Path(__file__).parent / "model.pkl"

with open(model_path, "rb") as f:
    model = pickle.load(f)

st.title("ML Model Deployment with Streamlit 🎯")
st.write("Enter input values below:")

feature1 = st.number_input("Feature 1")
feature2 = st.number_input("Feature 2")
feature3 = st.number_input("Feature 3")

if st.button("Predict"):
    input_data = np.array([[feature1, feature2, feature3]])
    prediction = model.predict(input_data)
    st.success(f"Prediction: {prediction[0]}")





