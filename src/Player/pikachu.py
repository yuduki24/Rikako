import pygame
from pygame.locals import *

from Player.player import *

from Util.loader import *

class Pikachu(Player):
    reload_time = 90
    speed = 5
    hp_max = 2
    NAME = "ピカチュウ"
    RANK = "レア"
    BRIEF = ["ピカチュウ", "ねずみポケモン", "たかさ 0.4m", "おもさ 6.0kg", "でんきを　ためこむ　せいしつ。", "ピカチュウが　むれて　くらす　もりは", "らくらいが　たえず　きけんだ。"]
    def __init__(self):
        super().__init__()
        Kaminari.scr_rect = self.scr_rect
    def shot(self):
        Kaminari((self.rect.centerx, 0))

class Kaminari(Shot):
    speed = 20
    power = 10
    def __init__(self, pos):
        super().__init__(pos)
    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > self.scr_rect.height:
            self.kill()