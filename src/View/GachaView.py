from View.view import *

BEFORE_GACHA, AFTER_GACHA = 0, 1

class GachaView(View):
    def __init__(self, scr_rect):
        super().__init__(scr_rect)
        self.screen.fill(WHITE)
        self.gachaState = BEFORE_GACHA
    def draw(self):
        # TODO:ガチャのアニメーション
        if self.gachaState == BEFORE_GACHA:
            self.screen.fill(WHITE)
            text = getText("before_gacha", 100, BLACK)
        elif self.gachaState == AFTER_GACHA:
            self.screen.fill(GREEN)
            text = getText("after_gacha", 100, BLACK)
        self.screen.blit(text, (self.scr_rect.width//2 - text.get_width()//2, self.scr_rect.height//4))
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