import random
from components.file_logic import FileLogic
from components.text_delay import text_delay
from game_logic.medical_centre import MedicalCentre
from game_logic.monster_fight import MonsterFight
from models.monster import Monster
from models.player import Player

PLAYER_FILENAME = "./player.json"

def enter_field(player):
    '''
    Where players can fight monsters to gain coins.
    Args:
        player: obj, representing a player.
    '''
    monster = Monster()
    playing = True

    while playing:
        text_delay(f"You have encountered a {monster.name}")
        monster_fight = MonsterFight(player, monster)
        monster_fight.monster_fight(1, 20)

        if monster.health <= 0:
            print("------------------------------------------------------------------------------")
            text_delay("You defeated the monster!")
            
            ran_int = random.randint(0,2)
            if ran_int == 0:
                coins_earned = 10
            else:
                coins_earned = 5

            player.coins += coins_earned
            FileLogic().update_player_property(PLAYER_FILENAME, player, "Coins", player.coins)
            text_delay(f"You earned {coins_earned} coins putting your total to {player.coins}.")

            if monster.name not in player.monsters_killed:
                player.monsters_killed[monster.name] = 1
            else:
                player.monsters_killed[monster.name] += 1

            FileLogic().update_player_property(PLAYER_FILENAME, player, "Monsters Killed", player.monsters_killed)

        if player.health <= 0:
            player.health = 0
            print("------------------------------------------------------------------------------")
            text_delay("You have died losing all coins and items on your person.")
            player.inventory = {}
            player.coins = 0
            FileLogic().update_player_property(PLAYER_FILENAME, player, "Coins", player.coins)
            FileLogic().update_player_property(PLAYER_FILENAME, player, "Inventory", player.inventory)
            text_delay("You've been transported to the medical centre for emergency help!")
            MedicalCentre(player).enter_medical_centre(True)
        playing = False