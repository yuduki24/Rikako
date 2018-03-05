import pygame
from pygame.locals import *

from Util.textMaker import *

class GameState:
    Title, Gacha, Wait, Play, Clear, Gameover, Finish, Quit, Pass = range(1, 10)

class View():
    def __init__(self):
        self.returnStatus = GameState.Pass
    def main(self):
        self.draw()
        self.key_handler()
        return self.returnStatus
    def key_handler(self):
        """キーハンドラー"""
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
    def draw(self):
        pass