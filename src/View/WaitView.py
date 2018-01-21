from View.View import *

class WaitView(View):
    def __init__(self, scr_rect):
        super().__init__(scr_rect)
    def draw(self):
        # TODO:ガチャで出たキャラの説明など
        self.screen.fill((20, 20, 200))
    def key_handler(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_RETURN:
                self.returnStatus = GameState.Play