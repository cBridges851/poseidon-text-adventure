import time 

class Hospital:
    '''
        Class for when the user chooses to enter the hospital
    '''
    def __init__(self, currentHealth):
        '''
            Initialises the hospital
        '''
        self.currentHealth = currentHealth

    def heal(self):
        '''
            Heals the player by setting their health to 100
            Args:
                self: to retrieve the player, which has the health property
        '''
        print("You enter the hospital. There are lots of ill people about, but at least the place is clean.")
        print("Healing...")
        delayTime = (100 - self.currentHealth) / 2 / 10 
        print(delayTime)
        time.sleep(delayTime)
        print("You are all better!")
        return 100