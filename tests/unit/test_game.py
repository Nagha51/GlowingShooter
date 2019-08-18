from glowing_shooter.server.core.game import Game
from glowing_shooter.server.core.bullet import Bullet


def test_remove_bullet_twice_is_safe():
    # GIVEN
    game = Game()
    bullet = Bullet("puid", "buid", 0, 0, 0, 0, 0)
    game.add_bullet(bullet)
    # WHEN
    bullet.delete()
    bullet.delete()
    # THEN
    assert len(game.all_bullets()) == 0
