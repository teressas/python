# Your program should have the following output

# For example, http://localhost:5000/10/10 should display 10 by 10 checkerboard.  
# Before you pass x or y to Jinja, please remember to convert it to integer first 
# (so that you can use x or y in a for loop)

# Have the root route render a template with a checkerboard on it

from flask import Flask, render_template
app = Flask(__name__)

# http://localhost:5000 - should display 8 by 8 checkerboard
@app.route('/')
def index():
    return render_template("index.html", num1=4,oddcolor="black", evencolor="red")	

# http://localhost:5000/4 - should display 8 by 4 checkerboard
@app.route('/<int:num1>')
def widthfour(num1):
    return render_template("index.html", num1=int(num1/2), oddcolor="black", evencolor="red")

#http://localhost:5000/(x)/(y) - should display x by y checkerboard.
@app.route('/<int:num1>/<int:num2>')
def changebox(num1, num2):
    return render_template  ("index.html", num1=int(num1/2), num2=int(num2), oddcolor="black", evencolor="red")


if __name__=="__main__":
    app.run(debug=True)

