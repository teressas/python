# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

from flask_bcrypt import Bcrypt   
bcrypt = Bcrypt(app)

# captialize global variables
DATABASE = 'movies'

# model the class after the user table from our database
class Movie:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        # to link other class
        # self.ninjas = []

    # Now we use class methods to query our database

    # C
    # class method to save our user to the DATABASE
    # learn platform calls it def save():
    @classmethod
    def create(cls, data:dict):
        query = "INSERT INTO movies ( first_name , last_name , email , created_at, updated_at ) VALUES ( %(first_name)s , %(last_name)s , %(email)s , NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        # returns an id
        return connectToMySQL('movies').query_db( query, data )

    # R
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM movies;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        # connectToMySQL is class, ('movies') is an instance of a class
        results = connectToMySQL(DATABASE).query_db(query)
        # Create an empty list to append our instances of movies
        movies = []
        # Iterate over the db results and create instances of movies with cls.
        for movie in results:
            movies.append( cls(movie) )
        return movies

    
    @classmethod
    def get_one(cls, data:dict):
        query = "SELECT * FROM movies WHERE id=%(id)s;"
        # A LIST OF ONE DICTIONARY
        results = connectToMySQL(DATABASE).query_db(query, data)
        if not results:
            return False
        return cls(results[0])

    # U
    @classmethod
    def update_one(cls, data):
        query = "UPDATE movies SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)

    # D
    @classmethod
    def delete_one(cls,data):
        query  = "DELETE FROM movies WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)

    ## !!!!LINKS OTHER CLASS METHOD TO THIS METHOD!!!!

    # @classmethod
    # def get_dojo_with_ninjas(cls,data):
    #     query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
    #     results = connectToMySQL(DATABASE).query_db( query , data )
        
    #     if len(results) == 0:
    #         return False

    #     dojo = cls( results[0] )
        
    #     if results[0]["ninjas.id"] != None:
    #         for row_from_db in results:
    #             ninjaData = {
    #                 "id" : row_from_db["ninjas.id"],
    #                 "first_name" : row_from_db["first_name"],
    #                 "last_name" : row_from_db["last_name"],
    #                 "age" : row_from_db["age"],
    #                 "created_at" : row_from_db["ninjas.created_at"],
    #                 "updated_at" : row_from_db["ninjas.updated_at"],
    #                 "dojo_id" : row_from_db["dojo_id"]
    #             }
    #             print(ninjaData)
    #             dojo.ninjas.append(Ninja( ninjaData ) )

    #     # cls()
    #     return dojo

    @staticmethod
    def is_valid(email):
        is_valid = True
        query = "SELECT * FROM email WHERE email = %(email)s;"
        results = connectToMySQL(DATABASE).query_db(query,email)
        if len(results) >= 1:
            flash("Email already taken.")
            is_valid=False
        if not EMAIL_REGEX.match(email['email']):
            flash("Invalid Email!!!")
            is_valid=False
        return is_valid