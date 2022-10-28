from app import app
from flask import render_template


@app.route('/')
def home_page():
    return render_template('home.html')

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


    # https://media.npr.org/assets/img/2020/06/05/rtj-by-tim-saccenti-2_wide-db330e92d4712fb8374a3ba7ff522be91325c1bd-s1400-c100.jpg