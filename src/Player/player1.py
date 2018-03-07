import pygame
from pygame.locals import *

from Player.player import *

from Util.loader import *

class Player1(Player):
    reload_time = 15
    NAME = "2号機"
    RANK = "ノーマル"
    BRIEF = ["適当にペイントで作成した2号機", "何の変哲もない。", "初号機に比べて連射性能が高い", "弾の火力は低い"]
    def __init__(self):
        super().__init__()
    def shot(self):
        Shot1((self.rect.centerx, self.rect.top))

class Shot1(Shot):
    speed = -8
    power = 1
    def __init__(self, pos):
        super().__init__(pos)
