from Stage.stage1 import *

class GameManager():
    stageNumber = 1
    def __init__(self):
        self.createStage()
    def update(self):
        pass
    def createStage(self):
        if self.stageNumber == 1:
            self.stage = Stage1()
        self.stage.deployEnemy()