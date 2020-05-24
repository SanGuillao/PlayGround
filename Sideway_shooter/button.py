import pygame.font

class Button:
    """ allows for the creation of buttons for the game """
    
    def __init__(self, newGame, mssg):
        """ """
        self.screen = newGame.screen
        self.screen_rect = self.screen.get_rect()
        
        # set the dimensions of the button
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        
        # build the button's rect obj, and center the pos
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        
        # load the mssg into the button
        self._prep_mssg(mssg)
        
    def _prep_mssg(self, mssg):
        """ turn mssg into a rendered img and center the text on the button """
        # font render takes in the mssg, T/F for anti-aliasing, font-color, background-color
        self.mssg_image = self.font.render(mssg, True, self.text_color, self.button_color)
        self.mssg_image_rect = self.mssg_image.get_rect()
        # center the text by using the center of the button
        self.mssg_image_rect.center = self.rect.center
        
    def draw_button(self):
        """ Draw the button to the screen """
        # call fill to draw the rect portion of the button
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.mssg_image, self.mssg_image_rect)