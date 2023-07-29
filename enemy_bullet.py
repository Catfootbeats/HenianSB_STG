import math
import os
import pygame
from pygame.sprite import Sprite

from settings import Settings

# from random import choice

BULLET_IMAGE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images/bullet.png')


class EnemyBullet(Sprite):
    def __init__(self, screen: pygame.surface, settings: Settings, direction: float, enemy) -> None:
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.image = pygame.image.load(BULLET_IMAGE_PATH)

        self.rect = self.image.get_rect()
        self.rect.midtop = enemy.rect.center

        self.direction = direction
        self.x = self.rect.x
        self.y = self.rect.y

    def update(self):
        self._move(self.direction)

    def trace_update(self, direction: float):
        self._move(direction)

    def _move(self, direction: float) -> None:
        self.x += math.cos(math.radians(direction)) * self.settings.enemy_bullet_speed
        self.y += math.sin(math.radians(direction)) * self.settings.enemy_bullet_speed
        self.rect.x = self.x
        self.rect.y = self.y

    def draw_self_bullet(self) -> None:
        self.screen.blit(self.image, self.rect)
