from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return """
    <h1>Hello World<h1>
    <h2>My name is Abhigyan<h2>
    """

app.run(debug=True)