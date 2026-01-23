import streamlit as st

st.title("Hi from streamlit inside docker")
st.write("looks like this works properly.")
st.write("What happens if you change the file?")

st.text("Please enter your name:")
st.text_input("Name")