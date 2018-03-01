from Stage.stage1 import *

class GameManager():
    stageNumber = 1
    def __init__(self, render):
        self.createStage(render)
    def update(self):
        pass
    def createStage(self, render):
        if self.stageNumber == 1:
            self.stage = Stage1()
        self.stage.deployEnemy(render)