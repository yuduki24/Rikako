import pygame
from pygame.locals import *
import sys

from Enemy.enemy import *

from Player.player import *

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
        Stage.scr_rect = SCR_RECT
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
        image = loadImage("boss1.png", -1)
        image = pygame.transform.scale(image, (96, 96))
        Boss1.images = [image, pygame.transform.flip(image, 1, 0)]

        image = loadImage("player.png", -1)
        Player.image = image
        image = loadImage("shot.png")
        Shot.image = image

        image = loadImage("player1.png", -1)
        Player1.image = image
        image = loadImage("shot1.png")
        Shot1.image = image

        image = loadImage("player2.png", -1)
        Player2.image = image
        image = loadImage("shot2.png")
        Shot2.image = image

        image = loadImage("tofu.png")
        Tofu.image = image
        image = loadImage("tofu_shot.png")
        TofuShot.image = image

        image = loadImage("onigiri.png", -1)
        Onigiri.image = image
        image = loadImage("sio.png")
        Sio.image = image

        image = loadImage("itunes_card.png")
        iTunesCard.image = image
        images = loadImages("1yen.png", "5yen.png", "100yen.png", "1000yen.png", "10000yen.png"
)
        Money.images = images

        image = loadImage("ika.png", -1)
        Ika.image = image
        image = loadImage("sumi.png")
        Ikasumi.image = image

        image = loadImage("ka-kun.png", -1)
        Kakun.image = image
        images = splitImage(loadImage("puyo.png", -1), 5)
        Puyo.images = images

        image = loadImage("beam.png")
        Beam.image = image

        image = loadImage("boss1_shot.png")
        Beam2.image = image
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