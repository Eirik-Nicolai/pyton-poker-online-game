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
        self._image.convert()
        self.imghandler = self._image

    def resize(self, scale):
        self.imghandler = pg.transform.rotozoom(self._image,
                                                    0,
                                                    scale)

    def get_surf(self):
        return self.imghandler
