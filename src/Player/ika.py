import pygame
from pygame.locals import *

from Player.player import *

from Util.loader import *

class Ika(Player):
    reload_time = 45
    speed = 2
    hp_max = 5
    NAME = "イカ"
    RANK = "レア"
    BRIEF = ["スプラトゥーン", "マンメンミ", "ではない。", "リアル the イカ", "", "墨を吐く。"]
    def __init__(self):
        super().__init__()
    def shot(self):
        Ikasumi((self.rect.centerx, self.rect.top))

class Ikasumi(Shot):
    power = 4
    def __init__(self, pos):
        super().__init__(pos)
