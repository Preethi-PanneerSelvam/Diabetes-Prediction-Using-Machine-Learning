import numpy as np
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
import streamlit as st
import warnings
warnings.filterwarnings('ignore', category=UserWarning)

# read dataset
df = pd.read_csv("diabetes_prediction_dataset.csv")

# Preprocessing
enc = OrdinalEncoder()
df["smoking_history"] = enc.fit_transform(df[["smoking_history"]])
df["gender"] = enc.fit_transform(df[["gender"]])

# defining dependent and independent variables
x = df.drop("diabetes", axis=1)
y = df["diabetes"]

# training and testing the data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

# Random Forest
model = RandomForestClassifier().fit(x_train, y_train)

# Streamlit setup
st.set_page_config(page_title="Diabetes Prediction App", layout="wide")
st.markdown('<h1 style="text-align: center;">Diabetes Prediction</h1>', unsafe_allow_html=True)

# Setting up the columns
col1, col2 = st.columns(2, gap="large")

# User input
with col1:
    smoking_history = st.selectbox("Smoking History", ("Never", "Current", "Former", "Ever", "Not current", "No Info"))
    smoking_history_value = {"Never": 0, "Current": 1, "Former": 2, "Ever": 3, "Not current": 4, "No Info": 5}
    bmi = st.text_input(label="BMI")
    hba1c_level = st.text_input(label="HbA1c Level")
    blood_glucose_level = st.text_input(label="Blood Glucose Level")

# User input
with col2:
    gender = st.selectbox("Gender", ("Male", "Female", "Other"))
    gender_value = {"Female": 0, "Male": 1}
    age = st.text_input(label="Age")
    hypertension = st.selectbox("Hypertension", ("Yes", "No"))
    hypertension_value = {"No": 0, "Yes": 1}
    heart_disease = st.selectbox("Heart Disease", ("Yes", "No"))
    heart_disease_value = {"No": 0, "Yes": 1}
    st.write(" ")
    st.write(" ")
    col1, col2 = st.columns([0.438, 0.562])
    with col1:
        submit = st.button("Predict")

st.write(" ")

if submit:
    try:
        user_data = np.array([[
            float(gender_value[gender]), float(age), smoking_history_value[smoking_history],
            hypertension_value[hypertension], heart_disease_value[heart_disease], float(bmi),
            float(hba1c_level), float(blood_glucose_level)
        ]])
        test_result = model.predict(user_data)
        if test_result[0] == 0:
            col1, col2,col3 = st.columns([0.33,0.30,0.35])
            with col1:
                st.success(" Diabetic : Negative")
        else:
            col1, col2,col3 = st.columns([0.215, 0.57, 0.215])
            with col1:
                st.error("Diabetic :Positive  Please consult your doctor")
    except ValueError:
        st.error("Please enter valid input")
