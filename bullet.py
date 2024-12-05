# bullet.py

import pygame
from settings import *

class Bullet(pygame.sprite.Sprite):
    def __init__(self, position, direction, shooter, last_shot_time=None):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect(center=position)
        self.direction = direction
        self.speed = BULLET_SPEED
        self.shooter = shooter
        self.last_shot_time = last_shot_time if last_shot_time else pygame.time.get_ticks()

    def update(self):
        self.rect.center += self.direction * self.speed
        if not (0 <= self.rect.x <= SCREEN_WIDTH and 0 <= self.rect.y <= SCREEN_HEIGHT):
            self.kill()

    def can_shoot_again(self):
        current_time = pygame.time.get_ticks()
        if (current_time - self.last_shot_time) > 400: 
            self.last_shot_time = current_time
            return True
        return False