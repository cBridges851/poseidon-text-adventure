from components.text_delay import text_delay 
from game_logic.bank import bank_logic
from game_logic.shop import Shop

def go_north(player, playing):
    '''
    North part of the game map.
    Args:
        player: obj, representing a player.
        playing: obj, representing the active game.
    Returns:
        playing: bool, whether the game should run or not.
    '''
    active = True
    while active:
        text_delay("Around you is a shop, your house and the bank: ")
        print("------------------------------------------------------------------------------")
        user_input = ""
        valid_inputs = ["S", "H", "B", "SOUTH", "SHOP", "HOUSE", "BANK", "EXIT"]
        is_unacceptable = True
        while is_unacceptable:
            if user_input not in valid_inputs:
                user_input = input("What would you like to do? ").upper()
                split_input = user_input.split()
                if split_input[0] == "ENTER" or split_input[0] == "GO":
                    user_input = split_input[1]
            else:
                is_unacceptable = False

        print("------------------------------------------------------------------------------")
                
        if user_input == "S" or user_input == "SHOP":
            player = Shop(player).enter_shop()
            print("------------------------------------------------------------------------------")
        elif user_input == "H" or user_input == "HOUSE":
            NotImplemented
            print("------------------------------------------------------------------------------")
        elif user_input == "B" or user_input == "BANK":
            bank_logic(player)
            print("------------------------------------------------------------------------------")
        elif user_input == "SOUTH":
            print("", end="")
            active = False
        else:
            print("Goodbye, Thanks For Playing!")
            playing = False
            active = False
    
    return playing