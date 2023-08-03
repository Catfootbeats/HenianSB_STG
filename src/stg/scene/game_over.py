import os
from stg.components.text import Text
from stg.components.board import ScoreBoard
from stg import __resource_path__

FONT_PATH = os.path.join(__resource_path__, 'fonts/Curely.ttf')


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
        self.score_board = ScoreBoard(ty_game, 385, 342, "#66CCFF")
        self.elements.append(self.game_over_text)
        self.replay_button = Text(ty_game, '重新开始', 320, 442)
        self.elements.append(self.replay_button)
        self.back_menu_button = Text(ty_game, '返回标题', 320, 542)
        self.elements.append(self.back_menu_button)

    def draw(self, score: int):
        self.screen.fill('#FFFFFF')
        for element in self.elements:
            element.draw_element()
        self.score_board.draw(score)
