from flask_app.models import model_user
from flask_app import app
from flask import render_template, jsonify, request, redirect, session, flash

@app.route('/')
def index():
    if 'uuid' in session:
        return redirect('/pokedex')
    return render_template('index.html')

@app.route('/validate',methods = ['post'])
def validate():
    data = request.form
    if not data:
        data = request.json
    errors = {
        model_user.User.validate_reg_users(request.form),
        model_user.User.validate_users_login(request.form)
    }
    print(errors)
    if len(errors) > 0:
        msg = {
            'status': 400,
            'msg': errors
        }
        return jsonify(msg)
    
    msg = {
        'status': 200,
        'msg': 'Success'
        }
    return jsonify(msg)

@app.route('/create_user', methods=["post"])
def create_user():
    pass
@app.route('/user/process_login', methods=["post"])
def login_user():
    pass


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')




