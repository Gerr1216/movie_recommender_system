import streamlit as st
import pickle
import pandas as pd
import requests

# streamlit run C:\Users\USER\DeepLearn2024\movies-recommender-system\pythonProject\.venv\app.py

# API URL
API_KEY = "eb0494dc37538201b4a6e860cfbef22e"
API_URL = "https://api.themoviedb.org/3/movie/{}?api_key={}&language=en-US"

# Function to fetch movie poster
def fetch_poster(movie_id):
    response = requests.get(API_URL.format(movie_id, API_KEY))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommended(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters

# Load movies data and similarity matrix
movies_dict = pickle.load(open('C:\\Users\\USER\\DeepLearn2024\\movies-recommender-system\\pythonProject\\.venv\\movies_dict.pkl', 'rb'))
similarity = pickle.load(open('C:\\Users\\USER\\DeepLearn2024\\movies-recommender-system\\pythonProject\\.venv\\similarity.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

# Streamlit UI
custom_css = """
<style>
    .stApp {
        background-color: #031B28;
    }
    .custom-button {
        background-color: purple;
        color: white;
        border: none;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 12px;
    }
    h1,p, .custom-text {
        color: #DBA858;
        padding: 10px;
        border-radius: 5px;
        text-align: center;
        font-family: arial, helvetica, serif;
        white-space: nowrap;
    }
    .custom-text-scrollable {
        color: #DBA858;
        text-align: center;
        font-family: arial, helvetica, serif;
        white-space: nowrap;
        overflow-x: auto;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Enter the movie that you want',
    movies['title'].values
)

if st.markdown('<button class="custom-button">Recommend</button>', unsafe_allow_html=True):
    names, posters = recommended(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.markdown(f'<p class="custom-text-scrollable">{names[0]}</p>', unsafe_allow_html=True)
        st.image(posters[0])
    with col2:
        st.markdown(f'<p class="custom-text-scrollable">{names[1]}</p>', unsafe_allow_html=True)
        st.image(posters[1])
    with col3:
        st.markdown(f'<p class="custom-text-scrollable">{names[2]}</p>', unsafe_allow_html=True)
        st.image(posters[2])
    with col4:
        st.markdown(f'<p class="custom-text-scrollable">{names[3]}</p>', unsafe_allow_html=True)
        st.image(posters[3])
    with col5:
        st.markdown(f'<p class="custom-text-scrollable">{names[4]}</p>', unsafe_allow_html=True)
        st.image(posters[4])