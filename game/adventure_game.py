# Christa Bridges
# Josh Talbot
# John Mason
# The Adventure Game to end all adventure games
import time
import random
from components.text_delay import text_delay
from components.file_logic import FileLogic
from game_logic.game_areas.north import go_north
from game_logic.game_areas.west import go_west
from game_logic.game_areas.east import go_east
from game_logic.game_areas.south import go_south
from models.player import Player

PLAYER_FILENAME = "./player.json"

def adventure_game():
    '''
    Runs the main program.
    '''
    user_input = ""
    while user_input != "N" and user_input != "R":
        user_input = input("Welcome to the Poseidon text adventure! Are you a new(N) or returning(R) player? ").upper()

    if user_input == "N":
        player = Player()
        # Create some new stats the user can use
        player.name = input("What is your first name? ")
        FileLogic().add_new_player(PLAYER_FILENAME, player)

    if user_input == "R":
        # Read in the current users stats
        name = input("Welcome back to the program, what name did you use last time? ")
        player = FileLogic().retrieve_player(PLAYER_FILENAME, name)
        
        if player == None:
            adventure_game()
            return

    playing = True
    while playing == True:
        text_delay("You find yourself in the main square of PebbleTown...")

        direction = ""
        valid_inputs = ["N", "E", "S", "W", "NORTH", "EAST", "SOUTH", "WEST", "EXIT"]
        is_unacceptable = True
        while is_unacceptable:
            if direction not in valid_inputs:
                direction = input("Where would you like to go?: ").upper()
                split_direction = direction.split()
                if split_direction[0] == "GO":
                    direction = split_direction[1]
            else:
                is_unacceptable = False

        print("------------------------------------------------------------------------------")

        if direction == "N" or direction == "NORTH":
            playing = go_north(player, playing)
        elif direction == "E" or direction == "EAST":
            playing = go_east(player, playing)
        elif direction == "S" or direction == "SOUTH":
            playing = go_south(player, playing)
        elif direction == "W" or direction == "WEST":
            playing = go_west(player, playing)
        else:
            print("Goodbye, Thanks For Playing!")
            playing = False

# Driver function
if __name__ == "__main__":
    adventure_game()