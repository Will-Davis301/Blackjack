import card_classes
import player_classes
class controller():
    def __init__(self, chips, num_of_decks):
        self._player = player_classes.Player(chips)
        self._dealer = player_classes.Entity
        self._deck = card_classes.PlayingDeck(num_of_decks)
        self._bet = 0
    
    def get_player(self):
        return self._player
    
    def get_dealer(self):
        return self._dealer
    
    def get_deck(self):
        return self._deck
    
    def hit(self, entity):
        entity.get_hand().append(self._deck.get_next_card())
    
    def bet(self, bet_size):
        self._player.add_chips(-bet_size) # - Removes chips
        self._bet += bet_size
    
    def win(self, num_of_chips):
        self._player.add_chips(num_of_chips)
    