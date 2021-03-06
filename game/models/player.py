class Player:
    '''
        Used to represent the player during the game and
        passed around the methods when the player moves.
    '''
    def __init__(self):
        '''
            Defines what makes up a player.
        '''
        self.name = None
        self.bank_balance = 0
        self.health = 100
        self.damage = 15
        self.coins = 0
        self.house = "shack"
        self.boss_beaten = False
        self.inventory = {}
        self.house_storage = {}
        self.monsters_killed = {}

    def is_player_dead(self, player_health):
        '''
            Check whether a player has 0 or less health.
            
            Args:
                player_health: int, representing the player health.
            Returns:
                True: bool, if the players health is below or equal to 0.
        '''
        if player_health <= 0:
            return True