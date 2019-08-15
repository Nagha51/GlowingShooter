from config.default import PLAYER_UPDATE_EVENT, TICKRATE_SEC


def background_thread(socket_server, game, logger):
    """Continuously send game status to players """
    logger.debug("Start background infinite loop")
    game.start()
    while game.active:
        socket_server.sleep(TICKRATE_SEC)
        game.update()
        for player_payload in game.serialize_update():
            player_uid = player_payload["me"]["id"]
            logger.debug(f"Send {PLAYER_UPDATE_EVENT} - {player_uid} - {player_payload}")
            socket_server.emit(PLAYER_UPDATE_EVENT, player_payload, room=player_uid)
