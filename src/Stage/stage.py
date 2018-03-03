from Enemy.enemy import *

class Stage():
    def __init__(self):
        pass
    def deployEnemy(self, render):
        for i in range(0, 50):
            x = 300 + int(i % 10) * 40
            y = 60 + int(i / 10) * 40
            enemy = Enemy()
            enemy.containers = render
            enemy.initialise((x, y))
        
    def update(self):
        pass