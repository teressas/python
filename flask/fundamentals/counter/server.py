from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes
    
# Have the root route render a template that displays 
# the number of times the client has visited this site. 
# Refresh the page several times to ensure the counter is working.
@app.route('/')
def index():
    if 'count' in session:
        session['count']+=1
    else:
        session['count'] = 0
    count = session['count']
    return render_template('index.html', count = count)

# Add a "/destroy_session" route that clears the session 
# and redirects to the root route. Test it.
@app.route('/destroy')
def reset():
    session['count'] = 0
    session.clear()
    return redirect('/')
# session.pop('key_name')		# clears a specific key	 
    
# NINJA BONUS: Add a +2 button underneath the counter 
# and a new route that will increment the counter by 2
@app.route('/increment')
def increment():
    if 'count' in session:
        session['count']+=2
    else:
        session['count'] = 0
    count = session['count']
    return render_template('index.html', count = count)

@app.route('/count', methods=['POST'])
def input():
    if 'count' in session:
        session['count'] += int(request.form['count'])-1
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)

    