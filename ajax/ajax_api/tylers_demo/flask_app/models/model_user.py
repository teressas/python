# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import bcrypt

from flask_app.models import model_user

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$"
PASSWORD_REGEX = re.compile(reg)

# captialize global variables
DATABASE = 'users'

# model the class after the user table from our database
class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    # Now we use class methods to query our database

    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    # C
    # class method to save our user to the DATABASE
    # learn platform calls it def save():
    @classmethod
    def create(cls, data:dict):
        query = "INSERT INTO users ( first_name , last_name , email , password , created_at, updated_at ) VALUES ( %(first_name)s , %(last_name)s , %(email)s , %(password)s , NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        # returns an id
        return connectToMySQL(DATABASE).query_db( query, data )

    # R
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        # connectToMySQL is class, ('movies') is an instance of a class
        results = connectToMySQL(DATABASE).query_db(query)
        # Create an empty list to append our instances of movies
        users = []
        # Iterate over the db results and create instances of movies with cls.
        for user in results:
            users.append( cls(user) )
        return users

    @classmethod
    def get_one(cls, data:dict):
        query = "SELECT * FROM users WHERE id=%(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if not results:
            return False
        return cls(results[0])
    
    @classmethod
    def get_email(cls, data:dict):
        query = "SELECT * FROM users WHERE email=%(email)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if not results:
            return False
        return cls(results[0])

    # U
    @classmethod
    def update_one(cls, data):
        query = "UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s, password=%(password)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)

    # D
    @classmethod
    def delete_one(cls,data):
        query  = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)

#********VALIDATIONS******************
    @staticmethod
    def validate_users(data):
        errors = {}

        if 'first_name' in data and len(data['first_name']) < 2:
            errors['err_user_first_name'] = "First Name is required"

        if 'last_name' in data and len(data['last_name']) < 2:
            errors['err_user_last_name'] = "Last Name is required"

        if 'email' in data and len(data['email']) < 1:
            errors['err_user_email'] = "Email is required"
        elif not EMAIL_REGEX.match(data['email']):
            errors['err_user_email'] = "Email is required"
        
            
        if 'password' in data and len(data['password']) < 8:
            errors['err_user_password'] = "Password is required"
        elif not PASSWORD_REGEX.match(data['password']):
            errors['err_user_password'] = "Password is required"
            
        if 'confirm_password' in data and len(data['confirm_password']) < 8:
            errors['err_user_confirm_password'] = "Password is required"
            
        return errors

    @staticmethod
    def validate_users_login(data):
        errors = {}
    
        if 'email' in data and len(data['email']) < 1:
            errors['err_login_email'] = "Email is required"
        else:
            potential_user = User.get_email({'email':data['email']})
            if not potential_user:
                errors['err_login_email'] = "Email is required"

        if 'password' in data and len(data['password']) < 8:
            errors['err_login_password'] = "Password is required"

        return errors

