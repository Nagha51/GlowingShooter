from typing import Optional, Dict, List, Any

import time
from glowing_shooter.server.core.logger import Loggable
from glowing_shooter.server.core.player import Player
from config.default import LOGGER_LEVEL_TRACE


class Game(Loggable):
    def __init__(self):
        super().__init__()
        self.players = dict()
        self.last_update_time = round(time.time(), 2)
        self.logger = None

    def add_player(self, player: Player) -> None:
        self.players[player.uid] = player

    def remove_player(self, player_uid: int) -> Optional[Player]:
        return self.players.pop(player_uid, None)

    def get_player(self, player_uid: int) -> Optional[Player]:
        return self.players.get(player_uid, None)

    def all_players(self) -> Dict[str, Player]:
        return self.players

    def update(self) -> None:
        now = round(time.time(), 2)
        dt = now - self.last_update_time
        self.last_update_time = now
        self.get_logger().log(LOGGER_LEVEL_TRACE, f"DeltaTime elapsed since last game update: {dt}")
        for player_sid, player in self.all_players().items():
            player.update(dt)

    def serialize_update_by_player(self, player: Player) -> Dict[str, Any]:
        return {
            "t": self.last_update_time*1000,
            "me": player.serialize_update(),
            "others": [],
            "bullets": []
        }

    def serialize_update(self) -> List[Dict[str, Any]]:
        return [self.serialize_update_by_player(player) for player in self.all_players().values()]
