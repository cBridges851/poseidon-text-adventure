# Coding Challenge, adventure game!
# Name: (Worked on by John Mason, Christa Briges and Joshua Talbot)
# Student No: 

# Poseidon Adventure Game

# -----------------------------------
import time
import random
from components.file_logic import FileLogic
from components.help import Help
from components.text_delay import text_delay
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

    # Loops until the user specifies that they would like to create a new player or they are a returning player
    while user_input != "N" and user_input != "R":
        user_input = input("Welcome to the Poseidon text adventure! Are you a new(N) or returning(R) player? ").upper()

    if user_input == "N":
        # Creating a new user
        player = Player()
        creating_user = True

        # Make sure a user doesn't already exist.
        while creating_user:
            player.name = input("What is your first name? ")
            # Creates a new player and returns true, or returns false if 
            # there is already a player with the name that the user inputted
            player_exists = FileLogic().add_new_player(PLAYER_FILENAME, player)

            if player_exists:
                print("Player already exists, choose a new name.")
            else:
                # The user has been created, so the process of creating a user 
                # is complete and the loop ends
                creating_user = False 

    if user_input == "R":
        # Read in the current user's stats
        name = input("Welcome back to the program, what name did you use last time? ")
        player = FileLogic().retrieve_player(PLAYER_FILENAME, name)
        
        # Reload the game if user doesn't exist.
        if player is None:
            adventure_game()
            return

    print("------------------------------------------------------------------------------")
    playing = True

    while playing:
        # Main square leading off to further game areas
        text_delay("You find yourself in the main square of PebbleTown...")

        # Get user direction input.
        direction = ""
        valid_inputs = ["N", "E", "S", "W", "NORTH", "EAST", "SOUTH", "WEST", "EXIT", "QUIT", "HELP"]
        is_unacceptable = True

        # If the input isn't in the list ask again.
        while is_unacceptable:
            # If the value the user inputted is not one of the elements in the valid_inputs list
            if direction not in valid_inputs:
                direction = input("Where would you like to go?: ").upper()
                split_direction = direction.split()

                if split_direction != []:
                    # Sees if the first inputted word is "GO" or "MOVE"
                    if split_direction[0] == "GO" or split_direction[0] == "MOVE":
                        # The direction for the user to move will be the second inputted word
                        direction = split_direction[1]
            else:
                is_unacceptable = False

        print("------------------------------------------------------------------------------")

        # Action depending on the direction.
        if direction == "N" or direction == "NORTH":
            playing = go_north(player, playing)
        elif direction == "E" or direction == "EAST":
            playing = go_east(player, playing)
        elif direction == "S" or direction == "SOUTH":
            playing = go_south(player, playing)
        elif direction == "W" or direction == "WEST":
            playing = go_west(player, playing)
        elif direction == "HELP":
            Help().display_help()
        else:
            print("Goodbye, Thanks For Playing!")
            playing = False

# Driver function
if __name__ == "__main__":
    adventure_game()
