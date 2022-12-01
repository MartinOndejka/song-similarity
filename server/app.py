from flask import Flask, request
from .src.similarity import find_best_sample
from .src.db import load_songs

app = Flask(__name__)

load_songs()

@app.route("/api/find", methods=["POST"])
def find():
    dtw_implementation = request.args.get("dtw")
    file = request.files["file"]

    file.save("recording.webm")

    song = find_best_sample(file.filename, dtw_implementation=dtw_implementation)

    return song.split(".mp3")[0]
