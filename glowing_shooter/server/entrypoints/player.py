from typing import Tuple, Dict, Any
import logging

from glowing_shooter.server.core.player import Player
from glowing_shooter.server.core.game import Game

logger = logging.getLogger(__name__)


def new_connection(player_sid: str) -> None:
    logger.info(f"Client connection: {player_sid}")


def disconnect(game: Game, player_sid: str) -> None:
    # Might already be auto-magically handled by flask_socketio.SocketIO(monitor_clients=True)
    removed_player_sid = game.remove_player(player_sid)
    if removed_player_sid:
        logger.info(f"Client disconnected: {removed_player_sid}")
    else:
        logger.info(f"Failed to remove player: {player_sid}")


def join_game(game: Game, player_sid: str, username: str) -> Tuple[Player, Dict[str, Any]]:
    player = Player(player_sid, username)
    game.add_player(player)
    logger.info(f"Client: {player_sid} joined the game as {player.name}")
    return player, game.serialize_update_single_player(player)


def handle_movement(game: Game, player_sid: str,
                    move_direction: float, look_direction: float) -> None:
    player = game.get_player(player_sid)
    if player:
        player.move_direction = move_direction
        player.look_direction = look_direction


def handle_left_click(game: Game, player_sid: str) -> None:
    player = game.get_player(player_sid)
    if player:
        player.shoot()
