from flask import render_template, request, redirect, session

from flask_app import app

# import the class from user.py
from flask_app.models import model_dojo, model_ninja

# DISPLAY ROUTE: new ninja form
@app.route('/ninjas/new')
def new_ninjas():
    context = {
        'all_dojos' : model_dojo.Dojo.get_all()
    }
    return render_template("new_ninjas.html", **context)

# PROCESS ROUTE: create new ninja
@app.route("/ninjas/create", methods = ["POST"])
def create_ninjas():
    model_ninja.Ninja.create(request.form)
    id = request.form["dojo_id"]
    print(id)
    return redirect(f'/dojos/{id}')
