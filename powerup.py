import pygame

import random

class Powerup(pygame.sprite.Sprite):
    def __init__(self, position, image, effect):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft=position)
        self.effect = effect  # 效果，例如 'speed_up', 'bullet_power_up' 等

    def apply_effect(self, tank):
        if self.effect == 'speed_up':
            tank.speed += 1

        elif self.effect == 'bullet_power_up':
            tank.bullet_power += 1

        elif self.effect == 'bullet_limit_increase':
            tank.bullet_limit += 1