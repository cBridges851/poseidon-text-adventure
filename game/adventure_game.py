# Christa Bridges
# Josh Talbot
# John Mason
# The Adventure Game to end all adventure games
import time
import random
from models.monster import Monster
from models.player import Player
from components.text_delay import text_delay
from components.file_logic import FileLogic
from game_logic.monster_fight import monster_fight
from game_logic.bank import bank_logic
from game_logic.medical_centre import MedicalCentre
from game_logic.shop import Shop
from game_logic.casino import Casino
from game_logic.boss_battle import boss_battle

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
            text_delay("Around you is a shop(S), your house(H), the bank(B) (Type 'exit' to close the game): ")
            user_input = ""
            print("------------------------------------------------------------------------------")
            while user_input != "S" and user_input != "H" and user_input != "B" and user_input != "EXIT":
                user_input = input("What would you like to do? ").upper()
                print("------------------------------------------------------------------------------")
            
            if user_input == "S":
                player = Shop(player).enter_shop()
            
            elif user_input == "H":
                NotImplemented
            
            elif user_input == "B":
                bank_logic(player)
            
            else:
                print("Goodbye, Thanks for playing!")
                playing = False
        
        elif direction == "S":
            text_delay("Do you want to fight the boss?(Y/N) (Type 'exit' to close the game):")
            user_input = ""
            print("------------------------------------------------------------------------------")
            while user_input != "Y" and user_input != "N" and user_input != "EXIT":
                user_input = input("What would you like to do? ").upper()
                print("------------------------------------------------------------------------------")
            
            if user_input == "Y":
                if player.damage < 25:
                    text_delay("You aren't strong enough to defeat the boss. Level up your damage output at the shop.")
                elif player.health < 100:
                    text_delay("You are too weak go back to the Hospital and heal before trying again.")
                else:
                    boss_battle(player)

            else:
                print("Goodbye, Thanks for playing!")
                playing = False

        elif direction == "E":
            text_delay("Around you is the medical centre do you want to enter(Y/N) (Type 'exit' to close the game): ")
            user_input = ""
            print("------------------------------------------------------------------------------")
            while user_input != "Y" and user_input != "N" and user_input != "EXIT" and user_input != "C":
                user_input = input("What would you like to do? ").upper()
                print("------------------------------------------------------------------------------")

            if user_input == "Y":
                player.health = MedicalCentre(player.health).heal()
                FileLogic().update_player_property(PLAYER_FILENAME, player, "Health", player.health)

            elif user_input == "C":
                text_delay("You quickly run around the corner to avoid the police and enter the casino.")
                Casino().better_and_runner(player)
            
            else:
                print("Goodbye, Thanks for playing!")
                playing = False

        elif direction == "W":
            text_delay("You see a field do you want to go in it?(Y/N) (Type 'exit' to close the game): ")
            user_input = ""
            print("------------------------------------------------------------------------------")
            while user_input != "Y" and user_input != "N" and user_input != "EXIT":
                user_input = input("What would you like to do? ").upper()
                print("------------------------------------------------------------------------------")

            if user_input == "Y":
                monster_fight(player)
            
            else:
                print("Goodbye, Thanks for playing!")
                playing = False

        else:
            print("Goodbye, Thanks for playing!")
            playing = False

# Driver function
if __name__ == "__main__":
    adventure_game()
