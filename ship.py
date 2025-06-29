import pygame

class Ship:
    # ai_game give access to game resources
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings =ai_game.settings

        # rect is for rectangle, taken it as rects are easy to handle
        self.screen_rect = ai_game.screen.get_rect()

        #  returns a surface representing the ship
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        # movement flag
        self.moving_right =False
        self.moving_left =False

        # ship speed is in decimal
        self.x = float(self.rect.x)
    
    def update(self):
        if  self.moving_right:
            self.x += self.settings.ship_speed

        if  self.moving_left:
            self.x -= self.settings.ship_speed
        
        # Update rect object from self.x
        self.rect.x =self.x

# draws the image to the screen at the position specified by self.rect
    def blitme(self):
        self.screen.blit(self.image, self.rect)