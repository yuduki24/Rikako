from View.view import *

class WaitView(View):
    def __init__(self, player):
        super().__init__()
        self.screen.fill(GRAY)

        image = pygame.transform.scale(player.image, (160, 160))
        self.screen.blit(image, (50, 100))

        text = getText(player.RANK, 40, YELLOW)
        self.screen.blit(text, (10, 20))
        text = getText(player.NAME, 40, YELLOW)
        self.screen.blit(text, (80, 300))
        for i in range(len(player.BRIEF)):
            text = getText(player.BRIEF[i], 20, WHITE)
            self.screen.blit(text, (250, 100 + i*40))

        text = getText("Enterでスタート!", 20, BLACK, WHITE)
        self.screen.blit(text, (600, 550))
    def key_handler(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_RETURN:
                self.returnStatus = GameState.Play