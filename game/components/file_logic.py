import json
from models.player import Player

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

    def add_new_player(self, filepath, player):
        '''
            Add a new player to the player.json file with a balance of 0.  
            Args:
                filepath: string, representing a filepath.
                player: obj, player object representing a new player.
            Returns:
                player_exists: if the player already exists.
        '''
        file_content = FileLogic().get_json(filepath)

        new_player = {
            "Name" : player.name,
            "Bank Balance" : 0,
            "Health": 100,
            "Damage": 15,
            "Coins": 0,
            "House": "shack",
            "Boss Beaten" : False,
            "Inventory": {},
            "House Storage": {},
            "Monsters Killed": {}
        }

        player_exists = False

        # Player validation for when creating a new one making sure it can't already exist.
        for item in file_content["Players"]:
            if item["Name"] == new_player["Name"]:
                player_exists = True
                break

        if not player_exists:
            file_content["Players"].append(new_player)
            FileLogic().update_json_file(filepath, file_content)
        else:
            return player_exists

    def retrieve_player(self, filepath, name):
        '''
            Attempts to get the player based on the name that was inputted in adventure_game.py.  
            It creates an object if the player has been found.  
            Args:
                filepath: string, represents the file path that contains information about the registered players.
                name: string, the name the user inputted in adventure_game.py and this is used to find the player object.
            Returns:
                player: obj, the player object OR None if the player is not found.
        '''
        file_content = FileLogic().get_json(filepath)
        player = Player()
        playerFound = False

        # Get a player and all it's profile contents.
        for item in file_content["Players"]:
            if item["Name"] == name:
                playerFound = True
                player.name = item["Name"]
                player.bank_balance = item["Bank Balance"]
                player.health = item["Health"]
                player.damage = item["Damage"]
                player.coins = item["Coins"]
                player.house = item["House"]
                player.boss_beaten = item["Boss Beaten"]
                player.inventory = item["Inventory"]
                player.house_storage = item["House Storage"]
                player.monsters_killed = item["Monsters Killed"]

        if not playerFound:
            print("Hmmmm, we could not find that player.")
            return None

        return player

    def update_player_property(self, filepath, player, property_name, property_value):
        '''
            Updates the value of a given property.  
            Args:
                filepath: string, the file path to the file that needs to be adjsuted
                player: obj, player object
                property_name: string, the name of the property that needs to be changed.
                property_value: any, the value that the given property will be updated to.
        '''
        file_content = FileLogic().get_json(filepath)

        # Search for the player and update their profile.
        for item in file_content["Players"]:
            if item["Name"] == player.name:
                item[property_name] = property_value
        
        FileLogic().update_json_file(filepath, file_content)