from flask import Flask, render_template
from random import randint

app = Flask(__name__)

@app.route('/')
def home():
    return 'This is the home page.'

@app.route('/roll-dice/<int:ndice>')
def roll(ndice):
    rolls = [randint(1,6) for _ in range(ndice)]
    return str(rolls)

@app.route('/hello/<name>')
def hello(name):
    return 'Hello, ' + name + '!'

@app.route('/i-can-html')
def htmlpage():
    rolls = [randint(1, 6) for _ in range(10)]
    return render_template(
        'my-html-page.html',
        rolls=rolls
        )