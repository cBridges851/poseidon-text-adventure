# Christa Bridges
# Josh Talbot
# John Mason
# The Adventure Game to end all adventure games
import time
import random
from monster import Monster
from player import Player

BANK_FILENAME = "./bank.txt"

def text_delay(sentence):
    '''
    Prints out text in a retro games console style.
    Args:
        sentence: string, to print out.
    '''
    for letter in sentence:
        print(letter, sep="", end="", flush=True)
        time.sleep(.03)
    print("")


def open_file_by_newline(filepath):
    '''
    Open a file and split the content by newlines.
    Args:
        filepath: string, representing a filepath.
    Returns:
        file: list, representing the file contents by newline.
    '''
    try:
        with open(filepath, "r") as content:
            file = content.read().split("\n")
    except FileNotFoundError:
        print("ERROR: File not found, check your file path.")
        exit()
    except PermissionError:
        print("ERROR: You lack the permissions to read this file.")
        exit()

    return file


def write_file_using_list(file_content):
    '''
    Write to a file using an given in list.
    Args: 
        list: list, containing the file contents.
    '''
    try:
        with open(BANK_FILENAME, "w") as content:
            content.writelines(file_content)
    except FileNotFoundError:
        print("ERROR: File not found, check your file path.")
        exit()
    except PermissionError:
        print("ERROR: You lack the permissions to write this file.")
        exit()


def get_balance(player):
    '''
    Get the coin balance of a given player.
    Args:
        player: string, player name.
    Returns:
        balance: integer, player coin balance.
    '''
    records = open_file_by_newline(BANK_FILENAME)
    
    individual_player = ""
    balance = 0

    for record in range(len(records)):
        individual_player = records[record].split()
        if individual_player[1] == player:
            balance = int(individual_player[0])

    return balance


def update_balance(player, coins):
    '''
    Update the coin balance of an existing player.
    Args:
        player: string, player name.
        coins: integer, coins in the players inventory.
    '''
    file = open_file_by_newline(BANK_FILENAME)

    for item in range(len(file)):
        if file[item] == "":
            file.remove(file[item])

    individual_player = ""
    for item in range(len(file)):
        individual_player = file[item].split()

        if individual_player[1] == player:
            updated_total = int(individual_player[0]) + coins
            if item != 0:
                file[item] = "\n" + str(updated_total) + " " + player
            else:
                file[item] = str(updated_total) + " " + player
        elif item != 0:
            file[item] = "\n" + file[item]
        else:
            file[item] = file[item]

    write_file_using_list(file)


def add_player(player):
    '''
    Adds a new player to the database.
    Args:
        player: string, player name.
    '''
    file = open_file_by_newline(BANK_FILENAME)

    for item in range(len(file)):
        if file[item] == "":
            file.remove(file[item])

    file.append("0" + " " + player)

    for item in range(len(file)):
        if item != 0:
            file[item] = "\n" + file[item]
        else:
            file[item] = file[item]
            
    write_file_using_list(file)


def is_player_dead(player_health):
    '''
    Check whether a player has 0 or less health.
    Args:
        player_health: int, representing the player health.
    Returns:
        True: bool, if the players health is below or equal to 0.
    '''
    if player_health <= 0:
        return True


def monster_fight(player):
    '''
    Reuseable component where players can fight monsters to gain coins.
    Args:
        player: obj, representing a player.
    '''
    monster = Monster()

    playing = True
    while playing:
        text_delay(f"You have encoutered a {monster.name}")
        while monster.health > 0:
            print("------------------------------------------------------------------------------")
            player_input = input("To attack the monster, press (A). To run away press (R): ").upper()

            while player_input != "A" and player_input != "R":
                player_input = input("To attack the monster, press (A). To run away press (R): ").upper()
            
            if player_input == "A":
                monster.health -= player.damage
                print(f"You attacked the {monster.name} dealing {player.damage}. The monster has {monster.health} left.")
                monster.damage = random.randint(1, 20)
                player.health -= monster.damage
                print(f"The monster attacked you leaving you with {player.health}.")

            if player_input == "R":
                break
            
            if is_player_dead(player.health) == True:
                break

        if monster.health <= 0:
            print("------------------------------------------------------------------------------")
            print("You defeated the monster!")
            coins_earned = player.health / 10
            player.coins += round(coins_earned)
            text_delay(f"You earned {round(coins_earned)} coins putting your total to {player.coins}.")

        if player.health <= 0:
            print("------------------------------------------------------------------------------")
            text_delay("You have died losing all coins on your person.")
            player.coins = 0
        playing = False


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
        add_player(player.name)

    if user_input == "R":
        # Read in the current users stats
        player.name = input("Welcome back to the program, what name did you use last time? ")
    
    text_delay("You find yourself in the main square of PebbleTown...")

    playing = True
    while playing == True:
        
        print("------------------------------------------------------------------------------")
        text_delay("Around you is a shop(S), your house(H), the bank(B), the hospital(H) and what appears to be a field(F) and finally to exit the game press(E): ")
        user_input = input("What would you like to do? ").upper()
        print("------------------------------------------------------------------------------")

        while user_input != "S" and user_input != "H" and user_input != "B" and user_input != "H" and user_input != "F" and user_input != "E":
            user_input = input("What would you like to do? ").upper()
            print("------------------------------------------------------------------------------")

        if user_input == "S":
            NotImplemented
        
        if user_input == "H":
            NotImplemented

        if user_input == "B":
            text_delay("You open the door to the bank and look inside...")
            text_delay("You notice you can deposit the coins on you into your account or check your balance.")
            user_input = input("Do you want to deposit(D) or checkout your balance(C)? ").upper()

            while user_input != "D" and user_input != "C":
                user_input = input("Do you want to deposit(D) or checkout your balance(C)? ").upper()

            print("------------------------------------------------------------------------------")

            if user_input == "D":
                print("You chose too deposit")
                update_balance(player.name, player.coins)
                print(f"Balanced has been updated, new balance is {get_balance(player.name)} coins.")

            if user_input == "C":
                print("You chose too checkout your balance.")
                print(f"Your current balance is {get_balance(player.name)} coins.")

        if user_input == "H":
            NotImplemented
        
        if user_input == "F":
            monster_fight(player)

        if user_input == "E":
            print("Goodbye, Thanks for playing!")
            playing = False


# Driver function
if __name__ == "__main__":
    adventure_game()


# could deposit a set amount
# take money out of the bank
# monster shouldn't be able to attack when dead pepe4head
# staying in the bank!
# location var poss