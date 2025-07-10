from controller import *
from support import *
def main():
    print(WELCOME_MESSAGE)
    controller = Controller()
    controller.play_hand()
    while controller._model.get_player().get_chips() > 0:
        user_input = input(CONTINUE_PLAY).lower().strip()
        if user_input == 'leave':
            break
        controller.play_hand()
    print(f'{GOODBYE_MESSAGE} You left the table with {controller._model.get_player().get_chips()} chips')

if __name__ == "__main__":
    main()