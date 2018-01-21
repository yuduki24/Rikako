from View.View import *

class PlayView(View):
    def __init__(self, scr_rect, player):
        super().__init__(scr_rect)
        self.player = player

        self.all = pygame.sprite.RenderUpdates()
        self.player.containers = self.all
        self.player.initialise(scr_rect)
        
        self.screen.fill((20, 20, 20))

    def draw(self):
        self.all.update()
        self.all.draw(self.screen)
    def key_handler(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
