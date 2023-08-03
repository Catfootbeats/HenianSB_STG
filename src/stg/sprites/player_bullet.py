import os
import pygame
import random
from pygame.sprite import Sprite
from stg import __resource_path__

BULLET_IMAGE_PATH = os.path.join(__resource_path__, 'images/bullet.png')
FONT_PATH = os.path.join(__resource_path__, 'fonts/NotoEmoji-Bold.ttf')


class PlayerBullet(Sprite):
    def __init__(self, ty_game) -> None:
        super().__init__()
        self.screen = ty_game.screen
        self.config = ty_game.config
        self.width = self.config.player_bullet_width
        self.height = self.config.player_bullet_height
        note_list = ['🎵', '🎶']
        self.note = random.choice(note_list)
        self.font = pygame.font.Font(FONT_PATH, 24)
        self.bullet_image = self.font.render(self.note, True, (0, 0, 0), None)
        self.rect = self.bullet_image.get_rect()

        self.rect.midtop = ty_game.player.rect.midtop

        self.y = self.rect.y

    def update(self) -> None:
        self.y -= self.config.player_bullet_speed
        self.rect.y = self.y

    def draw_player_bullet(self) -> None:
        # TODO note image bullet
        self.screen.blit(self.bullet_image, self.rect)
