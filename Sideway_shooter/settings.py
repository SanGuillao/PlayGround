class Settings:
    """ Hold all setting values """
    def __init__(self):
        # Screen
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230, 230, 230) # RGB code
        
        # Ship
        self.ship_speed = 1.5
        self.ship_limit = 3
        
        # Bullet
        self.bullet_speed = 1.5
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60) # RGB code
        # prevent the user from spamming bullets
        self.bullets_allowed = 3
        
        # Alien
        self.alien_speed = 1.0
        self.fleet_drop_speed = 15
        # fleet_direction = 1 means moving right, -1 means moving left
        self.fleet_direction = 1