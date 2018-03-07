import pygame
from pygame.locals import *

from Player.player import *

from Util.loader import *

class Tofu(Player):
    reload_time = 60
    speed = 4
    hp_max = 1
    NAME = "豆腐"
    RANK = "レア"
    BRIEF = ["お豆腐", "お豆腐おいしい。", "小さい頃は嫌いだったけど最近好き", "めんつゆサイコー!", "", "シューティングには向いていない"]
    def __init__(self):
        super().__init__()
    def shot(self):
        TofuShot((self.rect.centerx, self.rect.top))

class TofuShot(Shot):
    speed = -3
    power = 1
    def __init__(self, pos):
        super().__init__(pos)
