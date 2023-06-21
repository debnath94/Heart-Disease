import os
import streamlit as st
import numpy as np
import pickle
from pickle import load
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression




scaler = load(open('standard_scaler.pkl', 'rb'))
lr = load(open('lr_model.pkl', 'rb'))



st.title(":red[Heart Disease Prediction]")


age = st.slider(":blue[Select Your Age]",21, 80, 30 )

sex = st.radio(":blue[Select Your Gender]", ["Male", "Female"])
if sex == "Male":
    sex = 1
else:
    sex = 0


cp = st.radio(":blue[Select Chest Pain Type]",["Stable", "Unstable", "Microvascular", "Variant"])
if cp == "Stable":
    cp=1
elif cp == "Unstable":
    cp = 2
elif cp == "Microvascular":
    cp = 3
elif cp == "Variant":
    cp = 4


trestbps = st.number_input(":Select your Resting Blood Pressure", value=0)


chol = st.number_input("Select Your Cholestrol Level", value=0)


fbs = st.radio(":blue[Fasting Blood Sugar]", ["Yes", "No"])
if fbs == "Yes":
    fbs = 1
else:
    fbs = 0


restecg = st.radio(":blue[Select Resting ECG Type]", ["Normal", "Abnormal", "High"])
if restecg == "Normal":
    restecg = 0
elif restecg == "Abnormal":
    restecg = 1
elif restecg == "High":
    restecg = 2


thalach = st. number_input("Select Your Max Heart Rate", value = 0)

exang = st.radio(":blue[Select Excercise Induced Angina]", ["Yes", "No"])
if exang == "Yes":
    exang = 1
else:
    exang = 0


oldpeak = st.number_input("Select Your Depression Level", value=0)


slope = st.radio(":blue[Select the Slope Type]", ["Upsloping", "Flat","Downsloping"])
if slope == "Upsloping":
    slope = 1
elif slope == "Flat":
    slope = 2
elif slope == "Downsloping":
    slope = 3


ca = st.number_input("[Select the Major Vessels]", value=0)


thal = st.radio(":blue[Select The Thalassemia Level]", ["Normal", "Reversable Defect", "Fixed Defect"])
if thal == "Normal":
    thal = 3
elif thal == "Reversable Defect":
    thal = 7
elif thal == "Fixed Defect":
    thal = 6




if st.button('Predict'):
    query_point = np.array([age, sex,cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal])
    query_point = query_point.reshape(1, -1)
    query_point_transformed = scaler.transform(query_point)
    prediction = lr.predict(query_point_transformed)
    if prediction == 0:
        st.success("You don't have a Heart Disease 😊!")
        st.image('happy_heart.jfif')
    else:
        st.error("You have a Heart Disease 😥!")
        st.image('damaged_heart.jfif')
        

    
    # prediction=pipe.predict(df_userinput)[0]
    # st.header(prediction)
    # st.write("of disease is detected")


# age = float(input('Enter the age : '))
# sex = float(input('Enter the sex : '))
# cp = float(input('Enter the cp : '))
# trestbps = float(input('Enter the trestbps : '))
# chol = float(input('Enter the chol : '))
# fbs = float(input('Enter the fbs : '))
# restecg = float(input('Enter the restecg : '))
# thalach = float(input('Enter the thalach : '))
# exang = float(input('Enter the exang : '))
# oldpeak = float(input('Enter the oldpeak : '))
# slope = float(input('Enter the slope : '))
# ca = float(input('Enter the ca : '))
# thal = float(input('Enter the thal : '))
