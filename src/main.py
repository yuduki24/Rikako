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
from View.gameoverView import *

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
        Player.pos = (SCR_RECT.width//2, SCR_RECT.height-80)
        Player.scr_rect = SCR_RECT
        Enemy.scr_rect = SCR_RECT
        Beam.scr_rect = SCR_RECT
        
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
        image = loadImage("enemy1.png", -1)
        Enemy1.images = [image, pygame.transform.flip(image, 1, 0)]
        image = loadImage("player.png", -1)
        Player.image = image
        image = loadImage("shot.png")
        Shot.image = image
        image = loadImage("player1.png", -1)
        Player1.image = image
        image = loadImage("shot1.png")
        Shot1.image = image
        image = loadImage("beam.png")
        Beam.image = image
        # 音楽.
        
        all = pygame.sprite.RenderUpdates()    
        players = pygame.sprite.Group()
        enemys = pygame.sprite.Group()
        shots = pygame.sprite.Group()
        beams = pygame.sprite.Group()
        lastenemy = pygame.sprite.GroupSingle()
        
        GameManager.screen = screen
        GameManager.playerGroup = players
        GameManager.enemyGroup = enemys
        GameManager.shotGroup = shots
        GameManager.beamGroup = beams
        GameManager.all = all
        
        Player.containers = players, all
        Enemy.containers = enemys, all, lastenemy
        Shot.containers = shots, all
        Beam.containers = beams, all
        # Explosion.containers = all
    
        clock = pygame.time.Clock()
        view = TitleView()
        while True:
            clock.tick(60)
            event = view.main()
            pygame.display.update()
            if(event == GameState.Title):
                view = TitleView()
            elif(event == GameState.Gacha):
                view = GachaView()
            elif(event == GameState.Wait):
                view = WaitView(view.player)
            elif(event == GameState.Play):
                view = PlayView(view.player)
            elif(event == GameState.Gameover):
                view = GameoverView(view.player)
            elif(event == GameState.Quit):
                pygame.quit()
                sys.exit()
                break
            elif(event == GameState.Pass):
                pass
if __name__ == "__main__":
    GaSshoo()