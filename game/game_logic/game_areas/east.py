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
        text_delay("In front of you is the medical centre.")
        print("Do you want to enter (Y/N) (Type 'exit' to close the game): ")
        user_input = ""
        print("------------------------------------------------------------------------------")
        while user_input != "Y" and user_input != "N" and user_input != "EXIT" and user_input != "C":
            user_input = input("What would you like to do? ").upper()
            print("------------------------------------------------------------------------------")

        if user_input == "Y":
            MedicalCentre(player).enter_medical_centre()
            print("------------------------------------------------------------------------------")
        elif user_input == "N":
            print("", end="")
            active = False
        elif user_input == "C":
            text_delay("You look around and see a casino near the medical centre and decide to go inside.")
            Casino().better_and_runner(player)
            print("------------------------------------------------------------------------------")
        else:
            print("Goodbye, Thanks For Playing!")
            playing = False
            active = False

    return playing
