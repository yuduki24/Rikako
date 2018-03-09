from Stage.stage1 import *
from Stage.stage2 import *
from Stage.stage3 import *
from Stage.stage4 import *
from Stage.stage5 import *
PLAY, GAMEOVER, GAMECLEAR = (0, 1, 2)

class GameManager():
    stageNumber = 1
    def __init__(self, player):
        self.player = player
        self.createStage()
    def update(self):
        self.all.update()
        self.all.draw(self.screen)
        if len(self.enemyGroup.sprites()) == 0:
            self.reset()
            self.state = GAMECLEAR
        self.collisionDetection()
        return self.state
    def createStage(self):
        if self.stageNumber == 1:
            self.stage = Stage1()
        elif self.stageNumber == 2:
            self.stage = Stage2()
        elif self.stageNumber == 3:
            self.stage = Stage3()
        elif self.stageNumber == 4:
            self.stage = Stage4()
        elif self.stageNumber == 5:
            self.stage = Stage5()
        else:
            self.stage = Stage()
        self.state = PLAY
    def collisionDetection(self):
        enemy_collided = pygame.sprite.groupcollide(self.enemyGroup, self.shotGroup, False, True)
        for enemy, shot in enemy_collided.items():
            enemy.damage(shot[0].power)
            # 爆発音.
            # 爆発エフェクトself.
        player_collided = pygame.sprite.groupcollide(self.playerGroup, self.beamGroup, False, True)
        for player, beam in player_collided.items():
            if player.damage(beam[0].power):
                self.reset()
                self.state = GAMEOVER
    def reset(self):
        self.player.reset()
        for sprite in self.enemyGroup.sprites():
            sprite.kill()
        for sprite in self.shotGroup.sprites():
            sprite.kill()
        for sprite in self.beamGroup.sprites():
            sprite.kill() 
        # self.enemyGroup.empty()
        # self.shotGroup.empty()
        # self.beamGroup.empty()
        self.all.update()
