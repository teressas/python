import re
from flask_app import app, bcrypt
from flask import render_template, request, redirect, session, flash
from flask_app.models import model_recipe, model_user

# SHOW RECIPE
@app.route('/recipes/<int:id>')
def show_recipe(id):
    if 'uuid' not in session:
        return redirect('/')
    context = {
        'user': model_user.User.get_one({'id':session['uuid']}),
        'recipe': model_recipe.Recipe.get_one({'id':id})
    }
    return render_template('view_recipe.html', **context)

# ADD RECIPE
@app.route('/recipes/new')
def new_recipes():
    if 'uuid' not in session:
        return redirect('/recipes/new')
    return render_template('new_recipe.html')

# PROCESS NEW RECIPE
@app.route('/recipes/create', methods=['POST'])
def create_recipes():
    is_valid = model_recipe.Recipe.validate_recipes(request.form)
    print(is_valid)
    
    if not is_valid:
        return redirect('/recipes/new')

    # print(request.form['under_30_mins'])

    data = {
        **request.form,
        "user_id" : session['uuid']
    }

    model_recipe.Recipe.create(data)
    
    return redirect('/dashboard')

# EDIT RECIPE
@app.route('/recipes/edit/<int:id>')
def edit_recipes(id):
    if 'uuid' not in session:
            return redirect(f'/recipes/edit/{id}')
    context = {
        'recipe': model_recipe.Recipe.get_one({'id':id})    
    }
    return render_template('edit_recipe.html',**context)

# UPDATE RECIPE
@app.route('/recipes/update/<int:id>', methods=['POST'])
def update_recipes(id):
    is_valid = model_recipe.Recipe.validate_recipes(request.form)
    print(is_valid)
    
    if not is_valid:
        return redirect(f'/recipes/edit/<int:id>')
    data = {
        'id':id,
        **request.form,
        'user_id' : session['uuid']
    }
    print(data)
    print(id)
    model_recipe.Recipe.update_one(data)
    
    return redirect('/dashboard')

@app.route('/recipes/delete/<int:id>')
def delete(id):
    data = {
        'id': id,
    }
    model_recipe.Recipe.delete_one(data)
    return redirect('/dashboard')

