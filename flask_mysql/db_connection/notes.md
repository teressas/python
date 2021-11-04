# Flask
1. What is flask?


## Terminal Navigation Commands
- cd: change directory (folder)
- cd ..:
- ls: list [] dif
- pwd: print working directory
- md or mkdir: make directory
- touch(git) or echo(cmd): make a file
- rm -r -f to remove a file/dir !!!!<Warning>

## View
- what is a view?
    - what the end user sees


# Get a flask app up nd running

## one off commands
```
pip3 install pipenv
```

## __Steps__
1. Create a folder in which your current assignment will live.
2. Go into that folder
3. Create virtual environment
    - click on the folder the python script is stored
    - services -> open terminal in new folder
    - connect our Flask applications to a database
        ```
        pipenv install flask pymysql
        ```
    
4. Will create two files:
    - Pipfile will display the packages installed
    - Pipfile.lock will have the specific details on what version is being used.
    - the two files should be stored inside the folder
5. launch shell
    ```
    pipenv shell 
    or
    python3 -m pipenv shell
    ```
6. Create file structure
    - pipfile
    - pipfile.lock
    - flask app
        - config
            - mysqlconnection.py
        - controllers
            - controller_table_name.py
        - models
            - model_table_name.py
    - templates
        - index.html
    - static
        - css
            - style.css
        - js
            - script.js
        img
    - __init__.py
    - server.py
    
    
7. Create server.py file
    ```py
    from flask import Flask, render_template, request, redirect, session
    # Import Flask to allow us to create our app
    app = Flask(__name__)    # Create a new instance of the Flask class called "app"
    
    # secret key for session
    app.secret_key = 'keep it secret, keep it safe'

    @app.route('/')          # The "@" decorator associates this route with the function,immediately following
                             # route: - is the path, is a function ('/') is a string
    def hello_world():
        return 'Hello World!'  # Return the string 'Hello World!' as a response
    if __name__=="__main__":   # Ensure this file is being run directly and not from a different module. Name of module will __main__.
                               # Imported file doesn't run code  
        app.run(debug=True)    # Run the app in debug mode.
    ```

7. go to browswer and type http://localhost:5000/ in URL.
8. create mysqlconnection.py
```py
# a cursor is the object we use to interact with the database
import pymysql.cursors
# this class will give us an instance of a connection to our database
class MySQLConnection:
    def __init__(self, db):
        # change the user and password as needed
        connection = pymysql.connect(host = 'localhost',
                                    user = 'root', 
                                    password = 'root', 
                                    db = db,
                                    charset = 'utf8mb4',
                                    cursorclass = pymysql.cursors.DictCursor,
                                    autocommit = True)
        # establish the connection to the database
        self.connection = connection
    # the method to query the database
    def query_db(self, query, data=None):
        with self.connection.cursor() as cursor:
            try:
                query = cursor.mogrify(query, data)
                print("Running Query:", query)
     
                cursor.execute(query, data)
                if query.lower().find("insert") >= 0:
                    # INSERT queries will return the ID NUMBER of the row inserted
                    self.connection.commit()
                    return cursor.lastrowid
                elif query.lower().find("select") >= 0:
                    # SELECT queries will return the data from the database as a LIST OF DICTIONARIES
                    result = cursor.fetchall()
                    return result
                else:
                    # UPDATE and DELETE queries will return nothing
                    self.connection.commit()
            except Exception as e:
                # if the query fails the method will return FALSE
                print("Something went wrong", e)
                return False
            finally:
                # close the connection
                self.connection.close() 
# connectToMySQL receives the database we're using and uses it to create an instance of MySQLConnection
def connectToMySQL(db):
    return MySQLConnection(db)

```
9. Create my model folder
    model_user.py

10. _init__.py
```py
# __init__.py
from flask import Flask
app = Flask(__name__)
app.secret_key = "shhhhhh"
```

10. Run it
11. Session only runs on own computer
