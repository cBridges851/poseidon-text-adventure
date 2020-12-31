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
    if player.boss_beaten == False:
        text_delay("The Princess Belle has been taken hostage by the evil monster Gorgo. Your mission should you chose to accept it...")
        text_delay("Is to fight past Grogo's Minions before taking on Grogo himself in a battle to save Princess Belle.")
        print("------------------------------------------------------------------------------")
        print("Do you want to fight the boss? Or are you too scared... (Y/N) (Type 'exit' to close the game):")
        user_input = ""
        print("------------------------------------------------------------------------------")
        while user_input != "Y" and user_input != "N" and user_input != "EXIT":
            user_input = input("What would you like to do? ").upper()
            print("------------------------------------------------------------------------------")
            
        if user_input == "Y":
            if player.damage < 25:
                text_delay("You aren't strong enough to defeat the boss. Level up your damage output before trying again.")
                print("------------------------------------------------------------------------------")
            elif player.health < 100:
                text_delay("You are too weak. Heal before trying again.")
                print("------------------------------------------------------------------------------")
            else:
                boss_battle(player)
        elif user_input == "N":
            print("", end="")
        else:
            print("Goodbye, Thanks For Playing!")
            playing = False
    else:
        text_delay("You've already saved Princess Belle and defeated Gorgo. The world is calm and safe! Have a good day.")
        print("------------------------------------------------------------------------------")
    
    return playing
