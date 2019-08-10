import random
import math
from glowing_shooter.server.core.physical_object import PhysicalObject

PLAYER_HP = 100

class Player(PhysicalObject):
    def __init__(self, sid: int, name: str):
        super().__init__(0, 0, random.uniform(0, 1) * 2 * math.pi)
        self.sid = sid
        self.name = name
        self.hp = PLAYER_HP

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    def serialize_update(self):
        return {
            "id": self.sid,
            "x": self.x,
            "y": self.y,
            "direction": self.direction,
            "hp": self.hp,
        }
