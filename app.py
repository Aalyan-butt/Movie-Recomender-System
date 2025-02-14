import streamlit as st
import pickle
import pandas as pd

movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)



st.title('Movie Recommendor System')

selected_movie_name = st.selectbox(
    "How would you like to be contacted?",
    movies['title'].values
)

