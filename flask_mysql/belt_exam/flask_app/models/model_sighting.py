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
DATABASE = 'users_sightings'

# model the class after the user table from our database
class Sightings:
    def __init__( self , data ):
        self.id = data['id']
        self.location = data['location']
        self.what_happened = data['what_happened']
        self.date_sighting = data['date_sighting']
        self.num_of_sasquatche = data['num_of_sasquatche']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.users=[]
        

    # Now we use class methods to query our database

    # C
    # class method to save our user to the DATABASE
    # learn platform calls it def save():
    @classmethod
    def create(cls, data:dict):
        query = "INSERT INTO sightings ( location , what_happened , date_sighting , num_of_sasquatche , created_at, updated_at, user_id ) VALUES ( %(location)s , %(what_happened)s , %(date_sighting)s , %(num_of_sasquatche)s , NOW() , NOW(),  %(user_id)s);"
        # data is a dictionary that will be passed into the save method from server.py
        # returns an id
        return connectToMySQL(DATABASE).query_db( query, data )

    # R

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM sightings;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        # connectToMySQL is class, ('movies') is an instance of a class
        results = connectToMySQL(DATABASE).query_db(query)
        # Create an empty list to append our instances of movies
        sightings = []
        # Iterate over the db results and create instances of movies with cls.
        for sighting in results:
            curr_sighting = cls(sighting)
            curr_sighting.users.append(model_user.User.get_one({'id':curr_sighting.user_id}))
            sightings.append( curr_sighting )
        return sightings

    @classmethod
    def get_one(cls, data:dict):
        query = "SELECT * FROM sightings WHERE id=%(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if not results:
            return False
        return cls(results[0])

    # get data from receipes table
    @classmethod
    def get_reportedby(cls,data:dict):
        query = "SELECT * FROM sightings LEFT JOIN users ON sightings.user_id = users.id WHERE sightings.id=%(id)s;"
        results = connectToMySQL(DATABASE).query_db( query , data ) 
        
        if not results:
            return False

        sighting = cls( results[0] )
        
        if results[0]["users.id"] != None:
            for row_from_db in results:
                userData = {
                    "id" : row_from_db["users.id"],
                    "first_name" : row_from_db["first_name"],
                    "last_name" : row_from_db["last_name"],
                    "email" : row_from_db["email"],
                    "password" : row_from_db["password"],
                    "created_at" : row_from_db["users.created_at"],
                    "updated_at" : row_from_db["users.updated_at"],
                    "user_id" : row_from_db["user_id"]
                }
                print(userData)
                sighting.users.append(model_user.User( userData ) )
                

        # cls()
        return sighting

    # U
    @classmethod
    def update_one(cls, data):
        query = "UPDATE sightings SET location=%(location)s, what_happened=%(what_happened)s, date_sighting=%(date_sighting)s, num_of_sasquatche=%(num_of_sasquatche)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)

    # D
    @classmethod
    def delete_one(cls,data):
        query  = "DELETE FROM sightings WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)

#********VALIDATIONS******************
    @staticmethod
    def validate_sightings(data):
        is_valid = True # we assume this is true
        if len(data['location']) < 2:
            is_valid = False
            flash("Location is required", "err_report_location")

        if len(data['what_happened']) < 2:
            is_valid = False
            flash("What Happened is required","err_report_what_happened")
        
        if len(data['date_sighting']) < 1:
            is_valid = False
            flash("Date is required","err_report_date_sight")
        
        if len(data['num_of_sasquatche']) < 1:
            is_valid = False
            flash("Number of Sasquatches are required","err_report_num_of_sasquatche")

        return is_valid

 

