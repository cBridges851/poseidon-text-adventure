from models.boss_monster import BossMonster
from models.monster import Monster
from models.player import Player
import random
from components.file_logic import FileLogic
from components.text_delay import text_delay

PLAYER_FILENAME = "./player.json"

def boss_battle(player):
    '''
    Fill in later on:
    Todo: 
        1 big battle at the end
        Rescure the princess?
    '''
    playing = True
    while playing:
        for i in range(3):
            monster = Monster()
            print(f"Minion {i + 1} of 3")
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
                        FileLogic().update_player_property(PLAYER_FILENAME, player, "Health", player.health)
                    print(f"The monster attacked you leaving you with {player.health}.")

                if player_input == "R":
                    break
                
                if Player().is_player_dead(player.health) == True:
                    break
            player.health = player.health * 1.4

        boss_monster = BossMonster()
        text_delay(f"You have managed to get past {boss_monster.name}'s minions... your not done yet though. Time to fight {boss_monster.name}!")
        player.health = 100
        text_delay(f"Your health has been restored to 100% before the fight. Good luck...")

        break