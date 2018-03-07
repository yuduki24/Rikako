import pygame
from pygame.locals import *

from Player.player import *

from Util.loader import *

class Onigiri(Player):
    reload_time = 50
    speed = 2
    hp_max = 1
    NAME = "おにぎり"
    RANK = "レア"
    BRIEF = ["おにぎり", "絶対に許さない", "", "投げるのは、塩."]
    def __init__(self):
        super().__init__()
    def shot(self):
        Sio((self.rect.centerx, self.rect.top))

class Sio(Shot):
    speed = -10
    power = 1
    def __init__(self, pos):
        super().__init__(pos)
