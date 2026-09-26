import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


st.title('Streamlit practice')

st.header('Testing to the streamlit wedgets')

#sidebar
st.sidebar.header('This Setting Part')
name=st.sidebar.text_input('Enter User Name?','Pramod')

age=st.sidebar.slider('Select Your Age?',0,25,50)

favorite_color=st.sidebar.selectbox('Select Favorite Color?',['Pink','Purpal','Yellow'])

#designing left side panal

st.header(f'Login User Name? {name}')

st.write(f'Your age is {age} and your favorite Color is {favorite_color}')

#display subheader

#display the random data

df=pd.DataFrame(
    np.random.rand(10,5),
    columns=('col %d' % i for i in range(5)) 
)

#display Data frame
st.dataframe(df)

#check box to show/hide content

if st.checkbox('Show Row Data'):
    st.subheader('Row Data')
    st.write(df)

# button to tigger action

if st.button('Say Hello'):
    st.write(f'Hello There..{name}')
else:
    st.write('Good By!..')        