import logging
from flask_socketio import emit
from flask import request

from glowing_shooter.server.core.flaskio_server import socketio, game

from glowing_shooter.server.core.player import Player
from config.default import PLAYER_UPDATE_EVENT, PLAYER_INPUT_EVENT

logger = logging.getLogger(__name__)


@socketio.on("connect")
def new_connection():
    logger.info(f"Client connection: {request.sid}")
    emit("info", {"message": "Hello you !"})


@socketio.on("disconnect")
def disconnect():
    # Might already be auto-magically handled by flask_socketio.SocketIO(monitor_clients=True)
    removed_player_sid = game.remove_player(request.sid)
    if removed_player_sid:
        logger.info(f"Client disconnected: {removed_player_sid}")
    else:
        logger.info(f"Failed to remove player: {request.sid}")


@socketio.on("join_game")
def join_game(username):
    player = Player(request.sid, username)
    game.add_player(player)
    logger.info(f"Client: {request.sid} joined the game as {player.name}")
    emit("info", {"message": f"Welcome into the game {player.name}"})
    emit(PLAYER_UPDATE_EVENT, game.serialize_update_by_player(player), room=player.uid)


@socketio.on(PLAYER_INPUT_EVENT)
def handle_input(direction):
    player = game.get_player(request.sid)
    if player:
        player.direction = direction
