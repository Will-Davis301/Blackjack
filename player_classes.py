class Entity:
    def __init__(self):
        self._hand = []

    def hand_total(self):
        total = 0
        num_of_soft_aces = 0

        for card in self._hand:
            card_value = card.get_value()

            if (card.get_symbol()) == 'A':
                if total < 11:
                    num_of_soft_aces += 1
                    card_value = 11

                else:
                    card_value = 1

            total += card_value

        while num_of_soft_aces and total > 21:
            total -= 10
            num_of_soft_aces -= 1

        return total

    def __str__(self):
        return "Dealer"
    
    def get_hand(self):
        return self._hand
    
class Player(Entity):
    def __init__(self, chips):
        super().__init__()
        self._chips = chips
    
    def get_chips(self):
        return self._chips
    
    def __str__(self):
        return "Player"
    
    def add_chips(self, num_of_chips):
        self._chips += num_of_chips

    