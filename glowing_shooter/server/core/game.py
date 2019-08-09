from glowing_shooter.server.core.player import Player


class Game:
    def __init__(self):
        self.players = dict()

    def add_player(self, player: Player):
        self.players[player.session_id] = player

    def remove_player(self, player_sid: int):
        return self.players.pop(player_sid, None)

    def get_player(self, player_sid: int):
        return self.players.get(player_sid, None)
