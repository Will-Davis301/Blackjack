import collections
from random import shuffle
class Card:
    def __init__(self, value, suit, symbol):
        self._value = value
        self._suit = suit
        self._symbol = symbol
    
    def __repr__(self):
        return f'Card({self._value!r}, {self._suit!r}, {self._symbol!r})'
    
    def get_value(self):
        return self._value
    
    def get_suit(self):
        return self._suit
    
    def get_symbol(self):
        return self._symbol
    
class Deck:
    def __init__(self):
        self._deck = []
    
    def get_next_card(self):
        return self._deck.pop()
    
    def shuffle_deck(self):
        shuffle(self._deck)
    
    