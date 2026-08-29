#!/usr/bin/env python3
import logging

import click
from flask import Flask, Response, send_from_directory

from utils.config_reader import Config

config = Config()

if not config["DEBUG"]["flask_output"]:
    # Surpress any output from Flask & Werkzeug for clean terminal
    logging.getLogger("werkzeug").disabled = True
    click.echo = lambda *args, **kwargs: None
    click.secho = lambda *args, **kwargs: None

app = Flask(__name__)


@app.route("/tts/<path:filename>", methods=["GET"])
def serve_mp3(filename: str) -> Response:
    return send_from_directory("static/tts", filename, mimetype="audio/mpeg")
