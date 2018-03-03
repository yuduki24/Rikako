from View.view import *

class WaitView(View):
    def __init__(self):
        super().__init__()
    def draw(self):
        # TODO:ガチャで出たキャラの説明など
        self.screen.fill(BLUE)
        text = getText("wait", 100, BLACK)
        self.screen.blit(text, (self.scr_rect.width//2 - text.get_width()//2, self.scr_rect.height//4))
    def key_handler(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_RETURN:
                self.returnStatus = GameState.Play