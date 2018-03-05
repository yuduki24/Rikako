from Enemy.enemy import *

class Stage():
    def __init__(self):
        pass
    def deployEnemy(self):
        for i in range(0, 10):
            x = 100 + int(i % 10) * 40
            y = 50 + int(i / 10) * 40
            enemy = Enemy((x, y))
        
    def update(self):
        pass