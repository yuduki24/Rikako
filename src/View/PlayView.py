from View.View import *

class PlayView(View):
    def __init__(self, scr_rect):
        super().__init__(scr_rect)
    def draw(self):
        self.screen.fill((20, 20, 20))
    def key_handler(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
