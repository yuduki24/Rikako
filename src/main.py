import pygame
from pygame.locals import *
import sys

from View.TitleView import *

SCR_RECT = Rect(0, 0, 1200, 800)

if __name__ == "__main__":
    titleView = TitleView(SCR_RECT)
    while True:
        titleView.main()

