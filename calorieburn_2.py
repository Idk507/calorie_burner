import streamlit as st
import pickle
import pandas as pd 
import numpy as np

model = pickle.load(open('model.pkl','rb'))
st.write("calories burn app")

gender = st.selectbox("Select gender",("male","female"))

if gender == "male":
    g = 0
else :
    g =1


age = st.number_input("Enter age")

height = st.number_input("Enter height")

weight = st.number_input("Enter weight")

duration = st.number_input("Enter workout duration ")

heartrate = st.number_input("enter heartrate :")       
bodytemp = st.number_input("enter body temperature")

prediction = model.predict(pd.DataFrame(columns = ['Gender','Age','Height','Weight','Duration','Heart_Rate','Body_temp'],
               data = np.array([g,age,height,weight,duration,heartrate,bodytemp]).reshape(1,7)))

if st.button("Predict"):
    st.write("Calorie burned")
    st.success(prediction)