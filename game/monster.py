import random

class Monster:
    def __init__(self):
        self.name = random.choice(["Trow", "Kobold", "Hobgoblin", "Bugbear"])
        self.health = random.randint(90, 100)
        self.damage = random.randint(1, 20)