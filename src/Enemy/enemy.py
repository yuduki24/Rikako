import pygame
from pygame.locals import *

from Util.loader import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        self.image = loadImage("enemy.png")
    def initialise(self):
        scr_rect = Rect(0, 0, 1200, 800)
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.rect = self.image.get_rect()
        self.rect.center = scr_rect.center
        self.rect.top = scr_rect.top + 50
