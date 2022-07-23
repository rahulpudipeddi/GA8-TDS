import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
import pickle

st.write("""
# Find out If Number is Odd or Even
""")
#Get Input




number = st.number_input("Number",min_value=-999999999,max_value=999999999)



#Preprocessing



#Model Inferencing

prediction = number%2


st.subheader('Result')
if prediction == 0:
    st.write('Even')
else:
    st.write('Odd')
