from typing import Optional, Dict, List, Any, Callable

import time

from glowing_shooter.server.core.bullet import Bullet
from glowing_shooter.server.core.logger import Loggable
from glowing_shooter.server.core.player import Player
from config.default import LOGGER_LEVEL_TRACE


class Game(Loggable):
    def __init__(self):
        super().__init__()
        self.players = dict()
        self.bullets = list()
        self.last_update_time = None
        self.logger = None
        self.get_time = lambda: round(time.time(), 2)
        self.active = False

    def set_get_time(self, func: Callable):
        """ Mostly defined for tests purpose """
        self.get_time = func

    def start(self):
        self.active = True
        self.last_update_time = self.get_time()

    def stop(self):
        self.active = False

    def add_player(self, player: Player) -> None:
        self.players[player.uid] = player
        player.on.shoot.append(self.add_bullet)

    def remove_player(self, player_uid: str) -> Optional[Player]:
        return self.players.pop(player_uid, None)

    def get_player(self, player_uid: str) -> Optional[Player]:
        return self.players.get(player_uid, None)

    def all_players(self) -> Dict[str, Player]:
        return self.players

    def add_bullet(self, bullet: Bullet) -> None:
        self.bullets.append(bullet)
        bullet.on.delete.append(self.remove_bullet)

    def remove_bullet(self, bullet: Bullet) -> None:
        self.bullets.remove(bullet)

    def all_bullets(self) -> List[Bullet]:
        return self.bullets

    def update(self) -> None:
        now = self.get_time()
        dt = now - self.last_update_time
        self.last_update_time = now
        self.get_logger().log(LOGGER_LEVEL_TRACE, f"DeltaTime elapsed since last game update: {dt}")
        for player_sid, player in self.all_players().items():
            player.update(dt)
        for bullet in self.all_bullets():
            bullet.update(dt)

    def serialize_update_all_players(self) -> Dict[str, Any]:
        return {player_id: player_instance.serialize_update()
                for player_id, player_instance in self.all_players().items()}

    def serialize_update_all_bullets(self) -> List[Dict]:
        return [bullet.serialize_update() for bullet in self.all_bullets()]

    def serialize_update_by_player(self, player: Player, all_players_serialized: Dict[str, Any],
                                   all_bullets_serialized: List[Any]) -> Dict[str, Any]:
        all_others = [player_deserialized for some_player_uid, player_deserialized in all_players_serialized.items()
                      if some_player_uid != player.uid]
        return {
            "t": self.last_update_time * 1000,
            "me": all_players_serialized[player.uid],
            "others": all_others,
            "bullets": all_bullets_serialized
        }

    def serialize_update_single_player(self, player: Player) -> Dict[str, Any]:
        all_serialized_players = self.serialize_update_all_players()
        all_serialized_bullets = self.serialize_update_all_bullets()
        return self.serialize_update_by_player(player, all_serialized_players, all_serialized_bullets)

    def serialize_update(self) -> List[Dict[str, Any]]:
        all_serialized_players = self.serialize_update_all_players()
        all_serialized_bullets = self.serialize_update_all_bullets()
        return [self.serialize_update_by_player(player_instance, all_serialized_players, all_serialized_bullets) for
                player_instance in self.all_players().values()]
