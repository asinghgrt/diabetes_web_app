# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 16:24:46 2024

@author: anura
"""

import numpy as np
import pickle
import streamlit as st

#creating fucntions:

loaded_model=pickle.load(open('C:/Users/anura/Desktop/Ml opss2/trained_model.sav','rb'))

def diabtes_prediction(input_data):
    
    input_numpy=np.asarray(input_data)
    input_reshape=input_numpy.reshape(1,-1)
    

    predit=loaded_model.predict(input_reshape)
    
    
    if(predit[0]==0):
      return 'Person is not diabetic'
    else:
      return 'person is diabteic'
      
def main():
    #giving a title
    st.title('Diabetes Prediction Web App')
    
    #giving input fro users:
       
    Pregnancies=st.text_input('Pregnancies')
    Glucose=st.text_input('Glucose')
    BloodPressure=st.text_input('BloodPressure,')
    SkinThickness=st.text_input('SkinThickness')
    Insulin=st.text_input('Insulin')
    BMI=st.text_input('BMI')
    DiabetesPedigreeFunction=st.text_input('DiabetesPedigreeFunction')
    Age=st.text_input('Age')
    
    #code for prediction
    diagnosis=''
    #creating a button
    if st.button('Diabetes Test Result'):
        diagnosis=diabtes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
    st.success(diagnosis)
    
    
if __name__ == '__main__':
    main()
    
    