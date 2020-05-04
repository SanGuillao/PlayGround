import pygame
from pygame.sprite import Sprite

# Bullet extends from the Sprite class
class Bullet(Sprite):
    """ Init bullet vars, and funcs """
    
    def __init__(self, newGame):
        """ Init variables """
        
        # we're extending from the Sprite class, must init parent
        super().__init__()
        
        # get the current screen from the newGame instance
        self.screen = newGame.screen
        
        # get acess to the settings in the current instance
        self.settings = newGame.settings
        self.color = self.settings.bullet_color
        
        # no img for bullet, so we make a rect
        # to do so, we need to specify the (x,y) coord of top-left corner
        # width, and height
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
            self.settings.bullet_height)
        
        # we need to position the bullet at generation infront of the 
        # ship img
        self.rect.midright = newGame.ship.rect.midright
        
        # store the position of the bullet in decimal format
        self.x = float(self.rect.x)
        
    def update(self):
        """ Move the bullet accross the screen """
        # update the position of the bullet (x-value)
        self.x += self.settings.bullet_speed
        
        # update the rect (hit-box) of the bullet itself
        self.rect.x = self.x
        
    def draw_bullet(self):
        """ Draw bullet to the screen """
        # pass in the current screen instance, the bullet color, and the bullet
        # rect
        pygame.draw.rect(self.screen, self.color, self.rect)