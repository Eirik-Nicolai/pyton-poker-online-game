import pygame as pg

class Card():
    def __init__(self, id, imagepath):
        if id == "back":
            self._rank = None
            self._suit = None
        else:
            card = id.split(".")[0]
            self._rank = card[0]
            self._suit = card[1]

        self._image = pg.image.load(imagepath)

    def get_surf(self):
        return self._image


class CardInUse():
    def __init__(self, pos=(0,0), scale=1, card=None):
        self._pos = pos
        self._scale = scale
        self._card = card

    def set_card(self, card):
        self._card = card

    def get_surf(self):
        return pg.transform.rotozoom(self._card.get_surf(),
                                     0,
                                     self._scale).convert_alpha()

    def get_pos(self):
        return self._pos


if __name__ == '__main__':
    print("card")
