from models.boss_monster import BossMonster
from models.monster import Monster
from models.player import Player
import random
from components.file_logic import FileLogic
from components.text_delay import text_delay

def boss_battle(player):
    '''
    Fill in later on:
    Todo: 
        3 battles with goblins beforehand
        1 big battle at the end
        Rescure the princess?
    '''
    monster = Monster()
    boss_monster = BossMonster()

    playing = True
    while playing:
        for i in range(3):
            text_delay(f"You have encountered a {monster.name}")
        break