
from player import Player

class Game():
    def __init__(self):
        self._players = []
        self._rounds = []
        self.colour = [0,0,0]
        #self._current_round

    def test(self):
        print("Inside game class")
