import math
import logging
from stg.__version__ import __version__, __resource_path__, __pyproject__, __is_pyinstaller__

logging.basicConfig(
    format="[%(asctime)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S %z",
    level=logging.DEBUG,
)

def debug(msg, *args):
    logging.debug(msg, *args)



def msgbox(msg):
    import os
    import pygame
    import textwrap
    pygame.init()
    screen = pygame.display.set_mode((400, 200))
    pygame.display.set_caption("错误")
    font = pygame.font.Font(os.path.join(__resource_path__, "fonts/SourceHanSansCN-Normal.otf"), 15)
    wraps = textwrap.wrap(msg, width=40)
    texts = [font.render(wrap, True, (0, 0, 0)) for wrap in wraps]
    while True:
        screen.fill((255, 255, 255))
        for i, text in enumerate(texts):
            screen.blit(text, (10, 10 + i * 20))
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
