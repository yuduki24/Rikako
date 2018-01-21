from Enemy.enemy import *

class Stage():
    def __init__(self):
        pass
    def deployEnemy(self, render):
        self.enemy = Enemy()
        self.enemy.containers = render
        self.enemy.initialise()
    def update(self):
        pass