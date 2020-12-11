# Christa Bridges
# Josh Talbot
# John Mason
# The Adventure Game to end all adventure games
import time

BANK_FILENAME = "./bank.txt"

def text_delay(sentence):
    '''
    Print's out text in a retro games console style.
    Args:
        sentence: string, to print out.
    '''
    for letter in sentence:
        print(letter, sep="", end="", flush=True)
        time.sleep(.1)


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


print(get_balance("John"))
update_balance("John", 12)