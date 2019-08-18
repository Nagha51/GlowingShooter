from typing import Dict, Any, Type
import math
from glowing_shooter.server.core.logger import Loggable
from glowing_shooter.server.core.callbacks import DefaultCallbackManager
from glowing_shooter.server.core.rules import PhysicalObjectRules


class PhysicalObject(Loggable):

    def __init__(self, uid: str, x: float, y: float,
                 move_direction: float, look_direction: float,
                 speed: int,
                 callback_manager: Type[DefaultCallbackManager] = DefaultCallbackManager,
                 rule_manager: Type[PhysicalObjectRules] = PhysicalObjectRules):
        super().__init__()
        self.on = callback_manager()
        self.rules = rule_manager()
        self.to_delete = False
        self._uid = uid
        self._x = x
        self._y = y
        self._move_direction = move_direction
        self._look_direction = look_direction
        self._speed = speed
        self.to_left = False
        self.to_right = False
        self.to_top = False
        self.to_down = False

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
        self._x = round(self.rules.x(self, value), 2)

    @property
    def y(self) -> float:
        return self._y

    @y.setter
    def y(self, value) -> None:
        self._y = round(self.rules.y(self, value), 2)

    @property
    def move_direction(self) -> float:
        return self._move_direction

    @move_direction.setter
    def move_direction(self, value) -> None:
        self._move_direction = value

    @property
    def look_direction(self) -> float:
        return self._look_direction

    @look_direction.setter
    def look_direction(self, value) -> None:
        self._look_direction = value

    @property
    def speed(self) -> int:
        return self._speed

    @speed.setter
    def speed(self, value) -> None:
        self._speed = value

    def update(self, dt) -> None:
        """ dt is the delta-time in second used to calculate position given speed (v = dist/dt)"""
        if self.to_delete:
            self.delete()
        else:
            self.x += dt * self.speed * math.sin(self.move_direction)
            # MIND THE "MINUS" OPERATOR, on a web browser "y" point downwards, infinite scrollers ;)
            self.y -= dt * self.speed * math.cos(self.move_direction)

    def serialize_update(self) -> Dict[str, Any]:
        return {
            "id": self.uid,
            "x": self.x,
            "y": self.y,
            "direction": self.look_direction
        }

    def delete(self):
        for callback in self.on.delete:
            callback(self)
