import pygame
from pygame.locals import *
import sys

SCR_RECT = Rect(0, 0, 1200, 800)



class Shooting:
    def __init__(self):
        pygame.init()
        screen = pygame.display.set_mode(SCR_RECT.size)
        pygame.display.set_caption(u"uwaaaaaa")
        self.initialize(screen)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            self.draw(screen)
            pygame.display.update()
            self.key_handler()
    def initialize(self, screen):
        """ゲームオブジェクトの初期化"""
        self.all = pygame.sprite.RenderUpdates()
    def key_handler(self):
        """キーハンドラー"""
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
    def draw(self, screen):
        screen.fill((25, 50, 75))


if __name__ == "__main__":
    Shooting()
