from View.View import *

class GachaView(View):
    def __init__(self, scr_rect):
        super().__init__(scr_rect)
        pass
    def draw(self):
        self.screen.fill((200, 200, 200))