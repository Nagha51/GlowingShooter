import pytest
from tests.utils import fake_get_time

from glowing_shooter.server.core.game import Game
from glowing_shooter.server.core.player import Player

from glowing_shooter.server.entrypoints.player import join_game, handle_left_click


def test_everything_works():
    print("Bip boop running tests")
    assert True


def test_bullet_added_to_game_on_shoot():
    # GIVEN
    p_uid = "super_uid"
    p_name = "super_name"
    shoot_times = 3
    fake_time_array = [0, 0.1, 0.2, 0.3]

    game = Game()
    game.set_get_time(fake_get_time(fake_time_array))
    game.start()

    join_game(game, p_uid, p_name)
    # WHEN
    for time in range(len(fake_time_array)-1):
        handle_left_click(game, p_uid)
        game.update()
    # THEN
    assert len(game.all_bullets()) == shoot_times


@pytest.mark.skip
def test_bullet_removed_from_game_on_map_edge():
    # GIVEN
    p_uid = "super_uid"
    p_name = "super_name"
    fake_time_array = [0, 0.1, 0.2, 0.3]

    def fake_start_pos():
        # In the corner facing top of the window
        return 1, 1, 0

    game = Game()
    game.set_get_time(fake_get_time(fake_time_array))
    game.start()

    player = Player(p_uid, p_name, start_pos=fake_start_pos)
    game.add_player(player)
    # WHEN
    for time in range(len(fake_time_array)-1):
        player.shoot()
        game.update()
    # THEN

    assert len(game.all_bullets()) == 0
    # TODO: Implement it =D
