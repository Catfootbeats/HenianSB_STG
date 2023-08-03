import pygame


class CircleCollideBody:
    def __init__(self, r: int):
        self.r = r

    # 会短暂卡墙角的方法
    # def update(self, rect: pygame.Rect, screen_rect: pygame.Rect):
    #     if rect.centerx - self.r < screen_rect.left:
    #         rect.centerx = screen_rect.left + self.r
    #     if rect.centerx + self.r > screen_rect.right:
    #         rect.centerx = screen_rect.right - self.r
    #     if rect.centery - self.r < screen_rect.top:
    #         rect.centery = screen_rect.top + self.r
    #     if rect.centery + self.r > screen_rect.bottom:
    #         rect.centery = screen_rect.bottom - self.r

    def left(self, rect: pygame.Rect, screen_rect: pygame.Rect) -> bool:
        if rect.centerx - self.r < screen_rect.left:
            return True
        else: 
            return False
        
    def right(self, rect: pygame.Rect, screen_rect: pygame.Rect) -> bool:
        if rect.centerx + self.r > screen_rect.right:
            return True
        else: 
            return False
        
    def top(self, rect: pygame.Rect, screen_rect: pygame.Rect) -> bool:
        if rect.centery - self.r < screen_rect.top:
            return True
        else: 
            return False
        
    def bottom(self, rect: pygame.Rect, screen_rect: pygame.Rect) -> bool:
        if rect.centery + self.r > screen_rect.bottom:
            return True
        else: 
            return False
