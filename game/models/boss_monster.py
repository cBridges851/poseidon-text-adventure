import random

class BossMonster:
    '''
    Used to represent the boss monster during the game and
    used during the boss monster fight.
    '''
    def __init__(self):
        '''
        Defines what makes up a boss monster.
        '''
        self.name = "Gorgo"
        self.health = 150
        self.damage = random.randint(15, 20)