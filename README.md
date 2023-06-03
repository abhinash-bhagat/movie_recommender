## Link to Webapp: https://abhinash-bhagat-movie-recommender-app-vb9cbh.streamlit.app/
# Movie Recommender System

This is a movie recommender system built with Streamlit. It allows users to select a movie and get recommendations based on that selection.

## Getting Started

To get started with the movie recommender system, follow these steps:

1. Clone the repository:

   ```shell
   https://github.com/abhinash-bhagat/movie_recommender.git
   
2. Install the required dependencies:

   ```shell
   pip install -r requirements.txt
   
3. Run the Streamlit app:
   ```shell
   streamlit run app.py
   
4. Most Probably it'll automatically open the localhost page but if not open your web browser and navigate to http://localhost:8501 to        access the movie recommender system.

# Features
Select a movie from the dropdown menu to see recommendations based on that movie.
The recommendations include similar movies along with their posters.

# Customization
## Background Image
You can customize the background image of the app by replacing the net.jpg file in the root directory with your desired image. Make sure the file is named net.jpg and has the appropriate dimensions.

# Styling
You can modify the styling of the app by editing the HTML and CSS code within the app.py file. There are specific sections in the code where you can make changes to the app's title, button styles, and more.

# Data Sources
The movie data and similarity matrix used for the recommender system are stored in pickle files located in the Models/ directory. These files are loaded into the app during runtime.

# Acknowledgements
The movie data is obtained from TMDB API.
The movie posters are fetched from the TMDB API based on the movie IDs.
