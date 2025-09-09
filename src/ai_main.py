import sys
from src.settings import Settings
import pygame
from ship import Ship
from bullets import Bullets

class AlienInvasion:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Alien Invasion')

        self.clock = pygame.time.Clock()
        self.bg_color = (0, 0, 0)

        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screenwidth, self.settings.screenheight),
            pygame.RESIZABLE
        )

        self.ship = Ship(self)
        self.fullscreen = False
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.VIDEORESIZE and not self.fullscreen:
                self.settings.screenwidth, self.settings.screenheight = event.size
                self.screen = pygame.display.set_mode(event.size, pygame.RESIZABLE)
                self.ship.rect.midbottom = self.screen.get_rect().midbottom
                self.ship.x = float(self.ship.rect.x)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_f:
            if not self.fullscreen:
                self.windowed_size = self.screen.get_size()
                self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                self.fullscreen = True
            else:
                self.screen = pygame.display.set_mode(self.windowed_size, pygame.RESIZABLE)
                self.settings.screenwidth, self.settings.screenheight = self.windowed_size
                self.fullscreen = False
        elif event.key == pygame.K_ESCAPE:
            if self.fullscreen:
                self.screen = pygame.display.set_mode(self.windowed_size, pygame.RESIZABLE)
                self.settings.screenwidth, self.settings.screenheight = self.windowed_size
                self.fullscreen = False
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.ship.moving_left = False

    def _fire_bullet(self):
        new_bullet = Bullets(self)
        self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
            print(len(self.bullets))

    def _update_screen(self):
        self.screen.fill(self.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
