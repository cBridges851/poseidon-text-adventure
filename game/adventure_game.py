# Christa Bridges
# Josh Talbot
# John Mason
# The Adventure Game to end all adventure games
import time
import random
from components.text_delay import text_delay
from components.file_logic import FileLogic
from game_logic.field import enter_field
from game_logic.bank import bank_logic
from game_logic.medical_centre import MedicalCentre
from game_logic.shop import Shop
from game_logic.casino import Casino
from game_logic.boss_battle import boss_battle
from game_logic.game_areas.north import go_north
from game_logic.game_areas.west import go_west
from game_logic.game_areas.east import go_east
from game_logic.game_areas.south import go_south
from models.monster import Monster
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
    
    text_delay("You find yourself in the main square of PebbleTown...")

    playing = True
    while playing == True:
        direction = ""
        while direction != "N" and direction != "S" and direction != "E" and direction != "W" and direction != "EXIT":
            direction = input("Would you like to go North(N), South(S), East(E) or West(W) (Type 'exit' to close the game): ").upper()
        
        print("------------------------------------------------------------------------------")

        if direction == "N":
            playing = go_north(player, playing)

        elif direction == "S":
            playing = go_south(player, playing)

        elif direction == "E":
            playing = go_east(player, playing)

        elif direction == "W":
            playing = go_west(player, playing)

        else:
            print("Goodbye, Thanks For Playing!")
            playing = False

# Driver function
if __name__ == "__main__":
    adventure_game()
