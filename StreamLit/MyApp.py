import streamlit as st

st.title("My First Streamlit App Created by Praveen")

st.write("welcome! This app calculate the square of a number")

st.header("Select a Number")
number = st.slider("Pick a numebr",0,100,25)

st.subheader("Result")
squared_number = number * number

st.write(f"The square of **{number}** is **{squared_number}**.")
