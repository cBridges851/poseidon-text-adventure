from text_delay import text_delay
from file_logic import FileLogic

BANK_FILENAME = "./bank.txt"

def bank_logic(player):
    text_delay("You open the door to the bank and look inside...")
    text_delay("You notice you can deposit the coins on you into your account or check your balance.")
    user_input = input("Do you want to deposit(D) or checkout your balance(B)? ").upper()

    while user_input != "D" and user_input != "B":
        user_input = input("Do you want to deposit(D) or checkout your balance(B)? ").upper()

    print("------------------------------------------------------------------------------")

    if user_input == "D":
        print("You chose too deposit")
        FileLogic().update_balance(BANK_FILENAME, player.name, player.coins)
        print(f"Balanced has been updated, new balance is {FileLogic().get_balance(BANK_FILENAME, player.name)} coins.")

    if user_input == "B":
        print("You chose too checkout your balance.")
        print(f"Your current balance is {FileLogic().get_balance(BANK_FILENAME, player.name)} coins.")


# could deposit a set amount
# take money out of the bank
# monster shouldn't be able to attack when dead pepe4head
# staying in the bank!
# location var poss