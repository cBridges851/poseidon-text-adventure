from components.text_delay import text_delay
from components.file_logic import FileLogic
import json

GAME_ITEMS_FILEPATH = "./game_items.json"
PLAYER_FILEPATH = "./player.json"

class Shop():
    def __init__(self, player):
        '''
            The method for initalising the shop.  
            Args:
                player: obj, player object.
        '''
        self.player = player
        # All the houses the player could buy and their cost
        self.available_houses = {
            "shack": 0,  # The house the player starts with
            "bungalow": 100, 
            "two-story house": 300, 
            "mansion": 500
        }
        # All the items in the shop
        self.shop_items = ["armour", "apple", "jar of air", "sword upgrade"]
        # All the items in the game
        self.all_game_items = self.get_all_game_items()

    def get_all_game_items(self):
        '''
            Gets all the items the player could possibly buy and/or sell.  
            Returns:
                item_content: dictionary, all the possible items in the game.
        '''
        # Gets all the game items and returns them
        item_content = FileLogic().get_json(GAME_ITEMS_FILEPATH)
        return item_content

    def enter_shop(self):
        '''
            The method is called when the player enters the shop.  
            Returns:
                player: obj, player object.
        '''
        text_delay("You open the door to the shop and step inside. It's a little bit dark given" 
                    + " it is only lit using candles, so do watch your step." 
                    + " There are a few risen floor boards"
                    + " and a few mice here and there... Anyway, you can buy and sell items here! Oh!"
                    + " You can upgrade your house too.")
        # Runs the shop menu until the player wants to leave, leading to the player object being returned
        self.shop_menu()
        return self.player

    def shop_menu(self):
        '''
            The method that allows the player to select what they will do in the shop.    
            Returns (when the user chooses to exit):
                player: obj, player object.
        '''
        print("---------------------------------------------------------------------------------------------")
        text_delay(f"You have {self.player.coins} coins on your person.")

        # Print inventory.
        if len(self.player.inventory) != 0:
            print("Here is your inventory:")
            for item in self.player.inventory:
                print(f"Item Name: {item}")
                print(f"Quantity: {self.player.inventory[item]}")
                print("---------------------------------------------------------------------------------------------")

        user_input = ""

        # Get user choice for what they want to do inside shop.
        while user_input != "B" and user_input != "S" and user_input != "U" and user_input != "E":
            user_input = input("Would you like to buy(B) or sell(S) items, upgrade your house (U), or exit (E)? ").upper()

        if user_input == "B":
            # Calls the method that allows them to buy items
            self.buy()
        elif user_input == "S":
            # Calls the method that allows them to sell items
            self.sell()
        elif user_input == "U":
            # Calls the method that allows them to upgrade their house
            self.upgrade_house()
        else:
            # Kindly bids the player farewell if they choose to leave the shop
            text_delay("Great, thanks for stopping by. Now get out.")
            return self.player

    def buy(self):
        '''
            The method that allows the player to buy items from the shop.  
            Calls the shop_menu method when they have finished buying an item.  
            Returns:
                Just returns when there is an invalid input to prevent code continuing.
        '''
        print("\nHere are the items you can buy:")
        print("---------------------------------------------------------------------------------------------")

        # Print shop inventory.
        for item in self.shop_items:
            print(f"Item Name: {item}")
            
            if item in self.all_game_items:
                print(f"Price: {self.all_game_items[item]}")
            print("---------------------------------------------------------------------------------------------")

        # Get name of item.
        item_to_buy = input("Enter the item name of what you could like to buy," 
                            + " or press E if you're being awkward and changed your mind: ").lower()

        # Allows the user to leave this menu
        if item_to_buy == "e":
            self.shop_menu()
            return

        # Check what they entered is in the shop items.
        if item_to_buy not in self.shop_items:
            print("That isn't an item in the shop. Can you even read?")
            self.buy()
            return

        # Get quantity of item.
        quantity = int(input(f"How many {item_to_buy}s would you like to buy? "))
        cost = quantity * self.all_game_items[item_to_buy]

        # Check the quantity entered.
        if quantity == 0:
            print(f"What do you mean you want to buy 0 {item_to_buy}s?")
            self.buy()
        # Output with correct grammar
        elif quantity == 1:
            # Singular
            print(f"{quantity} {item_to_buy} costs {cost} coins.")
        else:
            # Plural
            print(f"{quantity} {item_to_buy}s cost {cost} coins.")

        # Check they can afford the item.
        if self.player.coins < cost:
            print("You don't have enough money, and we don't do discounts.")
            self.buy()
            return

        confirm_buy = ""

        # Checking if they want to really buy the item in a grammatically correct manner
        if quantity == 1:
            # Singular
            confirm_buy = input(f"Are you sure you want to buy { quantity } { item_to_buy }? (Y/N) ").upper()
        else:
            # Plural
            confirm_buy = input(f"Are you sure you want to buy { quantity } { item_to_buy }s? (Y/N) ").upper()

        while confirm_buy != "Y" and confirm_buy != "N":
            if quantity == 1:
                confirm_buy = input(f"Are you sure you want to buy { quantity } { item_to_buy }? (Y/N) ").upper()
            else:
                confirm_buy = input(f"Are you sure you want to buy { quantity } { item_to_buy }s? (Y/N) ").upper()

        # For if the user definitely does want to buy the item
        if confirm_buy == "Y":
            self.player.coins -= cost
            # If the sword upgraded is choose update damage else add to player inventory.
            if item_to_buy == "sword upgrade":
                damage_to_add = 5 * quantity
                self.player.damage += damage_to_add
                FileLogic().update_player_property(PLAYER_FILEPATH, self.player, "Damage", self.player.damage)
            else:
                # Updating the player object depending on the purchase.
                if item_to_buy in self.player.inventory:
                    self.player.inventory[item_to_buy] += quantity
                    FileLogic().update_player_property(PLAYER_FILEPATH, self.player, "Inventory", self.player.inventory)
                else:
                    self.player.inventory[item_to_buy] = quantity
                    FileLogic().update_player_property(PLAYER_FILEPATH, self.player, "Inventory", self.player.inventory)

        FileLogic().update_player_property(PLAYER_FILEPATH, self.player, "Coins", self.player.coins)
        self.shop_menu()

    def sell(self):
        '''
            The method that allow the player to sell items from their inventory.  
            Calls the shop_menu method when they have finished selling an item.  
            Returns:
                Just returns when there is an invalid input to prevent code continuing.
        '''
        # Check the player has items to sell.
        if len(self.player.inventory) == 0:
            print("You have no items you can sell. What do you plan to sell? Air from your lungs?")
            # Takes them back to the shop menu
            self.shop_menu()
            return

        # Print player inventory.
        print("\nHere are the items in your inventory you can sell:")
        print("---------------------------------------------------------------------------------------------")
        for item in self.player.inventory:
            print(f"Item: {item}")
            print(f"Quantity: {self.player.inventory[item]}")
            self.all_game_items[item] = round(self.all_game_items[item] * 0.90)
            print(f"Price per item: {self.all_game_items[item]}")
            print("---------------------------------------------------------------------------------------------")

        # Get inventory item.
        item_to_sell = input("What would you like to sell, or are you going to be awkward and press E to exit? ").lower()

        # Allow the player to exit this menu
        if item_to_sell == "e":
            self.shop_menu()
            return

        # Check the item they wanted to sell is in the player's inventory.
        if item_to_sell not in self.player.inventory:
            print(f"Oh you'd like to sell your {item_to_sell}? Where is it then?" 
                    + " Oh you don't actually have one? Funny that. I don't buy imaginary items.")
            self.sell()

        # Get quantity of items.
        quantity = int(input(f"How many {item_to_sell}s would you like to sell? "))

        # Checking the quantity entered.
        if quantity == 0:
            print(f"Fine, I won't buy any {item_to_sell}s from you then, weirdo.")
            self.sell()
            return

        # For if the quantity they inputted is more than what they actually have
        if quantity > self.player.inventory[item_to_sell]:
            print(f"You don't even have that many {item_to_sell}s, can you even count?")
            self.sell()
            return

        cost = self.all_game_items[item_to_sell] * quantity
        confirm_sell = ""
    
        # Confirming they want to sell the item in a grammatically correct manner
        if quantity == 1:
            # Singular
            confirm_sell = input(f"I'll buy {quantity} {item_to_sell} for {cost} coins. Does that sound good? (Y/N) ").upper()
        else:
            # Plural
            confirm_sell = input(f"I'll buy {quantity} {item_to_sell}s for {cost} coins. Does that sound good? (Y/N) ").upper()

        while confirm_sell != "Y" and confirm_sell != "N":
            if quantity == 1:
                confirm_sell = input(f"I'll buy {quantity} {item_to_sell} for {cost} coins. Does that sound good? (Y/N) ").upper()
            else:
                confirm_sell = input(f"I'll buy {quantity} {item_to_sell}s for {cost} coins. Does that sound good? (Y/N) ").upper()

        # Update player's inventory and coins based off the sale.
        if confirm_sell == "Y":
            self.player.coins += cost
            self.player.inventory[item_to_sell] -= quantity

            # Remove the item from the player's inventory list if they do not have any more of it
            if self.player.inventory[item_to_sell] == 0:
                self.player.inventory.pop(item_to_sell)

        FileLogic().update_player_property(PLAYER_FILEPATH, self.player, "Inventory", self.player.inventory)
        FileLogic().update_player_property(PLAYER_FILEPATH, self.player, "Coins", self.player.coins)
        self.shop_menu()

    def upgrade_house(self):
        '''
            The method that allows the user to upgrade their house.  
            Calls the shop_menu method when they have finished upgrading their house.  
            Returns:
                Just returns when the player does not have enough coins or 
                cannot upgrade anymore to prevent code continuing. 
        '''
        # Get the player's current house.
        print(f"\nThis is the house you currently have: {self.player.house}")
        current_house_index = list(self.available_houses.keys()).index(self.player.house)

        # Check if they can upgrade the house they own.
        if current_house_index + 1 > len(list(self.available_houses.keys())) - 1:
            # They cannot upgrade their house any more, so they are taken back to the shop menu
            print("You can't upgrade your house any more.")
            self.shop_menu()
            return

        # The next house they can buy will be the next one in the list
        next_house = list(self.available_houses.keys())[current_house_index + 1]

        # Check they can afford the purchase.
        if self.available_houses[next_house] > self.player.coins:
            print("You don't have enough money to upgrade")
            self.shop_menu()
            return
        
        confirm_upgrade = ""

        # Purchase input validation.
        while confirm_upgrade != "Y" and confirm_upgrade != "N":
            confirm_upgrade = input(f"Would you like to upgrade to a {next_house} for {self.available_houses[next_house]} coins?(Y/N) ").upper()

        # Update players balance and house.
        if confirm_upgrade == "Y":
            self.player.house = next_house
            self.player.coins -= self.available_houses[next_house]

        FileLogic().update_player_property(PLAYER_FILEPATH, self.player, "House", self.player.house)
        self.shop_menu()