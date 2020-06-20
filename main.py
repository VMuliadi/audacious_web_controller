from flask import Flask, jsonify
from subprocess import check_output
import os

app = Flask(__name__)

def get_output(command):
	return check_output(command, shell=True).decode("utf-8").rstrip()


@app.route("/")
def get_current_song():
	try:
		duration = get_output("audtool current-song-length")
		channels = get_output("audtool current-song-channels")
		time_elapsed = get_output("audtool current-song-output-length")
		bit_rate = get_output("audtool current-song-bitrate-kbps") + " kbps"
		frequency = get_output("audtool current-song-frequency-khz") + " kHz"
		filename = get_output("audtool current-song-filename").split("/")[-1]
		response = jsonify(
			message="INFO",
			filename=filename,
			channels=channels,
			bit_rate=bit_rate,
			frequency=frequency,
			played_time=time_elapsed + "/" + duration)
		response.headers.add('Access-Control-Allow-Origin', '*')
		return response, 200
	except subprocess.CalledProcessError:
		response = jsonify(message="No song playing in audacious")
		response.headers.add('Access-Control-Allow-Origin', '*')
		return response, 404
	except NameError:
		response = jsonify(message="Audacious is not running")
		response.headers.add('Access-Control-Allow-Origin', '*')
		return response, 500


@app.route("/pause")
def play_pause_song():
	try:
		status = get_output("audtool playback-status")
		duration = get_output("audtool current-song-length")
		channels = get_output("audtool current-song-channels")
		time_elapsed = get_output("audtool current-song-output-length")
		bit_rate = get_output("audtool current-song-bitrate-kbps") + " kbps"
		frequency = get_output("audtool current-song-frequency-khz") + " kHz"
		filename = get_output("audtool current-song-filename").split("/")[-1]
		os.system("audacious -u")  # send os command to play/pause songs
		response = jsonify(
			message="PAUSE" if status == "playing" else "RESUME",
			filename=filename,
			channels=channels,
			bit_rate=bit_rate,
			frequency=frequency,
			played_time=time_elapsed + "/" + duration)
		response.headers.add('Access-Control-Allow-Origin', '*')
		return response, 200
	except subprocess.CalledProcessError:
		response = jsonify(message="No song playing in audacious")
		response.headers.add('Access-Control-Allow-Origin', '*')
		return response, 404
	except NameError:
		response = jsonify(message="Audacious is not running")
		response.headers.add('Access-Control-Allow-Origin', '*')
		return response, 500


@app.route("/stop")
def stop_song():
	try:
		duration = get_output("audtool current-song-length")
		channels = get_output("audtool current-song-channels")
		time_elapsed = get_output("audtool current-song-output-length")
		bit_rate = get_output("audtool current-song-bitrate-kbps") + " kbps"
		frequency = get_output("audtool current-song-frequency-khz") + " kHz"
		filename = get_output("audtool current-song-filename").split("/")[-1]
		os.system("audtool playback-stop")
		response = jsonify(
			message="STOP",
			filename=filename,
			channels=channels,
			bit_rate=bit_rate,
			frequency=frequency,
			played_time=time_elapsed + "/" + duration)
		response.headers.add('Access-Control-Allow-Origin', '*')
		return response, 200
	except NameError:
		response = jsonify(message="Audacious is not running")
		response.headers.add('Access-Control-Allow-Origin', '*')
		return response, 500


@app.route("/play")
def play_song():
	try:
		duration = get_output("audtool current-song-length")
		channels = get_output("audtool current-song-channels")
		time_elapsed = get_output("audtool current-song-output-length")
		bit_rate = get_output("audtool current-song-bitrate-kbps") + " kbps"
		frequency = get_output("audtool current-song-frequency-khz") + " kHz"
		filename = get_output("audtool current-song-filename").split("/")[-1]
		os.system("audtool playback-play")
		response = jsonify(
			message="PLAY",
			filename=filename,
			channels=channels,
			bit_rate=bit_rate,
			frequency=frequency,
			played_time=time_elapsed + "/" + duration)
		response.headers.add('Access-Control-Allow-Origin', '*')
		return response, 200
	except subprocess.CalledProcessError:
		response = jsonify(message="No available song to play")
		response.headers.add('Access-Control-Allow-Origin', '*')
		return response, 404
	except NameError:
		response = jsonify(message="Audacious is not running")
		response.headers.add('Access-Control-Allow-Origin', '*')
		return response, 500
