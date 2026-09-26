import streamlit as st
import pandas as pd
import numpy as np
st.title('This is first app for using the python')

st.sidebar.header('show the balloon')
st.sidebar.markdown("""This is play ground this is for the fun
          ** their is the rainbow [so much] fun for all doc..
          we prepared five example for you to get started new course using streamlit """)

if st.sidebar.button('fire balloons'):
    st.sidebar.balloons()

#displaying the chart using streamlite          
st.subheader('Below are the Chart')

st.sidebar.header('Chart1')
st.write("Streamlit supports a wide range of data visualizations, including [Plotly, Altair, and Bokeh charts](https://docs.streamlit.io/develop/api-reference/charts). 📊 And with over 20 input widgets, you can easily make your data interactive!") 

all_users=['Pramod','Sai','Kiran']

with st.container(border=True):
    users=st.multiselect("Users",all_users,default=all_users)
    rolling_average=st.toggle('Rolling Average')

np.random.seed(42)
data = pd.DataFrame(np.random.randn(20, len(users)), columns=users)
if rolling_average:
    data = data.rolling(7).mean().dropna()    

np.random.seed(42)

data=pd.DataFrame(np.random.randn(20,len(users)),columns=users)
if rolling_average:
    data=data.rolling

tab1,tab2=st.tabs(['Charts','DataFrame'])    
tab1.line_chart(data,height=200)
tab2.dataframe(data, height=250, use_container_width=True)

