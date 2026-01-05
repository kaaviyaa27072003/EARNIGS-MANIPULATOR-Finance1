import streamlit as st
import numpy as np

st.title("ML App Demo with Streamlit 🎯")

st.write("Enter input values below:")

feature1 = st.number_input("Feature 1")
feature2 = st.number_input("Feature 2")
feature3 = st.number_input("Feature 3")

if st.button("Predict"):
    st.success("This is a demo — no real ML model is loaded 🙂")








