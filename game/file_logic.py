class FileLogic:
    def open_file_by_newline(self, filepath):
        '''
        Open a file and split the content by newlines.
        Args:
            filepath: string, representing a filepath.
        Returns:
            file: list, representing the file contents by newline.
        '''
        try:
            with open(filepath, "r") as content:
                file = content.read().split("\n")
        except FileNotFoundError:
            print("ERROR: File not found, check your file path.")
            exit()
        except PermissionError:
            print("ERROR: You lack the permissions to read this file.")
            exit()

        return file


    def write_file_using_list(self, filepath, file_content):
        '''
        Write to a file using an given in list.
        Args: 
            filepath: string, representing a filepath.
            list: list, containing the file contents.
        '''
        try:
            with open(filepath, "w") as content:
                content.writelines(file_content)
        except FileNotFoundError:
            print("ERROR: File not found, check your file path.")
            exit()
        except PermissionError:
            print("ERROR: You lack the permissions to write this file.")
            exit()

    
    def get_balance(self, filepath, player):
        '''
        Get the coin balance of a given player.
        Args:
            filepath: string, representing a filepath.
            player: string, player name.
        Returns:
            balance: integer, player coin balance.
        '''
        records = FileLogic().open_file_by_newline(filepath)
        
        individual_player = ""
        balance = 0

        for record in range(len(records)):
            individual_player = records[record].split()
            if individual_player[1] == player:
                balance = int(individual_player[0])

        return balance


    def update_balance(self, filepath, player, coins):
        '''
        Update the coin balance of an existing player.
        Args:
            filepath: string, representing a filepath.
            player: string, player name.
            coins: integer, coins in the players inventory.
        '''
        file = FileLogic().open_file_by_newline(filepath)

        for item in range(len(file)):
            if file[item] == "":
                file.remove(file[item])

        individual_player = ""
        for item in range(len(file)):
            individual_player = file[item].split()

            if individual_player[1] == player:
                updated_total = int(individual_player[0]) + coins
                if item != 0:
                    file[item] = "\n" + str(updated_total) + " " + player
                else:
                    file[item] = str(updated_total) + " " + player
            elif item != 0:
                file[item] = "\n" + file[item]
            else:
                file[item] = file[item]

        FileLogic().write_file_using_list(filepath, file)


    def add_player(self, filepath, player):
        '''
        Adds a new player to the database.
        Args:
            filepath: string, representing a filepath.
            player: string, player name.
        '''
        file = FileLogic().open_file_by_newline(filepath)

        for item in range(len(file)):
            if file[item] == "":
                file.remove(file[item])

        file.append("0" + " " + player)

        for item in range(len(file)):
            if item != 0:
                file[item] = "\n" + file[item]
            else:
                file[item] = file[item]
                
        FileLogic().write_file_using_list(filepath, file)