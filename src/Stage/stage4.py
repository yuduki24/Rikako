from Stage.stage import *

class Stage4(Stage):
    def deployEnemy(self):
        Boss2((self.scr_rect.width//2, 200))