from flask import Flask,render_template,request

app = Flask(__name__)

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
    return name + email + password

app.run(debug=True)