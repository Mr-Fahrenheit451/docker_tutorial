import streamlit as st

st.title("Hi from streamlit inside docker")

def submit_name():
    st.session_state.submitted = True

st.text_input(
    "Please enter your name:",
    key="name",
    on_change=submit_name
)

if st.session_state.get("submitted", False):
    st.write(f"My name is: {st.session_state.name}")