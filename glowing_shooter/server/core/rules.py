from typing import Callable
from config.default import MAP_SIZE


class PhysicalObjectRules:
    def __init__(self, x: Callable = None, y: Callable = None):
        self.x = x if x else PhysicalObjectRules.x_rule
        self.y = y if y else PhysicalObjectRules.y_rule

    @staticmethod
    def x_rule(obj, value):
        return max(0, min(MAP_SIZE, value))

    @staticmethod
    def y_rule(obj, value):
        return max(0, min(MAP_SIZE, value))


class SimpleBullet(PhysicalObjectRules):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
