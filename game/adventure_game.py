# Christa Bridges
# Josh Talbot
# John Mason
# The Adventure Game to end all adventure games
import time
import random

BANK_FILENAME = "./bank.txt"

class Monster:
    def __init__(self):
        self.name = random.choice(["Trow", "Kobold", "Hobgoblin", "Bugbear"])
        self.health = random.randint(90, 100)
        self.damage = random.randint(1, 20)

class Player:
    def __init__(self):
        self.name = None
        self.health = 100
        self.damage = 15
        self.coins = 0


def text_delay(sentence):
    '''
    Print's out text in a retro games console style.
    Args:
        sentence: string, to print out.
    '''
    for letter in sentence:
        print(letter, sep="", end="", flush=True)
        time.sleep(.03)
    print("")


def get_balance(player):
    '''
    Get the coin balance of a given player.
    Args:
        player: string, player name.
    Returns:
        balance: integer, player coin balance.
    '''
    try:
        with open(BANK_FILENAME, "r") as content:
            records = content.read().split("\n")
    except FileNotFoundError:
        print("ERROR: File not found check your file path.")
        exit()
    except PermissionError:
        print("ERROR: You lack the permissions to open this file.")
        exit()
    
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
    try:
        with open(BANK_FILENAME, "r") as content:
            file = content.read().split("\n")
    except FileNotFoundError:
        print("ERROR: File not found check your file path.")
        exit()
    except PermissionError:
        print("ERROR: You lack the permissions to write this file.")
        exit()

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

    try:
        with open(BANK_FILENAME, "w") as content:
            content.writelines(file)
    except FileNotFoundError:
        print("ERROR: File not found check your file path.")
        exit()
    except PermissionError:
        print("ERROR: You lack the permissions to write this file.")
        exit()


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
            player_input = input("To attack the monster press (A) to run away press (R): ").upper()

            while player_input != "A" and player_input != "R":
                player_input = input("To attack the monster press (A) to run away press (R): ").upper()
            
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
            print(f"You defeated the monster!")
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
    # user_input = input("Welcome to Pebble Town are you a new(N) or returning(R) player? ").upper()

    # while user_input != "N" and user_input != "R":
    #     user_input = input("Welcome to the Poseiden text adventure are you a new(N) or returning(R) player? ").upper()
    
    # if user_input == "N":
    #     # Create some new stats the user can use
    #     return True

    # if user_input == "R":
    #     # Read in the current users stats
    #     return True

    player = Player()

    monster_fight(player)


# Driver function
if __name__ == "__main__":
    adventure_game()