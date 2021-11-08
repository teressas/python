from flask import render_template, request, redirect, session

from flask_app import app

# import the class from user.py
from flask_app.models import model_dojo

# DISPLAY ROUTE: displays new dojo form, all dojos and allows user to create new ninja
@app.route('/')
def new_dojos():
    dojos = model_dojo.Dojo.get_all()
    print(dojos)
    return render_template("index.html", all_dojos = dojos)

# PROCESS ROUTE: add new dojo to all dojos
@app.route('/process', methods=["POST"])
def process_survey():
    # jf not Dojo.validate_dojo(request.form):
    #     return redirect('/')
    model_dojo.Dojo.create(request.form)
    id = request.form["id"]
    print(id)
    return redirect(f'/results/{id}')

@app.route('/results/<int:id>')
def show(id):
    dojos = model_dojo.Dojo.get_one({'id':id})
    return render_template("results.html", dojos=dojos)


@app.route('/clear')
def clear():
    session['count'] = 0
    session.clear()
    return redirect('/')
    

