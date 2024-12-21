# bullet.py

import pygame
from settings import *

class Bullet(pygame.sprite.Sprite):
    def __init__(self, position, direction, shooter, width):
        super().__init__()
        self.image = pygame.Surface((width, width))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect(center=position)
        self.direction = direction
        self.speed = BULLET_SPEED
        self.shooter = shooter

    def update(self):
        self.rect.center += self.direction * self.speed
        if not (0 <= self.rect.x <= SCREEN_WIDTH and 0 <= self.rect.y <= SCREEN_HEIGHT):
            self.kill()