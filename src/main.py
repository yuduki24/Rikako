import pygame
from pygame.locals import *
import sys

from Enemy.enemy import *

from Player.player import *
from Player.player1 import *

from View.titleView import *
from View.gachaView import *
from View.waitView import *
from View.playView import *

from Util.loader import *

from gameManager import *

SCR_RECT = Rect(0, 0, 800, 600)

class GaSshoo():
    def __init__(self):
        pygame.init()
        screen = pygame.display.set_mode(SCR_RECT.size)
        pygame.display.set_caption(u"uwaaaaaa")
        View.scr_rect = SCR_RECT
        View.screen = screen
        Player.pos = (SCR_RECT.width//2, SCR_RECT.height-50)
        # 画像.
        image = loadImage("normalGacha1.png")
        GachaView.normal1 = image
        image = loadImage("normalGacha2.png")
        GachaView.normal2 = image
        image = loadImage("ultraGacha1.png")
        GachaView.ultra1 = image
        image = loadImage("ultraGacha2.png")
        GachaView.ultra2 = image
        
        image = loadImage("enemy.png", -1)
        Enemy.images = [image, pygame.transform.flip(image, 1, 0)]
        image = loadImage("player.png", -1)
        Player.image = image
        image = loadImage("shot.png")
        Shot.image = image
        image = loadImage("player1.png", -1)
        Player1.image = image
        image = loadImage("shot1.png")
        Shot1.image = image        
        # 音楽.
        
        all = pygame.sprite.RenderUpdates()    
        enemys = pygame.sprite.Group()
        shots = pygame.sprite.Group()
        bombs = pygame.sprite.Group()
        lastenemy = pygame.sprite.GroupSingle()
        
        GameManager.enemyGroup = enemys
        GameManager.shotGroup = shots
        GameManager.screen = screen
        GameManager.all = all
        
        Player.containers = all
        Enemy.containers = enemys, all, lastenemy
        Shot.containers = shots, all
        # Bomb.containers = bombs, all
        # Explosion.containers = all
    
        clock = pygame.time.Clock()
        view = TitleView()
        while True:
            clock.tick(60)
            event = view.main()
            pygame.display.update()
            if(event == GameState.View):
                view = TitleView()
            elif(event == GameState.Gacha):
                view = GachaView()
            elif(event == GameState.Wait):
                self.createPlayer(view.playerID)
                view = WaitView(self.player)
            elif(event == GameState.Play):
                view = PlayView(self.player)
            elif(event == GameState.Quit):
                pygame.quit()
                sys.exit()
                break
            elif(event == GameState.Pass):
                pass
    def createPlayer(self, id):
        if id == 0:
            self.player = Player()
        elif id == 1:
            self.player = Player1()
if __name__ == "__main__":
    GaSshoo()