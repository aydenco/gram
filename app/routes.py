from app import app
from flask import render_template


@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/favorites')
def favorites_page():
    favartists = [
        {'name' : 'Run the Jewels', 'song' : 'Nobody Speak'},
        {'name' : 'Freddie Dredd', 'song' : 'Wrath'},
        {'name' : 'Half Alive', 'song' : 'still feel.'},
        {'name' : 'Joji', 'song' : 'CANT GET OVER YOU'},
        {'name' : 'Rainbow Kitten Suprise', 'song' : 'When it lands'}
    ]
    return render_template('favorites.html', favartists = favartists)