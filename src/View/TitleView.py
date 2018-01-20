from View.View import *

class TitleView(View):
    def __init__(self, scr_rect):
        super().__init__(scr_rect)
        pass
    def draw(self, screen):
        self.screen.fill((225, 5, 5))