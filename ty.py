import os.path
import sys
import pygame

import menu_scene
import tools
from game_over_scene import GameOver
from menu_scene import Menu
from settings import Settings
from ship import Ship
from enemy import Enemy
# from self_bullet import SelfBullet

ICO_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images/tysm.ico')
GAME_STATE_MENU = 0
GAME_STATE_GAMING = 1
GAME_STATE_GAME_OVER = 2


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

        self.ship = None
        self.self_bullets = None
        self.enemy_bullets = None
        self.enemies = None
        self.clock = pygame.time.Clock()

        self.game_state = GAME_STATE_MENU
        self.menu = Menu(self)
        self.game_over = GameOver(self)
        self.menu_sign = False

        self.game_is_init = False
        self.menu_is_init = False

    def run_game(self):
        while True:
            if self.settings.FPS != 0:
                self.clock.tick(self.settings.FPS)
            if self.game_state == GAME_STATE_MENU:
                # tools.debug('Menu')
                self.menu_update()
                self.menu.draw()
            if self.game_state == GAME_STATE_GAMING:
                tools.debug('Gaming')
                if not self.game_is_init:
                    self._init_game()
                    self.game_is_init = True
                self._update_logic()
                self._update_screen()
            if self.game_state == GAME_STATE_GAME_OVER:
                tools.debug('Game Over!')
                self.game_over_update()
                self.game_over.draw()
            pygame.display.flip()

    def _init_game(self):
        self.ship = Ship(self)
        self.self_bullets = pygame.sprite.Group()
        self.enemy_bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self._create_enemies()

    def game_over_update(self):
        self._check_events_over()

    def _check_events_over(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.game_over.replay_button.rect.collidepoint(mouse_pos):
                    self.game_state = GAME_STATE_GAMING
                if self.game_over.back_menu_button.rect.collidepoint(mouse_pos):
                    self.game_state = GAME_STATE_MENU


    def menu_update(self):
        self._check_events_menu()

    def _check_events_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                tools.debug(self.menu_sign)
                if self.menu.state != menu_scene.MENU_STATE_NORMAL and self.menu_sign:
                    self.menu.state = menu_scene.MENU_STATE_NORMAL
                    self.menu_sign = False
                if self.menu.play_button.rect.collidepoint(mouse_pos) and self.menu.state == menu_scene.MENU_STATE_NORMAL:
                    self.game_state = GAME_STATE_GAMING
                if self.menu.help_button.rect.collidepoint(mouse_pos) and self.menu.state == menu_scene.MENU_STATE_NORMAL:
                    self.menu.state = menu_scene.MENU_STATE_HELP
                    self.menu_sign = True
                if self.menu.about_button.rect.collidepoint(mouse_pos) and self.menu.state == menu_scene.MENU_STATE_NORMAL:
                    self.menu.state = menu_scene.MENU_STATE_ABOUT
                    self.menu_sign = True

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
        # debug.debug(len(self.enemies.sprites()))

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        self._update_bullets()
        self._draw_enemy()

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
        if pygame.sprite.spritecollide(self.ship,
                                       self.enemies,
                                       False,
                                       pygame.sprite.collide_circle) or pygame.sprite.spritecollide(self.ship,
                                                                                                    self.enemy_bullets,
                                                                                                    False,
                                                                                                    pygame.sprite.collide_circle):
            tools.debug('GAME OVER!!!')
            self.game_state = GAME_STATE_GAME_OVER
            self.game_is_init = False

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
        # debug.debug('Collisions')
        # debug.debug(collisions.values())
        for item in collisions.values():
            for enemy in item:
                # debug.debug(enemy.health)
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
            # debug.debug(len(self.self_bullets))
        for bullet in self.enemy_bullets.copy():
            if bullet.rect.bottom <= 0:
                self.enemy_bullets.remove(bullet)


if __name__ == '__main__':
    th = TY()
    th.run_game()
