from flask import Flask, render_template, request, redirect, session
import random 	# import the random module

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

# display form
@app.route('/')
def index():
    # creates the random number then store it into session[number]
    session['number'] = random.randint(1, 100)
    print(int(session['number']))
    return render_template('index.html')

# stores number into a session
@app.route('/random_num', methods=['POST'])
def random_num():
    session['guess'] = request.form['guess']
    print(request.form['guess'])
    return redirect('/guess')

# goes to guess route and tells user if their guess is low, high or correct
@app.route('/guess')
def guess():
    if int(session['number']) == int(session['guess']):
        results = f"You Guessed it, the number was {session['guess']}."
        color = results
    elif int(session['guess']) > int(session['number']):
        results =  "Too High"
        color = results
    elif int(session['guess']) < int(session['number']):
        results = "Too Low"
        color = results
    else:
        session['number'] = 0
    return render_template('guess.html', results=results, color=color)

if __name__=="__main__":
    app.run(debug=True)
    