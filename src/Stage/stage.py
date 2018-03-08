from Enemy.enemy import *
from Enemy.enemy1 import *
from Enemy.boss1 import *

class Stage():
    def __init__(self):
        self.deployEnemy()
    def deployEnemy(self):
        for i in range(0, 1):
            x = 100 + int(i % 10) * 40
            y = 50 + int(i / 10) * 40
            enemy = Enemy((x, y))
