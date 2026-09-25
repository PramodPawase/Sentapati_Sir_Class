import streamlit as st
import pandas as pd
from numpy.random import default_rng as rng
import altair as alt
import matplotlib.pyplot as plt
import numpy as np


st.title('this write function')

#header
st.header('This is the Write Function..')

#sidebar de
st.sidebar.title('this is Write function side bar')

#header
st.sidebar.header('Sidebar header')

st.sidebar.write('hello,*World!*,:sunglasses:')

#Designing main body
#data frame
df=pd.DataFrame(
    {
        'first_name':[1,2,3,3],
        'Second_name':[12,23,44,22],
    }
)
#data frame added in the st
st.dataframe(df)

st.write('1+1 =',2)
st.write('Below is DataFrame:',df,'Above is dataframe')


st.write('--------------------------------------------------')
df = pd.DataFrame(rng(0).standard_normal((200, 3)), columns=["a", "b", "c"])
chart = (
    alt.Chart(df)
    .mark_circle()
    .encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
)
st.write(chart)



# Draw a title and some text to the app:
'''
# This is the document title

This is some _markdown_.
'''

import pandas as pd
df = pd.DataFrame({'col1': [1,2,3]})
df  # 👈 Draw the dataframe

x = 10
'x', x  # 👈 Draw the string 'x' and then the value of x

# Also works with most supported chart types


arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

fig  # 👈 Draw a Matplotlib chart