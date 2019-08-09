import time
from glowing_shooter.server.core.player import Player


def create_update_payload(player: Player):
    payload = {
        "t": time.time(),
        "me": player.serialize_update(),
        "others": [],
        "bullets": []
    }
    return payload
