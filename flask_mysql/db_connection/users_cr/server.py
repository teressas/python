from flask import Flask, render_template, request, redirect, session
# import the class from user.py
from user import User

app = Flask(__name__)

# renders the user input form
@app.route("/user/new")
def create():
    return render_template("create.html")

# render the users table including the new user add from the input form
@app.route("/users")
def index():
    # call the get all classmethod to get all users
    users = User.get_all()
    print(users)
    return render_template("read_all.html", all_users = users)

# route to pull back data input from into dictionary 
# use save method from User class to save user database 
# then redirect data to /users and render new user data.
@app.route('/process', methods=["POST"])
def process():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
    # We pass the data dictionary into the save method from the User class.
    User.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/users')

if __name__ == "__main__":
    app.run(debug=True)