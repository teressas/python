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
    - install flask
    ```
    pipenv install flask
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
    - templates
        index.html
    - static
        css
            style.css
        js
            script.js
        img
    server.py
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
8. Run it
9. Session only runs on own computer
