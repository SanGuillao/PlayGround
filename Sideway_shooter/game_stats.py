class GameStats:
    """ Track stats for the Game """
    
    def __init__(self, newGame):
        """ initialize statistics """
        self.settings = newGame.settings
        self.reset_stats()
        
        # set the game flag, that will control the game
        self.game_active = True
        
    def reset_stats(self):
        """ Initialize stats tht may change during the game """
        self.ships_left = self.settings.ship_limit