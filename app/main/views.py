from flask import render_template,request,redirect,url_for,abort
from . import main
from ..request import get_movies,get_movie,search_movie
from ..models import Review,User
from .forms import ReviewForm,UpdateProfile
from flask_login import login_required
from .. import db,photos

# views
# @app.route('/')
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    #getting popular movie
    popular_movies = get_movies('popular')
    upcoming_movie = get_movies('upcoming')
    now_showing_movie = get_movies('now_playing')

    title = "Home - Welcome to the Best Online Movie Review Website"

    search_movie = request.args.get('movie_query')

    if search_movie:
        return redirect(url_for('.search',movie_name = search_movie))
    else:
        return render_template('index.html', title = title, popular = popular_movies, upcoming = upcoming_movie, now_showing = now_showing_movie)


#dynamic routing
# @app.route('/movie/<int:id>')
@main.route('/movie/<int:id>')
def movie(id):
    '''
    View root page function that returns the index page and its data
    '''
    movie = get_movie(id)
    title = f" { movie.title }"
    reviews = Review.get_reviews(movie.id)
    return render_template('movie.html', title = title, movie = movie,reviews = reviews)

#search movie
# @app.route('/search/<movie_name>')
@main.route('/search/<movie_name>')
def search(movie_name):
    '''
    View function to display the search results
    '''

    movie_name_list = movie_name.split(' ')
    movie_name_format = '+'.join(movie_name_list)
    searched_movies = search_movie(movie_name_format)
    title = f"search results for{movie_name}"

    return render_template("search.html", movies = searched_movies)

# reviews
# @app.route('/movie/review/new/<int:id>', methods = ['GET','POST'])
@main.route('/movie/review/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_review(id):
    '''
    Funtion to check Review Form
    '''
    form = ReviewForm()
    movie = get_movie(id)

    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data
        new_review = Review(movie.id,title,movie.poster,review)
        new_review.save_review()
        return redirect(url_for('.movie', id=movie.id))

    title = f"{movie.title} review"
    return render_template('new_review.html', title = title, review_form = form, movie = movie)

#Creating new profile
@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

#update profile
@main.route('/user/<uname>/update',methods = ["GET","POST"])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname = user.username))

    return render_template('profile/update.html', form =form)

#picture
@main.route('/user/<uname>/update/pic',methods = ["GET","POST"])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()

    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()

    return redirect(url_for('main.profile', uname = uname))
