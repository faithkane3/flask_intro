from flask import Flask, render_template, request
from random import randint
from time import strftime
from model import predict

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template(
        'home.html'
    )

@app.route('/about')
def about():
    return render_template(
        'about.html'
    )

@app.route('/roll-dice')
def rolldice():
    r1 = randint(1,6)
    r2 = randint(1,6)
    r3 = randint(1, 6)
    return str([r1, r2, r3])

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

@app.route('/html-fun-with/<name>')
def funpage(name):
    return render_template('html-fun.html',
    name=name,
    the_date=strftime('%B %d, %Y')
    )

@app.route('/greeting')
def show_greeting_form():
    return render_template('greeting.html')

@app.route('/greeting-result', methods=['POST'])
def show_greeting_result():
    name = request.form['name']
    return render_template(
        'greeting-result.html',
         name=name
    )

@app.route('/text-input')
def predict_text():
    return render_template(
        'text-input.html'
    )

@app.route('/text-result', methods=['POST'])
def predict_text_result():
    text = request.form['text']
    return render_template(
        'text-result.html',
        text = text,
        prediction = predict(text)
    )