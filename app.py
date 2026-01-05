import pickle

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

import numpy as np

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.title("ML Model Deployment with Streamlit 🎯")

st.write("Enter input values below:")

# Example input fields
feature1 = st.number_input("Feature 1")
feature2 = st.number_input("Feature 2")
feature3 = st.number_input("Feature 3")

if st.button("Predict"):
    input_data = np.array([[feature1, feature2, feature3]])
    prediction = model.predict(input_data)
    st.success(f"Prediction: {prediction[0]}")


