import pygame.font


class Text:
    def __init__(self,
                 ty_game,
                 msg: str,
                 x: int,
                 y: int,
                 size: int = 24,
                 background_color='#66CCFF',
                 text_color='#FFFFFF',
                 width=200,
                 height=50,
                 font='simhei'):
        self.screen = ty_game.screen
        self.screen_rect = ty_game.screen.get_rect()

        self.width, self.height = width, height
        self.button_color = background_color
        self.text_color = text_color
        self.font = pygame.font.SysFont(font, size)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centerx = x
        self.rect.centery = y

        self._prep_msg(msg)

    def _prep_msg(self, msg: str):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_element(self):
        if self.button_color:
            self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    # def on_click(self) -> bool:
    #     for event in pygame.event.get():
    #         if event.type == pygame.MOUSEBUTTONDOWN:
    #             mouse_pos = pygame.mouse.get_pos()
    #             if self.rect.collidepoint(mouse_pos):
    #                 return True
    #             else:
    #                 return False
    #         else:
    #             return False
