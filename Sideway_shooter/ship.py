import pygame

class Ship:
    """ Declare ship variables and func """
    # pass in an instance of the game
    def __init__(self, newGame):
        """ init variables """
        # get the current screen from the newGame instance 
        self.screen = newGame.screen
        # get the current settings from the newGame instance
        # for ship's speed
        self.settings = newGame.settings
        
        # set the current screen dimensions to the newGame instance
        self.screen_rect = newGame.screen.get_rect()
        
        # load the image onto the ship object
        self.image = pygame.image.load('images/ship.bmp')
        # get the rect around the img (basically hit-box)
        self.rect = self.image.get_rect()
        
        # set the starting coordinates of the ship
        # set it to the middle of the left side of the current instance of 
        # screen
        self.rect.midleft = self.screen_rect.midleft
        
        # store a decimal value for the ship's vertical position
        self.y = float(self.rect.y)
        
        # movement flags
        self.moving_up = False
        self.moving_down = False
        
    def blitme(self):
        """ Draw the ship at the current position """
        # pass both the image of the ship and the rect (hit-box)
        # to the current screen instance
        self.screen.blit(self.image, self.rect)
    
    def update(self):
        """ Update ship's position based on movement flags """
        
        # checks for collision between the top of the ship's rect and the 
        # top of the screen
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        
        # checks for collision between the bottom of the ship' rect and the 
        # bottom of the screen
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        
        # store the float value of y into the rect y value 
        self.rect.y = self.y