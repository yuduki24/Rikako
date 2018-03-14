import pygame
from pygame.locals import *

from Util.loader import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WATER_BLUE = (0, 255, 255)
YELLOW = (255, 255, 0)
GRAY = (50, 50, 50)
TITLE_GRAY = (225, 150, 75)
PLAY_COLOR = (10, 20, 10)

def getText(string, size, textColor, backgroundColor=None):
    sytemFont = loadFont('ipag.ttf', size)
    text = sytemFont.render(string, True, textColor, backgroundColor)
    return text
