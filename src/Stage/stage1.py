from Stage.stage import *

class Stage1(Stage):
    def deployEnemy(self):
        jodan = 100
        gedan = 200
        center = self.scr_rect.width//2
        Enemy((center, gedan))
        Enemy((center+25, jodan))
        Enemy((center+50, gedan))
        Enemy((center-25, jodan))
        Enemy((center-50, gedan))
