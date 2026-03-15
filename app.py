import streamlit as st
import pandas as pd
import joblib

model = joblib.load("model.pkl")

st.title("Medical Cost Prediction")

age = st.number_input("Age")
sex = st.selectbox("Sex", ["male","female"])
bmi = st.number_input("BMI")
children = st.number_input("Children",0,5)
smoker = st.selectbox("Smoker",["yes","no"])
region = st.selectbox("Region",
["southwest","southeast","northwest","northeast"])

if st.button("Predict Cost"):

    data = pd.DataFrame({
        "age":[age],
        "sex":[sex],
        "bmi":[bmi],
        "children":[children],
        "smoker":[smoker],
        "region":[region]
    })

    prediction = model.predict(data)

    st.success(f"Estimated Medical Cost: ${prediction[0]:.2f}")