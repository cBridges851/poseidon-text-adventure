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
        user_input = ""
        valid_inputs = ["F", "FIELD", "RUN AWAY", "EAST", "EXIT"]
        is_unacceptable = True
        while is_unacceptable:
            if user_input not in valid_inputs:
                user_input = input("What would you like to do? ").upper()
                split_input = user_input.split()
                if split_input[0] == "ENTER" or split_input[0] == "GO":
                    user_input = split_input[1]
            else:
                is_unacceptable = False

        print("------------------------------------------------------------------------------")

        if user_input == "F" or user_input == "FIELD":
            enter_field(player)
            print("------------------------------------------------------------------------------")
        elif user_input == "EAST" or user_input == "RUN AWAY":
            print("", end="")
            active = False
        else:
            print("Goodbye, Thanks For Playing!")
            playing = False
            active = False
    
    return playing