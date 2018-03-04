from View.view import *

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
                    self.playerID = self.gacha()
                    print(self.playerID)
                    self.returnStatus = GameState.Wait
    def gacha(self):
        # ガチャの種類によって変える.
        num = 0
        if random.randint(1,100) > 50:
            num = 1
        return num