import pygame
from pygame.locals import *

from Player.player import *

from Util.loader import *

import random

class Sushi(Player):
    reload_time = 15
    speed = 5
    hp_max = 2
    NAME = "すし"
    RANK = "レア"
    BRIEF = ["おしゅし", "I like SUSHI."]
    def __init__(self):
        super().__init__()
        self.image = self.images[0]
    def shot(self):
        SushiNeta((self.rect.centerx, self.rect.top))
    def move(self, pressed_keys):
        direction_x = pressed_keys[K_RIGHT] - pressed_keys[K_LEFT]
        direction_y = pressed_keys[K_DOWN] - pressed_keys[K_UP]
        if direction_x < 0:
            self.image = self.images[1]
        elif direction_x > 0:
            self.image = self.images[0]

        if (direction_x < 0 and self.rect.left < 30) or (direction_x > 0 and self.rect.right > self.scr_rect.right-30):
            direction_x = 0
        if (direction_y < 0 and self.rect.top < self.scr_rect.height*3//4) or (direction_y > 0 and self.rect.bottom > self.scr_rect.bottom-50):
            direction_y = 0
        self.rect.move_ip(direction_x*self.speed, direction_y*self.speed)
        # self.rect.clamp_ip(self.scr_rect)
class SushiNeta(Shot):
    speed = -5
    power = 2
    def __init__(self, pos):
        super().__init__(pos)
        neta = random.randint(0, 4)
        self.image = self.images[neta]
        
