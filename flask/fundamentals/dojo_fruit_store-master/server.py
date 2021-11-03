#!/usr/bin/env python3
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes
    

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout')         
def checkout():
    print(request.form)
    return render_template("checkout.html")

@app.route('/process', methods=['POST'])
def process():
    # pulls the number of items selected
    session['strawberry'] = int(request.form['strawberry'])
    session['raspberry'] = int(request.form['raspberry'])
    session['apple'] = int(request.form['apple'])
    # pulls the total number of items selected
    session['total'] = session['strawberry'] + session['raspberry'] + session['apple']
    #session['total'] = sum((session['strawberry'],session['raspberry'],session['apple']))
    # pulls the user information
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['student_id'] = request.form['student_id']
    return redirect('/checkout')

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')

if __name__=="__main__":   
    app.run(debug=True)    