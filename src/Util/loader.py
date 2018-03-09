import os.path
import sys

import pygame
from pygame.locals import *

current_dir = os.path.abspath(os.path.dirname(sys.argv[0]))  # スクリプトのディレクトリ
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))  # スクリプトの親ディレクトリ

def loadImage(file, colorkey=None):
    file = os.path.join(parent_dir, 'img', file)
    try:
        surface = pygame.image.load(file)
    except pygame.error:
        raise SystemExit('Could not load image "%s" %s'%(file, pygame.get_error()))
    surface = surface.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = surface.get_at((0,0))
        surface.set_colorkey(colorkey, RLEACCEL)
    return surface

def loadImages(*files):
    imgs = []
    for file in files:
        imgs.append(loadImage(file))
    return imgs

def loadSound(file):
    file = os.path.join(parent_dir, 'sound', file)
    return pygame.mixer.Sound(file)

def playSound(file, repeat=None):
    file = os.path.join(parent_dir, 'sound', file)
    pygame.mixer.music.load(file)
    if repeat is not None:
        if repeat is -1:
            pygame.mixer.music.play(-1)

def loadFont(file, size):
    file = os.path.join(parent_dir, 'font', file)
    return pygame.font.Font(file, size)

def splitImage(image, n):
    """横に長いイメージを同じ大きさのn枚のイメージに分割
    分割したイメージを格納したリストを返す"""
    image_list = []
    w = image.get_width()
    h = image.get_height()
    w1 = int(w / n)
    for i in range(0, w, w1):
        surface = pygame.Surface((w1,h))
        surface.blit(image, (0,0), (i,0,w1,h))
        surface.set_colorkey(surface.get_at((0,0)), RLEACCEL)
        surface.convert()
        surface = pygame.transform.scale(surface, (16, 16))
        image_list.append(surface)
    return image_list
