from typing import Tuple, Dict, Any, Type, Callable
import random
import math
from glowing_shooter.server.core.logger import Loggable
from glowing_shooter.server.core.physical_object import PhysicalObject
from glowing_shooter.server.core.callbacks import PlayerCallBackManager
from glowing_shooter.server.core.canon import CustomCanon, SingleFireCanon
from config.default import PLAYER_HP, PLAYER_SPEED


class Player(PhysicalObject, Loggable):
    def __init__(self, uid: str, name: str, canon: Type[CustomCanon] = SingleFireCanon,
                 start_pos: Callable = None,
                 callback_manager: Type[PlayerCallBackManager] = PlayerCallBackManager):
        start_pos = start_pos if start_pos else Player.start_position
        super().__init__(uid, *start_pos(), PLAYER_SPEED, callback_manager=callback_manager)
        self.name = name
        self.hp = PLAYER_HP
        self.canon = canon(self.uid)

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @staticmethod
    def start_position() -> Tuple[float, float, float, float]:
        """ 0 Pi is top
            0.5 Right
            1  Bottom
            1.5 Left"""
        return 1500, 1500, 0, random.uniform(0, 1) * 2 * math.pi

    def shoot(self):
        bullet = self.canon.shoot(self.x, self.y, self.move_direction)
        if bullet:
            for callback in self.on.shoot:
                callback(bullet)

    def update(self, dt) -> None:
        """ dt is in second """
        super().update(dt)
        self.canon.update(dt)

    def serialize_update(self) -> Dict[str, Any]:
        super_dict = super().serialize_update()
        player_dict = {"hp": self.hp}
        return dict(**super_dict, **player_dict)
