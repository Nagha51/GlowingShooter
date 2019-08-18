from tests.utils import fake_get_time

from glowing_shooter.server.core.game import Game
from glowing_shooter.server.core.player import Player


def test_everything_works():
    print("Bip boop running tests")
    assert True


def test_bullet_removed_from_game_on_map_edge():
    # GIVEN
    p_uid = "super_uid"
    p_name = "super_name"
    fake_time_array = [0, 0.1, 0.2, 0.3, 2, 2]

    def fake_start_pos():
        # In the corner, moving & facing to top of the window
        return 1, 1, 0, 0

    game = Game()
    game.set_get_time(fake_get_time(fake_time_array))
    game.start()

    player = Player(p_uid, p_name, start_pos=fake_start_pos)
    game.add_player(player)
    # WHEN
    shoot_frames = range(len(fake_time_array) - 1)
    for time in shoot_frames[0:2]:
        player.shoot()
        game.update()
    for time in shoot_frames[2:-1]:
        game.update()

    # THEN

    assert len(game.all_bullets()) == 0
