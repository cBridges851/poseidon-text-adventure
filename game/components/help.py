class Help:
    def display_help(self):
        '''
        Displays help for the user, such as commands and hints.
        '''
        print("Navigation:")
        print("When in the main square -")
        print("    To move: 'n/north/go north/move north'")
        print("    To move: 'e/east/go east/move east'")
        print("    To move: 's/south/go south/move south'")
        print("    To move: 'w/west/go west/move west'")
        print("    To close the game: 'exit/quit'")
        print("When in another area -")
        print("    'enter *name*/go in *name*/*name*/short hand name e.g. B, S, M'")
        print("    To return to the main square, move in the opposite direction.")
        print("        E.g. 'move south' if you are in the north.")
        print("Fighting bosses:")
        print("Commands you can use -")
        print("    'a/attack/attack monster/attack *monster name*'")
        print("    'r/run/run away'")
        print("------------------------------------------------------------------------------")