from Stage.stage1 import *

class GameManager():
    stageNumber = 1
    def __init__(self):
        self.createStage()
    def update(self):
        self.collisionDetection()
    def createStage(self):
        if self.stageNumber == 1:
            self.stage = Stage1()
        self.stage.deployEnemy()
    def collisionDetection(self):
        enemy_collided = pygame.sprite.groupcollide(self.enemyGroup, self.shotGroup, True, True)
        for enemy in enemy_collided.keys():
            # 爆発音.
            # 爆発エフェクトself.
            pass
        