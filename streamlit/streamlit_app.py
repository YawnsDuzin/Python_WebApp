import streamlit as st


st.header('st.button')

# st.write('Hello world')

if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.button('Say Goodbye')
    st.write('Goodbye')
    
import pandas as pd

df = pd.DataFrame(
    [
        {"command": "st.selectbox", "rating": 4, "is_widget": True},
        {"command": "st.balloons", "rating": 5, "is_widget": False},
        {"command": "st.time_input", "rating": 3, "is_widget": True},
    ]
)

st.dataframe(df, use_container_width=True)
