from support import *
class View:
    def display_welcome_message(self):
        print(WELCOME_MESSAGE)
    
    def display_hand(self, entity):
        hand = entity.get_hand()
        for 
    
    def prompt_bet(self):
        while True:
            try:
                bet = int(input("Enter your bet amount: "))
                print(f"You have bet: {bet}")
                return bet
            except ValueError:
                print("Invalid input. Please enter a number.")

    def prompt_action(self):
        while True:
            action = input(ACTION_MESSAGE).strip().lower()
            if action in ['hit', 'stay']:
                return action
            print(INVALID_INPUT)

    def display_goodbye(self, chips):
        print(f'{GOODBYE_MESSAGE} You left the table with {chips} chips')