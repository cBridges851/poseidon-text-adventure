from text_delay import text_delay
from file_logic import FileLogic

BANK_FILENAME = "./bank.txt"

def bank_logic(player):
    text_delay("You open the door to the bank and look inside...")
    text_delay("You notice you can deposit the coins on you into your account, check your balance or take some money out.")
    user_input = input("Do you want to deposit(D), checkout your balance(B) or take money out the bank(T)? ").upper()

    while user_input != "D" and user_input != "B" and user_input != "T":
        user_input = input("Do you want to deposit(D), checkout your balance(B) or take money out the bank(T)? ").upper()

    print("------------------------------------------------------------------------------")

    if user_input == "D":

        user_input = input("Do you want to deposit all your coins(A) or a certain amount(C)? ").upper()

        while user_input != "A" and user_input != "C":
            user_input = input("Do you want to deposit all your coins(A) or a certain amount(C)? ").upper()

        if user_input == "A":
            print("You chose too deposit all your coins.")
            FileLogic().update_balance(BANK_FILENAME, player.name, player.coins)
            print(f"Balanced has been updated, new balance is {FileLogic().get_balance(BANK_FILENAME, player.name)} coins.")
        
        if user_input == "C":
            print("You chose too deposit a set amount.")
            print(f"You currently have {player.coins} coins.")
            user_input = int(input("How much do you want to deposit? "))

            if user_input > player.coins or user_input <= 0:
                print("The amount your entered was out of range.")
            else:
                print("Coins added to your account.")
                FileLogic().update_balance_set_amount(BANK_FILENAME, player.name, user_input)
                player.coins -= user_input
                print(f"Balanced has been updated, new balance is {FileLogic().get_balance(BANK_FILENAME, player.name)} coins.")

    if user_input == "B":
        print("You chose too checkout your balance.")
        print(f"Your current balance is {FileLogic().get_balance(BANK_FILENAME, player.name)} coins.")

    if user_input == "T":
        print("You have chosen to take money out.")
        current_amount = FileLogic().get_balance(BANK_FILENAME, player.name)
        print(f"Your current balance is {current_amount} coins.")
        user_input = int(input("How much do you want to take out? "))

        if user_input > current_amount or user_input <= 0:
                print("The amount your entered was out of range.")
        else:
            update_amount = current_amount - user_input
            FileLogic().remove_by_set_amount(BANK_FILENAME, player.name, update_amount)
            player.coins += user_input
            print(f"You now have {player.coins} in your inventory.")

# monster shouldn't be able to attack when dead pepe4head
# staying in the bank!
import player
player = player.Player()
player.name = "John"
player.coins = 3
bank_logic(player)