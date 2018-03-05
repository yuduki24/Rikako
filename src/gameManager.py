from Stage.stage1 import *

class GameManager():
    stageNumber = 1
    def __init__(self, player):
        self.player = player
        self.createStage()
    def update(self):
        self.all.update()
        self.all.draw(self.screen)
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
        beam_collided = pygame.sprite.spritecollide(self.player, self.beams, True)
        if beam_collided:  # プレイヤーと衝突したビームがあれば
            self.player.kill()