from text_delay import text_delay
from file_logic import FileLogic
from player import Player

PLAYER_FILENAME = "./player.json"

def bank_logic(player):
    '''
    Main program logic for the bank.
    Args:
        player: obj, player object.
    '''
    text_delay("You open the door to the bank and look inside...")
    text_delay("You notice you can deposit the coins on you into your account, check your balance or withdraw money out.")
    playing = True
    while playing == True:
        user_input = input("Do you want to deposit(D), checkout your balance(B), withdraw money from the bank(W) or exit(E)? ").upper()

        while user_input != "D" and user_input != "B" and user_input != "W" and user_input != "E":
            user_input = input("Do you want to deposit(D), checkout your balance(B), withdraw money from the bank(W) or exit(E)? ").upper()
        print("------------------------------------------------------------------------------")

        if user_input == "D":

            user_input = input("Do you want to deposit all your coins(A) or a certain amount(C)? ").upper()

            while user_input != "A" and user_input != "C":
                user_input = input("Do you want to deposit all your coins(A) or a certain amount(C)? ").upper()

            if user_input == "A":
                text_delay("You chose to deposit all your coins.")
                FileLogic().update_balance(PLAYER_FILENAME, player)
                player.coins = 0
                FileLogic().update_player_property(PLAYER_FILENAME, player, "Coins", player.coins)
                print(f"Balance has been updated, new balance is {FileLogic().get_balance(PLAYER_FILENAME, player)} coins.")
            
            if user_input == "C":
                text_delay("You chose to deposit a set amount.")
                print(f"You currently have {player.coins} coins.")
                user_input = int(input("How much do you want to deposit? "))

                if user_input > player.coins or user_input <= 0:
                    text_delay("The amount your entered was out of range.")
                else:
                    text_delay("Coins added to your account.")
                    FileLogic().update_balance_by_set_amount(PLAYER_FILENAME, player, user_input)
                    player.coins -= user_input
                    FileLogic().update_player_property(PLAYER_FILENAME, player, "Coins", player.coins)
                    print(f"Balance has been updated, new balance is {FileLogic().get_balance(PLAYER_FILENAME, player)} coins.")

        if user_input == "B":
            text_delay("You chose to checkout your balance.")
            print(f"Your current balance is {FileLogic().get_balance(PLAYER_FILENAME, player)} coins.")

        if user_input == "W":
            text_delay("You have chosen to take money out.")
            current_amount = FileLogic().get_balance(PLAYER_FILENAME, player)
            print(f"Your current balance is {current_amount} coins.")
            user_input = int(input("How much do you want to take out? "))

            if user_input > current_amount or user_input <= 0:
                    text_delay("The amount you entered was out of range.")
            else:
                player = FileLogic().withdraw_by_set_amount(PLAYER_FILENAME, player, user_input)
                text_delay(f"You now have {player.coins} in your inventory.")
        
        if user_input == "E":
            text_delay("Goodbye, thanks for using the bank.")
            playing = False