import math
import logging
from stg.__version__ import __version__, __resource_path__, __pyproject__

logging.basicConfig(
    format="[%(asctime)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S %z",
    level=logging.DEBUG,
)

def debug(msg, *args):
    logging.debug(msg, *args)


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
