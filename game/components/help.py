class Help:
    def display_help(self):
        '''
        Displays help for the user, such as commands and hints.
        '''
        print("Navigation:")
        print("When in the main square -")
        print("    'n/north/go north/move north' To move.")
        print("    'e/east/go east/move east' To move.")
        print("    's/south/go south/move south' To move.")
        print("    'w/west/go west/move west' To move.")
        print("    'exit/quit' To close the game.")
        print("When in another area -")
        print("    'enter *name*/go in *name*/*name*/short hand name e.g. B, S, M'")
        print("    To return to the main square, move in the opposite direction.")
        print("        E.g. 'move south' if you are in the north.")
        print("Fighting bosses:")
        print("Commands you can use -")
        print("    'a/attack/attack monster/attack *monster name*'")
        print("    'r/run/run away'")
        print("------------------------------------------------------------------------------")