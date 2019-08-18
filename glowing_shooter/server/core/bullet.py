from typing import Type
from uuid import uuid4

from glowing_shooter.server.core.physical_object import PhysicalObject
from glowing_shooter.server.core.rules import PhysicalObjectRules, SimpleBullet


class Bullet(PhysicalObject):
    def __init__(self, parent_id: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parent_id = parent_id


class BulletFactory:
    def __init__(self, bullet_speed,
                 rule_manager: Type[PhysicalObjectRules] = SimpleBullet):
        self.bullet_speed = bullet_speed
        self.rule_manager = rule_manager

    def create(self, parent_id: str, x: float, y: float, direction: float) -> Bullet:
        return Bullet(parent_id, str(uuid4()), x, y, direction, direction, self.bullet_speed,
                      rule_manager=self.rule_manager)
