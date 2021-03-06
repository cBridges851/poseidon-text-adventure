from components.help import Help
from components.text_delay import text_delay 
from game_logic.field import enter_field

def go_west(player, playing):
    '''
        West part of the game map.  
        Args:
            player: obj, representing a player.
            playing: obj, representing the active game.
        Returns:
            playing: bool, whether the game should run or not.
    '''
    active = True
    
    # Loops until the player leaves this area
    while active:
        text_delay("You see a field in the distance")
        user_input = ""
        valid_inputs = ["F", "FIELD", "RUN AWAY", "EAST", "BACK", "EXIT", "QUIT"]
        is_unacceptable = True

        # If the input isn't in the list ask again.
        while is_unacceptable:
            # If the value the user inputted is not one of the elements in the valid_inputs list
            if user_input not in valid_inputs:
                user_input = input("What would you like to do? ").upper()
                split_input = user_input.split()
                if split_input != []:
                    if len(split_input) == 3:
                        # If the first inputted word is enter, go or move
                        if split_input[0] == "ENTER" or split_input[0] == "GO" or split_input[0] == "MOVE":
                            # The direction for the player to go in is the third inputted word
                            user_input = split_input[2]
                    else:
                        # If the first inputted word is enter, go or move
                        if split_input[0] == "ENTER" or split_input[0] == "GO" or split_input[0] == "MOVE":
                            # The direction for the user to go in is the second inputted word
                            user_input = split_input[1]
            else:
                is_unacceptable = False

        print("------------------------------------------------------------------------------")

        # Decide what the player entered and enter that part of the map.
        if user_input == "F" or user_input == "FIELD":
            enter_field(player)
            print("------------------------------------------------------------------------------")
        elif user_input == "EAST" or user_input == "RUN AWAY" or user_input == "BACK":
            print("", end="")
            active = False
        elif user_input == "HELP":
            Help().display_help()
        else:
            print("Goodbye, Thanks For Playing!")
            playing = False
            active = False
    
    return playing