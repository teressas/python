from flask import Flask, render_template # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

# localhost:5000/ - have it say "Hello World!"
@app.route('/') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello_world():
    return "Hello World"

#localhost:5000/dojo - have it say "Dojo!"
@app.route('/dojo')
def dojo():
    return 'Dojo!'

# 3.Create one url pattern and function that can handle the following examples:
# localhost:5000/say/flask - have it say "Hi Flask!"
# localhost:5000/say/michael - have it say "Hi Michael!"
# localhost:5000/say/john - have it say "Hi John!"    
# NINJA BONUS: Ensure the names provided in the 3rd task are strings
@app.route('/say/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello(name):
    print(name)
    return (f'Hi {name.capitalize()}')

# 4. Create one url pattern and function that can handle the following examples (HINT: int() will come in handy! For example int("35") returns 35):
    # localhost:5000/repeat/35/hello - have it say "hello" 35 times
    # localhost:5000/repeat/80/bye - have it say "bye" 80 times
    # localhost:5000/repeat/99/dogs - have it say "dogs" 99 times
    # NINJA BONUS: For the 4th task, ensure the 2nd element in the URL is an integer, and the 3rd element is a string

@app.route('/repeat/<int:num>/<str:name>')
def repeat(num,name):
    repeat_string = int(num)* str(name)
    return(repeat_string)

@app.route('/')
def specified():
    if app.route != app('/')

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.


