import re
from flask_app.models import model_user
from flask_app import app
from flask import render_template, jsonify, request, redirect


@app.route('/user/new')
def users():
    return jsonify(model_user.User.get_all_json())

# @app.route('/create/user',methods=['POST'])
# def create_user():
#     return redirect('/')

@app.route('/api/user/create', methods=['POST'])
def api_user_create():
    
    if len(model_user.User.validate(request.form)) > 0:
        mgs = {
            'status' : 400,
            'msg' : errors
        }

    msg = {
        'status' : 200,
        'msg' : 'This is a message'
    }
    return jsonify(msg)