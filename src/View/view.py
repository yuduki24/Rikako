import pygame
from pygame.locals import *

from Util.textMaker import *

class GameState:
    Title, Gacha, Wait, Play, Clear, Finish, Quit, Pass = range(1, 9)

class View():
    def __init__(self, scr_rect):
        pygame.init()
        self.screen = pygame.display.set_mode(scr_rect.size)
        self.scr_rect = scr_rect
        self.returnStatus = GameState.Pass
        pygame.display.set_caption(u"uwaaaaaa")
    def main(self):
        self.draw()
        pygame.display.update()
        self.key_handler()
        return self.returnStatus
    def key_handler(self):
        """キーハンドラー"""
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
    def draw(self):
        self.screen.fill((225, 150, 75))