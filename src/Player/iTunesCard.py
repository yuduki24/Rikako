import pygame
from pygame.locals import *

from Player.player import *

from Util.loader import *

import random

class iTunesCard(Player):
    speed = 4
    hp_max = 4
    NAME = "iTunesカード"
    RANK = "レア"
    BRIEF = ["みんな大好きiTunesカード", "昨年は何枚積みましたか??", "", "iTunesカードを使うということは、", "お金が飛んでいくということ...."]
    def __init__(self):
        super().__init__()
    def shot(self):
        Money((self.rect.centerx, self.rect.top))

class Money(Shot):
    power = 3
    def __init__(self, pos):
        super().__init__(pos)
        money = random.randint(0, 4)
        self.image = self.images[money]
        
