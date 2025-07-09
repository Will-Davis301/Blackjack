from random import shuffle
class Card():
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
    
class PlayingDeck():
    #Add deck pen/high low system
    def __init__(self, num_of_decks):
        self._playing_deck = [card for a in range(num_of_decks) for card in self.generate_deck()]
        
    def generate_deck(self):
        deck_symbols = [str(i) for i in range(2,11)] + list('JQKA')
        deck_suits = 'spades diamonds clubs hearts'.split()
        deck = []
        for suit in deck_suits:

            for symbol in deck_symbols:
                try:
                    value = int(symbol)

                except:
                    if symbol == "A":
                        value = [1, 11]
                    else:
                        value = 10

                deck.append(Card(value, suit, symbol))

        return deck
        
    def shuffle_playing_deck(self):
        shuffle(self._playing_deck)

    def get_next_card(self):
        return self._playing_deck.pop()
    
    def get_deck(self):
        return self._playing_deck
    
    def num_of_cards_left(self):
        return len(self._playing_deck)