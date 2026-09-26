import streamlit as st

#simple button

st.button('Reset',type='primary')
if st.button('Say Hello'):
    st.write('Why Hello There')
else:
    st.write('Good By')

if st.button('Aloha',type='tertiary'):
    st.write('Coro')

# using Icon

left,middle,right=st.columns(3)

if left.button('Plain button',width='stretch'):
    st.markdown('You click on plain buttons')
if middle.button('Emoji Icon',icon='😃',width='stretch'):
    st.markdown('You click on emoji button')   
if right.button("Material button", icon=":material/mood:", width="stretch"):
    right.markdown("You clicked the Material button.")

