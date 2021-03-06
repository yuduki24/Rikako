from View.view import *

BUTTON_SIZE_W, BUTTON_SIZE_H = 200, 50
CONTINUE_BUTTON, END_BUTTON = 0, 1

class GameoverView(View):
    def __init__(self, player):
        super().__init__()
        self.screen.fill(BLACK)
        self.chooing_buton = CONTINUE_BUTTON
        self.player = player
        # ゲームタイトル.
        titleText = getText("GAME OVER", 75, RED)
        self.screen.blit(titleText, (self.scr_rect.width//2 - titleText.get_width()//2, self.scr_rect.height//4))
        self.updateButtonView()

    def draw(self):
        self.updateButtonView()
    
    def updateButtonView(self):
        if self.chooing_buton == CONTINUE_BUTTON:
            startButtonColor = RED
            quitButtonColor = WATER_BLUE
        elif self.chooing_buton == END_BUTTON:
            startButtonColor = WATER_BLUE
            quitButtonColor = RED
        # CONTINUEボタン.
        pygame.draw.rect(self.screen, startButtonColor, Rect(self.scr_rect.width//2 - BUTTON_SIZE_W//2, self.scr_rect.height//2 + 100, BUTTON_SIZE_W, BUTTON_SIZE_H))
        startText = getText("CONTINUE", 50, BLACK)
        self.screen.blit(startText, (self.scr_rect.width//2 - startText.get_width()//2, self.scr_rect.height//2 + BUTTON_SIZE_H//2 - startText.get_height()//2 + 100))
        # ENDボタン.
        pygame.draw.rect(self.screen, quitButtonColor, Rect(self.scr_rect.width//2 - BUTTON_SIZE_W//2, self.scr_rect.height//2 + 200, BUTTON_SIZE_W, BUTTON_SIZE_H))
        quitText = getText("END", 50, BLACK)
        self.screen.blit(quitText, (self.scr_rect.width//2 - quitText.get_width()//2, self.scr_rect.height//2 + BUTTON_SIZE_H//2 - quitText.get_height()//2 + 200))

    def key_handler(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_UP:
                self.chooing_buton = CONTINUE_BUTTON
            if event.type == KEYDOWN and event.key == K_DOWN:
                self.chooing_buton = END_BUTTON
            if event.type == KEYDOWN and event.key == K_RETURN:
                if self.chooing_buton == CONTINUE_BUTTON:
                    self.returnStatus = GameState.Wait
                elif self.chooing_buton == END_BUTTON:
                    self.player.kill()
                    self.returnStatus = GameState.Title
