import pygame
from pygame.sprite import Sprite
# import ty


class Enemy(Sprite):

    def __init__(self, ty_game, x: int, y: int, enter_speed: int = 0, is_boss: bool = False):
        super().__init__()
        self.health = ty_game.settings.enemy_health
        if is_boss:
            self.health = ty_game.settings.boss_health
        self.screen = ty_game.screen
        self.image = pygame.image.load('images/v (Custom).png')
        self.rect = self.image.get_rect()

        self.is_in_position = False

        if enter_speed == 0:
            self.is_in_position = True
            self.rect.y = y
        else:
            self.want_y = y

        self.rect.x = x

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.enter_speed = enter_speed

    def draw_enemy(self):
        if not self.is_in_position:
            self._enter()
        self._draw_enemy()

    def hurt(self) -> bool:
        self.health -= 1
        if self.health <= 0:
            return True
        else:
            return False

    # TODO Fall into player
    def run(self):
        pass

    def _draw_enemy(self):
        self.screen.blit(self.image, self.rect)

    def _enter(self):
        if self.rect.y == self.want_y:
            self.is_in_position = True
            return

        self.y += self.enter_speed
        if self.y >= self.want_y:
            self.y = self.want_y
            self.is_in_position = True

        self.rect.y = self.y
