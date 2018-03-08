import pygame
from pygame.locals import *

from Enemy.enemy import *

from Util.loader import *

import random

class Boss1(Enemy):
    speed = 5       #移動速度.
    animcycle = 18  #アニメーション速度
    frame = 0
    prob_beam = 0.05  # ビームを発射する確率
    prob_reverse = 0.005  # 方向転換する確率
    hp = 30
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect(midbottom=pos)
        self.direction_x = 1
        self.direction_y = 1
    def update(self):

        if (self.direction_x < 0 and self.rect.left < 100) or (self.direction_x > 0 and self.rect.right > self.scr_rect.right-100) or (random.random() < self.prob_reverse):
            self.direction_x *= -1
        if (self.direction_y < 0 and self.rect.top < 100) or (self.direction_y > 0 and self.rect.bottom > self.scr_rect.bottom*3//5) or (random.random() < self.prob_reverse):
            self.direction_y *= -1
        self.rect.move_ip(self.speed * self.direction_x, self.speed * self.direction_y)

        # キャラクターアニメーション
        self.frame += 1
        self.image = self.images[self.frame//self.animcycle%2]
        # ビームを発射
        if random.random() < self.prob_beam:
            Beam2(self.rect.center)
    def damage(self, point):
        self.hp -= point
        if self.hp <= 0:
            self.kill()
