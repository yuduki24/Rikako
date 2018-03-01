import pygame
from pygame.locals import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WATER_BLUE = (0, 255, 255)
YELLOW = (255, 255, 0)
GRAY = (50, 50, 50)
TITLE_GRAY = (225, 150, 75)

def getText(string, size, textColor, font=None, backgroundColor=None):
    sytemFont = pygame.font.SysFont(font, size)
    text = sytemFont.render(string, True, textColor, backgroundColor)
    return text
