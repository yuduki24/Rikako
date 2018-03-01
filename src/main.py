import pygame
from pygame.locals import *
import sys

from View.titleView import *
from View.gachaView import *
from View.waitView import *
from View.playView import *

from Player.player import *

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
        elif(event == GameState.Wait):
            view = WaitView(SCR_RECT)
        elif(event == GameState.Play):
            # TODO:ガチャで出たキャラをPlayViewに渡すようにする
            player = Player()
            view = PlayView(SCR_RECT, player)
        elif(event == GameState.Quit):
            pygame.quit()
            sys.exit()
            break

