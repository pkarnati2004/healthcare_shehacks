from flask import Flask, render_template, request
import pandas as pd
import matplotlib

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "hello world, welcome to SheHacks!!!!! Standalone page for index!!!!"

@app.route('/form')
def form():
    return render_template('index.html')

@app.route('/plotlib')
def plot():
    return "plotlib"
    

@app.route('/submitted', methods=['POST'])
def submitted_form():
    name = request.form['name']
    email = request.form['email']
    gender = request.form['gender']
    race = request.form['race']
    return render_template(
        'submitted_form.html',
        name=name,
        email=email,
        gender=gender,
        race=race)


if __name__ == "__main__":
    app.run(debug=True)