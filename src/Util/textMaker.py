import pygame
from pygame.locals import *

RED = (255, 0, 0)
WATER_BLUE = (0, 255, 255)
YELLOW = (255, 255, 0)
GRAY = (50, 50, 50)
TITLE_GRAY = (225, 150, 75)

def getText(string, size, textColor, font=None, backgroundColor=None):
    sytemFont = pygame.font.SysFont(font, size)
    text = sytemFont.render(string, True, textColor, backgroundColor)
    return text
