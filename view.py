from support import *
class View:
    
    def display_hands(self, player, dealer, bet_size):
        player_output = dealer_output = ""
        player_hand = player.get_hand()
        dealer_hand = dealer.get_hand()
        for card in player_hand:
            player_output += f" {card.get_symbol()}"

        for card in dealer_hand:
            dealer_output += f" {card.get_symbol()}"
        

        print(f"{str(dealer)}: {dealer_output} \nTotal: {dealer.hand_total()}")
        
        print(f"{str(player)}: {player_output} \nTotal: {player.hand_total()}\nCurrent Bet: {bet_size}")
        
        print("###############################################################################")
    
    def prompt_bet(self, current_chips):
        while True:
            try:
                bet = int(input(f'Currently you have {current_chips} number of chips. {BET_PROMPT}'))
                print(f"You have bet: {bet}")
                return bet
            except ValueError:
                print(INVALID_INPUT)

    def normal_prompt_action(self):
        while True:
            action = input(ACTION_MESSAGE).lower().strip()
            
            if action:
                return True
            
            return False
