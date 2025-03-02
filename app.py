import pickle
import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Fetch API key from .env
TMDB_API_KEY = os.getenv("TMDB_API_KEY")

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"

    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {TMDB_API_KEY}"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return "https://via.placeholder.com/500"  # Fallback image

    data = response.json()
    
    poster_path = data.get('poster_path', None)
    if not poster_path:
        return "https://via.placeholder.com/500"  # Fallback image

    full_path = f"https://image.tmdb.org/t/p/w500/{poster_path}"
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters

st.header('🎬 Movie Recommender System Using Machine Learning')

movies = pickle.load(open('artifacts/movie_list.pkl', 'rb'))
similarity = pickle.load(open('artifacts/similarity.pkl', 'rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    for idx, col in enumerate([col1, col2, col3, col4, col5]):
        with col:
            st.text(recommended_movie_names[idx])
            st.image(recommended_movie_posters[idx])
