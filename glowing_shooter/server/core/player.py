from typing import Tuple, Dict, Any
import random
import math
from glowing_shooter.server.core.logger import Loggable
from glowing_shooter.server.core.physical_object import PhysicalObject
from config.default import PLAYER_HP, PLAYER_SPEED


class Player(PhysicalObject, Loggable):
    def __init__(self, uid: str, name: str):
        super().__init__(uid, *self.start_position(), PLAYER_SPEED)
        self.name = name
        self.hp = PLAYER_HP

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @staticmethod
    def start_position() -> Tuple[float, float, float]:
        return 1500, 1500, random.uniform(0, 1) * 2 * math.pi

    def update(self, dt) -> None:
        super().update(dt)

    def serialize_update(self) -> Dict[str, Any]:
        super_dict = super().serialize_update()
        player_dict = {"hp": self.hp}
        return dict(**super_dict, **player_dict)
