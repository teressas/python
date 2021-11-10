# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import bcrypt
import re

from flask_app.models import model_recipe

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

# (?=.*[@$!%*#?&]) = special charater
# needs lowercase, uppercase, number, and special charater in password
PASSWORD_REGEX = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$')

# captialize global variables
DATABASE = 'user_recipes'

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
        self.recipes = []

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

    # get data from receipes table
    @classmethod
    def get_user_recipes(cls,data:dict):
        query = "SELECT * FROM users LEFT JOIN recipes ON users.id = recipes.user_id WHERE users.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db( query , data )
        
        if len(results) == 0:
            return False

        user = cls( results[0] )
        
        if results[0]["recipes.id"] != None:
            for row_from_db in results:
                recipeData = {
                    "id" : row_from_db["recipe.id"],
                    "name" : row_from_db["name"],
                    "description" : row_from_db["description"],
                    "under_30_mins" : row_from_db["under_30_mins"],
                    "instructions" : row_from_db["instructions"],
                    "created_at" : row_from_db["recipe.created_at"],
                    "updated_at" : row_from_db["recipe.updated_at"],
                    "date_made" : row_from_db["date_made"],
                    "user_id" : row_from_db["user_id"]
                }
                print(recipeData)
                user.recipes.append(model_recipe.Recipe( recipeData ) )

        # cls()
        return user

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
        is_valid = True 
        if len(data['first_name']) < 2:
            is_valid = False
            flash("First Name is required", "err_reg_first_name")

        if len(data['last_name']) < 2:
            is_valid = False
            flash("Last Name is required","err_reg_last_name")

        # if len(data['email']) < 1:
        #     is_valid = False
        #     flash("Email name is required.","err_reg_email")
        # elif not EMAIL_REGEX.match(data['email']):
        #     flash("Invalid Email!!!","err_reg_email")
        #     is_valid=False    
        
        if not EMAIL_REGEX.match(data['email']):
            flash("Invalid Email!!!","err_reg_email")
            is_valid=False
        elif User.get_email({'email':data['email']}):
            is_valid=False
            flash("Email already taken.","err_reg_email")
        
            
        if len(data['password']) < 8:
            is_valid = False
            flash("Password is required","err_reg_password")
        elif not PASSWORD_REGEX.match(data['password']):
            flash("Invalid Password!!!","err_reg_password")
            is_valid=False
            
        if len(data['confirm_password']) < 8:
            is_valid = False
            flash("Confirm Password is required","err_reg_confirm_password")

        if data['confirm_password']!= data['password']:
            is_valid = False
            flash("Confirm Password is required","err_reg_confirm_password")

        return is_valid

    @staticmethod
    def validate_users_login(data):
        is_valid = True
    
        if len(data['email']) < 1:
            is_valid = False
            flash('email is required','err_login_email')
        else:
            potential_user = User.get_email({'email':data['email']})
            print(potential_user)
            if not potential_user:
                is_valid = False
                flash('email not found','err_login_email')

        if len(data['password']) < 8:
            is_valid = False
            flash('Password is required', 'err_login_password')

        return is_valid

