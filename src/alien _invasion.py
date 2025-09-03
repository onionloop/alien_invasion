import sys
from src.settings import Settings
import pygame

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption('Alien Invasion')
        self.clock = pygame.time.Clock()
        self.bg_color = (230, 230, 230)
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screenwidth, self.settings.screenheight))
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.flip()
            self.clock.tick(60)
            self.screen.fill(self.settings.bg_color)
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()