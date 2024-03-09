from flask import Flask,render_template,request,redirect
from db import *

app = Flask(__name__)

dbo = Database()

@app.route('/')
def index():
    return render_template('login.html')

# create registration page
@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/perform_registration',methods = ['post'])
def perform_registration():
    name = request.form.get('username')
    email = request.form.get('useremail')
    password = request.form.get('password')

    response = dbo.insert(name,email,password)

    if response == 1:
        return render_template('login.html', message = "Registration successful. Login to proceed")
    else:
        return render_template('register.html', message = "Email already exists")

@app.route('/perform_login',methods = ['post'])
def perform_login():
    # check and then execute login actions if email and password matches
    email = request.form.get('useremail')
    password = request.form.get('password')

    response = dbo.search(email,password)

    if response == 1:
        return 'Welcome'
    else:
        return "Email or password combination does not exist"

@app.route('/profile')
def profile():
    return "Profile"

app.run(debug=True)