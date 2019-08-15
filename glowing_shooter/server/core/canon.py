from typing import Optional
from glowing_shooter.server.core.bullet import BulletFactory, Bullet


class Canon:
    def __init__(self, parent_id: str, reload_time_ms: int, bullet_factory: BulletFactory):
        self.parent_id = parent_id
        self.reload_time_ms = reload_time_ms
        self.next_reload_time_ms = 0
        self.bullet_factory = bullet_factory

    def shoot(self, x: float, y: float, direction: float) -> Optional[Bullet]:
        if self.next_reload_time_ms <= 0:
            self.next_reload_time_ms = self.reload_time_ms
            return self.bullet_factory.create(self.parent_id, x, y, direction)

    def update(self, dt: float) -> None:
        """ dt is in second """
        self.next_reload_time_ms -= dt * 1000


class CustomCanon(Canon):
    def __init__(self, parent_id: str, reload_time_ms: int = 20,
                 bullet_factory: BulletFactory = BulletFactory(600)):
        super().__init__(parent_id, reload_time_ms, bullet_factory)


class SingleFireCanon(CustomCanon):
    pass
