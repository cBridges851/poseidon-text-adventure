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
            NotImplemented
        
        if user_input == "H":
            NotImplemented

        if user_input == "M":
            player.health = MedicalCentre(player.health).heal()

        if user_input == "B":
            bank_logic(player)

        if user_input == "F":
            monster_fight(player)

        if user_input == "C":
            text_delay("Welcome to the casino here you can play blackjack: ")
            in_casino = True
            while in_casino == True:
                user_input = input("Would you like to play?(Y/N): ").upper()

                while user_input != "Y" and user_input != "N":
                    user_input = input("Would you like to play?(Y/N): ").upper()

                if user_input == "Y":
                    game_result = ""
                    while True:
                        bet = input("How much do you want to bet? ")
                        while isinstance(user_input, int):
                            print("Invalid bet!")
                            bet = input("How much do you want to bet? ")
                        bet = int(bet)
                        if bet > player.coins or bet <= 0:
                            text_delay("The amount your entered was out of range.")
                        else:
                            text_delay(f"Taken {bet} coins from your inventory.")
                            player.coins -= bet
                            game_result = Casino().play_blackjack()
                            break

                    if game_result == "W":
                        player.coins += bet * 2
                        text_delay("You doubled your bet. Added your earnings to your inventory.")
                    elif game_result == "L":
                        text_delay("You lost your bet.")
                    else:
                        player.coins += bet
                        text_delay("Bet returned to your inventory.")

                if user_input == "N":
                    text_delay("Okay, thanks for coming!")
                    in_casino = False

        if user_input == "E":
            print("Goodbye, Thanks for playing!")
            playing = False


# Driver function
if __name__ == "__main__":
    adventure_game()