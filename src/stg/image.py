import pygame


class Image:
    def __init__(self,
                 ty_game,
                 x: int,
                 y: int,
                 path: str,
                 is_transformation: bool = False,
                 width: int = None,
                 height: int = None):
        self.screen = ty_game.screen
        self.image = pygame.image.load(path)
        if is_transformation:
            self.rect = pygame.rect.Rect(x, y, width, height)
        else:
            self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

    def draw_element(self):
        self.screen.blit(self.image, self.rect)
