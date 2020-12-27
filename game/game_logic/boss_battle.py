from models.boss_monster import BossMonster
from models.monster import Monster
from models.player import Player
import random
from components.file_logic import FileLogic
from components.text_delay import text_delay

PLAYER_FILENAME = "./player.json"

def boss_battle(player):
    '''
    Boss fight logic where the player takes on the boss.
    Args:
        player: obj, representing a player.
    '''
    playing = True
    while playing:
        for i in range(3):
            monster = Monster()
            print(f"Minion {i + 1} of 3")
            text_delay(f"You have encountered a {monster.name}")
            while monster.health > 0:
                print("------------------------------------------------------------------------------")
                player_input = ""

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

            if monster.health <= 0:
                print("------------------------------------------------------------------------------")
                print("You defeated the monster!")
                coins_earned = player.health / 10
                player.coins += round(coins_earned)
                FileLogic().update_player_property(PLAYER_FILENAME, player, "Coins", player.coins)
                text_delay(f"You earned {round(coins_earned)} coins putting your total to {player.coins}.")
                player.health = player.health * 1.4
                print("------------------------------------------------------------------------------")

            if player.health <= 0:
                print("------------------------------------------------------------------------------")
                text_delay("You have died losing all coins on your person and need to restart the boss battle from the start.")
                text_delay("You've been taken back shamefully to PebbleTown...")
                player.coins = 0
                FileLogic().update_player_property(PLAYER_FILENAME, player, "Coins", player.coins)
                playing = False
                break
            
        if playing == False:
            break

        boss_monster = BossMonster()
        text_delay(f"You have managed to get past {boss_monster.name}'s minions... your not done yet though. Time to fight {boss_monster.name}!")
        player.health = 100
        text_delay(f"Your health has been restored to 100% before the fight. Good luck...")

        print("------------------------------------------------------------------------------")

        text_delay(f"You have encountered the {boss_monster.name} the toughest monster in the land.")
        text_delay(f"The {boss_monster.name} has taken the Princess hostage. To save her defeat the Monster and get rewarded handsomly.")

        while boss_monster.health > 0:
            print("------------------------------------------------------------------------------")
            player_input = ""

            while player_input != "A" and player_input != "R":
                player_input = input("To attack the monster, press (A). To run away press (R): ").upper()
                
            if player_input == "A":
                boss_monster.health -= player.damage
                print(f"You attacked the {boss_monster.name} dealing {player.damage}. The monster has {boss_monster.health} left.")
                boss_monster.damage = random.randint(15, 20)
                if boss_monster.health < 0:
                    break
                else:
                    player.health -= boss_monster.damage
                    FileLogic().update_player_property(PLAYER_FILENAME, player, "Health", player.health)
                print(f"The monster attacked you leaving you with {player.health}.")

            if player_input == "R":
                break
            
            if Player().is_player_dead(player.health) == True:
                break
        
        if boss_monster.health <= 0:
            print("------------------------------------------------------------------------------")
            print("You defeated the Boss Monster and in the process saved the Princess! Welldone!")
            coins_earned = 1000
            player.coins += coins_earned
            FileLogic().update_player_property(PLAYER_FILENAME, player, "Coins", player.coins)
            text_delay(f"You earned {coins_earned} coins putting your total to {player.coins}.")
            print("------------------------------------------------------------------------------")
            playing = False
            break

        if player.health <= 0:
            print("------------------------------------------------------------------------------")
            text_delay("You have died losing all coins on your person and need to restart the boss battle from the start.")
            text_delay("You've been taken back shamefully to PebbleTown...")
            player.coins = 0
            FileLogic().update_player_property(PLAYER_FILENAME, player, "Coins", player.coins)
