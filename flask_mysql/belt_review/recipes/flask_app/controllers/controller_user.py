import re
from flask_app import app, bcrypt
from flask import render_template, request, redirect, session, flash
from flask_app.models import model_user, model_recipe

# DISPLAY ROUTE -LOGIN
@app.route('/')
def index():
    if 'uuid' in session:
        return redirect('/dashboard')

    return render_template("index.html")

# DISPLAY ROUTE
# show the page with the form to add a new user
@app.route('/dashboard')
def dashboard():
    if 'uuid' not in session:
        return redirect('/')
    context = {
        'user': model_user.User.get_one({'id':session['uuid']}),
        'recipes' : model_recipe.Recipe.get_all()
    }
    return render_template('dashboard.html', **context)


# ACTION ROUTE
# register the new user and add it to the DB
@app.route('/user/create', methods=['POST'])
def create_user():
    is_valid = model_user.User.validate_users(request.form)
    print(is_valid)
    
    if not is_valid:
        return redirect('/')
    
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    data = {
        **request.form,
        'password': pw_hash
    }
    
    id = model_user.User.create(data)
    session['uuid'] = id

    return redirect('/dashboard')

@app.route('/user/process_login',methods=['POST'])
def process_login():
    is_valid = model_user.User.validate_users_login(request.form)

    if not is_valid:
        return redirect('/')
    
    user = model_user.User.get_email({'email':request.form['email']})
    
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash('Invalid Credentials', 'err_login_password')
        return redirect('/')
    
    session['uuid'] = user.id

    return redirect('/dashboard')

@app.route('/logout')
def logout():
    del session['uuid']
    return redirect('/')


@app.route('/', defaults = {'path':''})
@app.route('/<path:path>')
def catch_al(path):
    return 'page not found'


