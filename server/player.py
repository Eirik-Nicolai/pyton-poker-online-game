class Player():
    def __init__(self):
        self._name = "player"
        self._hand = []

        self._money = 0


    def set_name(self, name):
        if name is not None: self._name = name

    def set_money(self, amount):
        self._money = amount

    def give_hand(self, cards):
        pass
        #self._hand[0].set_card(cards[0])
        #self._hand[1].set_card(cards[1])

    def set_active_state(self, active):
        self._active = active
        if not active:
            pass
            #self._hand[0] = None
            #self._hand[1] = None

if __name__ == '__main__':
    print("player")
