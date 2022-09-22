from flask import Flask, render_template, redirect
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('signup')
def signup():
    return render_template('index.html')