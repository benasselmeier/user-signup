from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/signup", methods=['POST'])
def signup():

    username = request.form['username']
    password = request.form['password']
    confirm = request.form['confirm']
    email = request.form['email']
    error = ""

    if (len(username) < 3) or (len(username) > 20):
        error = "invalid username"
        return redirect("/?error=" + error)

    render_template('index.html')

@app.route("/")
def index():
    return render_template('form-signup.html')

app.run()