import pygame
from pygame.locals import *

from Enemy.enemy import *

class Boss2(Enemy):
    hp = 100
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.rect = self.image.get_rect(midbottom=pos)
    def update(self):
        pass
