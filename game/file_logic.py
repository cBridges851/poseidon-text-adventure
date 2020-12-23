import json
from player import Player
from types import SimpleNamespace

class FileLogic:
    def get_json(self, filepath):
        '''
        Opens the content of the Json file.
        Args:
            filepath: string, representing a filepath.
        Returns:
            file_content: dic, representing file contents.
        '''
        try:
            with open(filepath, "r") as content:
                file = content.read()
        except FileNotFoundError:
            print("ERROR: File not found, check your file path.")
            exit()
        except PermissionError:
            print("ERROR: You lack the permissions to read this file.")
            exit()

        file_content = json.loads(file)

        return file_content


    def update_json_file(self, filepath, file_content):
        '''
        Update the Json file using the content passed in.
        Args:
            filepath: string, representing a filepath.
            file_content: dic, representing Json.
        '''
        try:
            file_content = json.dumps(file_content)
            with open(filepath, "w") as content:
                content.write(file_content)
        except FileNotFoundError:
            print("ERROR: File not found, check your file path.")
            exit()
        except PermissionError:
            print("ERROR: You lack the permissions to read this file.")
            exit()


    def get_balance(self, filepath, player):
        '''
        Get the coin balance of a given player.
        Args:
            filepath: string, representing a filepath.
            player: obj, player object with properties on.
        Returns:
            balance: integer, player's coin balance.
        '''
        file_content = FileLogic().get_json(filepath)

        balance = 0

        for item in file_content["Players"]:
            if item["Name"] == player.name:
                balance = item["Bank Balance"]

        return balance


    def update_balance(self, filepath, player):
        '''
        Update the coin balance in the bank.
        Args:
            filepath: string, representing a filepath.
            player: obj, player object with properties on.
        '''
        file_content = FileLogic().get_json(filepath)

        for item in file_content["Players"]:
            if item["Name"] == player.name:
                item["Bank Balance"] += player.coins
        
        FileLogic().update_json_file(filepath, file_content)


    def update_balance_by_set_amount(self, filepath, player, coins):
        '''
        Update the coin balance in the bank by a set amount.
        Args:
            filepath: string, representing a filepath.
            player: obj, player object with properties on.
            coins: integer, coins to update by.
        '''

        file_content = FileLogic().get_json(filepath)

        for item in file_content["Players"]:
            if item["Name"] == player.name:
                item["Bank Balance"] += coins

        FileLogic().update_json_file(filepath, file_content)


    def withdraw_by_set_amount(self, filepath, player, coins):
        '''
        Withdraw money from the bank by a set amount.
        Args:
            filepath: string, representing a filepath.
            player: obj, player object with properties on.
            coins: integer, amount to restore.
        Returns: 
            player: obj, player object with updated properties on.
        '''
        file_content = FileLogic().get_json(filepath)

        for item in file_content["Players"]:
            if item["Name"] == player.name:
                item["Bank Balance"] -= coins
        
        FileLogic().update_json_file(filepath, file_content)
        player.coins += coins
        FileLogic().update_player_property(filepath, player, "Coins", player.coins)

        return player


    def add_new_player(self, filepath, player):
        '''
        Add a new player to the player.json file with a balance of 0.
        Args:
            filepath: string, representing a filepath.
            player: obj, player object representing a new player.
        '''
        file_content = FileLogic().get_json(filepath)

        new_player = {
            "Name" : player.name,
            "Bank Balance" : 0,
            "Health": 100,
            "Damage": 15,
            "Coins": 0,
            "House": "shack",
            "Inventory": {}
        }

        file_content["Players"].append(new_player)

        FileLogic().update_json_file(filepath, file_content)

    def retrieve_player(self, filepath, name):
        file_content = FileLogic().get_json(filepath)
        player = Player()
        playerFound = False

        for item in file_content["Players"]:
            if item["Name"] == name:
                playerFound = True
                player.name = item["Name"]
                player.health = item["Health"]
                player.damage = item["Damage"]
                player.coins = item["Coins"]
                player.house = item["House"]
                player.inventory = item["Inventory"]

        if playerFound == False:
            print("Player not found, creating a new player.")
            player.name = name
            FileLogic().add_new_player("./player.json", player)

        return player


    def update_player_property(self, filepath, player, propertyName, propertyValue):
        file_content = FileLogic().get_json(filepath)
        for item in file_content["Players"]:
            if item["Name"] == player.name:
                item[propertyName] = propertyValue
        
        FileLogic().update_json_file(filepath, file_content)