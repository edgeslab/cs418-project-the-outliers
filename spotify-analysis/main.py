import logging
from flask import Flask, render_template, request
import classification

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submitted', methods=['POST'])
def submitted_form():
    playlist_id = request.form['playlist_id']
    song_id = request.form['song_id']
    _, year = classification.predictYear('2018TopTracks')
    logging.warning("the predicted year was" + str(year))
    return render_template(
        'submitted_form.html',
        playlist_id=playlist_id,
        song_id=song_id, prediction=str(year))

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
