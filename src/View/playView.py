from View.view import *
from gameManager import *

from Player.player import *

class PlayView(View):
    def __init__(self, scr_rect, player):
        super().__init__(scr_rect)
        self.screen.fill(BLACK)
        self.player = player

        self.all = pygame.sprite.RenderUpdates()
        Shot.containers = self.all
        self.player.containers = self.all
        self.player.initialise(scr_rect)
        self.gameManager = GameManager(self.all)
    def main(self):
        # これをやるといい感じにできる.
        # self.all.clear(self.screen, Surface)
        self.screen.fill(BLACK)
        
        self.key_handler()
        self.gameManager.update()
        self.draw()
        pygame.display.update()
        return self.returnStatus
    def draw(self):
        self.all.update()
        self.all.draw(self.screen)
    def key_handler(self):
        pressed_keys = pygame.key.get_pressed()
        self.player.move(pressed_keys)
        if pressed_keys[K_SPACE]:
            Shot(self.player.getPossition())
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
