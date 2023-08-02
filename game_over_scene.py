import os

from text import Text
from xlb_board import XLBBoard

FONT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fonts/curely.ttf')


class GameOver:
    def __init__(self, ty_game):
        self.elements = []

        self.screen = ty_game.screen

        self.game_over_text = Text(ty_game,
                                   'Game Over',
                                   320,
                                   242,
                                   60,
                                   None,
                                   '#EE0000',
                                   font=FONT_PATH)
        self.xlb_board = XLBBoard(ty_game, 385, 342, "#66CCFF")
        self.elements.append(self.game_over_text)
        self.replay_button = Text(ty_game, '重新开始', 320, 442)
        self.elements.append(self.replay_button)
        self.back_menu_button = Text(ty_game, '返回标题', 320, 542)
        self.elements.append(self.back_menu_button)

    def draw(self, xlb: int):
        self.screen.fill('#FFFFFF')
        for element in self.elements:
            element.draw_element()
        self.xlb_board.draw(xlb)
