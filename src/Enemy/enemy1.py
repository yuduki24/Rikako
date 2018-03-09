import pygame
from pygame.locals import *

from Enemy.enemy import *

import random

class Enemy1(Enemy):
    speed = 2       #移動速度.
    animcycle = 18  #アニメーション速度
    frame = 0
    move_width = 230  # 横方向の移動範囲
    prob_beam = 0.005  # ビームを発射する確率
    hp = 2
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect(midbottom=pos)
        self.speed = random.randint(3,7)
    def update(self):
        direction_x = random.randint(1,3) - 2
        direction_y = random.randint(1,3) - 2
        if (direction_x < 0 and self.rect.left < 30) or (direction_x > 0 and self.rect.right > self.scr_rect.right-30):
            direction_x = 0
        if (direction_y < 0 and self.rect.top < 30) or (direction_y > 0 and self.rect.bottom > self.scr_rect.bottom*3//4):
            direction_y = 0
        self.rect.move_ip(self.speed * direction_x, self.speed * direction_y)

        # キャラクターアニメーション
        self.frame += 1
        self.image = self.images[self.frame//self.animcycle%2]
        # ビームを発射
        if random.random() < self.prob_beam:
            Beam(self.rect.center)
