import logging
from flask import Flask, render_template, request
import classification

app = Flask(__name__)

def merge(dicta, dictb):
    dictc = dicta.copy()
    dictc.update(dictb)
    return dictc

@app.route('/')
def form():
    default = {'max': 1, 'min': 0, 'step': 0.1}
    features = [
        merge({'name' : 'Acousticness'}, default),
        merge({'name' : 'Danceability'}, default),
        merge({'name' : 'Energy'}, default),
        merge({'name' : 'Instrumentalness'}, default),
        merge({'name' : 'Liveness'}, default),
        {'name': 'Loudness', 'min':-60 , 'max':0, 'step':1},
        merge({'name' : 'Speechiness'}, default),
        {'name': 'Valence', 'min': 0, 'max': 600, 'step': 10},
        {'name': 'Tempo', 'min': 0, 'max': 1750, 'step': 10},
    ]

    return render_template('form.html', features=features)

@app.route('/submit_playlist_song_id', methods=['POST'])
def submit_playlist_song_id():
    playlist_id = request.form['playlist_id']
    song_id = request.form['song_id']

    song_year = ""
    if song_id != "":
        song_year = classification.predict_user_song_year(song_id)
    
    playlist_year = ""
    if playlist_id != "":
        playlist_year = classification.predict_playlist_year(playlist_id)

    logging.warning("the predicted year was " + str(song_year))
    return render_template(
        'submitted_playlist_form.html',
        playlist_id=playlist_id,
        song_id=song_id, song_prediction=str(song_year), playlist_prediction=str(playlist_year))

@app.route('/submit_diy_values', methods=['POST'])
def submit_diy_values():
    acousticness = request.form['acousticness']
    return render_template(
        'submitted_diy_form.html',
        acousticness=acousticness, year_prediciton="1989", genre_prediction="tswifty")

@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500

if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
