import pygame
from pygame.locals import *

from Player.player import *

from Util.loader import *

class Homuhomu(Player):
    reload_time = 40
    hp_max = 5
    NAME = "ほむほむ"
    RANK = "レア"
    BRIEF = ["ほむほむ", "", "交わした約束忘れない", "忘れちゃダメ、絶対。"]
    def __init__(self):
        super().__init__()
    def shot(self):
        Arrow((self.rect.centerx, self.rect.top))

class Arrow(Shot):
    speed = -18
    power = 2
    def __init__(self, pos):
        super().__init__(pos)
