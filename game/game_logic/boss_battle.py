import random
from components.file_logic import FileLogic
from components.text_delay import text_delay
from game_logic.monster_fight import MonsterFight
from models.boss_monster import BossMonster
from models.monster import Monster
from models.player import Player

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

            monster_fight = MonsterFight(player, monster)
            active = monster_fight.monster_fight(1, 20)

            if not active:
                print("------------------------------------------------------------------------------")
                break

            if monster.health <= 0:
                print("------------------------------------------------------------------------------")
                text_delay("You defeated the monster!")
                coins_earned = player.health / 10
                player.coins += round(coins_earned)
                FileLogic().update_player_property(PLAYER_FILENAME, player, "Coins", player.coins)
                text_delay(f"You earned {round(coins_earned)} coins putting your total to {player.coins}.")
                new_health = player.health * 1.4
                player.health = round(new_health)
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

        if not active:
            break

        boss_monster = BossMonster()
        text_delay(f"You have managed to get past {boss_monster.name}'s minions... your're not done yet though. Time to fight {boss_monster.name}!")
        player.health = 100
        text_delay(f"Your health has been restored to 100% before the fight. Good luck...")

        print("------------------------------------------------------------------------------")

        text_delay(f"You have encountered the {boss_monster.name}, the toughest monster in the land.")
        text_delay(f"The {boss_monster.name} has taken Princess Belle hostage. To save her, defeat the monster and you will be get rewarded handsomely.")

        monster_fight = MonsterFight(player, boss_monster)
        active = monster_fight.monster_fight(15, 20)

        if not active:
            print("------------------------------------------------------------------------------")
            break
        
        if boss_monster.health <= 0:
            print("------------------------------------------------------------------------------")
            text_delay(f"You defeated {boss_monster.name}! In the process, you saved Princess Belle! Well done!")
            coins_earned = 1000
            player.coins += coins_earned
            FileLogic().update_player_property(PLAYER_FILENAME, player, "Coins", player.coins)
            text_delay(f"You earned {coins_earned} coins, putting your total to {player.coins}.")
            print("------------------------------------------------------------------------------")
            playing = False
            break

        if player.health <= 0:
            print("------------------------------------------------------------------------------")
            text_delay("You have died losing all coins on your person. You need to restart the boss battle from the start.")
            text_delay("You've been taken back shamefully to PebbleTown...")
            player.coins = 0
            FileLogic().update_player_property(PLAYER_FILENAME, player, "Coins", player.coins)