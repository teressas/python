from flask_app import app, bcrypt
from flask import json, render_template, redirect, request, session, flash, jsonify
from flask_app.controllers import controller_route
from flask_app.models import model_user

@app.route('/user/new')
def new_user():
    pass

@app.route('/user/create')
def create_user():
    pass

@app.route('/user/<int:id>')
def show_user(id):
    pass

@app.route('/user/<int:id>/edit')
def edit_user():
    pass

@app.route('/user/<int:id>/update')
def update_user():
    pass

@app.route('/user/<int:id>/delete')
def delete_user():
    pass

@app.route('/api/user/create',methods = ['post'])
def api_user_create():
    data = request.form
    if not data:
        data = request.json
    errors = model_user.User.validate_users(request.form)
    print(errors)
    if len(errors) > 0:
        msg = {
            'status': 400,
            'msg': errors
        }
        return jsonify(msg)
    
    msg = {
        'status': 200,
        'msg': 'This is a message'
        }
    return jsonify(msg)