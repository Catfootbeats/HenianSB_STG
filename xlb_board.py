import os

from image import Image
from text import Text

XLB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images/Xiaolongbao.jpg')


class XLBBoard:
    def __init__(self, ty_game, x: int, y: int, text_color="#FFFFFF"):
        self.game = ty_game
        self.text_color = text_color
        self.x = x
        self.y = y
        self.msg = None

        self.xlb_image = Image(ty_game, x - 100, y, XLB_PATH)
        self.text = Text(self.game, self.msg, self.x, self.y, background_color=None, text_color=self.text_color)

    def draw(self, xlb: int):
        self.msg = "  *  " + str(xlb)
        self.text.draw_element(self.msg)
        self.xlb_image.draw_element()
