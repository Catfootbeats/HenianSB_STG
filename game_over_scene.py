from button import Button


class GameOver:
    def __init__(self, ty_game):
        self.elements = []

        self.screen = ty_game.screen

        self.game_over_text = Button(ty_game,
                                     'Game Over',
                                     320,
                                     242,
                                     60,
                                     None,
                                     '#EE0000')
        self.elements.append(self.game_over_text)
        self.replay_button = Button(ty_game, '重新开始', 320, 342)
        self.elements.append(self.replay_button)
        self.back_menu_button = Button(ty_game, '返回标题', 320, 442)
        self.elements.append(self.back_menu_button)

    def draw(self):
        self.screen.fill('#FFFFFF')
        for element in self.elements:
            element.draw_element()
