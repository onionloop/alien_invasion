import pygame

class Ship:
    def __init__(self , ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load('../images/ship.bmp')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        self.moving_right = False

    def update(self):
        if self.moving_right:
            self.rect.x += 30
    def blitme(self):
        """.blit(source, destination)”"""
        self.screen.blit(self.image, self.rect)
