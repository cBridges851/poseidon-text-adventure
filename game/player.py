class Player:
    def __init__(self):
        self.name = None
        self.health = 100
        self.damage = 15
        self.coins = 0
        self.house = "shack"
        self.inventory = {}

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