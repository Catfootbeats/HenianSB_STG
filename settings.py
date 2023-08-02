class Settings:
    def __init__(self):

        # General Settings
        self.screen_width = 1280
        self.screen_height = 768
        self.bg_color = '#66ccff'
        self.is_full_screen = False
        self.FPS = 90
        # If FPS = 0, no limitation

        # Ship Settings
        self.ship_speed = 9
        self.ship_low_speed = 3
        self.ship_hitbox_r = 5

        # Bullet Settings
        self.self_bullet_delay = 2
        self.self_bullet_speed = 15
        self.self_bullet_width = 10
        self.self_bullet_height = 10

        self.enemy_bullet_speed = 10
        self.enemy_bullet_delay = 1
        self.enemy_xlb = 1000
        # 为什么干掉小兵获得的小笼包比BOSS还多？

        self.create_enemy_delay = 100
        self.create_sleep = 500
        self.create_max = 10
        self.screen_enemy_max = 10

        self.boss_bullet_delay = 100
        self.boss_xlb = 100

        # Enemy Settings
        self.enemy_health = 1
        self.boss_health = 1
        self.enemy_count = 2
