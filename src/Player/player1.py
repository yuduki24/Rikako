import pygame
from pygame.locals import *

from Player.player import *

from Util.loader import *

class Player1(Player):
    speed = 4
    reload_time = 30
    NAME = "2号機"
    RANK = "ノーマル"
    BRIEF = ["適当にペイントで作成した2号機", "何の変哲もない。", "初号機よりも早いが、打つスピードと弾の速度が遅い。"]
    def __init__(self):
        super().__init__()
    def shot(self):
        Shot1((self.rect.centerx, self.rect.top))

class Shot1(Shot):
    speed = -5
    def __init__(self, pos):
        super().__init__(pos)
    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top <= 0:
            self.kill()