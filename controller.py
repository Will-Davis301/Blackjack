from model import *
from view import *
from support import *
from time import sleep
class Controller:
    def __init__(self):
        self._model = Model(1000, 8)
        self._view = View()
        self._model.get_deck().shuffle_playing_deck()
    
    def play_hand(self):
        dealer = self._model.get_dealer()
        player = self._model.get_player()
        while True:
            bet_size = self._view.prompt_bet(player.get_chips())
            if self.check_bet(bet_size):
                break
            print(INVALID_BET)
        self._model.bet(bet_size)
        self._model.hit(player)
        self._view.display_hands(player, dealer, bet_size)
        sleep(1)
        self._model.hit(dealer)
        self._view.display_hands(player, dealer, bet_size)
        sleep(1)
        self._model.hit(player)
        self._view.display_hands(player, dealer, bet_size)
        sleep(1)
        choice = self._view.normal_prompt_action()

        while choice and player.hand_total() < 21:
            self._model.hit(player)
            self._view.display_hands(player, dealer, bet_size)
            choice = self._view.normal_prompt_action()
        
        while dealer.hand_total() < 17:
            self._model.hit(dealer)
            self._view.display_hands(player, dealer, bet_size)
            sleep(1)
        
        if player.hand_total() > 21 or dealer.hand_total() > player.hand_total():
            print(TOO_MANY)
        
        else:
            self._model.win(bet_size)
            print(f'{WINNER} You now have {player.get_chips()} chips')

    def check_bet(self, bet_size):

        if bet_size > self._model.get_player().get_chips() or bet_size <= 0 or type(bet_size) == float:
            return False
        else:
            return True
