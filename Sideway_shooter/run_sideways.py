import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet

class SidewayShooter:
    """ Manages the overall game """
    
    def __init__(self):
        """ Init the game, and variables """
        pygame.init()
        
        # access the settings stored in the Settings file
        self.settings = Settings()
        
        # set the screen
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("G's Sideway Shooter")
        
        # init the ship
        # pass in the current game instance to make sure everything gets
        # initiliazed correctly
        self.ship = Ship(self)
        
        # init bullets
        # store them into a group
        self.bullets = pygame.sprite.Group()
    
    def run_game(self):
        """ Run the actual game """
        while True:
            # check for events
            self._get_events()
            # update the ship
            self.ship.update()
            # update bullets
            self._update_bullets()
            # update the screen
            self._update_screen()
            
    def _get_events(self):
        """ Respond to events """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self._keydown_events(event)
            if event.type == pygame.KEYUP:
                self._keyup_events(event)
                
    def _keydown_events(self, event):
        """ respond to keydown events """
        # pretty explanatory stuff here..
        if event.key == pygame.K_ESCAPE:
            sys.exit()
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        if event.key == pygame.K_SPACE:
            self._fire_bullets()
    
    def _keyup_events(self, event):
        """ respond to the relase of a key """
        # pretty explanatory stuff here..
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = False
            
    def _fire_bullets(self):
        """ Generate bullets fired due to keydown """
        # check to see tht the user hasnt already fired more bullets than 
        # allowed
        if len(self.bullets) < self.settings.bullets_allowed:
            # remember to pass in the current instance of the game into bullets
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            
    def _update_bullets(self):
        """ Updates the positions of the bullets and cleans up old bullets """
        
        # the Group datatype will automatically call the update function
        # of each bullet object
        self.bullets.update()

        # get the current screen rect
        screen_rect = self.screen.get_rect()
        
        # clean up bullets
        for bullet in self.bullets.copy():
            if bullet.rect.right >= screen_rect.right:
                # remove bullets tht reach the end of the screen
                self.bullets.remove(bullet)
                
    def _update_screen(self):
        """ Update the screen to the most recent screen """
        # set the bg_color        
        self.screen.fill(self.settings.bg_color)
        
        # update the ship
        self.ship.blitme()
        
        # draw the bullets
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        
        # Make the most recently drawn screen visible            
        pygame.display.flip()
    
if __name__ == '__main__':
    newGame = SidewayShooter()
    newGame.run_game()