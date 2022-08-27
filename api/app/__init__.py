import io
import logging
import os
import threading

from confugue import Configuration
import flask
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import werkzeug.exceptions
from werkzeug.middleware.proxy_fix import ProxyFix


app = flask.Flask(__name__,
                  instance_relative_config=True)
app.config.from_object('app.config')
if 'STATIC_FOLDER' in app.config:
    app.static_folder = app.config['STATIC_FOLDER']
    app.static_url_path = '/'

app.wsgi_app = ProxyFix(app.wsgi_app, **app.config.get('PROXY_FIX', {}))
limiter = Limiter(app, key_func=get_remote_address, headers_enabled=True, **app.config.get('LIMITER', {}))
CORS(app, **app.config.get('CORS', {}))




# Requires 
@app.route('/api/style_transfer/', methods=['POST'])
def to_lofi():
    files = flask.request.files
    # Split into 5 tracks
    voice, bass, piano, drums, other = split_audio(files['audio'].read())

    # Combine voice, piano and other for use in tomidi
    combined_for_midi = piano.overlay(other)

    midi_file_string = to_midi(combined_for_midi)

    return error_response("Not implemented")



@app.errorhandler(werkzeug.exceptions.HTTPException)
def http_error_handler(error):
    response = error.get_response()
    response.data = flask.json.dumps({
        'code': error.code,
        'error': error.name,
        'description': error.description
    })
    response.content_type = 'application/json'
    return response


def error_response(error, status_code=400):
    response = flask.make_response(flask.json.dumps({'error': error}), status_code)
    response.content_type = 'application/json'
    return response
