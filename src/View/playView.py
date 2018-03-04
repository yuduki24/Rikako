from View.view import *
from gameManager import *

from Player.player import *

class PlayView(View):
    def __init__(self, player):
        super().__init__()
        self.screen.fill(BLACK)
        self.player = player
        self.gameManager = GameManager()
    def main(self):
        # これをやるといい感じにできる.
        # self.all.clear(self.screen, Surface)
        self.screen.fill(BLACK)
        
        self.key_handler()
        self.gameManager.update()
        return self.returnStatus
    def draw(self):
        pass
    def key_handler(self):
        pressed_keys = pygame.key.get_pressed()
        self.player.execEvent(pressed_keys)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
