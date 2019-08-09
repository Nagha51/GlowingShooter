import asyncio
from flask import Flask, render_template, send_from_directory, request
from flask_socketio import SocketIO, emit
from config.default import assets_path, dist_path
from glowing_shooter.server.core.game import Game
from glowing_shooter.server.core.player import Player
from glowing_shooter.server.core.state import create_update_payload

app = Flask(__name__)

socketio = SocketIO(app)

game = Game()


def configure_app(app):
    app.template_folder = dist_path
    app.static_folder = dist_path
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/<path:filename>")
def serve_static_file(filename: str):
    return app.send_static_file(filename)


@app.route("/assets/<path:filename>")
def serve_assets_file(filename: str):
    return send_from_directory(assets_path, filename)


@socketio.on("connect")
def new_connection():
    print(f"Client connection: {request.sid}")
    emit("info", {"message": "Hello you !"})


@socketio.on("disconnect")
def disconnect():
    removed_player_sid = game.remove_player(request.sid)
    if removed_player_sid:
        print(f"Client disconnected: {removed_player_sid}")
    else:
        print(f"Failed to remove player: {request.sid}")


@socketio.on("join_game")
def join_game(username):
    player = Player(request.sid, username)
    game.add_player(player)
    print(f"Client: {request.sid} joined the game as {player.name}")
    emit("info", {"message": f"Welcome into the game {player.name}"})
    emit("update", create_update_payload(player))


def run(host: str, port: int):
    configure_app(app)
    print(f"Running flaskio server on {host}:{port}")
    socketio.run(app, host=host, port=port)
