from flask_socketio import emit
from flask import request

from glowing_shooter.server.core.flaskio_server import socketio, game

from glowing_shooter.server.entrypoints.player import disconnect, handle_movement, handle_left_click, join_game, \
    new_connection
from config.default import PLAYER_UPDATE_EVENT, PLAYER_LEFT_CLICK_EVENT, PLAYER_LOOK_EVENT, PLAYER_MOVE_EVENT


@socketio.on("connect")
def io_new_connection() -> None:
    new_connection(request.sid)
    emit("info", {"message": "Hello you !"})


@socketio.on("disconnect")
def io_disconnect() -> None:
    # Might already be auto-magically handled by flask_socketio.SocketIO(monitor_clients=True)
    disconnect(game, request.sid)


@socketio.on("join_game")
def io_join_game(username) -> None:
    player, game_update = join_game(game, request.sid, username)
    emit("info", {"message": f"Welcome into the game {player.name}"})
    emit(PLAYER_UPDATE_EVENT, game_update, room=player.uid)


@socketio.on(PLAYER_MOVE_EVENT)
def io_handle_move(move_direction) -> None:
    handle_movement(game, request.sid, move_direction=move_direction)


@socketio.on(PLAYER_LOOK_EVENT)
def io_handle_look(look_direction) -> None:
    handle_movement(game, request.sid, look_direction=look_direction)


@socketio.on(PLAYER_LEFT_CLICK_EVENT)
def io_handle_left_click() -> None:
    handle_left_click(game, request.sid)
