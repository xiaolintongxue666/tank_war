# wall.py

import pygame
import random

class Wall(pygame.sprite.Sprite):
    def __init__(self,position,size,color):
        super().__init__()
        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=position)