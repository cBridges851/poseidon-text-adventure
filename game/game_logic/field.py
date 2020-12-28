import random
from components.file_logic import FileLogic
from components.text_delay import text_delay
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
            coins_earned = player.health / 10
            player.coins += round(coins_earned)
            FileLogic().update_player_property(PLAYER_FILENAME, player, "Coins", player.coins)
            text_delay(f"You earned {round(coins_earned)} coins putting your total to {player.coins}.")

        if player.health <= 0:
            print("------------------------------------------------------------------------------")
            text_delay("You have died losing all coins on your person.")
            player.coins = 0
            FileLogic().update_player_property(PLAYER_FILENAME, player, "Coins", player.coins)
        playing = False