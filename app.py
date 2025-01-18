import streamlit as st

st.title('Movie Recommendor System')

option = st.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone"),
)