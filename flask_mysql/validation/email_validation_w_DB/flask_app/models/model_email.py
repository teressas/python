# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

DATABASE = 'emails'
class Email:
    def __init__( self , data ):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls, data ):
        query = "INSERT INTO emails ( email , created_at, updated_at ) VALUES ( %(email)s , NOW() , NOW() );"
        return connectToMySQL(DATABASE).query_db( query, data )
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM email;"
        results = connectToMySQL(DATABASE).query_db(query)
        emails = []
        for email in results:
            emails.append( cls(email) )
        return emails
    
    @classmethod
    def get_one(cls, data:dict):
        query = "SELECT * FROM emails WHERE id=%(id)s;"
        # LIST OF DICTIONARIES
        results = connectToMySQL(DATABASE).query_db(query, data)
        if not results:
            return False
        return cls(results[0])

    @classmethod
    def update_one(cls, data):
        query = "UPDATE emails SET email=%(email)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def delete_one(cls,data):
        query  = "DELETE FROM emails WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)
        
    @staticmethod
    def validate_email( email ):
        is_valid = True
        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(email['email']): 
            flash("Invalid email address!")
            is_valid = False
        return is_valid