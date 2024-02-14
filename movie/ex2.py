import pandas as pd
import streamlit as st
import datetime
movies_data = pd.read_csv("movies.csv")
st.header('Movie Recommender System')

movies_data['release_date'] = pd.to_datetime(movies_data['release_date'])
movies_data['release_year'] = datetime.datetime.now().year - movies_data['release_date'].dt.year

movies_data = movies_data[movies_data['vote_count'] >= 100]
movies_data = movies_data[movies_data['vote_average'] >= 5]

# Prompt the user for their favorite genre
favorite_genre = st.text_input('Enter your favorite genre: ')

# Prompt the user for how many years back movies they want to watch
years_back = st.number_input('How many years back do you want to watch movies from? ',0,100,None)

# Prompt the user for their favorite cast member
favorite_cast =  st.text_input('Enter your favorite cast member: ')

# Prompt the user for their favorite director
favorite_director =  st.text_input('Enter your favorite director: ')

# Prompt the user for the minimum vote average
min_vote_average = st.number_input('Enter the minimum vote average: ',0,10,None)
# Filter the DataFrame based on the user's input
choices=movies_data[
        (movies_data['cast'].str.contains(favorite_cast, case=False, regex=True))
        &(movies_data['genres'].str.contains(favorite_genre, case=False, regex=True))
         &(movies_data['release_year']<=years_back)
         &(movies_data['vote_average'] >= min_vote_average)
         |(movies_data['director'].str.contains(favorite_director, case=False, regex=True))
   ]
sorted_movies = choices.sort_values(by='popularity', ascending=False)
sorted_movies=sorted_movies[['original_title','homepage']]
button=st.button("Search")
if button:
    st.dataframe(sorted_movies.head())
