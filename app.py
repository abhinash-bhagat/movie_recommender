import streamlit as st
import pandas as pd
import requests
import base64


# Styling Start
st.set_page_config(layout="wide")
st.markdown("""
<h1 style="color:#e51c13;
            font-family:Netflix Sans;
            font-size:35px;
            position: absolute;
            top:-100px;
            left:0px;">FILM-PEDIA
            </h1>
<button style="background-color:#e51c13;
            color:#fff;
            font-size:16px;
            border: 1px #ffffff solid;
            border-radius:8px;
            position: absolute;
            top:-80px;
            right:0px;"><a href='https://abhinashbhagat.com.np'>Contact</a></button>
<style>
    button a{
        text-decoration:none;
    }
</style>

""", unsafe_allow_html=True)
#Adding background Image to the Page using "Base64"
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    .css-uf99v8 {{
        background-color: #000000b0;
    }}
    .css-1avcm0n {{
        display:none;
    }}
    .css-nahz7x a {{ 
        color: #ffffff;
    }}
    .css-q8sbsg p{{
        font-size: 21px;
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('net.jpg')    
# Styling Ends

#Importing the Pickle Files
movies_list = pd.read_pickle('Models/movies.pkl')
movies_df = pd.DataFrame(movies_list, columns=['title','movie_id'])
similarity = pd.read_pickle('Models/similarity.pkl')

#Fetching Poster from TMDB API
def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8a915044e58eae6912fcb4bf025ec4ec'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500" + data['poster_path']

#Recommending the movies
def recommend(movie):
    movie_index = movies_df[movies_df['title']== movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]
    recommended_movies = []
    recommended_movies_posters = []
    for i in movie_list:
        movie_id = movies_df.iloc[i[0]].movie_id
        recommended_movies.append(movies_df.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters

# Main title of the Page
st.markdown("""
    <h1 style="font-size:3.8rem;margin-bottom:25px;">Movie Recommender System</h1>
""", unsafe_allow_html=True)

# Dropdowns
selected_movie = st.selectbox(
    "Select the movie to show recommendations based on that:",
    movies_df['title']
)

#Buttons
if st.button('Recommend'):
    names, posters = recommend(selected_movie)
    col1, col2, col3 = st.columns(3)

    with col1:
       st.text(names[0])
       st.image(posters[0])

    with col2:
       st.text(names[1])
       st.image(posters[1])

    with col3:
       st.text(names[2])
       st.image(posters[2])
    
    col4, col5, col6 = st.columns(3)

    with col4:
       st.text(names[3])
       st.image(posters[3])
    
    with col5:
       st.text(names[4])
       st.image(posters[4])