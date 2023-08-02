from stg.components.text import Text
from stg import __version__

MENU_STATE_NORMAL = 0
MENU_STATE_HELP = 1
MENU_STATE_ABOUT = 2


class Menu:
    def __init__(self, ty_game):
        self.normal_elements = []
        self.help_elements = []
        self.about_elements = []

        self.state = MENU_STATE_NORMAL
        self.screen = ty_game.screen

        self.title_text = Text(ty_game,
                               '暴打老V',
                               320,
                               242,
                               60,
                               None,
                               '#66CCFF')

        self.play_button = Text(ty_game, '开始', 320, 342)
        self.normal_elements.append(self.play_button)
        self.help_button = Text(ty_game, '帮助', 320, 442)
        self.normal_elements.append(self.help_button)
        self.about_button = Text(ty_game, '关于', 320, 542)
        self.normal_elements.append(self.about_button)

        self.help_text_0 = Text(ty_game, '按方向键移动', 320, 342)
        self.help_elements.append(self.help_text_0)
        self.help_text_1 = Text(ty_game, '按 Z 射击', 320, 442)
        self.help_elements.append(self.help_text_1)
        self.help_text_2 = Text(ty_game, '按 Shift 减速', 320, 542)
        self.help_elements.append(self.help_text_2)
        self.help_text_3 = Text(ty_game, '按 P 暂停', 320, 642)
        self.help_elements.append(self.help_text_3)

        self.about_text_0 = Text(ty_game, '制作：Catfootbeats (某某)', 320, 542, background_color=None,
                                 text_color='#66CCFF')
        self.about_elements.append(self.about_text_0)
        self.about_text_1 = Text(ty_game, '试玩版，图片并无版权！！！', 320, 342, background_color=None,
                                 text_color='#EE0000')
        self.about_elements.append(self.about_text_1)
        self.about_text_2 = Text(ty_game, '仅供娱乐，切勿当真！', 320, 442, background_color=None,
                                 text_color='#EE0000')
        self.about_elements.append(self.about_text_2)
        # self.about_text_3 = Text(ty_game, 'GitHub', 260, 642, background_color=None,
        #                          text_color='#66CCFF')
        # self.about_elements.append(self.about_text_3)
        # self.about_text_4 = Text(ty_game, 'Bilibili', 370, 642, background_color=None,
        #                          text_color='#66CCFF')
        # self.about_elements.append(self.about_text_4)
        self.about_text_5 = Text(ty_game, '版本 ' + __version__, 260, 642, background_color=None,
                                 text_color='#66CCFF')
        self.about_elements.append(self.about_text_5)

    def draw(self):
        self.screen.fill('#FFFFFF')
        self.title_text.draw_element()
        if self.state == MENU_STATE_NORMAL:
            for element in self.normal_elements:
                element.draw_element()
        if self.state == MENU_STATE_HELP:
            for element in self.help_elements:
                element.draw_element()
        if self.state == MENU_STATE_ABOUT:
            for element in self.about_elements:
                element.draw_element()

    # def update(self):
    #     pass
