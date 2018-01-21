from View.View import *
from GameManager import *

class PlayView(View):
    def __init__(self, scr_rect, player):
        super().__init__(scr_rect)
        self.player = player

        self.all = pygame.sprite.RenderUpdates()
        self.player.containers = self.all
        self.player.initialise(scr_rect)
        self.gameManager = GameManager(self.all)
    def main(self):
        self.gameManager.update()
        self.draw()
        pygame.display.update()
        self.key_handler()
        return self.returnStatus
    def draw(self):
        self.screen.fill((20, 20, 20))
        self.all.update()
        self.all.draw(self.screen)
    def key_handler(self):
        pressed_keys = pygame.key.get_pressed()
        self.player.move(pressed_keys)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
