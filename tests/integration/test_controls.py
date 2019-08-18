import math
from tests.utils import fake_get_time

from glowing_shooter.server.core.game import Game
from glowing_shooter.server.core.player import Player

from glowing_shooter.server.entrypoints.player import join_game, handle_left_click, handle_movement


def test_bullet_added_to_game_on_shoot():
    # GIVEN
    p_uid = "super_uid"
    p_name = "super_name"
    shoot_times = 2
    fake_time_array = [0, 0.1, 0.2, 0.3]

    game = Game()
    game.set_get_time(fake_get_time(fake_time_array))
    game.start()

    join_game(game, p_uid, p_name)
    # WHEN
    for time in range(len(fake_time_array) - 1):
        handle_left_click(game, p_uid)
        game.update()
    # THEN
    assert len(game.all_bullets()) == shoot_times


def test_player_move_direction():
    # GIVEN
    p_uid, p_name = "super_uid", "super_name"
    fake_time_array = [0, 0.1, 0.2, 0.3]

    # Move left
    move_direction = - 0.5 * math.pi
    look_direction = math.pi

    def fake_start_pos():
        # In the middle, moving & facing top of the window
        return 1500, 1500, 0, 0

    game = Game()
    game.set_get_time(fake_get_time(fake_time_array))

    player = Player(p_uid, p_name, start_pos=fake_start_pos)

    game.start()
    game.add_player(player)

    # WHEN
    for time in range(len(fake_time_array) - 1):
        handle_movement(game, p_uid, move_direction, look_direction)
        game.update()
    # THEN
    assert player.x < 1500
    assert player.y == 1500
    assert player.look_direction == look_direction
    # TODO:
#   #       - Test the other directions
#   #       - Implement in the .JS the arrow pressed to a moved direction
