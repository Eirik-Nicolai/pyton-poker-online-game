import pygame

from card import CardInUse
from consts import *

class Player():
    def __init__(self, player_index, name = None, money_size = 28, action_size = 26):
        self._pos = (0,0)
        if name is None:
            self._name = "player_"+str(player_index)
        else:
            self._name = name

        self._hand = []
        self._hand.append(CardInUse(POSITION["player_"+str(player_index)+"_card_left"],
                                    SCALE["player_"+str(player_index)]
                                    ))
        self._hand.append(CardInUse(POSITION["player_"+str(player_index)+"_card_right"],
                                    SCALE["player_"+str(player_index)]
                                    ))

        self._money_pos  = POSITION["player_"+str(player_index)+"_money"]
        self._money_size = money_size
        self._money_surf = None

        self._action_pos  = POSITION["player_"+str(player_index)+"_action"]
        self._action_size = action_size
        self._action_surf = None

        self._connected = False
        self._active = False

    def set_name(self, name):
        if name is not None: self._name = name

    def set_money(self, amount):
        self._money_surf = self.get_string_surf(self.money_formatted(amount),
                                                self._money_size,
                                                (255,255,255))
    def disconnect(self):
        pass
        #do things ? 

    def give_hand(self, cards):
        self._hand[0].set_card(cards[0])
        self._hand[1].set_card(cards[1])

    def set_connective_state(self, active):
        self._connected = active
        #destroy object

    def set_active_state(self, active):
        self._active = active
        if not active:
            pass
            #self._hand[0] = None
            #self._hand[1] = None

    def action_fold(self):
        self.set_active_state(False)
        self._action_surf = self.get_string_surf("RAISE\n£1.0k",self._action_size,(255,255,255))

    def action_raise(self, amount):
        self._action_surf = self.get_string_surf("CHECK",
                                            self._action_size,
                                            (255,255,255))

    def action_check(self):
        self._action_surf = self.get_string_surf("CHECK",
                                            self._action_size,
                                            (255,255,255))

    def money_formatted(self, amount):
        str_money = "£"
        if amount > 500:
            moneyl = str(amount / 1000).split('.')
            str_money += moneyl[0] + "." + moneyl[1][:1] + "k"
        else:
            str_money += str(amount)
        return str_money

    def get_string_surf(self, text, size, colour_front, colour_back = (0,0,0)):
        font = pygame.font.Font('freesansbold.ttf', size)
        return font.render(text, True, colour_front, colour_back)

    def blit_to_surface(self, surf):
        if self._active:
            for card in self._hand:
                if card._card is not None:
                    surf.blit(card.get_surf(), card.get_pos())
        surf.blit(self.get_string_surf(self._name,self._action_size,(255,255,255)),
                  card.get_pos())
        if self._money_surf is not None:
            surf.blit(self._money_surf, self._money_pos)
        if self._action_surf is not None:
            surf.blit(self._action_surf, self._action_pos)

if __name__ == '__main__':
    print("player")
