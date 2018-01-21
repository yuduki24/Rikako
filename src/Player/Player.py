import pygame
from pygame.locals import *
import sys
import os

def load_image(filename, colorkey=None):
    current_dir = os.path.abspath(os.path.dirname(sys.argv[0]))  # スクリプトのディレクトリ
    parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))  # スクリプトの親ディレクトリ
    filename = os.path.join("img", filename)
    filename = os.path.join(parent_dir, filename)
    try:
        image = pygame.image.load(filename)
    except pygame.error as message:
        print ("Cannot load image:", filename)
        raise SystemExit(message)
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image

class Player(pygame.sprite.Sprite):
    speed = 10
    hp = 2
    power = 1
    reloadTime = 5
    def __init__(self):
        self.image = load_image("player.png")
    def initialise(self, scr_rect):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.scr_rect = scr_rect
        self.rect = self.image.get_rect()
        self.rect.center = scr_rect.center
        self.rect.bottom = scr_rect.bottom
    def move(self, pressed_keys):
        if pressed_keys[K_LEFT]:
            if self.rect.left > 0:
                self.rect.move_ip(-self.speed, 0)
        elif pressed_keys[K_RIGHT]:
            if self.rect.right < self.scr_rect.right:
                self.rect.move_ip(self.speed, 0)
        if pressed_keys[K_UP]:
            if self.rect.top > self.scr_rect.top:
                self.rect.move_ip(0, -self.speed)
        elif pressed_keys[K_DOWN]:
            if self.rect.bottom < self.scr_rect.bottom:
                self.rect.move_ip(0, self.speed)
        self.rect.clamp_ip(self.scr_rect)