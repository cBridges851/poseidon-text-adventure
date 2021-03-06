from components.help import Help
from components.text_delay import text_delay 
from game_logic.bank import bank_logic
from game_logic.house import House
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

    # Loops until the player leaves this area
    while active:
        text_delay("Around you is a shop, your house and the bank. ")
        print("------------------------------------------------------------------------------")
        user_input = ""
        valid_inputs = ["S", "H", "B", "SOUTH", "SHOP", "HOUSE", "BANK", "BACK", "EXIT", "QUIT", "HELP"]
        is_unacceptable = True
        
        # If the input isn't in the list ask again.
        while is_unacceptable:
            # If the value the user inputted is not one of the elements in the valid_inputs list
            if user_input not in valid_inputs:
                user_input = input("What would you like to do? ").upper()
                split_input = user_input.split()
                if split_input != []:
                    if len(split_input) == 2:
                        # If the first inputted word is enter, go or move
                        if split_input[0] == "ENTER" or split_input[0] == "GO" or split_input[0] == "MOVE":
                            # The direction for the user will be the second inputted word
                            user_input = split_input[1]
                    else:
                        # If the first inputted word is enter, go or move
                        if split_input[0] == "ENTER" or split_input[0] == "GO" or split_input[0] == "MOVE":
                            # The direction for the user to go in will be the third inputted word
                            user_input = split_input[2]
            else:
                is_unacceptable = False

        print("------------------------------------------------------------------------------")
        
        # Decide what the player entered and enter that part of the map.
        if user_input == "S" or user_input == "SHOP":
            player = Shop(player).enter_shop()
            print("------------------------------------------------------------------------------")
        elif user_input == "H" or user_input == "HOUSE":
            House(player).enter_house()
            print("------------------------------------------------------------------------------")
        elif user_input == "B" or user_input == "BANK":
            bank_logic(player)
            print("------------------------------------------------------------------------------")
        elif user_input == "SOUTH" or user_input == "BACK":
            print("", end="")
            active = False
        elif user_input == "HELP":
            Help().display_help()
        else:
            print("Goodbye, Thanks For Playing!")
            playing = False
            active = False
    
    return playing