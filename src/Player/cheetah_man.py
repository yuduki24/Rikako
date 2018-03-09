import pygame
from pygame.locals import *

from Player.player import *

from Util.loader import *

class CheetahMan(Player):
    speed = 10
    hp_max = 1000
    reload_time = 2
    NAME = "チーターマン"
    RANK = "ウルトラレア"
    BRIEF = ["チーターマン 俺ってチーター", "チーターマン オレオレってチーター", "チーターマン 俺ってチーター", "チーターマン 俺達ってチーター", "この俺こそチーターマン", "この俺こそチーターマン", "走り続ける バグにも負けず", "俺正義のヒーロー 誰にも負けないぜ"]
    def __init__(self):
        self.pos = (self.scr_rect.width//2, self.scr_rect.height-120)
        super().__init__()
        self.image = self.images[0]
    def shot(self):
        SilverBullet((self.rect.centerx, self.rect.top))
    def move(self, pressed_keys):
        direction_x = pressed_keys[K_RIGHT] - pressed_keys[K_LEFT]
        direction_y = pressed_keys[K_DOWN] - pressed_keys[K_UP]
        if direction_x < 0:
            self.image = self.images[1]
        elif direction_x > 0:
            self.image = self.images[0]

        if (direction_x < 0 and self.rect.left < 30) or (direction_x > 0 and self.rect.right > self.scr_rect.right-30):
            direction_x = 0
        if (direction_y < 0 and self.rect.top < self.scr_rect.height*3//4) or (direction_y > 0 and self.rect.bottom > self.scr_rect.bottom-50):
            direction_y = 0
        self.rect.move_ip(direction_x*self.speed, direction_y*self.speed)
        # self.rect.clamp_ip(self.scr_rect)
class SilverBullet(Shot):
    speed = -30
    power = 50
    def __init__(self, pos):
        super().__init__(pos)
        
