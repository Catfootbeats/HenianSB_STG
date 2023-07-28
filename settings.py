class Settings:
    def __init__(self):

        # General Settings
        self.screen_width = 1280
        self.screen_height = 768
        self.bg_color = '#66ccff'
        self.is_full_screen = False
        self.FPS = 60
        # If FPS = 0, no limitation

        # Ship Settings
        self.ship_speed = 9
        self.ship_low_speed = 3
        self.ship_hitbox_r = 10

        # Bullet Settings
        self.self_bullet_delay = 2
        self.self_bullet_speed = 15
        self.self_bullet_width = 10
        self.self_bullet_height = 10

        # Enemy Settings
        self.enemy_health = 1
        self.boss_health = 10
        self.boss_count = 1
