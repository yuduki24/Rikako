from View.View import *

BEFORE_GACHA, AFTER_GACHA = 0, 1

class GachaView(View):
    def __init__(self, scr_rect):
        super().__init__(scr_rect)
        self.gachaState = BEFORE_GACHA
    def draw(self):
        # TODO:ガチャのアニメーション
        if self.gachaState == BEFORE_GACHA:
            self.screen.fill((200, 200, 200))
        elif self.gachaState == AFTER_GACHA:
            self.screen.fill((20, 200, 20))
    def key_handler(self):
        # TODO:Enterで抜けるようにしてる
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_RETURN:
                if self.gachaState == BEFORE_GACHA:
                    self.gachaState = AFTER_GACHA
                elif self.gachaState == AFTER_GACHA:
                    self.returnStatus = GameState.Wait