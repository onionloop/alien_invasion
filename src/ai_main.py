import sys
from src.settings import Settings
import pygame
from ship import Ship

class AlienInvasion:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption('Alien Invasion')
        self.clock = pygame.time.Clock()
        self.bg_color = (230, 230, 230)
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screenwidth, self.settings.screenheight),
            pygame.RESIZABLE
        )

        self.ship = Ship(self)

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screenwidth = self.screen.get_rect().width
        self.settings.screenheight = self.screen.get_rect().height
        self.fullscreen = False



    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)
            self.ship.update()


    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.VIDEORESIZE:
                self.settings.screenwidth, self.settings.screenheight = event.size

                self.screen = pygame.display.set_mode(
                    event.size, pygame.RESIZABLE
                )

                self.ship.rect.midbottom = self.screen.get_rect().midbottom
                self.ship.x = float(self.ship.rect.x)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_F11:
           if not self.fullscreen:
                self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                self.fullscreen = True
           else:
                self.screen = pygame.display.set_mode((self.settings.screenwidth, self.settings.screenheight),
                    pygame.RESIZABLE)
                self.fullscreen = False

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False


    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        pygame.display.flip()



if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()