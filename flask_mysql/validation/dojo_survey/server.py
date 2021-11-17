from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes
    
# Have the root route render a template that displays 
# the number of times the client has visited this site. 
# Refresh the page several times to ensure the counter is working.
@app.route('/')
def index():
    return render_template('index.html')

# Have the "/result" route display the information 
# from the form on a new HTML page
@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/process', methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    session['fav_language'] = request.form['fav_language']
    session['season'] = request.form['season']
    print(request.form['name'])
    print(request.form['location'])
    print(request.form['language'])
    print(request.form['comments'])
    return redirect('/result')

@app.route('/clear')
def clear():
    session['count'] = 0
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)

    