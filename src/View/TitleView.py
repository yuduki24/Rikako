from View.View import *
BUTTON_SIZE_W, BUTTON_SIZE_H = 200, 50

class TitleView(View):
    def __init__(self, scr_rect):
        super().__init__(scr_rect)
        self.screen.fill((50, 50, 50))

        # ゲームタイトル.
        titleFont = pygame.font.SysFont(None, 100)
        titleText = titleFont.render("my shooooooooting", True, (255,0,0))
        self.screen.blit(titleText, (self.scr_rect.width//2 - titleText.get_width()//2, self.scr_rect.height//4))
        
        buttonFont = pygame.font.SysFont(None, 50)
        # STARTボタン.
        startText = buttonFont.render("START", True, (0,0,0))
        pygame.draw.rect(self.screen, (0, 255, 255), Rect(self.scr_rect.width//2 - BUTTON_SIZE_W//2, self.scr_rect.height//2 - BUTTON_SIZE_H//2 + 100, BUTTON_SIZE_W, BUTTON_SIZE_H))
        self.screen.blit(startText, (self.scr_rect.width//2 - startText.get_width()//2, self.scr_rect.height//2 - startText.get_height()//2 + 100))
        # QUITボタン.
        quitText = buttonFont.render("QUIT", True, (0,0,0))
        pygame.draw.rect(self.screen, (0, 255, 255), Rect(self.scr_rect.width//2 - BUTTON_SIZE_W//2, self.scr_rect.height//2 - BUTTON_SIZE_H//2 + 200, BUTTON_SIZE_W, BUTTON_SIZE_H))
        self.screen.blit(quitText, (self.scr_rect.width//2 - quitText.get_width()//2, self.scr_rect.height//2 - quitText.get_height()//2 + 200))
        pass
    def draw(self, screen):
        pass
        
        