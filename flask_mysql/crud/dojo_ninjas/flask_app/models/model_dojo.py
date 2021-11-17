# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models.model_ninja import Ninja

DATABASE = 'dojos_and_ninjas'
# model the class after the user table from our database
class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
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
        query = "INSERT INTO dojos ( name , created_at, updated_at ) VALUES ( %(name)s , NOW() , NOW() );"
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
        query = "UPDATE dojos SET name=%(name)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def delete_one(cls,data):
        query  = "DELETE FROM dojos WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)
    
    @classmethod
    def get_dojo_with_ninjas(cls,data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db( query , data )
        
        if len(results) == 0:
            return False

        dojo = cls( results[0] )
        
        if results[0]["ninjas.id"] != None:
            for row_from_db in results:
                ninjaData = {
                    "id" : row_from_db["ninjas.id"],
                    "first_name" : row_from_db["first_name"],
                    "last_name" : row_from_db["last_name"],
                    "age" : row_from_db["age"],
                    "created_at" : row_from_db["ninjas.created_at"],
                    "updated_at" : row_from_db["ninjas.updated_at"],
                    "dojo_id" : row_from_db["dojo_id"]
                }
                print(ninjaData)
                dojo.ninjas.append(Ninja( ninjaData ) )

        # cls()
        return dojo