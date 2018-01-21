import pygame
from pygame.locals import *
import sys

from View.TitleView import *

SCR_RECT = Rect(0, 0, 1200, 800)

if __name__ == "__main__":
    clock = pygame.time.Clock()
    view = TitleView(SCR_RECT)
    while view.main():
        clock.tick(60)
