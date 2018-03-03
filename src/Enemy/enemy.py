import pygame
from pygame.locals import *

from Util.loader import *

class Enemy(pygame.sprite.Sprite):
    speed = 2       #移動速度.
    animcycle = 18  #アニメーション速度
    frame = 0
    move_width = 230  # 横方向の移動範囲
    def __init__(self):
        image = loadImage("enemy.png")
        self.images = [image, pygame.transform.flip(image, 1, 0)]
        self.image = self.images[0]
    def initialise(self, pos):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.left = pos[0]
        self.right = self.left + self.move_width
    def update(self):
        self.rect.move_ip(self.speed, 0)
        if self.rect.center[0] < self.left or self.rect.center[0] > self.right:
            self.speed = -self.speed
        # キャラクターアニメーション
        self.frame += 1
        self.image = self.images[self.frame//self.animcycle%2]