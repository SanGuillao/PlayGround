import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

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
        
        # init the aliens
        self.aliens = pygame.sprite.Group()
        
        # create the alien fleet
        self._create_fleet()
    
    def run_game(self):
        """ Run the actual game """
        while True:
            # check for events
            self._get_events()
            # update the ship
            self.ship.update()
            # update bullets
            self._update_bullets()
            # update the alien fleet
            self._update_aliens()
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
            
    def _check_fleet_edges(self):
        """ Check to see if any alien has reached the edge """
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        """ Change the fleet direction and drop the aliens """
        for alien in self.aliens.sprites():
            # we do -= because we're going from right most to left most
            alien.rect.x -= self.settings.fleet_drop_speed
        
        # Change the direction of the fleet
        self.settings.fleet_direction *= -1
        
    def _check_bullet_alien_collisions(self):
        """ Respond to any bullet-alien collisions """
        # Check for collision between aliens and bullets
        # whenever objects in bullets and aliens collide, the True True tells pygame
        # to delete both objects
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        # print(len(self.aliens))
        
        # Create a new fleet of aliens if no more aliens exist
        if not self.aliens:
            # Destroy any remaining bullets
            self.bullets.empty()
            self._create_fleet()
    
    def _fire_bullets(self):
        """ Generate bullets fired due to keydown """
        # check to see tht the user hasnt already fired more bullets than 
        # allowed
        if len(self.bullets) < self.settings.bullets_allowed:
            # remember to pass in the current instance of the game into bullets
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
        
    def _create_alien(self, alien_number, row_number):
        """ Create an alien and place it in the row """
        # Create the alien object
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        
        # calculate the y position
        alien.y = alien_width + 2 * alien_width * alien_number
        
        # calculate the x position, have the original aliens start at the right most point
        alien.x = self.settings.screen_width - 2 * alien_height * row_number - alien_height
        # set the rect x value = to alien.x
        alien.rect.x = alien.x
        alien.rect.y = alien.y
        # print(f"Alien.x: {alien.x} : Alien.y: {alien.y}")
        # add the alien
        self.aliens.add(alien)
        
    def _create_fleet(self):
        """ Create alien fleet, add them into aliens group """
        # Create an alien
        # Spacing between each alien is equal to alien width
        alien = Alien(self)
        
        # get the width & height of the rect, conveniance really
        # makes a local variable
        # rect.size returns a tuple of width and height
        alien_width, alien_height = alien.rect.size
        
        # get the total amnt of space tht is available for us to use
        # by calculating the screen_height - the two margings on the top/bottom * the alien 
        # width. makes the margins the size of the alien width
        available_space_y = self.settings.screen_height - (2 * alien_height)
        
        # get the number of aliens tht can fit on the current screen
        # the // is floor division, gets the value drops the remainder 
        number_aliens_y = available_space_y // (2 * alien_height)
        
        # determine the number of rows of aliens tht can fit on the screen
        ship_width = self.ship.rect.width
        available_space_x = (self.settings.screen_width - (3 * alien_width) - ship_width)
        number_rows = available_space_x // (2 * alien_width)
        
        # create the number of aliens that can fit onto the screen
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_y):
                # Create an alien and place it in the row
                self._create_alien(alien_number, row_number)
                
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
        
        # check for collision between bullets and aliens
        self._check_bullet_alien_collisions()
                
    def _update_aliens(self):
        """ Update the positions of the alien fleet """
        self._check_fleet_edges()
        self.aliens.update()
        
    def _update_screen(self):
        """ Update the screen to the most recent screen """
        # set the bg_color        
        self.screen.fill(self.settings.bg_color)
        
        # update the ship
        self.ship.blitme()
        
        # draw the bullets
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        
        # draw all the aliens in the aliens group
        # the group draw() needs the current screen to output the aliens to
        # will draw each element in the group        
        self.aliens.draw(self.screen)
        
        # Make the most recently drawn screen visible            
        pygame.display.flip()
    
if __name__ == '__main__':
    newGame = SidewayShooter()
    newGame.run_game()