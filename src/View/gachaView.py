from View.view import *

from Player.player import *
from Player.player1 import *
from Player.player2 import *
from Player.tofu import *
from Player.onigiri import *
from Player.iTunesCard import *
from Player.ika import *
from Player.kakun import *
from Player.pikachu import *
from Player.homuhomu import *
from Player.sushi import *
from Player.cheetah_man import *

import random

BEFORE_GACHA, AFTER_GACHA = 0, 1
NORMAL_GACHA, ULTRA_GACHA = 0, 1

class GachaView(View):
    def __init__(self):
        super().__init__()
        self.screen.blit(self.normal1, (0, 0))
        self.gachaState = BEFORE_GACHA
        self.gachaKind  = NORMAL_GACHA
    def draw(self):
        text = None
        if self.gachaState == BEFORE_GACHA:
            if self.gachaKind == NORMAL_GACHA:
                image = self.normal1
            elif self.gachaKind == ULTRA_GACHA:
                image = self.ultra1
            text = getText("ガチャる\n(please Enter)", 20, BLACK)
        elif self.gachaState == AFTER_GACHA:
            if self.gachaKind == NORMAL_GACHA:
                image = self.normal2
            elif self.gachaKind == ULTRA_GACHA:
                image = self.ultra2
        self.screen.blit(image, (0, 0))
        if text:
            self.screen.blit(text, (self.scr_rect.width//2 - text.get_width()//2, self.scr_rect.height-50))
    def key_handler(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_LEFT:
                self.gachaKind  = NORMAL_GACHA
            if event.type == KEYDOWN and event.key == K_RIGHT:
                self.gachaKind  = ULTRA_GACHA
            if event.type == KEYDOWN and event.key == K_RETURN:
                if self.gachaState == BEFORE_GACHA:
                    self.gachaState = AFTER_GACHA
                elif self.gachaState == AFTER_GACHA:
                    if self.gachaKind == NORMAL_GACHA:
                        self.gacha(95, 5, 0)
                    elif self.gachaKind == ULTRA_GACHA:
                        #self.gacha(15, 80, 5)
                        self.gacha(0, 97, 3)
                    self.returnStatus = GameState.Wait
    def gacha(self, N, R, UR):
        # ガチャの種類によって変える.
        gacha_num = random.randint(1,100)
        if gacha_num < N:
            self.normalGacha()
        elif gacha_num < N+R:
            self.rareGacha()
        else:
            self.ultraGacha()
    def normalGacha(self):
        normal_count = 3
        gacha_num = random.randint(1, normal_count)
        if gacha_num == 1:
            self.player = Player()
        elif gacha_num == 2:
            self.player = Player1()
        elif gacha_num == 3:
            self.player = Player2()
    def rareGacha(self):
        rare_count = 8
        gacha_num = random.randint(1, rare_count)
        #gacha_num = 5
        if gacha_num == 1:
            self.player = Tofu()
        elif gacha_num == 2:
            self.player = Onigiri()
        elif gacha_num == 3:
            self.player = iTunesCard()
        elif gacha_num == 4:
            self.player = Ika()
        elif gacha_num == 5:
            self.player = Kakun()
        elif gacha_num == 6:
            self.player = Pikachu()
        elif gacha_num == 7:
            self.player = Homuhomu()
        elif gacha_num == 8:
            self.player = Sushi()

    def ultraGacha(self):
        ultra_count = 1
        gacha_num = random.randint(1, ultra_count)
        if gacha_num == 1:
            self.player = CheetahMan()
