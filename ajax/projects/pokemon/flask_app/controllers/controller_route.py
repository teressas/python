from flask_app.models import model_user
from flask_app import app
from flask import render_template, jsonify, request, redirect, session

@app.route('/')
def index():
    if 'uuid' in session:
        return redirect('/pokedex')
    return render_template('index.html')

@app.route('/pokedex')
def pokedex():
    if 'uuid' not in session:
        return redirect('/')
    context = {
        'user': model_user.User.get_one({'id':session['uuid']})
    }
    print(context)
    return render_template('pokedex.html', **context)






