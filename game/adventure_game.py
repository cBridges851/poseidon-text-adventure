# Christa Bridges
# Josh Talbot
# John Mason
# The Adventure Game to end all adventure games
import time
import random
from monster import Monster
from player import Player
from text_delay import text_delay
from file_logic import FileLogic
from monster_fight import monster_fight
from bank import bank_logic
from medical_centre import MedicalCentre
from shop import Shop
from casino import Casino

BANK_FILENAME = "./bank.txt"

def adventure_game():
    '''
    Runs the main program.
    '''
    user_input = input("Welcome to PebbleTown are you a new(N) or returning(R) player? ").upper()

    while user_input != "N" and user_input != "R":
        user_input = input("Welcome to the Poseidon text adventure! Are you a new(N) or returning(R) player? ").upper()
    
    player = Player()

    if user_input == "N":
        # Create some new stats the user can use
        player.name = input("What is your first name? ")
        FileLogic().add_player(BANK_FILENAME, player.name)

    if user_input == "R":
        # Read in the current users stats
        player.name = input("Welcome back to the program, what name did you use last time? ")
    
    text_delay("You find yourself in the main square of PebbleTown...")

    playing = True
    while playing == True:
        
        print("------------------------------------------------------------------------------")
        text_delay("Around you is a shop(S), your house(H), the bank(B), the medical centre(M) and what appears to be a field(F) and finally to exit the game press(E): ")
        user_input = input("What would you like to do? ").upper()
        print("------------------------------------------------------------------------------")

        while user_input != "S" and user_input != "H" and user_input != "B" and user_input != "M" and user_input != "F" and user_input != "E" and user_input != "C":
            user_input = input("What would you like to do? ").upper()
            print("------------------------------------------------------------------------------")

        if user_input == "S":
            shop = Shop(player.coins, player.house, player.inventory).enter_shop()
            player.coins = shop[0]
            player.house = shop[1]
            player.inventory = shop[2]
        
        if user_input == "H":
            NotImplemented

        if user_input == "M":
            player.health = MedicalCentre(player.health).heal()

        if user_input == "B":
            bank_logic(player)

        if user_input == "F":
            monster_fight(player)

        if user_input == "C":
            Casino().better_and_runner(player)

        if user_input == "E":
            print("Goodbye, Thanks for playing!")
            playing = False


# Driver function
if __name__ == "__main__":
    adventure_game()
