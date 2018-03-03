import pygame
from pygame.locals import *
import sys

from Enemy.enemy import *

from Player.player import *

from View.titleView import *
from View.gachaView import *
from View.waitView import *
from View.playView import *

from Util.loader import *

SCR_RECT = Rect(0, 0, 1200, 800)

class GaSshoo():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCR_RECT.size)
        pygame.display.set_caption(u"uwaaaaaa")
        View.scr_rect = SCR_RECT
        View.screen = self.screen
        
        # 画像.
        image = loadImage("enemy.png")
        Enemy.images = [image, pygame.transform.flip(image, 1, 0)]
        image = loadImage("player.png")
        Player.image = image
        image = loadImage("shot.png")
        Shot.image = image
        
        # 音楽.
        
        all = pygame.sprite.RenderUpdates()    
        enemy = pygame.sprite.Group()
        shots = pygame.sprite.Group()
        bombs = pygame.sprite.Group()
        lastenemy = pygame.sprite.GroupSingle()
        
        Player.containers = all
        Enemy.containers = enemy, all, lastenemy
        Shot.containers = shots, all
        # Bomb.containers = bombs, all
        # Explosion.containers = all
    
        clock = pygame.time.Clock()
        view = TitleView()
        while True:
            clock.tick(60)
            event = view.main()
            all.update()
            all.draw(self.screen)
            pygame.display.update()
            if(event == GameState.Pass):
                pass
            elif(event == GameState.Gacha):
                view = GachaView()
            elif(event == GameState.Wait):
                view = WaitView()
            elif(event == GameState.Play):
                # TODO:ガチャで出たキャラをPlayViewに渡すようにする
                player = Player((SCR_RECT.width//2, SCR_RECT.height*3//4))
                view = PlayView(player)
            elif(event == GameState.Quit):
                pygame.quit()
                sys.exit()
                break

if __name__ == "__main__":
    GaSshoo()