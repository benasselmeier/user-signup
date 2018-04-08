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

    if len(username) >= 3 and len(username) <= 20 and " " not in username:
        username=username
        username_error = ""
    else:
        username_error = "invalid username"

    if len(password) >= 3 and len(password) <= 20 and " " not in password:
        password=password
        password_error = ""
    else:
        password_error = "invalid password"
    
    if confirm == password:
        confirm=confirm
        confirm_error = ""
    else:
        confirm_error = "passwords don't match"

    if email == "" or (len(email) >= 3 and len(email) <= 20) and ('.' in email and '@' in email) and " " not in email:
        email = email
        email_error = ""
    else:
        email_error = "invalid email"

    rules = (username_error == "", password_error == "", confirm_error == "", email_error == "")

    if all(rules):
        return render_template('welcome.html', username = username)
    else:
        return render_template('form-signup.html', username=username, username_error=username_error, password_error=password_error, confirm_error = confirm_error, email_error = email_error)

@app.route("/")
def index():
    return render_template('form-signup.html')

app.run()