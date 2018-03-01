import pygame
from pygame.locals import *

from Util.loader import *

class Player(pygame.sprite.Sprite):
    speed = 10
    hp = 2
    power = 1
    reloadTime = 5
    def __init__(self):
        self.image = loadImage("player.png")
    def initialise(self, scr_rect):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.scr_rect = scr_rect
        self.rect = self.image.get_rect()
        self.rect.center = scr_rect.center
        self.rect.bottom = scr_rect.bottom
    def move(self, pressed_keys):
        direction_x = pressed_keys[K_RIGHT] - pressed_keys[K_LEFT]
        direction_y = pressed_keys[K_DOWN] - pressed_keys[K_UP]
        self.rect.move_ip(direction_x*self.speed, direction_y*self.speed)
        self.rect.clamp_ip(self.scr_rect)
    def getPossition(self):
        return self.rect.centerx, self.rect.top

class Shot(pygame.sprite.Sprite):
    speed = -11
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = loadImage("shot.png")
        self.rect = self.image.get_rect(midbottom=pos)

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top <= 0:
            self.kill()