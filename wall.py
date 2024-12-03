# wall.py

import pygame
import random

class Wall(pygame.sprite.Sprite):
    def __init__(self,position,size,color,HP=4):
        super().__init__()
        self.HP = HP
        self.image = pygame.Surface(size)
        self.color = color
          #千万注意，self.color先从元组变为list最后还要变成tuple，不然会导致self.color在各个instance间共享
        if self.HP != -1:
            self.change_color_by_HP()
        self.image.fill(self.color)
        self.rect = self.image.get_rect(topleft=position)

    def update_hit(self):
        if self.HP != -1:
            self.HP -= 1
            self.change_color_by_HP()
            if self.HP == 0:
                self.kill()
    
    def change_color_by_HP(self):
        self.color = list(self.color)
        for i in range(3):
                _ = self.color[i] + 20 * self.HP
                if _ < 200:
                    self.color[i] = _
                else:
                    self.color[i] = 200
        self.color = tuple(self.color)
        self.image.fill(self.color)