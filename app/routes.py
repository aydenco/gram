from app import app
from flask import render_template


@app.route('/')
def HomePage():
    people = [
        {'name' : "Ayden",
        'age' : 23},
        {'name' : "Joey",
        'age' : 20},
        {'name' : "Ivan",
        'age' : 16}]
    return render_template('index.html', names = people)

@app.route('/login')
def loginPage():
    return render_template('login.html')