from components.file_logic import FileLogic
from components.help import Help
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
        text_delay("Around you is the medical centre and, well, nothing...")
        print("------------------------------------------------------------------------------")
        user_input = ""
        valid_inputs = ["M", "MEDICAL CENTRE", "MC", "INSIDE", "WEST", "BACK", "C", "CASINO", "EXIT", "QUIT"]
        is_unacceptable = True

        while is_unacceptable:
            if user_input not in valid_inputs:
                user_input = input("What would you like to do? ").upper()
                split_input = user_input.split()
                if split_input != []:
                    if len(split_input) == 2:
                        if split_input[0] == "ENTER" or split_input[0] == "GO" or split_input[0] == "MOVE":
                            user_input = split_input[1]
                    elif len(split_input) == 4:
                        if split_input[0] == "GO" or split_input[1] == "IN" or split_input[0] == "MOVE":
                            user_input = split_input[2] + " " + split_input[3]
                    else:
                        if split_input[0] == "ENTER" or split_input[0] == "GO" or split_input[0] == "MOVE":
                            user_input = split_input[2]
            else:
                is_unacceptable = False

        print("------------------------------------------------------------------------------")

        if user_input == "M" or user_input == "MC" or user_input == "MEDICAL CENTRE" or user_input == "INSIDE":
            player.health = MedicalCentre(player.health).heal()
            FileLogic().update_player_property(PLAYER_FILENAME, player, "Health", player.health)
            print("------------------------------------------------------------------------------")
        elif user_input == "WEST" or user_input == "BACK":
            print("", end="")
            active = False
        elif user_input == "C" or user_input == "CASINO":
            text_delay("You look around and see a casino near the medical centre and decide to go inside.")
            Casino().better_and_runner(player)
            print("------------------------------------------------------------------------------")
        elif user_input == "HELP":
            Help().display_help()
        else:
            print("Goodbye, Thanks For Playing!")
            playing = False
            active = False

    return playing
