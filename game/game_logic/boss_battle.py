import random
from components.file_logic import FileLogic
from components.text_delay import text_delay
from game_logic.medical_centre import MedicalCentre
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

    # Loops until the player wins, loses or runs away from the boss battle
    while playing:
        # Minions fight - fight against 3 minions
        for i in range(3):
            monster = Monster()
            print(f"Minion {i + 1} of 3")
            text_delay(f"You have encountered a {monster.name}")
            # Calls the method for the player to fight the monster
            monster_fight = MonsterFight(player, monster)
            active = monster_fight.monster_fight(1, 20)
            
            # Should the monster be dead.
            if monster.health <= 0:
                print("------------------------------------------------------------------------------")
                text_delay(f"You defeated the {monster.name}!")
                # Add to the number of coins the player has and update the JSON
                coins_earned = player.health / 10
                player.coins += round(coins_earned)
                FileLogic().update_player_property(PLAYER_FILENAME, player, "Coins", player.coins)
                text_delay(f"You earned {round(coins_earned)} coins putting your total to {player.coins}.")

                # Updates the player's record of the monsters they have killed
                if monster.name not in player.monsters_killed:
                    # Set value of monster if it is the first on the player has killed of this species
                    player.monsters_killed[monster.name] = 1
                else:
                    # Append the number killed if the player has killed this species before
                    player.monsters_killed[monster.name] += 1

                FileLogic().update_player_property(PLAYER_FILENAME, player, "Monsters Killed", player.monsters_killed)
                
                # Increases the health by 40% unless it is the last monster
                if i != 2:
                    new_health = player.health * 1.4

                    if new_health > 100:
                        player.health = 100
                    else:
                        player.health = round(new_health)
                    
                    text_delay("Health increased by 40%...")
                    FileLogic().update_player_property(PLAYER_FILENAME, player, "Health", player.health)

                print("------------------------------------------------------------------------------")

            # If the player is dead.
            if player.health <= 0:
                player.health = 0
                print("------------------------------------------------------------------------------")
                text_delay("You have died losing all coins on your person and need to restart the boss battle from the start.")
                text_delay("You've been transported to the medical centre for emergency help!")
                MedicalCentre(player).enter_medical_centre(True)
                print("------------------------------------------------------------------------------")
                player.coins = 0
                FileLogic().update_player_property(PLAYER_FILENAME, player, "Coins", player.coins)
                playing = False
                break

            if not active:
                print("------------------------------------------------------------------------------")
                break
            
        if not playing:
            break

        if not active:
            break
        
        # Boss fight
        boss_monster = BossMonster()
        text_delay(f"You have managed to get past {boss_monster.name}'s minions... you're not done yet though. Time to fight {boss_monster.name}!")
        player.health = 100
        FileLogic().update_player_property(PLAYER_FILENAME, player, "Health", player.health)
        text_delay(f"Your health has been restored to 100% before the fight. Good luck...")
        print("------------------------------------------------------------------------------")
        text_delay(f"You have encountered the {boss_monster.name}, the toughest monster in the land.")
        text_delay(f"The {boss_monster.name} has taken Princess Belle hostage. To save her, defeat the monster and you will be rewarded handsomely.")

        monster_fight = MonsterFight(player, boss_monster)
        # Sends the player to the boss fight, setting the minimum damage to 20 and maximum to 35
        active = monster_fight.monster_fight(20, 35)
        
        # If the player has won
        if boss_monster.health <= 0:
            print("------------------------------------------------------------------------------")
            text_delay(f"You defeated {boss_monster.name}! In the process, you saved Princess Belle! Well done!")
            # Reward the player for defeating the boss
            player.coins += 1000
            FileLogic().update_player_property(PLAYER_FILENAME, player, "Coins", player.coins)
            player.boss_beaten = True
            FileLogic().update_player_property(PLAYER_FILENAME, player, "Boss Beaten", player.boss_beaten)
            player.health += 10
            FileLogic().update_player_property(PLAYER_FILENAME, player, "Health", player.health)
            text_delay(f"You gained 10 health for defeating {boss_monster.name}!")
            text_delay(f"You earned 1000 coins, putting your total to {player.coins}.")
            print("------------------------------------------------------------------------------")
            playing = False
            break

        # If the player has lost.
        if player.health <= 0:
            print("------------------------------------------------------------------------------")
            text_delay("You have died losing all coins and items on your person. You need to restart the boss battle from the start.")
            text_delay("You've been transported to the medical centre for emergency help!")
            MedicalCentre(player.health).enter_medical_centre()
            FileLogic().update_player_property(PLAYER_FILENAME, player, "Health", player.health)
            player.inventory = {}
            player.coins = 0
            FileLogic().update_player_property(PLAYER_FILENAME, player, "Inventory", player.inventory)
            FileLogic().update_player_property(PLAYER_FILENAME, player, "Coins", player.coins)
        
        if not active:
            print("------------------------------------------------------------------------------")
            break
