from Stage.stage1 import *

PLAY, GAMEOVER, GAMECLEAR = (0, 1, 2)

class GameManager():
    stageNumber = 1
    def __init__(self, player):
        self.player = player
        self.createStage()
        self.state = PLAY
    def update(self):
        self.all.update()
        self.all.draw(self.screen)
        self.collisionDetection()
        if len(self.enemyGroup.sprites()) == 0:
            self.state = GAMECLEAR
        return self.state
    def createStage(self):
        if self.stageNumber == 1:
            self.stage = Stage()
    def collisionDetection(self):
        enemy_collided = pygame.sprite.groupcollide(self.enemyGroup, self.shotGroup, True, True)
        for enemy in enemy_collided.keys():
            # 爆発音.
            # 爆発エフェクトself.
            pass
        beam_collided = pygame.sprite.spritecollide(self.player, self.beamGroup, True)
        if beam_collided:  # プレイヤーと衝突したビームがあれば
            self.player.kill()
            self.state = GAMEOVER
    def reset(self):
        self.player.kill()
        self.enemyGroup.empty()
        self.shotGroup.empty()
        self.beamGroup.empty()
        self.all.update()
        pass