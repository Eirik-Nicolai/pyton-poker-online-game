import pygame as pg

from card   import Card

from player import Player
from table  import Table
from consts import CARD, NUMBER

class Game():
    def __init__(self):
        self._me = Player()
        self._players = []
        self._table = Table()
        self._deck = {}

        self.pos = (0,0)
        self.card_scale = 1


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


    def blit_players(self):
        surf = pg.Surface.Surface((NUMBER["game_width"],NUMBER["game_height"]))
        surf.blit(self._me.surf)


    #
    #       DEV METHODS
    #

    def set_card_pos(self, pos):
        self.pos = pos
        print(self.pos)

    def set_card_size(self, scale):
        self.card_scale += scale
        print(self.card_scale)
        self._deck["2H"].resize(self.card_scale)

    def test(self):
        print("Inside game class")
