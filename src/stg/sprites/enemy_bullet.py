import math
import os
import pygame
from pygame.sprite import Sprite

from stg.config import Config
from stg import __resource_path__

BULLET_IMAGE_PATH = os.path.join(__resource_path__, 'images/bullet.png')


class EnemyBullet(Sprite):
    def __init__(self, screen: pygame.surface, config: Config, direction: float, enemy) -> None:
        super().__init__()
        self.screen = screen
        self.config = config
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
        self.x += math.cos(math.radians(direction)) * self.config.enemy_bullet_speed
        self.y += math.sin(math.radians(direction)) * self.config.enemy_bullet_speed
        self.rect.x = self.x
        self.rect.y = self.y

    def draw_player_bullet(self) -> None:
        self.screen.blit(self.image, self.rect)
