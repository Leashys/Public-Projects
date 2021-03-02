from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/programs')
def programs():
    return render_template("programs.html")


@app.route('/courses')
def courses():
    return render_template("courses.html")


