from text_delay import text_delay
from monster import Monster
from player import Player
import random

def monster_fight(player):
    '''
    Reuseable component where players can fight monsters to gain coins.
    Args:
        player: obj, representing a player.
    '''
    monster = Monster()

    playing = True
    while playing:
        text_delay(f"You have encountered a {monster.name}")
        while monster.health > 0:
            print("------------------------------------------------------------------------------")
            player_input = input("To attack the monster, press (A). To run away press (R): ").upper()

            while player_input != "A" and player_input != "R":
                player_input = input("To attack the monster, press (A). To run away press (R): ").upper()
            
            if player_input == "A":
                monster.health -= player.damage
                print(f"You attacked the {monster.name} dealing {player.damage}. The monster has {monster.health} left.")
                monster.damage = random.randint(1, 20)
                if monster.health < 0:
                    break
                else:
                    player.health -= monster.damage
                print(f"The monster attacked you leaving you with {player.health}.")

            if player_input == "R":
                break
            
            if Player().is_player_dead(player.health) == True:
                break

        if monster.health <= 0:
            print("------------------------------------------------------------------------------")
            print("You defeated the monster!")
            coins_earned = player.health / 10
            player.coins += round(coins_earned)
            text_delay(f"You earned {round(coins_earned)} coins putting your total to {player.coins}.")

        if player.health <= 0:
            print("------------------------------------------------------------------------------")
            text_delay("You have died losing all coins on your person.")
            player.coins = 0
        playing = False