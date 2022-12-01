from flask import Flask, request
from .src.similarity import find_most_sample
from .src.db import load_songs

app = Flask(__name__)

load_songs()

@app.route("/api/find", methods=["POST"])
def find():
    file = request.files["file"]

    file.save("recording.webm")

    song = find_most_sample(file.filename)

    return song.split(".mp3")[0]
