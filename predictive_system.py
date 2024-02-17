# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pickle
#loading a saved model
loaded_model=pickle.load(open('C:/Users/anura/Desktop/Ml opss2/trained_model.sav','rb'))

input=(5,166,72,19,175,25.8,0.587,51)
input_numpy=np.asarray(input)
input_reshape=input_numpy.reshape(1,-1)
#standardize the input data

predit=loaded_model.predict(input_reshape)
print(predit)
if(predit[0]==0):
  print("Person is not diabetic")
else:
  print("person ias diabteic")