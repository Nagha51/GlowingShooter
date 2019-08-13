from glowing_shooter.server.core.physical_object import PhysicalObject
from uuid import uuid4


class Bullet(PhysicalObject):
    def __init__(self, parent_id: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parent_id = parent_id


class BulletFactory:
    def __init__(self, bullet_speed):
        self.bullet_speed = bullet_speed

    def create(self, parent_id: str, x: float, y: float, direction: float) -> Bullet:
        return Bullet(parent_id, str(uuid4()), x, y, direction, self.bullet_speed)
