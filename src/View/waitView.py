from View.view import *

class WaitView(View):
    def __init__(self):
        super().__init__()
    def draw(self):
        # TODO:ガチャで出たキャラの説明など
        self.screen.fill(BLUE)
        text = getText("待機画面", 30, BLACK)
        self.screen.blit(text, (0, 0))
    def key_handler(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_RETURN:
                self.returnStatus = GameState.Play