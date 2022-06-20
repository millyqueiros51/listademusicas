from flask import Flask, render_template, request, url_for, redirect
from jinja2 import Environment, FileSystemLoader


app = Flask(__name__)

env = Environment(loader=FileSystemLoader("templates"))
env.globals["enumerate"] = enumerate


playlists = []


@app.route('/')
def hello_world():
    return render_template('index.html', playlist=enumerate(playlists))


@app.route('/add-playlist', methods=['POST'])
def add_playlist():
    playlist_form = {
        'musica': request.form['musica'],
        'artista': request.form['artista']
    }

    playlists.append(playlist_form)

    return redirect(url_for('hello_world'))


@app.route('/remove-playlist/<int:playlist>', methods=['POST'])
def remove_playlist(playlist):
    del(playlists[playlist])

    return redirect(url_for('hello_world'))
