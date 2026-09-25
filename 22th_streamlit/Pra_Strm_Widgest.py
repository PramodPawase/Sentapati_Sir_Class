import streamlit as st
import pandas as pd
import numpy as np


st.title('Using  Pandas and Numpy in streamlit')

st.write('this is simple app to demonstrate showing basic functionalities using streamlit')

st.sidebar.header('user input header')

user_name=st.sidebar.text_input('What ia your name?','Pramod Pawase')

age=st.sidebar.slider('select your age',0,25,45,100)

favorite_color=st.sidebar.selectbox('What is your favorite color',['Blue','Red','Pink'])

st.header(f"Welcome ,{user_name}!")

st.write(f"your age is {age} and your favorite color is {favorite_color}.")

st.subheader('Here is some randome data')

#create some sampal data frame

df=pd.DataFrame(
    np.random.rand(10,5),
    columns=('col %d' % i for i in range(5))
)
st.dataframe(df)

#checkbox hide/show content
if st.checkbox('Show the data'):
    st. subheader('Row Data')
    st.write(df)

#trigger to action 

if st.button('say hello'):
    st.write('Hello there!')
else:
    st.write('Goodby')

    



