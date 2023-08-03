import math
import logging
from pygame.font import Font
from stg.__version__ import __version__, __resource_path__, __pyproject__, __is_pyinstaller__, __is_macos_appbundle__

logging.basicConfig(
    format="[%(asctime)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S %z",
    level=logging.DEBUG,
)

def debug(msg, *args):
    logging.debug(msg, *args)


def msgbox(msg: str):
    import os
    import pygame
    ERROR_WINDOW_SIZE = (400, 200)
    ERROR_WINDOW_COLOR = (255, 255, 255)
    ERROR_FONT_SIZE = 15
    ERROR_FONT_COLOR = (0, 0, 0)
    ERROR_LINE_WIDTH = 360
    ERROR_LINE_HEIGHT = 25

    pygame.init()
    screen = pygame.display.set_mode(ERROR_WINDOW_SIZE)
    pygame.display.set_caption("错误")
    pygame.display.set_icon(pygame.image.load(os.path.join(__resource_path__, "images/tysm.ico")))
    font = pygame.font.Font(os.path.join(__resource_path__, "fonts/SourceHanSansCN-Normal.otf"), ERROR_FONT_SIZE)
    lines = wrap_text(font, msg, ERROR_LINE_WIDTH)
    lines = [font.render(line, True, ERROR_FONT_COLOR) for line in lines]
    while True:
        screen.fill(ERROR_WINDOW_COLOR)
        for i, text in enumerate(lines):
            screen.blit(text, (10, 10 + i * ERROR_LINE_HEIGHT))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        pygame.display.update()


def get_player_direction(self, player_x: int, player_y: int) -> float:
    # Get player's position and transform into direction.
    x: float = player_x - self.rect.centerx
    y: float = player_y - self.rect.centery
    if x >= 0:
        # print('x >= 0')
        if y >= 0:
            # print('y >= 0')
            return 90 - math.degrees(math.asin(x / math.sqrt(x * x + y * y)))
        if y < 0:
            # print('y < 0')
            return math.degrees(math.asin(x / math.sqrt(x * x + y * y))) - 90
    elif x < 0:
        # print('x < 0')
        if y >= 0:
            # print('y >= 0')
            return 90 - math.degrees(math.asin(x / math.sqrt(x * x + y * y)))
        elif y < 0:
            # print('y < 0')
            return math.degrees(math.asin(x / math.sqrt(x * x + y * y))) - 90


def string_width(font: Font, text: str) -> int:
    rect = font.render(text, True, (0, 0, 0))
    return rect.get_width()


def wrap_text(font: Font, text: str, line_width: int) -> int:
    lines = []
    current_line = ""
    for i in text:
        if (i == "\n") or (string_width(font, current_line) > line_width):
            lines.append(current_line)
            current_line = i.strip()
            continue
        current_line += i
    if current_line.strip() != "":
        lines.append(current_line)
    return [line.strip() for line in lines]
