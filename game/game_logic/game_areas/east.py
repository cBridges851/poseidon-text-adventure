from components.file_logic import FileLogic
from components.text_delay import text_delay 
from game_logic.casino import Casino
from game_logic.medical_centre import MedicalCentre

PLAYER_FILENAME = "./player.json"

def go_east(player, playing):
    '''
    East part of the game map.
    Args:
        player: obj, representing a player.
        playing: obj, representing the active game.
    Returns:
        playing: bool, whether the game should run or not.
    '''
    active = True
    while active:
        text_delay("Around you is the medical centre and well nothing...")
        print("------------------------------------------------------------------------------")
        user_input = ""
        valid_inputs = ["M", "MEDICAL CENTRE", "MC", "WEST", "C", "CASINO", "EXIT"]
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

        if user_input == "M" or user_input == "MC" or user_input == "MEDICAL CENTRE":
            player.health = MedicalCentre(player.health).heal()
            FileLogic().update_player_property(PLAYER_FILENAME, player, "Health", player.health)
            print("------------------------------------------------------------------------------")
        elif user_input == "WEST":
            print("", end="")
            active = False
        elif user_input == "C" or user_input == "CASINO":
            text_delay("You look around and see a casino near the medical centre and decide to go inside.")
            Casino().better_and_runner(player)
            print("------------------------------------------------------------------------------")
        else:
            print("Goodbye, Thanks For Playing!")
            playing = False
            active = False

    return playing
