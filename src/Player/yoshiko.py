import pygame
from pygame.locals import *

from Player.player import *

import math

class Yoshiko(Player):
    speed = 7
    hp_max = 4
    NAME = "善子(ヨハネ)"
    RANK = "ウルトラレア"
    BRIEF = ["堕天使のヨハネよ!", "", "かわいいは正義", "(かわいい.......)"]
    def __init__(self):
        super().__init__()
    def shot(self):
        LovekaStone((self.rect.centerx, self.rect.top), 105)
        LovekaStone((self.rect.centerx, self.rect.top),  90)
        LovekaStone((self.rect.centerx, self.rect.top),  75)

class LovekaStone(Shot):
    speed = -12
    power = 3
    def __init__(self, pos, rad):
        super().__init__(pos)
        # 弾の角度. 0度が右、90度が上.
        self.rad = rad
    def update(self):
        angle = math.radians(self.rad)
        dx =  self.speed * math.cos(angle)
        dy =  self.speed * math.sin(angle)
        self.rect.move_ip(dx, dy)
        if self.rect.top <= 0:
            self.kill()
