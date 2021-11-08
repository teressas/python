from flask import render_template, request, redirect, session, flash

from flask_app import app

# import the class from user.py
from flask_app.models.model_email import Email

# renders the user input form
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    if not Email.validate_email(request.form):
        Email.create(request.form)
        return redirect('/success')
    return redirect('/')
    
@app.route("/success")
def success():
    # call the get all classmethod to get all users
    emails = Email.get_all()
    print(emails)
    return render_template("success.html", all_emails = emails)

