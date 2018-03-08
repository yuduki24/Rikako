import pygame
from pygame.locals import *

from Util.loader import *

import random

class Enemy(pygame.sprite.Sprite):
    speed = 2       #移動速度.
    animcycle = 18  #アニメーション速度
    frame = 0
    move_width = 230  # 横方向の移動範囲
    prob_beam = 0.003  # ビームを発射する確率
    hp = 2
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect(midbottom=pos)
        self.left = pos[0]
        self.right = self.left + self.move_width
    def update(self):
        self.rect.move_ip(self.speed, 0)
        if self.rect.center[0] < self.left or self.rect.center[0] > self.right:
            self.speed = -self.speed
        # キャラクターアニメーション
        self.frame += 1
        self.image = self.images[self.frame//self.animcycle%2]
        # ビームを発射
        if random.random() < self.prob_beam:
            Beam(self.rect.center)
    def damage(self, point):
        self.hp -= point
        if self.hp <= 0:
            self.kill()
class Beam(pygame.sprite.Sprite):
    speed = 6
    power = 1
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.rect = self.image.get_rect(midbottom=pos)
    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > self.scr_rect.height:
            self.kill()

class Beam1(Beam):
    speed = 8
    power = 2
