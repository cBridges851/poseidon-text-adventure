import random
from components.file_logic import FileLogic
from components.text_delay import text_delay
from models.player import Player

class MonsterFight:
    def __init__(self, player, monster):
        '''
            Initialises the player and monster in the class.  
            Args:
                player: obj, representing a player.
                monster: obj, representing a monster.
        '''
        self.PLAYER_FILENAME = "./player.json"
        self.player = player
        self.monster = monster

    def monster_fight(self, min_val, max_val):
        '''
            Reusable component where players can fight monsters.  
            Args:
                min_val: integer, representing a min value for damage.
                max_val: integer, representing a max value for damage.
            Returns:
                active: bool, returns depending on whether the user runs away or not.
        '''
        active = True

        # Monster battle
        while self.monster.health > 0:
            print("------------------------------------------------------------------------------")
            valid_inputs = ["A", "R", "ATTACK", "RUN", "RUN AWAY", f"ATTACK {self.monster.name}".upper(), "ATTACK MONSTER"]
            player_input = ""
            is_unacceptable = True
            
            # Get user input
            while is_unacceptable:
                if player_input not in valid_inputs:
                    player_input = input(f"What would you like to do: ").upper()
                else:
                    is_unacceptable = False
            
            # Attack monster
            if player_input == "A" or player_input == "ATTACK" or player_input == f"ATTACK {self.monster.name}".upper() or player_input == "ATTACK MONSTER":
                self.monster.health -= self.player.damage
                if self.monster.health < 0:
                    self.monster.health = 0
                print(f"You attacked the {self.monster.name} dealing {self.player.damage}. The monster has {self.monster.health} left.")
                # Randomise the monster attack.
                self.monster.damage = random.randint(min_val, max_val)

                if self.monster.health <= 0:
                    break
                else:
                    self.player.health -= self.monster.damage
                    FileLogic().update_player_property(self.PLAYER_FILENAME, self.player, "Health", self.player.health)

                print(f"{self.monster.name} attacked you, leaving you with {self.player.health}.")

            # Run away from monster
            if player_input == "R" or player_input == "RUN" or player_input == "RUN AWAY":
                active = False
                break
            
            # Is player dead yet?
            if Player().is_player_dead(self.player.health):
                active = False
                break
        
        return active