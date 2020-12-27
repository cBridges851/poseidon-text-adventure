from components.text_delay import text_delay 
from game_logic.field import enter_field

def go_west(player, playing):
    '''
    West part of the game map.
    Args:
        player: obj, representing a player.
        playing: obj, representing the active game.
    Returns:
        playing: bool, whether the game should run or not.
    '''
    active = True
    while active:
        text_delay("You see a field in the distance")
        print("Do you want to go in it? (Y/N) (Type 'exit' to close the game): ")
        user_input = ""
        print("------------------------------------------------------------------------------")
        while user_input != "Y" and user_input != "N" and user_input != "EXIT":
            user_input = input("What would you like to do? ").upper()
            print("------------------------------------------------------------------------------")

        if user_input == "Y":
            enter_field(player)
            print("------------------------------------------------------------------------------")
        elif user_input == "N":
            print("", end="")
            active = False
        else:
            print("Goodbye, Thanks For Playing!")
            playing = False
            active = False
    
    return playing