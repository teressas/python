# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL

DATABASE = 'dojos_and_ninjas'
# model the class after the user table from our database
class Ninja:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']
    
    # create full name
    # def fullname(self):
    #     return f"{self.first_name} {self.last_name}"

    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        # connectToMySQL is class, ('users') is an instance of a class
        results = connectToMySQL(DATABASE).query_db(query)
        # Create an empty list to append our instances of users
        ninjas = []
        # Iterate over the db results and create instances of users with cls.
        for ninja in results:
            ninjas.append( cls(ninja) )
        return ninjas

        # class method to save our user to the DATABASE
    @classmethod
    def create(cls, data ):
        query = "INSERT INTO ninjas ( first_name , last_name , age , dojo_id , created_at , updated_at ) VALUES ( %(first_name)s , %(last_name)s , %(age)s , %(dojo_id)s ,  NOW() , NOW());"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL(DATABASE).query_db( query, data )
    
    @classmethod
    def get_one(cls, data:dict):
        query = "SELECT * FROM ninjas WHERE id=%(id)s;"
        # LIST OF DICTIONARIES
        results = connectToMySQL(DATABASE).query_db(query, data)
        if not results:
            return False
        return cls(results[0])

    @classmethod
    def update_one(cls, data):
        query = "UPDATE ninjas SET name=%(name)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def delete_one(cls,data):
        query  = "DELETE FROM ninjas WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)

