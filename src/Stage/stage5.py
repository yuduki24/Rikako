from Stage.stage import *

class Stage5(Stage):
    def deployEnemy(self):
        for i in range(0, 10):
            x = 50 + int(i % 5) * 40
            y = 200 + int(i / 5) * 40
            Enemy1((x, y))
        for i in range(0, 10):
            x = 500 + int(i % 5) * 40
            y = 200 + int(i / 5) * 40
            Enemy1((x, y))
        for i in range(0, 10):
            x = int(i % 5) * 40
            Enemy((self.scr_rect.width//2 + x, self.scr_rect.height*3//4))
        Boss3((self.scr_rect.width//2, 200))