from View.view import *
from gameManager import *

from Player.player import *

import time

BUTTON_SIZE_W, BUTTON_SIZE_H = 200, 50
NEXT_BUTTON, END_BUTTON = 0, 1

class PlayView(View):
    def __init__(self, player):
        super().__init__()
        self.screen.fill(BLACK)
        self.chooing_buton = NEXT_BUTTON
        self.player = player
        self.gameManager = GameManager(self.player)
        self.gameState = PLAY
        self.stime = time.time()
    def main(self):
        # これをやるといい感じにできる.
        # self.all.clear(self.screen, Surface)
        self.draw()
        
        self.key_handler()
        if self.gameState == PLAY:
            self.gameState = self.gameManager.update()
        elif self.gameState == GAMEOVER:
            self.returnStatus = GameState.Gameover
        return self.returnStatus
    def draw(self):
        self.screen.fill(PLAY_COLOR)
        if self.gameState == PLAY:
            # 残機とか体力とかスコアとか.
            # プレイ時間.
            self.result = time.time() - self.stime
            result = int(self.result * 100)
            text = getText("{:.2f}".format(result/100), 30, WHITE)
            self.screen.blit(text, (self.scr_rect.width - text.get_width() - 5, self.scr_rect.height - text.get_height() - 5))
            # 体力
            
            text = getText(str(self.player.hp), 30, WHITE)
            self.screen.blit(text, (150, self.scr_rect.height - text.get_height() - 5))
            pygame.draw.rect(self.screen, YELLOW, Rect(30, self.scr_rect.height - text.get_height() - 5, 100 * self.player.hp / self.player.hp_max, 30))
            
        elif self.gameState == GAMECLEAR:
            titleText = getText("CLEAR", 75, YELLOW)
            self.screen.blit(titleText, (self.scr_rect.width//2 - titleText.get_width()//2, self.scr_rect.height//4))
            self.updateButtonView()
    def updateButtonView(self):
        if self.chooing_buton == NEXT_BUTTON:
            startButtonColor = RED
            quitButtonColor = WATER_BLUE
        elif self.chooing_buton == END_BUTTON:
            startButtonColor = WATER_BLUE
            quitButtonColor = RED
        # STARTボタン.
        pygame.draw.rect(self.screen, startButtonColor, Rect(self.scr_rect.width//2 - BUTTON_SIZE_W//2, self.scr_rect.height//2 + 100, BUTTON_SIZE_W, BUTTON_SIZE_H))
        startText = getText("NEXT", 50, BLACK)
        self.screen.blit(startText, (self.scr_rect.width//2 - startText.get_width()//2, self.scr_rect.height//2 + BUTTON_SIZE_H//2 - startText.get_height()//2 + 100))
        # QUITボタン.
        pygame.draw.rect(self.screen, quitButtonColor, Rect(self.scr_rect.width//2 - BUTTON_SIZE_W//2, self.scr_rect.height//2 + 200, BUTTON_SIZE_W, BUTTON_SIZE_H))
        quitText = getText("END", 50, BLACK)
        self.screen.blit(quitText, (self.scr_rect.width//2 - quitText.get_width()//2, self.scr_rect.height//2 + BUTTON_SIZE_H//2 - quitText.get_height()//2 + 200))
    def key_handler(self):
        pressed_keys = pygame.key.get_pressed()
        if self.gameState == PLAY:
            self.player.execEvent(pressed_keys)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if self.gameState == PLAY:
                if event.type == KEYDOWN and event.key == K_q:
                    self.gameManager.reset()
                    self.gameState = GAMEOVER
            elif self.gameState == GAMECLEAR:
                if event.type == KEYDOWN and event.key == K_UP:
                    self.chooing_buton = NEXT_BUTTON
                if event.type == KEYDOWN and event.key == K_DOWN:
                    self.chooing_buton = END_BUTTON
                if event.type == KEYDOWN and event.key == K_RETURN:
                    if self.chooing_buton == NEXT_BUTTON:
                        self.returnStatus = GameState.Pass
                        self.gameManager.stageNumber += 1
                        self.gameManager.createStage()
                        self.gameState = PLAY
                    elif self.chooing_buton == END_BUTTON:
                        self.player.kill()
                        self.returnStatus = GameState.Title