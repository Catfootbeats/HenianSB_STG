import os

from stg.image import Image
from stg.components.text import Text
from stg import __resource_path__

XLB_PATH = os.path.join(__resource_path__, 'images/xiaolongbao.jpg')


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
