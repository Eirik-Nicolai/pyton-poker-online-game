import pygame as pg

from card   import Card, CardInUse
from player import Player
from table  import Table
from consts import POSITION, NUMBER, SCALE

class Game():
    def __init__(self):
#       self._me
        self._players = []
        self._table = Table()
        self._deck = {}

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

    def load_player(self, index, player):
        if index == 0:
            self._me = player
        else:
            self._players.append(player)



    def blit_to_surface(self, surf):
        self._me.blit_to_surface(surf)
        for player in self._players:
            if player._connected:
                player.blit_to_surface(surf)

        self._table.blit_to_surface(surf)

        return surf

    #
    #       DEV METHODS
    #

    def init_values(self):
        self._me.set_name("player_1")
        self._me.set_active_state(True)
        self._me.set_connective_state(True)
        self._me.give_hand(
                (self._deck["6C"],self._deck["KS"])
            )
        self._me.set_money(342)
        for i in range(4):
            self._players[i].set_name("player_"+str(i))
            self._players[i].set_active_state(True)
            self._players[i].set_connective_state(True)
            self._players[i].give_hand(
                    (self._deck["2H"],self._deck["AS"])
                )
            print(1342*(i+1))
            self._players[i].set_money(1342*(i+1))

    def test(self):
        print("Inside game class")
