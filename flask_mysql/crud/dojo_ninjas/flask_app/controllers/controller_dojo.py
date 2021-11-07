from flask import render_template, request, redirect, session

from flask_app import app

# import the class from user.py
from flask_app.models import model_dojo, model_ninja


# DISPLAY ROUTE: displays new dojo form, all dojos and allows user to create new ninja
@app.route('/')
@app.route('/dojos/new')
def new_dojos():
    context = {
        'all_dojos' : model_dojo.Dojo.get_all()
    }
    return render_template("new_dojos.html", **context)

# PROCESS ROUTE: add new dojo to all dojos
@app.route('/dojos/create', methods=["POST"])
def create_dojo():
    id = model_dojo.Dojo.create(request.form)
    print(id)
    return redirect('/')

@app.route('/dojos/<int:id>')
def show_dojo(id):
    data = {
        'id':id
    }
    dojo = model_dojo.Dojo.get_dojo_with_ninjas(data)
    print(data)
    return render_template("show_dojo.html", dojo = dojo)


