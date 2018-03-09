import pygame
from pygame.locals import *

from Enemy.enemy import *

import random

class Boss3(Enemy):
    speed = 10       #移動速度.
    prob_beam = 0.05  # ビームを発射する確率
    prob_reverse = 0.005  # 方向転換する確率
    hp = 200
    frame = 0
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.rect = self.image.get_rect(midbottom=pos)
    def update(self):
        self.speed = random.randint(-5, 5) * 5
        if (self.speed < 0 and self.rect.left < 100) or (self.speed > 0 and self.rect.right > self.scr_rect.right-100):
            self.speed = 0
        self.frame += 1
        if self.frame % 10 == 0:
            self.rect.move_ip(self.speed, 0)
        # ビームを発射
        if random.random() < self.prob_beam:
            Beam(self.rect.center)
            x, y = self.rect.center
            Beam((x + 64, y))
            Beam((x - 64, y))