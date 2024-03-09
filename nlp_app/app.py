from flask import Flask,render_template,request
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
        return "Registration successful"
    else:
        return "email already registered"

app.run(debug=True)