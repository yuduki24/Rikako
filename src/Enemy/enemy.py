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

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        self.image = load_image("enemy.png")
    def initialise(self):
        scr_rect = Rect(0, 0, 1200, 800)
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.rect = self.image.get_rect()
        self.rect.center = scr_rect.center
        self.rect.top = scr_rect.top + 50
        print("aa")
