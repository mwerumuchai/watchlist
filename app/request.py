# from app import app
import urllib.request,json
# from .models import movie
from .models import Movie

# Movie = movie.Movie

# Getting API key
#api_key = app.config["MOVIE_API_KEY"]
api_key = None

# Getting the movie base url
#base_url = app.config["MOVIE_API_BASE_URL"]
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config["MOVIE_API_KEY"]
    base_url = app.config["MOVIE_API_BASE_URL"]



# Putting movies in categories e.g upcoming,popular, now showing

def get_movies(category):
    '''
    Function that gets the JSON response to our url requests
    '''
    get_movies_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_movies_url) as url:
        get_movies_data = url.read()
        get_movies_response = json.loads(get_movies_data)

        movie_results = None

        if get_movies_response['results']:
            movie_results_list = get_movies_response['results']
            movie_results = process_results(movie_results_list)

    return movie_results


# Takes one to another route where there is more information about the specific movie
def get_movie(id):
    get_movie_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_movie_details_url) as url:
        movie_details_data = url.read()
        movie_details_response = json.loads(movie_details_data)

        movie_object = None
        if movie_details_response:
            id = movie_details_response ['id']
            title = movie_details_response ['original_title']
            overview = movie_details_response ['overview']
            poster = movie_details_response ['poster_path']
            vote_average = movie_details_response ['vote_average']
            vote_count = movie_details_response ['vote_count']

            movie_object = Movie(id,title,overview,poster,vote_average,vote_count)


    return movie_object


# Movie list
def process_results(movie_list):
    '''
    function that processes the movie result and transform them to a list of objects

    Args:
        movie_list: A list of dictionaries that contaun movie details

    Returns:
        movie_results: a list of movie objects

    '''


    movie_results = []

    for movie_item in movie_list:
        id = movie_item.get('id')
        title = movie_item.get('original_title')
        overview = movie_item.get('overview')
        poster = movie_item.get('poster_path')
        vote_average = movie_item.get('vote_average')
        vote_count = movie_item.get('vote_count')

        if poster:
            movie_object = Movie(id,title,overview,poster,vote_average,vote_count)

            movie_results.append(movie_object)

    return movie_results

# Search a movie
def search_movie(movie_name):
    search_movie_url = "https://api.themoviedb.org/3/search/movie?api_key={}&query={}".format(api_key,movie_name)

    with urllib.request.urlopen(search_movie_url) as url:
        search_movie_data = url.read()
        search_movie_response = json.loads(search_movie_data)

        search_movie_results = None

        if search_movie_response["results"]:
            search_movie_list = search_movie_response["results"]
            search_movie_results = process_results(search_movie_list)

    return search_movie_results
