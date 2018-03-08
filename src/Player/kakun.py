import pygame
from pygame.locals import *

from Player.player import *

from Util.loader import *

import random

class Kakun(Player):
    hp_max = 5
    NAME = "カーくん"
    RANK = "レア"
    BRIEF = ["みんな大好きカーくん", "ぷよぷよのマスコットキャラクター", "みんなぷよぷよしよう(布教)"]
    def __init__(self):
        super().__init__()
    def shot(self):
        Puyo((self.rect.centerx, self.rect.top))

class Puyo(Shot):
    speed = -2
    power = 5
    def __init__(self, pos):
        super().__init__(pos)
        color = random.randint(0, 4)
        self.image = self.images[color]