from components.file_logic import FileLogic
from components.text_delay import text_delay

class House():
    def __init__(self, player):
        self.player = player
        self.all_houses = {
            "shack": {
                "sleep": ["sack on the floor", 20]
            },
            "bungalow": {
                "sleep": ["mattress with a blanket", 40]
            },
            "two-story house": {
                "sleep": ["single bed", 60]
            },
            "mansion": {
                "sleep": ["king-sized bed", 80]
            }
        }
        self.player_house_object = self.all_houses[self.player.house]
        self.PLAYER_FILENAME = "./player.json"

    def enter_house(self):
            text_delay(f"You get the keys out of your pocket and unlock the door to your {self.player.house}.")
            text_delay(f"In your house, there is a {self.player_house_object['sleep'][0]}.")
            self.house_menu()

    def house_menu(self):
        active = True

        while active == True:
            user_input = ""

            while user_input != "S" and user_input != "E":
                user_input = input(f"Would you like to sleep in your {self.player_house_object['sleep'][0]} (S) or exit (E)? ").upper()

            if user_input == "S":
                self.sleep()
            else:
                active = False

    def sleep(self):
        if self.player.health < self.player_house_object["sleep"][1]:
            self.player.health = self.player_house_object["sleep"][1]
            FileLogic().update_player_property(self.PLAYER_FILENAME, self.player, "Health", self.player.health)
            text_delay(f"Ah that was a nice sleep! You feel well-rested, and your health is now {self.player.health}")
        else:
            if self.player.house == "mansion":
                text_delay("You've already had plenty of sleep, go off and play! Kids these days, all they want to do is sleep.")
            else:
                text_delay("You need to upgrade your house to get a good night's sleep and heal more.")