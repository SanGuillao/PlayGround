import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """ Holds alien variables and functions """
    
    def __init__(self, newGame):
        """ Init all variables """
        super().__init__()
        self.screen = newGame.screen
        self.settings = newGame.settings
        
        # load the image
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        
        # start positions
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # store the position as a decimal
        self.x = float(self.rect.x)
        
    def check_edges(self):
        """ Returns true if an alien is at an edge """
        screen_rect = self.screen.get_rect()
        
        # we compare the bottom of the alien rect to the screen bottom, to see if an alien
        # has reach the bottom of the screen
        if self.rect.bottom >= screen_rect.bottom or self.rect.top <= 0:
            return True
            
    def update(self):
        """ Move alien """
        self.y += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.y = self.y