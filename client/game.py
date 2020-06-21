import pygame as pg

from card   import Card, CardInUse
from player import Player
from table  import Table
from consts import POSITION, NUMBER, SCALE

class Game():
    def __init__(self):
        self._players = {}
        self._table = Table()
        self._deck = {}

    def handle_connected_players(self, new_players):
        disconnect = len(self._players) > len(new_players)
        for player in new_players:
            if player["id"] not in self._players:
                print("Adding new player ", player)
                newplayer = Player(len(self._players), player["name"])
                newplayer.set_connective_state(True)
                newplayer.set_active_state(True)
                self._players[player["id"]] = newplayer
        if disconnect:
            for player in self._players:
                if player not in new_players:
                    print("Removing player ", player)
                    self._players[player].disconnect()
                    del self._players[player]

    def add_card_to_deck(self, card_id, imagepath):
        c = Card(card_id, imagepath)
        self._deck[card_id] = c
        return True

    def load_background(self, imagepath):
        self._image = pg.image.load(imagepath)
        self._image.convert()
        self.BG = self._image
        self.BG.convert()
        return True

    def load_table(self):
        list = []
        self._table.set_none_card(SCALE["table_card"],
                                  self._deck["back"])
        pos = POSITION["table_cards_position"]
        for i in range(1, 6):
            newpos = (pos[0] + (NUMBER["card_size_w"]*SCALE["table_card"]+ 3)*i,
                      pos[1])
            list.append(CardInUse(newpos,
                                  SCALE["table_card"],
                                  self._deck["2H"]))
        self._table.set_cards(list)

    def load_new_player(self, id, name = None):
        player = Player(len(self._players))
        player.set_name(name)
        player.set_active_state(True)
        player.set_connective_state(True)
        player.set_money(10000)
        self._players[id] = player

    def blit_to_surface(self, surf):
        for (id, player) in self._players.items():
            if player._connected:
                player.blit_to_surface(surf)

        self._table.blit_to_surface(surf)

        return surf

    #
    #       DEV METHODS
    #

    def init_values(self):
        pass

    def test(self):
        print("Inside game class")

if __name__ == '__main__':
    print("game")
