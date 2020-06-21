from player import Player

class Game():
    def __init__(self):
        self._players = {}
        self._table = None


    def get_player(self, id):
        for player in self._players:
            if id == player._id:
                return player

    def add_player(self, id):
        player = Player()
        player.set_active_state(True)
        self._players[str(id)] = player
