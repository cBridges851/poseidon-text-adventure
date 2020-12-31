class Help:
    def display_help(self):
        '''
        Display help for the user. Such as commands and hints.
        '''
        print("Navigation:")
        print("When in the main square -")
        print("    'n, north, go north, move north' To move.")
        print("    'exit/quit' To close the game.")
        print("When in another area -")
        print("    '*name* enter, go in *name*, *name*, short hand name e.g. B, S, M'")
        print("    To return to the main square, move in the opposite direction.")
        print("        E.g. 'move south' if you are in the north.")
        print("Fighting bosses:")
        print("Commands you can use -")
        print("    'a, r, attack, run, run away, attack monster, attack *monster name*'")
        print("------------------------------------------------------------------------------")

Help().display_help()