import time 
from components.text_delay import text_delay

class MedicalCentre:
    '''
        Class for when the user chooses to enter the medical centre
    '''
    def __init__(self, current_health):
        '''
            Initialises the medical centre
        '''
        self.current_health = current_health

    def heal(self):
        '''
            Heals the player by setting their health to 100
            Args:
                self: to retrieve the player, which has the health property
        '''
        text_delay("You enter the medical centre. There are lots of ill people about, but at least the place is somewhat clean.")
        print(f"Your current health is {self.current_health}!")
        text_delay("Healing...")
        delay_time = (100 - self.current_health) / 20 
        time.sleep(delay_time)
        print("You are all better!")
        print(f"Your current health is now 100!")
        return 100