from components.help import Help
from components.text_delay import text_delay 
from game_logic.boss_battle import boss_battle

def go_south(player, playing):
    '''
        South part of the game map.  
        Args:
            player: obj, representing a player.
            playing: obj, representing the active game.
        Returns:
            playing: bool, whether the game should run or not.
    '''
    if not player.boss_beaten:
        text_delay("The Princess Belle has been taken hostage by the evil monster Gorgo. Your mission should you chose to accept it...")
        text_delay("Is to fight past Gorgo's Minions before taking on Gorgo himself in a battle to save Princess Belle.")
        print("------------------------------------------------------------------------------")
        user_input = ""
        valid_inputs = ["F", "FIGHT", "YES", "Y", "NO", "RUN AWAY", "I'M TOO SCARED", "NORTH", "BACK", "EXIT", "QUIT"]
        is_unacceptable = True
        
        # If the input isn't in the list ask again.
        while is_unacceptable:
            if user_input not in valid_inputs:
                user_input = input("Do you want to fight the boss? Or are you too scared? ").upper()
                split_input = user_input.split()
                if split_input != []:
                    if split_input[0] == "ENTER" or split_input[0] == "GO" or split_input[0] == "MOVE":
                        user_input = split_input[1]
            else:
                is_unacceptable = False
        
        print("------------------------------------------------------------------------------")
            
        # Decide what the player entered.
        if user_input == "F" or user_input == "FIGHT" or user_input == "YES" or user_input == "Y":
            if player.damage < 25:
                text_delay("You aren't strong enough to defeat the boss. Level up your damage output before trying again.")
                print("------------------------------------------------------------------------------")
            elif player.health < 100:
                text_delay("You are too weak. Heal before trying again.")
                print("------------------------------------------------------------------------------")
            else:
                boss_battle(player)
        elif user_input == "NORTH" or user_input == "RUN AWAY" or user_input == "I'M TOO SCARED" or user_input == "NO" or user_input == "BACK":
            print("", end="")
        elif user_input == "HELP":
            Help().display_help()
        else:
            print("Goodbye, Thanks For Playing!")
            playing = False
    else:
        text_delay("You've already saved Princess Belle and defeated Gorgo. The world is calm and safe! Have a good day.")
        print("------------------------------------------------------------------------------")
    
    return playing
