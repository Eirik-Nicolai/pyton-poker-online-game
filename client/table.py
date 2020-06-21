import pygame

from card import CardInUse
from consts import *

class Table():
    def __init__(self, card = [], none_card_offset = 0):
        self._cards = []
        self._none_cards_amount = 3
        self._none_card_position_offset = none_card_offset
        self._none_card = CardInUse()
        self._moneypot = 24300

    def blit_to_surface(self, surface):
        for card in self._cards:
            surface.blit(card.get_surf(),
                         card.get_pos())
        for i in range(self._none_cards_amount):
            pos = self._none_card.get_pos()
            posx, posy = (pos[0] - self._none_card_position_offset*i/2,
                          pos[1] - self._none_card_position_offset*i)
            surface.blit(self._none_card.get_surf(),
                         (posx,posy))
            amount = self._moneypot
            font = pygame.font.Font('freesansbold.ttf', 28)
            str_money = "£"
            if amount > 500:
                moneyl = str(amount / 1000).split('.')
                str_money += moneyl[0] + "." + moneyl[1][:1] + "k"
            else:
                str_money += str(amount)
            money_surf = font.render(str_money, True, (250,250,250), (0,0,0))
            surface.blit(money_surf.convert(),
                         POSITION["table_pot_position"])

    def set_none_card(self, scale, card):
        self._none_card = CardInUse(POSITION["table_cards_position"],
                                    scale,
                                    card)
        self._none_card_position_offset = NUMBER["table_none_offset"]

    def set_cards(self, cards):
        self._cards = cards

    def add_card(self, card):
        self._cards.append(card)

if __name__ == '__main__':
    print("table")
