from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/welcome", methods=['POST'])
def signup():

    username = request.form['username']
    password = request.form['password']
    confirm = request.form['confirm']
    email = request.form['email']
    error = ""

    if len(username) > 3 and len(username) <20:
        return render_template('welcome.html', username=username)
    else:
        error = "invalid username"
        return render_template('form-signup.html', error=error)

@app.route("/")
def index():
    return render_template('form-signup.html')

app.run()