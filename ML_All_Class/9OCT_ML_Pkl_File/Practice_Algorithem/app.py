import pandas as pd
import numpy as np
import pickle
import streamlit as st


#loading the pickle file

model = pickle.load(open(r'C:\Users\Pramod\OneDrive\AI Python\Senapati Sir\Class Document\ML_All_Class\9OCT_ML_Pkl_File\Practice_Algorithem\linear_regression_model.pkl','rb'))

#set title

st.title('Salary Prediction app by Pramod')

#add breef description
st.write('This is app predction salary base on years of exprerience uisng a simple linear regression model.')



