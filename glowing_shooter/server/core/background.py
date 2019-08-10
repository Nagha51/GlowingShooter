import logging
from flask_socketio import emit

from glowing_shooter.server.core.state import create_update_payload
from config.default import UPDATE_EVENT, TICKRATE_SEC


def background_thread(socket_server, game, logger):
    """Continuously send game status to players """
    logger.debug("Start background infinite loop")
    while True:
        socket_server.sleep(TICKRATE_SEC)
        for player_sid, player_inst in game.all_players().items():
            update_payload = create_update_payload(player_inst)
            logger.debug(f"Send {UPDATE_EVENT} - {player_sid} - {update_payload}")
            socket_server.emit(UPDATE_EVENT, update_payload, room=player_sid)
