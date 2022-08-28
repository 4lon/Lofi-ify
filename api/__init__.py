import io
import logging
import os
import threading

from confugue import Configuration
import flask
from flask import request, send_from_directory
from flask_cors import CORS
import werkzeug.exceptions
from werkzeug.middleware.proxy_fix import ProxyFix
from processing.lofi_processing import lofify

app = flask.Flask(__name__,
                  instance_relative_config=True)

app.wsgi_app = ProxyFix(app.wsgi_app, **app.config.get('PROXY_FIX', {}))
CORS(app, **app.config.get('CORS', {}))




# Requires 
@app.route('/api/style_transfer/<user_file>', methods=['POST'])
def to_lofi():
    # audio_filename = get_youtube_download(request.args.get('youtube_link'))    
    audio_filename = "hello"
    # generate_wav_file should take a file as parameter and write a wav in it
    result_filename = lofify(request.args.get("user_file"), audio_filename)

    return send_from_directory(request.args.get("user_file"), result_filename)

    # return error_response("Not implemented")



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

    

@app.route('/api/yt-download/', methods=['GET'])
def yt_download():
    return "test"

@app.route('/hello')
def hello():
    # response = flask.make_response(flask.json.dumps({'error': 200}), 200)
    # return response
    return "test"
    