from typing import Dict, Any
import math
from config.default import MAP_SIZE
from glowing_shooter.server.core.logger import Loggable


class PhysicalObject(Loggable):

    def __init__(self, uid: str, x: float, y: float, direction: float, speed: int):
        super().__init__()
        self._uid = uid
        self._x = x
        self._y = y
        self._direction = direction
        self._speed = speed

    @property
    def uid(self) -> str:
        return self._uid

    @uid.setter
    def uid(self, value) -> None:
        self._uid = value

    @property
    def x(self) -> float:
        return self._x

    @x.setter
    def x(self, value) -> None:
        in_map_value = max(0, min(MAP_SIZE, value))
        self._x = round(in_map_value, 2)

    @property
    def y(self) -> float:
        return self._y

    @y.setter
    def y(self, value) -> None:
        in_map_value = max(0, min(MAP_SIZE, value))
        self._y = round(in_map_value, 2)

    @property
    def direction(self) -> float:
        return self._direction

    @direction.setter
    def direction(self, value) -> None:
        self._direction = round(value, 2)

    @property
    def speed(self) -> int:
        return self._speed

    @speed.setter
    def speed(self, value) -> None:
        self._speed = value

    def update(self, dt) -> None:
        """ dt is the delta-time used to calculate speed (distance/second)"""
        self.x += dt * self.speed * math.sin(self.direction)
        # MIND THE "MINUS" OPERATOR, on a web browser "y" point downwards, infinite scrollers ;)
        self.y -= dt * self.speed * math.cos(self.direction)

    def serialize_update(self) -> Dict[str, Any]:
        return {
            "id": self.uid,
            "x": self.x,
            "y": self.y,
            "direction": self.direction
        }
