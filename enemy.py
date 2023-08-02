import math
import os
import pygame
from pygame.sprite import Sprite

import tools
from enemy_bullet import EnemyBullet

# import ty

ENEMY_IMAGE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images/v.png')


class Enemy(Sprite):

    def __init__(self, ty_game, x: int, y: int, enter_speed: int = 3, is_boss: bool = False):
        super().__init__()
        self.health = ty_game.settings.enemy_health
        self.fire_delay = ty_game.settings.enemy_bullet_delay
        self.xiao_long_bao = ty_game.settings.enemy_xlb
        if is_boss:
            self.xiao_long_bao = ty_game.settings.boss_xlb
            self.health = ty_game.settings.boss_health
            self.fire_delay = ty_game.settings.boss_bullet_delay
        self.screen = ty_game.screen
        self.settings = ty_game.settings
        self.game = ty_game
        self.image = pygame.image.load(ENEMY_IMAGE_PATH)
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
        # Fire
        self.fire_delay_sign = 0

        self.is_boss = is_boss

        self.fire_angle = 0

    def draw_enemy(self):
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

    def enemy_update(self, player_x: int, player_y: int):
        if not self.is_in_position:
            self._enter()
        if self.is_boss:
            angle = 0
            while angle < 360:
                self._fire_angle(angle + self.fire_angle)
                angle += 25
            self.fire_angle += 10
            if self.fire_angle == 360:
                self.fire_angle = 0
        else:
            self._fire(player_x, player_y)

    # Trace bullets
    def _fire(self, player_x: int, player_y: int):
        # print(player_x, player_y)
        if self.fire_delay_sign == 0:
            bullet_move_direction = tools.get_player_direction(self, player_x, player_y)
            # print('Position:', '(', self.x, ',', self.y, ')', ':', bullet_move_direction)
            bullet = EnemyBullet(self.screen, self.settings, bullet_move_direction, self)
            self.game.enemy_bullets.add(bullet)
            self.fire_delay_sign += 1
        elif self.fire_delay_sign == self.fire_delay:
            self.fire_delay_sign = 0
        else:
            self.fire_delay_sign += 1

    def _fire_angle(self, direction: float):
        if self.fire_delay_sign == 0:
            bullet = EnemyBullet(self.screen, self.settings, direction, self)
            self.game.enemy_bullets.add(bullet)
            self.fire_delay_sign += 1
        elif self.fire_delay_sign == self.fire_delay:
            self.fire_delay_sign = 0
        else:
            self.fire_delay_sign += 1

    def _get_player_direction(self, player_x: int, player_y: int) -> float:
        # Get player's position and transform into direction.
        x: float = player_x - self.rect.centerx
        y: float = player_y - self.rect.centery
        if x >= 0:
            # print('x >= 0')
            if y >= 0:
                # print('y >= 0')
                return 90 - math.degrees(math.asin(x / math.sqrt(x * x + y * y)))
            if y < 0:
                # print('y < 0')
                return math.degrees(math.asin(x / math.sqrt(x * x + y * y))) - 90
        elif x < 0:
            # print('x < 0')
            if y >= 0:
                # print('y >= 0')
                return 90 - math.degrees(math.asin(x / math.sqrt(x * x + y * y)))
            elif y < 0:
                # print('y < 0')
                return math.degrees(math.asin(x / math.sqrt(x * x + y * y))) - 90

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
