import re
from flask_app import app, bcrypt
from flask import render_template, request, redirect, session, flash
from flask_app.models import model_user, model_sighting
import datetime

# ADD SIGHTING
@app.route('/new/sighting')
def new_sighting():
    if 'uuid' not in session:
        return redirect('/')
    context = {
        'user': model_user.User.get_one({'id':session['uuid']})
    }
    return render_template('new_sighting.html', **context)

#PROCESS NEW SIGHTING
@app.route('/report/sighting', methods=['POST'])
def report_sighting():
    
    is_valid = model_sighting.Sightings.validate_sightings(request.form)
    print(is_valid)
    
    if not is_valid:
        return redirect('/new/sighting')

    data = {
        **request.form,
        "user_id" : session['uuid']
    }
    print(data)
    model_sighting.Sightings.create(data)
    
    return redirect('/dashboard')

# EDIT SIGHTING
@app.route('/edit/<int:id>')
def edit_sighting(id):
    #if session user id  != sighting userid then redirect
    if 'uuid' not in session:
        return redirect('/')
    context = {
        'user': model_user.User.get_one({'id':session['uuid']}),
        'sighting': model_sighting.Sightings.get_one({'id':id})
    }
    return render_template('edit_sighting.html', **context)

@app.route('/update/sighting/<int:id>', methods=['POST'])
def update_sighting(id):

    is_valid = model_sighting.Sightings.validate_sightings(request.form)
    print(is_valid)
    
    if not is_valid:
        return redirect(f'/edit/{id}')

    
    data = {
        'id':id,
        **request.form,
    }
    print(data)
    print(id)
    model_sighting.Sightings.update_one(data)
    
    return redirect('/dashboard')

@app.route('/show/<int:id>')
def show_sighting(id):
    if 'uuid' not in session:
        return redirect('/')
    context = {
        'user': model_user.User.get_one({'id':session['uuid']}),
    #     # 'sighting': model_sighting.Sightings.get_one({'id':id})
        'user_sighting' : model_sighting.Sightings.get_reportedby({'id':id})
    }

    print(id)
    
    return render_template('view_sighting.html', **context)
    


@app.route('/delete/<int:id>')
def delete(id):
    data = {
        'id': id,
    }
    model_sighting.Sightings.delete_one(data)
    return redirect('/dashboard')

