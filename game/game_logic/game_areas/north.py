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
        text_delay("Around you is a shop(S), your house(H), the bank(B) and (main square) to return to the main square. (Type 'exit' to close the game): ")
        user_input = ""
        print("------------------------------------------------------------------------------")

        while user_input != "S" and user_input != "H" and user_input != "B" and user_input != "MAIN SQUARE" and user_input != "EXIT":
            user_input = input("What would you like to do? ").upper()
        print("------------------------------------------------------------------------------")
                
        if user_input == "S":
            player = Shop(player).enter_shop()
            print("------------------------------------------------------------------------------")
        elif user_input == "H":
            NotImplemented
            print("------------------------------------------------------------------------------")
        elif user_input == "B":
            bank_logic(player)
            print("------------------------------------------------------------------------------")
        elif user_input == "MAIN SQUARE":
            print("", end="")
            active = False
        else:
            print("Goodbye, Thanks For Playing!")
            playing = False
            active = False
    
    return playing