from glowing_shooter.server.core.canon import CustomCanon


def test_single_fire_cannon_reload_time():
    # GIVEN
    criminal_id = "Gargamel"
    reload_time_sec = 0.020
    reload_time_ms = int(reload_time_sec * 1000)
    canon = CustomCanon(criminal_id, reload_time_ms=reload_time_ms)
    #                   SHOOT - SHOOT - WAIT - SHOOT
    fake_time_array = [0, reload_time_sec, reload_time_sec - 0.005, 2 * reload_time_sec]
    expected_bullets = 3

    bullet_shoot = []
    # WHEN
    for time_delta in fake_time_array:
        canon.update(time_delta)
        bullet = canon.shoot(0, 0, 0)
        if bullet:
            bullet_shoot.append(bullet)

    # THEN
    assert len(bullet_shoot) == expected_bullets
