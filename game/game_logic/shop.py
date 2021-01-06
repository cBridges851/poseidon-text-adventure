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
        self.available_houses = {
            "shack": 0, 
            "bungalow": 100, 
            "two-story house": 300, 
            "mansion": 500
        }
        self.shop_items = ["armour", "apple", "jar of air", "weapon upgrade", "bow and arrow", "heavy axe"]
        self.all_game_items = self.get_all_game_items()

    def get_all_game_items(self):
        '''
            Gets all the items the player could possibly buy and/or sell.
            Returns:
                item_content: dictionary, all the possible items in the game.
        '''
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
        self.shop_menu()
        return (self.player)

    def shop_menu(self):
        '''
            The method that allows the player to select what they will do in the shop.
            Returns (when the user chooses to exit):
                player: obj, player object.
        '''
        print("---------------------------------------------------------------------------------------------")
        text_delay(f"You have {self.player.coins} coins on your person.")

        if len(self.player.inventory) != 0:
            print("Here is your inventory:")
            for item in self.player.inventory:
                print(f"Item Name: {item}")
                print(f"Quantity: {self.player.inventory[item]}")
                print("---------------------------------------------------------------------------------------------")

        user_input = ""
        while user_input != "B" and user_input != "S" and user_input != "U" and user_input != "E":
            user_input = input("Would you like to buy(B) or sell(S) items, upgrade your house (U), or exit (E)? ").upper()

        if user_input == "B":
            self.buy()

        elif user_input == "S":
            self.sell()
        
        elif user_input == "U":
            self.upgrade_house()

        else:
            text_delay("Great, thanks for stopping by. Now get out.")
            return (self.player)

    def buy(self):
        '''
            The method that allows the player to buy items from the shop.
            Calls the shop_menu method when they have finished buying an item.
            Returns:
                Just returns when there is an invalid input to prevent code continuing.
        '''
        print("\nHere are the items you can buy:")
        print("---------------------------------------------------------------------------------------------")

        for item in self.shop_items:
            print(f"Item Name: {item}")
            
            if item in self.all_game_items:
                print(f"Price: {self.all_game_items[item]}")
            print("---------------------------------------------------------------------------------------------")

        item_to_buy = input("Enter the item name of what you could like to buy," 
                            + " or press E if you're being awkward and changed your mind: ").lower()

        if item_to_buy == "e":
            self.shop_menu()
            return

        if item_to_buy not in self.shop_items:
            print("That isn't an item in the shop. Can you even read?")
            self.buy()
            return

        quantity = int(input(f"How many {item_to_buy}s would you like to buy? "))
        cost = quantity * self.all_game_items[item_to_buy]

        if quantity == 0:
            print(f"What do you mean you want to buy 0 {item_to_buy}s?")
            self.buy()
        elif quantity == 1:
            print(f"{quantity} {item_to_buy} costs {cost} coins.")
        else:
            print(f"{quantity} {item_to_buy}s cost {cost} coins.")

        if self.player.coins < cost:
            print("You don't have enough money, and we don't do discounts.")
            self.buy()
            return

        confirm_buy = ""

        if quantity == 1:
            confirm_buy = input(f"Are you sure you want to buy { quantity } { item_to_buy }? (Y/N) ").upper()
        else:
            confirm_buy = input(f"Are you sure you want to buy { quantity } { item_to_buy }s? (Y/N) ").upper()

        while confirm_buy != "Y" and confirm_buy != "N":
            if quantity == 1:
                confirm_buy = input(f"Are you sure you want to buy { quantity } { item_to_buy }? (Y/N) ").upper()
            else:
                confirm_buy = input(f"Are you sure you want to buy { quantity } { item_to_buy }s? (Y/N) ").upper()

        if confirm_buy == "Y":
            self.player.coins -= cost
            if item_to_buy == "weapon upgrade":
                damage_to_add = 5 * quantity
                self.player.damage += damage_to_add
                FileLogic().update_player_property(PLAYER_FILEPATH, self.player, "Damage", self.player.damage)
            else:
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
        if len(self.player.inventory) == 0:
            print("You have no items you can sell. What do you plan to sell? Air from your lungs?")
            self.shop_menu()
            return

        print("\nHere are the items in your inventory you can sell:")
        print("---------------------------------------------------------------------------------------------")
        for item in self.player.inventory:
            print(f"Item: {item}")
            print(f"Quantity: {self.player.inventory[item]}")
            self.all_game_items[item] = round(self.all_game_items[item] * 0.90)
            print(f"Price per item: {self.all_game_items[item]}")
            print("---------------------------------------------------------------------------------------------")

        item_to_sell = input("What would you like to sell, or are you going to be awkward and press E to exit? ").lower()

        if item_to_sell == "e":
            self.shop_menu()
            return

        if item_to_sell not in self.player.inventory:
            print(f"Oh you'd like to sell your {item_to_sell}? Where is it then?" 
                    + " Oh you don't actually have one? Funny that. I don't buy imaginary items.")
            self.sell()

        quantity = int(input(f"How many {item_to_sell}s would you like to sell? "))

        if quantity == 0:
            print(f"Fine, I won't buy any {item_to_sell}s from you then, weirdo.")
            self.sell()
            return

        if quantity > self.player.inventory[item_to_sell]:
            print(f"You don't even have that many {item_to_sell}s, can you even count?")
            self.sell()
            return

        cost = self.all_game_items[item_to_sell] * quantity
        confirm_sell = ""

        if quantity == 1:
            confirm_sell = input(f"I'll buy {quantity} {item_to_sell} for {cost} coins. Does that sound good? (Y/N) ").upper()
        else:
            confirm_sell = input(f"I'll buy {quantity} {item_to_sell}s for {cost} coins. Does that sound good? (Y/N) ").upper()

        while confirm_sell != "Y" and confirm_sell != "N":
            if quantity == 1:
                confirm_sell = input(f"I'll buy {quantity} {item_to_sell} for {cost} coins. Does that sound good? (Y/N) ").upper()
            else:
                confirm_sell = input(f"I'll buy {quantity} {item_to_sell}s for {cost} coins. Does that sound good? (Y/N) ").upper()

        if confirm_sell == "Y":
            self.player.coins += cost
            self.player.inventory[item_to_sell] -= quantity

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
        print(f"\nThis is the house you currently have: {self.player.house}")
        current_house_index = list(self.available_houses.keys()).index(self.player.house)

        if current_house_index + 1 > len(list(self.available_houses.keys())) - 1:
            print("You can't upgrade your house any more.")
            self.shop_menu()
            return

        next_house = list(self.available_houses.keys())[current_house_index + 1]

        if self.available_houses[next_house] > self.player.coins:
            print("You don't have enough money to upgrade")
            self.shop_menu()
            return
        
        confirm_upgrade = ""

        while confirm_upgrade != "Y" and confirm_upgrade != "N":
            confirm_upgrade = input(f"Would you like to upgrade to a {next_house} for {self.available_houses[next_house]} coins?(Y/N) ").upper()

        if confirm_upgrade == "Y":
            self.player.house = next_house
            self.player.coins -= self.available_houses[next_house]

        FileLogic().update_player_property(PLAYER_FILEPATH, self.player, "House", self.player.house)
        self.shop_menu()