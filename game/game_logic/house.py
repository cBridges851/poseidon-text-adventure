from components.file_logic import FileLogic
from components.text_delay import text_delay

class House():
    def __init__(self, player):
        self.player = player
        self.all_houses = {
            "shack": {
                "sleep": ["sack on the floor", 20],
                "storage": ["rotting crate", 10]
            },
            "bungalow": {
                "sleep": ["mattress with a blanket", 40],
                "storage": ["chest", 20]
            },
            "two-story house": {
                "sleep": ["single bed", 60],
                "storage": ["closet", 40]
            },
            "mansion": {
                "sleep": ["king-sized bed", 80],
                "storage": ["storage room", 80]
            }
        }
        self.player_house_object = self.all_houses[self.player.house]
        self.PLAYER_FILEPATH = "./player.json"

    def enter_house(self):
        text_delay(f"You get the keys out of your pocket and unlock the door to your {self.player.house}.")
        text_delay(f"In your house, there is a {self.player_house_object['sleep'][0]} and a {self.player_house_object['storage'][0]}.")
        self.house_menu()

    def house_menu(self):
        active = True

        while active == True:
            print("---------------------------------------------------------------------------------------------")
            user_input = ""

            while user_input != "S" and user_input != "U" and user_input != "E":
                user_input = input(f"Would you like to sleep in your {self.player_house_object['sleep'][0]} (S), use your {self.player_house_object['storage'][0]} (U) or exit (E)? ").upper()

            if user_input == "S":
                self.sleep()
            elif user_input == "U":
                self.storage()
            else:
                active = False

    def sleep(self):
        print("---------------------------------------------------------------------------------------------")
        if self.player.health < self.player_house_object["sleep"][1]:
            self.player.health = self.player_house_object["sleep"][1]
            FileLogic().update_player_property(self.PLAYER_FILEPATH, self.player, "Health", self.player.health)
            text_delay(f"Ah that was a nice sleep! You feel well-rested, and your health is now {self.player.health}")
        else:
            if self.player.house == "mansion":
                text_delay("You've already had plenty of sleep, go off and play! Kids these days, all they want to do is sleep.")
            else:
                text_delay("You need to upgrade your house to get a good night's sleep and heal more.")
    
    def storage(self):
        active = True

        while active == True:
            print("---------------------------------------------------------------------------------------------")
            user_input = ""
            amount_in_storage = 0

            for item in self.player.house_storage:
                amount_in_storage += self.player.house_storage[item]

            while user_input != "P" and user_input != "S" and user_input != "I" and user_input != "O" and user_input != "Q":
                user_input = input(f"Would you like to view the items on your person (P), view items in your {self.player_house_object['storage'][0]} (S), put something in your {self.player_house_object['storage'][0]} (I), take something out (O), or quit using the {self.player_house_object['storage'][0]} (Q)? ").upper()

            if user_input == "P":
                if len(self.player.inventory) == 0:
                    print("You have no items on your person")
                else:
                    print("Here are the items on your person:")

                    for item in self.player.inventory:
                        print(f"Item Name: {item}")
                        print(f"Quantity: {self.player.inventory[item]}")
                        print("---------------------------------------------------------------------------------------------")
            elif user_input == "S":
                if len(self.player.house_storage) == 0:
                    print(f"You have no items in your {self.player_house_object['storage'][0]}")
                else:
                    print(f"Here are the items in your {self.player_house_object['storage'][0]}:")

                    for item in self.player.house_storage:
                        print(f"Item Name: {item}")
                        print(f"Quantity: {self.player.house_storage[item]}")
                        print("---------------------------------------------------------------------------------------------")
            elif user_input == "I":
                if amount_in_storage == self.player_house_object['storage'][1]:
                    print("You cannot put any more items in storage")
                    self.storage()
                    return
                
                item_to_store = input(f"What would you like to put in your {self.player_house_object['storage'][0]}? ")
                
                if item_to_store not in self.player.inventory:
                    print("You don't have that in your inventory")
                    self.storage()
                    return
                
                quantity = int(input(f"How may {item_to_store}s would you like to put away?"))

                if self.player.inventory[item_to_store] < quantity:
                    print(f"You don't have that many {item_to_store}s.")
                    self.storage()
                    return

                if (self.player_house_object['storage'][1] - quantity) < 0:
                    print("You do not have enough room for all those items.")
                    self.storage()
                    return

                # Adjust the amount in the house storage
                if item_to_store in self.player.house_storage:
                    self.player.house_storage[item_to_store] += quantity
                    FileLogic().update_player_property(self.PLAYER_FILEPATH, self.player, "House Storage", self.player.house_storage)
                else:
                    self.player.house_storage[item_to_store] = quantity
                    FileLogic().update_player_property(self.PLAYER_FILEPATH, self.player, "House Storage", self.player.house_storage)

                if self.player.house_storage[item_to_store] == 1:
                    print(f"You now have {self.player.house_storage[item_to_store]} {item_to_store} in your {self.player_house_object['storage'][0]}.")
                else:
                    print(f"You now have {self.player.house_storage[item_to_store]} {item_to_store}s in your {self.player_house_object['storage'][0]}.")

                # Adjust the amount in inventory
                self.player.inventory[item_to_store] -= quantity

                if self.player.inventory[item_to_store] == 0:
                    self.player.inventory.pop(item_to_store)

                FileLogic().update_player_property(self.PLAYER_FILEPATH, self.player, "Inventory", self.player.inventory)
            elif user_input == "O":
                if amount_in_storage == 0:
                    print("You don't have any items in storage you can take out.")
                    self.storage()
                    return
                
                item_to_store = input(f"What would you like to take out of your {self.player_house_object['storage'][0]}? ")

            else:
                active = False