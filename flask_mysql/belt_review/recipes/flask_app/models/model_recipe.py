# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
# from flask_app.models import model_user

# captialize global variables
DATABASE = 'user_recipes'

# model the class after the recipe table from our database
class Recipe:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.under_30_mins = data[int:'under_30_mins']
        self.instructions = data['instructions']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.date_made = data['date_made']
        self.user_id = data['user_id']

    # C
    # class method to save our recipe to the DATABASE
    # learn platform calls it def save():
    @classmethod
    def create(cls, data:dict):
        query = "INSERT INTO recipes ( name , description , under_30_mins , instructions , created_at , updated_at , date_made, user_id) VALUES ( %(name)s , %(description)s , %(under_30_mins)s , %(instructions)s , NOW() , NOW() , date_made , %(user_id)s);"
        # data is a dictionary that will be passed into the save method from server.py
        # returns an id
        return connectToMySQL(DATABASE).query_db( query, data )

    # R
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        # connectToMySQL is class, ('movies') is an instance of a class
        results = connectToMySQL(DATABASE).query_db(query)
        # Create an empty list to append our instances of movies
        recipes = []
        # Iterate over the db results and create instances of movies with cls.
        for recipe in results:
            recipes.append( cls(recipe) )
        return recipes

    @classmethod
    def get_one(cls, data:dict):
        query = "SELECT * FROM recipes WHERE id=%(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if not results:
            return False
        return cls(results[0])
    
    @classmethod
    def get_email(cls, data:dict):
        query = "SELECT * FROM recipes WHERE email=%(email)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if not results:
            return False
        return cls(results[0])

    # U
    @classmethod
    def update_one(cls, data):
        query = "UPDATE recipes SET name=%(name)s , description=%(description)s , under_30_mins=%(under_30_mins)s , instructions=%(instructions)s , date_made= %(date_made)s , user_id=%(user_id)s WHERE recipes.id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)

    # D
    @classmethod
    def delete_one(cls,data):
        query  = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)

#********VALIDATIONS******************
    @staticmethod
    def validate_recipes(data):
        is_valid = True # we assume this is true
        if len(data['name']) < 3:
            is_valid = False
            flash("Name is required", "err_add_name")

        if len(data['description']) < 3:
            is_valid = False
            flash("Description name is required.","err_add_desc") 
        
        if len(data['instructions']) < 3:
            is_valid = False
            flash("Instructions are required.","err_add_instruct") 

        return is_valid

