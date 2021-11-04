from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/page2/<name>')
def page2(name):
    return render_template("page2.html")

@app.route('/page3', methods=['POST'])
def page3():
    print(request.form['email'])
    return render_template("page3.html")


# Action Route -> never render a template ALWAYS redirect
app.route('/page3_process', methods=['POST'])
def page3_process():
    print(request.form['boo'])
    # some_dict = {}
    session['email'] = request.form['email']
    session['pw'] = request.form['pw']
    return redirect('/page3')

@app.route('/clear')
def clear():
    session.clear()
    # del session['email']
    return redirect('/page3')

if __name__=="__main__":
    app.run(debug=True)