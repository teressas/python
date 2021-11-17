from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models.model_movie import model_movie

@app.route('/')
def index():
    context = {
        'all_movies = model_movie.Movie.get_all()'
    }
    
    return render_template("index.html", **context)

# display route
# show the page with the form to add a new movie
@app.route('/movie/new')
def new_movie():

    return render_template('movie_new.html')

# Action Route
# process the new movie and add it to the DB
@app.route('/movie/create', methods=['POST'])
def create_movie():
    id = model_movie.Movie.create(request.form)
    print(id)
    return redirect('/')

# Display route
# show movie info
@app.route('/movie/<int:id>')
def show_movie(id):
    context = {
        'movie': model_movie.Movie.get_one({'id' : id})
    }
    return render_template("movie_show.html", **context)

# Display Route
# show movie the form to edit a movie
@app.route('/movie/<int:id>/edit')
def edit_movie():
    context = {
        'movie': model_movie.Movie.get_one({'id' : id})
    }
    return render_template('movie_edit.html',**context)

# process update of a movie
@app.route('/movie/<int:id>/update', methods=['POST'])
def update_movie(id):
    data = {
        # extract everything from request form
        **request.form,
        'id' : id
    }
    model_movie.Movie.update_one(data)
    return redirect(f'/movie/{id}')

# Action Route
# delete a movie
@app.route('/movie/<int:id>/delete')
def delete_movie():
    model_movie.Movie.delete_one({'id' : id})
    return redirect('/')
    

@app.route('/process', methods=["POST"])
def process():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with  the variables in our query string.
    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
    # We pass the data dictionary into the save method from the Movies class.
    id=model_movie.Movie.create(data)
    # Don't forget to redirect after saving to the database.
    return redirect(f'/movies/{id}')
