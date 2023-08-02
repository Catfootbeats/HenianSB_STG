class Settings:
    def __init__(self):

        # General Settings 基础设定
        # 屏幕宽高
        self.screen_width = 1280
        self.screen_height = 768
        # 背景颜色
        self.bg_color = '#66ccff'
        # 是否全屏
        self.is_full_screen = False
        # 帧率(改变会影响一切速度)
        self.FPS = 60
        # If FPS = 0, no limitation

        # Ship Settings 自机设定
        # 速度
        self.ship_speed = 9
        # Shift速度
        self.ship_low_speed = 3
        # 判定点半径
        self.ship_hitbox_r = 5

        # Bullet Settings 子弹设定
        # 自机子弹发射延迟
        self.self_bullet_delay = 2
        # 自机子弹速度
        self.self_bullet_speed = 15
        # 自机子弹宽高
        self.self_bullet_width = 10
        self.self_bullet_height = 10
        # 敌机子弹速度
        self.enemy_bullet_speed = 10
        # 敌机子弹发射延迟
        self.enemy_bullet_delay = 1
        # 打败敌机获得分数(小笼包)
        self.enemy_xlb = 1000
        # 为什么干掉小兵获得的小笼包比BOSS还多？

        # 创建敌机延迟(间隔)
        self.create_enemy_delay = 100
        # 每轮休息时间长度
        self.create_sleep = 500
        # 每轮最大敌机数
        self.create_max = 10
        # 单屏最大敌机数
        self.screen_enemy_max = 10

        # Boss(旋转发弹幕的敌机)子弹延迟
        self.boss_bullet_delay = 100
        # 打败Boss得分(小笼包)
        self.boss_xlb = 100

        # Enemy Settings 敌机设定
        # 敌机血量
        self.enemy_health = 1
        # Boss血量
        self.boss_health = 1
        # 计数，勿动
        self.enemy_count = 2
