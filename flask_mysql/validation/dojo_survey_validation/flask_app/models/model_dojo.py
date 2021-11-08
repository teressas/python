# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

DATABASE = 'dojo_survey'
# model the class after the user table from our database
class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        # connectToMySQL is class, ('users') is an instance of a class
        results = connectToMySQL(DATABASE).query_db(query)
        # Create an empty list to append our instances of users
        dojos = []
        # Iterate over the db results and create instances of users with cls.
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos

        # class method to save our user to the DATABASE
    @classmethod
    def create(cls, data ):
        query = "INSERT INTO dojos ( name , location , language , comment , created_at, updated_at ) VALUES ( %(name)s , %(location)s , %(language)s , %(comment)s , NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL(DATABASE).query_db( query, data )

    @classmethod
    def get_one(cls, data:dict):
        query = "SELECT * FROM dojos WHERE id=%(id)s;"
        # LIST OF DICTIONARIES
        results = connectToMySQL(DATABASE).query_db(query, data)
        if not results:
            return False
        return cls(results[0])

    @classmethod
    def update_one(cls, data):
        query = "UPDATE dojos SET name=%(name)s , location=%(location)s, language=%(language)s, comment=%(comment)s WHERE id=%(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def delete_one(cls,data):
        query  = "DELETE FROM dojos WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)

    # validation
    @staticmethod
    def validate_dojo(dojo):
        is_valid = True # we assume this is true
        if len(dojo['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(dojo['location']) < 3:
            flash("Must select a location.")
            is_valid = False
        if len(dojo['language']) < 200:
            flash("Must select a language.")
            is_valid = False
        return is_valid
    
