import random
from components.file_logic import FileLogic
from components.text_delay import text_delay
from models.player import Player

class MonsterFight:
    def __init__(self, player, monster):
        '''
        Initilises the player and monster in the class.
        Args:
            player: obj, representing a player.
            monster: obj, representing a monster.
        '''
        self.PLAYER_FILENAME = "./player.json"
        self.player = player
        self.monster = monster

    def monster_fight(self, min, max):
        '''
        Reusable component where players can fight monsters.
        Args:
            min: integer, representing a min value for damage.
            max: integer, representing a max value for damage.
        Returns:
            active: bool, returns depending on whether the user runs away or not.
        '''
        active = True
        while self.monster.health > 0:
            print("------------------------------------------------------------------------------")
            player_input = ""
            while player_input != "A" and player_input != "R":
                player_input = input(f"To attack {self.monster.name}, press (A). To run away press (R): ").upper()
            
            if player_input == "A":
                self.monster.health -= self.player.damage
                print(f"You attacked the {self.monster.name} dealing {self.player.damage}. The monster has {self.monster.health} left.")
                self.monster.damage = random.randint(min, max)

                if self.monster.health <= 0:
                    break
                else:
                    self.player.health -= self.monster.damage
                    FileLogic().update_player_property(self.PLAYER_FILENAME, self.player, "Health", self.player.health)

                print(f"{self.monster.name} attacked you, leaving you with {self.player.health}.")

            if player_input == "R":
                active = False
                break
            
            if Player().is_player_dead(self.player.health) == True:
                active = False
                break
        
        return active