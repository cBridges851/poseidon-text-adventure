from text_delay import text_delay
from file_logic import FileLogic
import json

GAME_ITEMS_FILEPATH = r"./game/game_items.json"

class Shop():
    def __init__(self, player_coins, player_house, player_inventory):
        self.player_coins = player_coins
        self.player_house = player_house
        self.player_inventory = {}
        self.available_houses = ["Bungalow"]
        self.shop_items = ["armour", "apple", "jar of air"]
        self.all_game_items = self.get_all_game_items()

    def get_all_game_items(self):
        item_content = FileLogic().open_json(GAME_ITEMS_FILEPATH)
        item_content = json.load(item_content)
        return item_content

    def enter_shop(self):
        text_delay("You open the door to the shop and step inside. It's a little bit dark given" 
                    + " it is only lit using candles, so do watch your step." 
                    + " There are a few risen floor boards"
                    + " and a few mice here and there... Anyway, you can buy and sell items here! Oh!"
                    + " You can upgrade your house too.")
        self.shop_menu()

    def shop_menu(self):
        text_delay(f"You have {self.player_coins} coins on your person.")

        if len(self.player_inventory) != 0:
            print("Here is your inventory:")
            for item in self.player_inventory:
                print(f"Item Name: {item}")
                print(f"Quantity: {self.player_inventory[item]}")
                print("----------------------------------------")

        user_input = input("Would you like to buy(B) or sell(S) items, upgrade your house (U), or exit (E)? ").upper()
        while user_input != "B" and user_input != "S":
            user_input = input("Would you like to buy(B) or sell(S) items, upgrade your house (U), or exit (E)? ").upper()

        if user_input == "B":
            self.buy()

        elif user_input == "S":
            print("You are choosing to sell")
        
        elif user_input == "U":
            print("You are choosing to upgrade your house")

        else:
            return (self.player_house, self.player_coins)

    def buy(self):
        print("Here are the items you can buy:")
        
        print("----------------------------------------")

        for item in self.shop_items:
            print(f"Item Name: {item}")
            
            if item in self.all_game_items:
                print(f"Price: {self.all_game_items[item]}")
            print("----------------------------------------")

        item_to_buy = input("Enter the item name of what you could like to buy," 
                            + " or press E if you're being awkward and changed your mind: ").lower()

        if item_to_buy not in self.shop_items:
            print("That isn't an item in the shop. Can you even read?")
            self.buy()
            return

        quantity = int(input(f"How many {item_to_buy}s would you like to buy?"))
        cost = quantity * self.all_game_items[item_to_buy]
        print(f"{item_to_buy} costs {cost}")

        if self.player_coins < cost:
            print("You don't have enough money, and we don't do discounts.")
            self.buy()
            return

        confirm_buy = input(f"Are you sure you want to buy { quantity } { item_to_buy }s? (Y/N)").upper()

        while confirm_buy != "Y" and confirm_buy != "N":
            confirm_buy = input(f"Are you sure you want to buy { quantity } { item_to_buy }s? (Y/N)").upper()

        if confirm_buy == "Y":
            self.player_coins -= cost
            if item_to_buy in self.player_inventory:
                self.player_inventory[item_to_buy] += quantity
            else:
                self.player_inventory[item_to_buy] = quantity

        self.shop_menu()

    def sell(self):
        print()



Shop(500, "no house", []).enter_shop()