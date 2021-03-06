from View.view import *

BUTTON_SIZE_W, BUTTON_SIZE_H = 200, 50
START_BUTTON, QUIT_BUTTON = 0, 1

class TitleView(View):
    def __init__(self):
        super().__init__()
        self.chooing_buton = START_BUTTON
        self.fullscreen_flag = False
        self.draw()
    def draw(self):
        self.screen.fill(GRAY)
        # ゲームタイトル.
        titleText = getText("BAN BANG", 100, RED)
        self.screen.blit(titleText, (self.scr_rect.width//2 - titleText.get_width()//2, self.scr_rect.height//4))
        # 操作説明
        titleText = getText("移動：十字キー", 20, WHITE)
        self.screen.blit(titleText, (self.scr_rect.width//2+100, self.scr_rect.height//4 + 125))
        titleText = getText("撃つ：スペースキー", 20, WHITE)
        self.screen.blit(titleText, (self.scr_rect.width//2+100, self.scr_rect.height//4 + 150))
        titleText = getText("決定：エンターキー", 20, WHITE)
        self.screen.blit(titleText, (self.scr_rect.width//2+100, self.scr_rect.height//4 + 175))
        titleText = getText("自爆：Qキー", 20, WHITE)
        self.screen.blit(titleText, (self.scr_rect.width//2+100, self.scr_rect.height//4 + 200))
        titleText = getText("フルスクリーン：F2キー", 20, WHITE)
        self.screen.blit(titleText, (self.scr_rect.width//2+100, self.scr_rect.height//4 + 225))
        self.updateButtonView()
    def updateButtonView(self):
        if self.chooing_buton == START_BUTTON:
            startButtonColor = RED
            quitButtonColor = WATER_BLUE
        elif self.chooing_buton == QUIT_BUTTON:
            startButtonColor = WATER_BLUE
            quitButtonColor = RED
        # STARTボタン.
        pygame.draw.rect(self.screen, startButtonColor, Rect(self.scr_rect.width//2 - BUTTON_SIZE_W//2, self.scr_rect.height//2 + 100, BUTTON_SIZE_W, BUTTON_SIZE_H))
        startText = getText("START", 50, BLACK)
        self.screen.blit(startText, (self.scr_rect.width//2 - startText.get_width()//2, self.scr_rect.height//2 + BUTTON_SIZE_H//2 - startText.get_height()//2 + 100))
        # QUITボタン.
        pygame.draw.rect(self.screen, quitButtonColor, Rect(self.scr_rect.width//2 - BUTTON_SIZE_W//2, self.scr_rect.height//2 + 200, BUTTON_SIZE_W, BUTTON_SIZE_H))
        quitText = getText("QUIT", 50, BLACK)
        self.screen.blit(quitText, (self.scr_rect.width//2 - quitText.get_width()//2, self.scr_rect.height//2 + BUTTON_SIZE_H//2 - quitText.get_height()//2 + 200))
    def key_handler(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_UP:
                self.chooing_buton = START_BUTTON
            if event.type == KEYDOWN and event.key == K_DOWN:
                self.chooing_buton = QUIT_BUTTON
            if event.type == KEYDOWN and event.key == K_RETURN:
                if self.chooing_buton == START_BUTTON:
                    self.returnStatus = GameState.Gacha
                elif self.chooing_buton == QUIT_BUTTON:
                    self.returnStatus = GameState.Quit
            if event.type == KEYDOWN and event.key == K_F2:
                # F2キーでフルスクリーンモードへの切り替え
                self.fullscreen_flag = not self.fullscreen_flag
                if self.fullscreen_flag:
                    self.screen = pygame.display.set_mode(self.scr_rect.size, FULLSCREEN, 32)
                else:
                    self.screen = pygame.display.set_mode(self.scr_rect.size, 0, 32)