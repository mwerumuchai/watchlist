from flask import render_template
from app import app
from .request import get_movies
from .request import get_movies,get_movie
# views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    #getting popular movie
    popular_movies = get_movies('popular')
    upcoming_movie = get_movies('upcoming')
    now_showing_movie = get_movies('now_playing')
    title = "Home - Welcome to the Best Online Movie Review Website"
    return render_template('index.html', title = title, popular = popular_movies, upcoming = upcoming_movie, now_showing =now_showing_movie)

@app.route('/movie/<int:id>')
def movie(id):
    '''
    View root page function that returns the index page and its data
    '''
    movie = get_movie(id)
    title = f" { movie.title }"
    return render_template('movie.html', title = title, movie = movie)
