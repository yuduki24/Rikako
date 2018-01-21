import pygame
from pygame.locals import *
import sys

from View.TitleView import *
from View.GachaView import *

SCR_RECT = Rect(0, 0, 1200, 800)

if __name__ == "__main__":
    clock = pygame.time.Clock()
    view = TitleView(SCR_RECT)
    while True:
        clock.tick(60)
        event = view.main()
        if(event == GameState.Pass):
            pass
        elif(event == GameState.Gacha):
            view = GachaView(SCR_RECT)
        elif(event == GameState.Quit):
            pygame.quit()
            sys.exit()
            break

