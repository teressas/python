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
    def delete_one(cls,data):
        query  = "DELETE FROM emails WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)
        
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