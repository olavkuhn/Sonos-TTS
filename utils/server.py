from flask import Flask, send_from_directory

app = Flask(__name__)


@app.route("/tts/<path:filename>", methods=["GET"])
def serve_mp3(filename: str) -> bool:
    return send_from_directory("static/tts", filename, mimetype="audio/mpeg")
