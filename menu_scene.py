from button import Button

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

        self.title_text = Button(ty_game,
                                 '暴打老V',
                                 320,
                                 242,
                                 60,
                                 None,
                                 '#66CCFF')

        self.play_button = Button(ty_game, '开始', 320, 342)
        self.normal_elements.append(self.play_button)
        self.help_button = Button(ty_game, '帮助', 320, 442)
        self.normal_elements.append(self.help_button)
        self.about_button = Button(ty_game, '关于', 320, 542)
        self.normal_elements.append(self.about_button)

        self.help_text_0 = Button(ty_game, '按方向键移动', 320, 342)
        self.help_elements.append(self.help_text_0)
        self.help_text_1 = Button(ty_game, '按 Z 射击', 320, 442)
        self.help_elements.append(self.help_text_1)
        self.help_text_2 = Button(ty_game, '按 Shift 减速', 320, 542)
        self.help_elements.append(self.help_text_2)

        self.about_text_0 = Button(ty_game, '前面的区域，以后再来探索吧！', 320, 342, background_color=None, text_color='#66CCFF')
        self.about_elements.append(self.about_text_0)

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
