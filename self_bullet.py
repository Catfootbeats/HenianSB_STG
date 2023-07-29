import os
import pygame
from pygame.sprite import Sprite
# from random import choice

BULLET_IMAGE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images/bullet.png')


class SelfBullet(Sprite):
    def __init__(self, ty_game) -> None:
        super().__init__()
        self.screen = ty_game.screen
        self.settings = ty_game.settings
        self.width = self.settings.self_bullet_width
        self.height = self.settings.self_bullet_height
        # list = ['🎵', '🎶']
        # self.note = choice(list)
        # self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.midtop = ty_game.ship.rect.midtop

        self.y = self.rect.y

    def update(self) -> None:
        self.y -= self.settings.self_bullet_speed
        self.rect.y = self.y

    def draw_self_bullet(self) -> None:
        # TODO note image bullet
        pygame.draw.rect(self.screen, (255, 255, 255), self.rect)
        # self.bullet_image = self.font.render(self.note,True,(0,0,0), None)
        # self.bullet_image_rect = self.bullet_image.get_rect()
        # self.bullet_image_rect.center = self.rect.center
