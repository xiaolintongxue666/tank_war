# wall.py

import pygame
import random

class Wall(pygame.sprite.Sprite):
    def __init__(self, position, size):
        super().__init__()
        self.image = pygame.Surface(size)
        a,b,c = random.randint(1,128),random.randint(1,128),random.randint(1,128)
        self.image.fill((a, b, c))
        self.rect = self.image.get_rect(topleft=position)