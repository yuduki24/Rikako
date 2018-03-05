import pygame
from pygame.locals import *

from Util.loader import *

class Player(pygame.sprite.Sprite):
    speed = 2
    reload_time = 20
    NAME = "初号機"
    RANK = "ノーマル"
    BRIEF = ["適当にペイントで作成した初号機", "何の変哲もない。", "最近太ってしまったせいか、動くのがとても遅い"]
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        # self.rect = self.image.get_rect(midbottom=pos)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.reload_timer = 0
    def execEvent(self, pressed_keys):
        self.move(pressed_keys)
        
        self.reload_timer -= 1
        if pressed_keys[K_SPACE]:
            if self.reload_timer < 0:
                self.shot()
                self.reload_timer = self.reload_time
    def move(self, pressed_keys):
        direction_x = pressed_keys[K_RIGHT] - pressed_keys[K_LEFT]
        direction_y = pressed_keys[K_DOWN] - pressed_keys[K_UP]
        if (direction_x < 0 and self.rect.left < 30) or (direction_x > 0 and self.rect.right > self.scr_rect.right-30):
            direction_x = 0
        if (direction_y < 0 and self.rect.top < self.scr_rect.height*3//4) or (direction_y > 0 and self.rect.bottom > self.scr_rect.bottom-30):
            direction_y = 0
        self.rect.move_ip(direction_x*self.speed, direction_y*self.speed)
        # self.rect.clamp_ip(self.scr_rect)
    def shot(self):
        Shot((self.rect.centerx, self.rect.top))


class Shot(pygame.sprite.Sprite):
    speed = -11
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.rect = self.image.get_rect(midbottom=pos)
    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top <= 0:
            self.kill()