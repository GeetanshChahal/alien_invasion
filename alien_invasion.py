import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Master class to manage game assets and behavoir."""
    
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        # set width and height,assigned to screen var to access in all funcs
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.bg_color = self.settings.bg_color
        # pass  an instance of AlienInvasion for ai_game
        self.ship = Ship(self)


    def run_game(self):
        while True:
            self.__check_events()
            # it calls the ship’s update() method on each pass through the loop
            self.ship.update()
            self.update_screen()

    def __check_events(self):
        # for keyboard and mouse events
        # pygame.event.get() returns a list of events 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # sys module to quit game
                sys.exit()
            # Each keypress is registered as a KEYDOWN event
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                     # Move ship to the right(x-axis) by 1pxl
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                     # Move ship to the right(x-axis)
                    self.ship.moving_left = True
            
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
                
    
    def update_screen(self):
        # Redraw screen during each pass through while loop.
            self.screen.fill(self.bg_color)
            # draw the ship on the screen
            self.ship.blitme()
            #  tells Pygame to make the most recently drawn screen visible
            pygame.display.flip()

        


if __name__ == '__main__':
    # make an instance of game, and run it
    ai = AlienInvasion()
    ai.run_game()
