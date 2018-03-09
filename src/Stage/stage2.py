from Stage.stage import *

class Stage2(Stage):
    def deployEnemy(self):
        for i in range(0, 10):
            x = 300 + int(i % 5) * 40
            y = 200 + int(i / 5) * 40
            Enemy1((x, y))