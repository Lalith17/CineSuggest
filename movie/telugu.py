import pandas as pd
import streamlit as st
import datetime
movies_data = pd.read_csv("TeluguMovies_dataset.csv")
st.header('Movie Recommender System')

# Prompt the user for their favorite genre
favorite_genre = st.text_input('Enter your favorite genre: ')

# Prompt the user for how many years back movies they want to watch
years_back = st.number_input('From which year onwards? ',0,3000,None)

# Prompt the user for the minimum vote average
min_vote_average = st.number_input('Enter the minimum vote average: ',0,10,None)
# Filter the DataFrame based on the user's input
choices=movies_data[
         (movies_data['Genre'].str.contains(favorite_genre, case=False, regex=True))
         &(movies_data['Year']>=years_back)
         &(movies_data['Rating'] >= min_vote_average)
   ]
sorted_movies = choices.sort_values(by='Rating', ascending=False)
sorted_movies=sorted_movies[['Movie','Overview']]
button=st.button("Search")
if button:
    st.dataframe(sorted_movies.head())
