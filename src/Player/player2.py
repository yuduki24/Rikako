import pygame
from pygame.locals import *

from Player.player import *

from Util.loader import *

class Player2(Player):
    reload_time = 40
    speed = 5
    NAME = "3号機"
    RANK = "ノーマル"
    BRIEF = ["適当にペイントで作成した3号機", "初号機と2号機の弟分", "若いためかスピードは少し早い", "連射性能は悪い"]
    def __init__(self):
        super().__init__()
    def shot(self):
        Shot2((self.rect.centerx, self.rect.top))

class Shot2(Shot):
    def __init__(self, pos):
        super().__init__(pos)
