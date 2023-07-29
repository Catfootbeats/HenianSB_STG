import os.path
import sys
import pygame

from settings import Settings
from ship import Ship
from enemy import Enemy
# from self_bullet import SelfBullet

ICO_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images/tysm.ico')


class TY:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.boss_count = self.settings.boss_count

        pygame.display.set_icon(pygame.image.load(ICO_PATH))
        if self.settings.is_full_screen:
            self.screen = pygame.display.set_mode((self.settings.screen_width,
                                                   self.settings.screen_height),
                                                  pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("天依嘿嘿嘿🤤 警告:图片仅为临时图片,并无版权,且判定点位置偏移 按ESC退出")

        self.ship = Ship(self)
        self.self_bullets = pygame.sprite.Group()
        self.enemy_bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.clock = pygame.time.Clock()

        self._create_enemies()

    def run_game(self):
        while True:
            if self.settings.FPS != 0:
                self.clock.tick(self.settings.FPS)
            else:
                pass
            # TODO present FPS
            self._update_logic()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event: pygame.event):
        if event.key == pygame.K_ESCAPE:
            sys.exit()

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
            self.ship.shift = True

        if event.key == pygame.K_z:
            self.ship.is_fire = True

    def _check_keyup_events(self, event: pygame.event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = False
        if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
            self.ship.shift = False

        if event.key == pygame.K_z:
            self.ship.is_fire = False

    def _update_logic(self):
        self._check_events()
        self.ship.update()
        self.enemies.update()
        self.enemy_bullets.update()
        self._update_enemy()
        self.self_bullets.update()
        if len(self.enemies.sprites()) == 0 and self.boss_count > 0:
            self._create_boss()
            self.boss_count -= 1
        # print(len(self.enemies.sprites()))

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        self._update_bullets()
        self._draw_enemy()
        pygame.display.flip()

    def _create_enemies(self):
        enemy_0 = Enemy(self,
                        self.settings.screen_width / 7,
                        self.settings.screen_height / 5,
                        1)
        self.enemies.add(enemy_0)

        enemy_1 = Enemy(self,
                        self.settings.screen_width - self.settings.screen_width / 5,
                        self.settings.screen_height / 5,
                        1)
        self.enemies.add(enemy_1)

    def _create_boss(self):
        enemy_2 = Enemy(self,
                        self.settings.screen_width/2,
                        self.settings.screen_height / 5,
                        1,
                        True)
        self.enemies.add(enemy_2)

    def _update_enemy(self):
        for enemy in self.enemies.sprites():
            enemy.enemy_update(self.ship.rect.centerx, self.ship.rect.centery)

    def _draw_enemy(self):
        for enemy in self.enemies.sprites():
            enemy.draw_enemy()

    def _update_bullets(self):
        self._check_bullet_enemy_collisions()
        self._draw_bullets()
        self._clear_bullets()

    def _check_bullet_enemy_collisions(self):
        collisions = pygame.sprite.groupcollide(self.self_bullets,
                                                self.enemies,
                                                True,
                                                False)
        # print('Collisions')
        # print(collisions.values())
        for item in collisions.values():
            for enemy in item:
                # print(enemy.health)
                if enemy.hurt():
                    self.enemies.remove(enemy)

    def _draw_bullets(self):
        for bullet in self.self_bullets.sprites():
            bullet.draw_self_bullet()
        for bullet in self.enemy_bullets.sprites():
            bullet.draw_self_bullet()

    def _clear_bullets(self):
        for bullet in self.self_bullets.copy():
            if bullet.rect.bottom <= 0:
                self.self_bullets.remove(bullet)
            # print(len(self.self_bullets))
        for bullet in self.enemy_bullets.copy():
            if bullet.rect.bottom <= 0:
                self.enemy_bullets.remove(bullet)


if __name__ == '__main__':
    th = TY()
    th.run_game()
