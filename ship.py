import os.path
import pygame
from collide_body import CircleCollideBody
from self_bullet import SelfBullet

SHIP_IMAGE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images/tianyi.png')
SHIP_WITH_POINT_IMAGE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images/tianyi_with_point.png')


class Ship(pygame.sprite.Sprite):

    def __init__(self, ty_game):
        super().__init__()
        self.game = ty_game
        self.screen = ty_game.screen
        self.settings = ty_game.settings
        self.radius = self.settings.ship_hitbox_r
        self.screen_rect = ty_game.screen.get_rect()

        # Get surface
        # TODO exchange image
        self.image = pygame.image.load(SHIP_IMAGE_PATH)
        self.rect = self.image.get_rect()

        # Set init position
        self.rect.midbottom = self.screen_rect.midbottom

        # Collide body
        self.collide_body = CircleCollideBody(self.radius)

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        # Moving sign
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.shift = False
        self.act_speed = self.settings.ship_speed

        # Fire sign
        self.is_fire = False
        self.fire_delay = self.settings.self_bullet_delay
        self.fire_delay_sign = 0

    def update(self):
        if self.shift:
            self.act_speed = self.settings.ship_low_speed
            # TODO exchange image
            self.image = pygame.image.load(SHIP_WITH_POINT_IMAGE_PATH)
        else:
            self.act_speed = self.settings.ship_speed
            # TODO exchange image
            self.image = pygame.image.load(SHIP_IMAGE_PATH)

        self._fire()
        self._move()

        self.rect.x = self.x
        self.rect.y = self.y
        # Collide body update
        # self.collide_body.update(self.rect, self.screen_rect)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def _fire(self):
        if self.fire_delay_sign == 0:
            if self.is_fire:
                new_bullet = SelfBullet(self.game)
                self.game.self_bullets.add(new_bullet)
            self.fire_delay_sign += 1
        elif self.fire_delay_sign == self.fire_delay:
            self.fire_delay_sign = 0
        else:
            self.fire_delay_sign += 1

    def _move(self):
        if self.moving_right and not self.collide_body.right(self.rect, self.screen_rect):
            self.x += self.act_speed
        if self.moving_left and not self.collide_body.left(self.rect, self.screen_rect):
            self.x -= self.act_speed
        if self.moving_up and not self.collide_body.top(self.rect, self.screen_rect):
            self.y -= self.act_speed
        if self.moving_down and not self.collide_body.bottom(self.rect, self.screen_rect):
            self.y += self.act_speed
