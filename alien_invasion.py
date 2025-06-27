import sys
import pygame
from settings import Settings

class AlienInvasion:
    """Master class to manage game assets and behavoir."""
    
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        # set width and height,assigned to screen var to access in all funcs
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.bg_color = self.settings.bg_color


    def run_game(self):
        while True:
            # for keyboard and mouse events
            # pygame.event.get() returns a list of events 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # sys module to quit game
                    sys.exit()
            # Redraw screen during each pass through while loop.
            self.screen.fill(self.bg_color)
            #  tells Pygame to make the most recently drawn screen visible
            pygame.display.flip()

if __name__ == '__main__':
    # make an instance of game, and run it
    ai = AlienInvasion()
    ai.run_game()
