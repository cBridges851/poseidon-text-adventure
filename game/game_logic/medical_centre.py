import time 
from components.file_logic import FileLogic
from components.text_delay import text_delay

class MedicalCentre:
    '''
        Class for when the user chooses to enter the medical centre
    '''
    def __init__(self, player):
        '''
            Initialises the medical centre
        '''
        self.player = player
        self.PLAYER_FILEPATH = "./player.json"

    def enter_medical_centre(self, near_death=False):
        '''
            Allows the player to enter the medical centre and they decide whether they  
            wish to have treatment.
        '''
        text_delay("You enter the medical centre. There are lots of ill people about, but at least the place is somewhat clean.")
        
        # If the player is not about to die, charge them
        if not near_death:
            text_delay("It costs 5 coins to get treatment from the medical centre.")
            get_treatment = ""

            # Check they want to have treatment.
            while get_treatment != "Y" and get_treatment != "N":
                get_treatment = input("Would you like to have treatment (Y/N)? ").upper()

            if get_treatment == "Y":
                # Check they can afford treatment.
                if self.player.coins < 5:
                    text_delay("You are too poor for treatment. Go away peasant.")
                else:
                    # Remove coins from the player.
                    self.player.coins -= 5
                    FileLogic().update_player_property(self.PLAYER_FILEPATH, self.player, "Coins", self.player.coins)
                    self.heal(100)
            else:
                text_delay("Okay. Bye.")

        else:
            # If the player is about to die, heal them up to 50 health points
            text_delay("You cannot afford great medical treatment since you lost all your coins in the fight, but I suppose we better give you SOME treatment since you're nearly dead.")
            self.heal(50)
            

    def heal(self, health_point_increase):
        '''
            Heals the player by setting their health to 100.  
            Args:
                self: to retrieve the player, which has the health property
        '''
        
        print(f"Your current health is {self.player.health}!")
        text_delay("Healing...")
        # Time in medical centre is based off how much health they have. 
        # Large amount, shorter time and vice versa.
        delay_time = (100 - self.player.health) / 20 
        time.sleep(delay_time)

        if health_point_increase == 100:
            print("You are all better!")
        else:
            print("You're not ALL better, but you're not as dead as before. Be grateful.")

        # Update the player health property based off the treatment.
        self.player.health = health_point_increase
        FileLogic().update_player_property(self.PLAYER_FILEPATH, self.player, "Health", self.player.health)
        print(f"Your current health is now {health_point_increase}!")
