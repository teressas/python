from flask import Flask, render_template # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

# localhost:5000/ - have it say "Hello World!"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return render_template('index.html')  # Return the string 'Hello World!' as a response
                                            # Index.html is the source, will look into the templates folder
                                            # and look and find for index.html

@app.route('/success/')
@app.route('/success/<int:num>')
def success(num=0): 
    # print(num)
    sum = num * 7
    return render_template('success.html', num1=sum)

# @app.route('/success/<name>')
# def success string(name):


#localhost:5000/dojo - have it say "Dojo!"
# @app.route('/success')
# def success():
#     return 'Success'

# @app.route('/success/<int:num>')
# def success_num(num):
#     print(num)
#     return {f'Success {num}!'}

# @app.... all will move to different file once we start modularizing

@app.route('/hello/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello(name):
    print(name)
    return "Hello, " + name

@app.route('/users/<username>/<id>') # for a route '/users/____/____', two parameters in the url get passed as username and id
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

# What render template does
# def render_template(str):
    # located templates folder
    # find file that matches the str
    # go through that html file
    # look for jinja tags
    # replace jinga tags with output of the logic
    # return the raw html page
    # pass 
        # returns the html at return when it gets passed back


