import os
import sys
import shutil
import random
import pygame
import platform

import stg.scene.menu as menu
import stg.components.text as text
from stg.scene.game_over import GameOver
from stg.scene.menu import Menu
from stg.config import load_config
from stg.sprites.player import Player
from stg.sprites.enemy import Enemy
from stg.components.board import ScoreBoard
from stg import debug, __resource_path__, __version__


ICO_PATH = os.path.join(__resource_path__, "images/tysm.ico")
GAME_STATE_MENU = 0
GAME_STATE_GAMING = 1
GAME_STATE_GAME_OVER = 2


class TY:
    def __init__(self):
        pygame.init()
        config = load_config()
        debug(f"Game config: {config}")
        self.config = config

        pygame.display.set_icon(pygame.image.load(ICO_PATH))
        if self.config.general.is_full_screen:
            self.screen = pygame.display.set_mode((self.config.general.screen_width,
                                                   self.config.general.screen_height),
                                                  pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode((self.config.general.screen_width, self.config.general.screen_height))
        pygame.display.set_caption("天依嘿嘿嘿🤤 警告:图片仅为临时图片,并无版权,且判定点位置偏移 按ESC退出")

        text.Text(self,
                  'Loading...',
                  self.config.general.screen_width/2,
                  self.config.general.screen_height/2, background_color=None).draw_element()
        pygame.display.flip()

        self.player = None
        self.player_bullets = None
        self.enemy_bullets = None
        self.enemies = None
        self.pause_text = None
        self.clock = pygame.time.Clock()

        self.game_state = GAME_STATE_MENU
        self.menu = Menu(self)
        self.game_over = GameOver(self)

        self.game_is_init = False
        self.game_is_pause = False
        self.pause_sign = 0

        # 小笼包计分
        self.score = 0
        self.score_board = ScoreBoard(self, self.config.general.screen_width - 150, 50)

        self.create_enemy_count = 0
        self.create_sleep_sign = -1
        self.create_delay_sign = self.config.level_create_enemy_delay

    def run_game(self):
        while True:
            if self.config.general.fps != 0:
                self.clock.tick(self.config.general.fps)
            if self.game_state == GAME_STATE_MENU:
                # tools.debug('Menu')
                self.menu_update()
                self.menu.draw()
            if self.game_state == GAME_STATE_GAMING:
                # tools.debug('Gaming')
                if not self.game_is_init:
                    self._init_game()
                    self.game_is_init = True
                if not self.game_is_pause:
                    self._update_logic()
                    self._update_screen()
                else:
                    self._update_screen()
                    self.pause_update()
            if self.game_state == GAME_STATE_GAME_OVER:
                # tools.debug('Game Over!')
                self.game_over_update()
                self.game_over.draw(self.score)
            pygame.display.flip()

    def _init_game(self):
        self.score = 0
        self.player = Player(self)
        self.player_bullets = pygame.sprite.Group()
        self.enemy_bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.pause_text = text.Text(self,
                                    '暂停',
                                    640,
                                    384,
                                    60,
                                    None,
                                    '#FFFFFF')

    def pause_update(self):
        self.pause_text.draw_element()
        if self.pause_sign != 0:
            self.pause_sign -= 1
        elif self.pause_sign == 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
                    if event.key == pygame.K_p:
                        self.game_is_pause = False

    def game_over_update(self):
        self._check_events_over()

    def _check_events_over(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
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
        menu_sign = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                menu_sign += 1
                mouse_pos = pygame.mouse.get_pos()
                # tools.debug(menu_sign)
                if self.menu.play_button.rect.collidepoint(
                        mouse_pos) and self.menu.state == menu.MENU_STATE_NORMAL:
                    self.game_state = GAME_STATE_GAMING
                if self.menu.help_button.rect.collidepoint(
                        mouse_pos) and self.menu.state == menu.MENU_STATE_NORMAL:
                    # print(self.menu.state)
                    self.menu.state = menu.MENU_STATE_HELP
                    menu_sign = 2
                if self.menu.about_button.rect.collidepoint(
                        mouse_pos) and self.menu.state == menu.MENU_STATE_NORMAL:
                    # 开你妹的浏览器啊 烦死了 你还是把这个加到关于页的 GitHub 链接里去
                    # webbrowser.open('https://github.com/Catfootbeats/HenianSB_STG')
                    self.menu.state = menu.MENU_STATE_ABOUT
                    menu_sign = 2
                if self.menu.state != menu.MENU_STATE_NORMAL and menu_sign == 1:
                    self.menu.state = menu.MENU_STATE_NORMAL
                    self.menu_sign = 0

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
            self.player.moving_right = True
        if event.key == pygame.K_LEFT:
            self.player.moving_left = True
        if event.key == pygame.K_UP:
            self.player.moving_up = True
        if event.key == pygame.K_DOWN:
            self.player.moving_down = True
        if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
            self.player.shift = True

        if event.key == pygame.K_z:
            self.player.is_fire = True
        if event.key == pygame.K_p:
            self.game_is_pause = True
            self.pause_sign = 10

    def _check_keyup_events(self, event: pygame.event):
        if event.key == pygame.K_RIGHT:
            self.player.moving_right = False
        if event.key == pygame.K_LEFT:
            self.player.moving_left = False
        if event.key == pygame.K_UP:
            self.player.moving_up = False
        if event.key == pygame.K_DOWN:
            self.player.moving_down = False
        if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
            self.player.shift = False

        if event.key == pygame.K_z:
            self.player.is_fire = False

    def _update_logic(self):
        self._check_events()
        self._create_enemies()
        self.player.update()
        self.enemies.update()
        self.enemy_bullets.update()
        self._update_enemy()
        self.player_bullets.update()
        # debug.debug(len(self.enemies.sprites()))

    def _update_screen(self):
        self.screen.fill(self.config.general.bg_color)
        self.player.blitme()
        self._update_bullets()
        self._draw_enemy()
        self.score_board.draw(self.score)

    def _create_enemies(self):
        self.create_delay_sign += 1
        # Sleep create
        # -1 不休息
        # 大于 0 小于 level_create_sleep 休息
        if self.create_sleep_sign >= self.config.level_create_sleep:
            self.create_enemy_count = 0
            self.create_sleep_sign = -1
        elif self.create_sleep_sign >= 0:
            self.create_sleep_sign += 1

        if self.create_enemy_count > self.config.level_create_max:
            self.create_enemy_count = 0
            self.create_sleep_sign = 0

        # 不休息 and 未超过创建极限 and 未超过同屏极限 and 创建延迟
        if (self.create_sleep_sign == -1
                and self.create_enemy_count <= self.config.level_create_max
                and len(self.enemies.sprites()) < self.config.level_screen_enemy_max
                and self.create_delay_sign >= self.config.level_create_enemy_delay):
            self.create_enemy_count += 1
            self.create_delay_sign = 0
            boss = Enemy(self,
                         random.randint(int(100),
                                        int(self.config.general.screen_width - 100)),
                         random.randint(int(100),
                                        int(self.config.general.screen_height / 2)),
                         1,
                         True)
            self.enemies.add(boss)
            if self.create_enemy_count % 4 == 0:
                enemy_0 = Enemy(self,
                                random.randint(int(25),
                                               int(self.config.general.screen_width - 25)),
                                random.randint(int(25),
                                               int(self.config.general.screen_height / 2)))
                self.enemies.add(enemy_0)
                enemy_1 = Enemy(self,
                                random.randint(int(25),
                                               int(self.config.general.screen_width - 25)),
                                random.randint(int(25),
                                               int(self.config.general.screen_height / 2)))
                self.enemies.add(enemy_1)
        """ 另一种玩法
        enemy_times = 2
        if len(self.enemies.sprites()) == 0 and self.create_enemy_count < enemy_times:
            self.create_enemy_count += 1
            while len(self.enemies.sprites()) < self.config.enemy_count:
                enemy = Enemy(self,
                              random.randint(int(25),
                                             int(self.config.general.screen_width - 25)),
                              random.randint(int(25),
                                             int(self.config.general.screen_height / 2)))
                self.enemies.add(enemy)
        if self.create_enemy_count == enemy_times:
            boss = Enemy(self,
                         random.randint(int(100),
                                        int(self.config.general.screen_width - 100)),
                         random.randint(int(100),
                                        int(self.config.general.screen_height / 2)),
                         1,
                         True)
            self.enemies.add(boss)
        """

    def _update_enemy(self):
        for enemy in self.enemies.sprites():
            enemy.enemy_update(self.player.rect.centerx, self.player.rect.centery)
        if pygame.sprite.spritecollide(self.player,
                                       self.enemies,
                                       False,
                                       pygame.sprite.collide_circle) or pygame.sprite.spritecollide(self.player,
                                                                                                    self.enemy_bullets,
                                                                                                    False,
                                                                                                    pygame.sprite.collide_circle):
            debug('GAME OVER!!!')
            self.game_state = GAME_STATE_GAME_OVER
            self.create_enemy_count = 0
            self.game_is_init = False

    def _draw_enemy(self):
        for enemy in self.enemies.sprites():
            enemy.draw_enemy()

    def _update_bullets(self):
        self._check_bullet_enemy_collisions()
        self._draw_bullets()
        self._clear_bullets()

    def _check_bullet_enemy_collisions(self):
        collisions = pygame.sprite.groupcollide(self.player_bullets,
                                                self.enemies,
                                                True,
                                                False)
        # debug.debug('Collisions')
        # debug.debug(collisions.values())
        for item in collisions.values():
            for enemy in item:
                # debug.debug(enemy.health)
                if enemy.hurt():
                    self.score += enemy.score
                    debug(self.score)
                    self.enemies.remove(enemy)

    def _draw_bullets(self):
        for bullet in self.player_bullets.sprites():
            bullet.draw_player_bullet()
        for bullet in self.enemy_bullets.sprites():
            bullet.draw_player_bullet()

    def _clear_bullets(self):
        for bullet in self.player_bullets.copy():
            if bullet.rect.bottom <= 0:
                self.player_bullets.remove(bullet)
        for bullet in self.enemy_bullets.copy():
            if bullet.rect.bottom <= 0:
                self.enemy_bullets.remove(bullet)


if __name__ == '__main__':
    debug(f"beating-agent-v-stg version {__version__} (python package: {__package__})")
    debug(f"Python {platform.python_version()} {platform.python_build()}")
    debug(f"Platform: {platform.system()}/{platform.release()}")
    debug(f"Command line: {sys.argv}")
    th = TY()
    th.run_game()
