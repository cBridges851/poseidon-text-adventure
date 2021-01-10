import random

class Monster:
    '''
    Used to represent the monster during the game and
    used during the monster fights.
    '''
    def __init__(self):
        '''
        Defines what makes up a monster.
        '''
        self.name = random.choice(["Trow", "Kobold", "Hobgoblin", "Bugbear"])
        self.health = random.randint(90, 100)
        self.damage = random.randint(1, 20)