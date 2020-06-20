import pygame

from card import CardInUse

class Player():
    def __init__(self, player_pos, lcard_values, rcard_values, money_pos, money_size = 28, name = ""):
        self._name = "name"
        self._pos = player_pos

        self._hand = []
        self._hand.append(CardInUse(lcard_values[0],lcard_values[1]))
        self._hand.append(CardInUse(rcard_values[0],rcard_values[1]))

        self._money_pos  = money_pos
        self._money_size = money_size
#       self._money

        self._connected = False
        self._active = False

    def set_name(self, name):
        self._name = name

    def set_money(self, amount):
        font = pygame.font.Font('freesansbold.ttf', self._money_size)
        str_money = "£"
        if amount > 500:
            moneyl = str(amount / 1000).split('.')
            str_money += moneyl[0] + "." + moneyl[1][:1] + "k"
        else:
            str_money += str(amount)
        self._money = font.render(str_money, True, (230,230,230), (0,0,0))

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

    def blit_to_surface(self, surf):
        if self._active:
            for card in self._hand:
                surf.blit(card.get_surf(), card.get_pos())
        surf.blit(self._money, self._money_pos)
        # TODO blit money number thing

    def get_surf(self):
        surf = pg.Surface.Surface(())
        return surf
