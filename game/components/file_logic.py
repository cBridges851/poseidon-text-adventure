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
        # Attempts to open the file specified in the filepath
        try:
            with open(filepath, "r") as content:
                file = content.read()
        except FileNotFoundError:
            print("ERROR: File not found, check your file path.")
            exit()
        except PermissionError:
            print("ERROR: You lack the permissions to read this file.")
            exit()

        # Deserialises the JSON
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
            # Serialises the content that will be written to the file, so it is
            # turned into JSON
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
            Add a new player to the player.json file with their name and 
            default values for the other properties  
            Args:
                filepath: string, representing a filepath.
                player: obj, player object representing a new player.
            Returns:
                player_exists: bool, if the player already exists.
        '''
        file_content = FileLogic().get_json(filepath)

        # Creates a new player with starting values
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
            # Appends the new player to the lists of players and the JSON is updated
            file_content["Players"].append(new_player)
            FileLogic().update_json_file(filepath, file_content)
        else:
            # Returns that the player does exist
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
        # Creates a new instance of the player class
        player = Player()
        player_found = False

        # Get a player and all its profile contents.
        for item in file_content["Players"]:
            if item["Name"] == name:
                player_found = True
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

        # Outputs if the player has not been found and returns null
        if not player_found:
            print("Hmmmm, we could not find that player.")
            return None

        # Otherwise, the player is returned
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

        # Search for the player and update the specified property.
        for item in file_content["Players"]:
            if item["Name"] == player.name:
                item[property_name] = property_value
        
        FileLogic().update_json_file(filepath, file_content)