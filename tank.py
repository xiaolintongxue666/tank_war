# tank.py

import pygame
from settings import *
from bullet import Bullet

class Tank(pygame.sprite.Sprite):
    def __init__(self, position, image_path, controls):
        super().__init__()
        self.original_image = pygame.image.load(image_path).convert_alpha()
        self.original_image = pygame.transform.scale(self.original_image, (50, 50))  # 缩放图片
        self.image = self.original_image
        self.rect = self.image.get_rect(center=position)
        self.speed = TANK_SPEED
        self.direction = pygame.math.Vector2(0, -1)
        self.controls = controls

    def update_image(self):
        angle = self.direction.angle_to(pygame.math.Vector2(0, -1))  # 修正角度
        self.image = pygame.transform.rotate(self.original_image, angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def update(self, keys_pressed, walls):
        moved = False
        if keys_pressed[self.controls['left']]:
            self.direction = pygame.math.Vector2(-1, 0)
            moved = True
        elif keys_pressed[self.controls['right']]:
            self.direction = pygame.math.Vector2(1, 0)
            moved = True
        elif keys_pressed[self.controls['up']]:
            self.direction = pygame.math.Vector2(0, -1)
            moved = True
        elif keys_pressed[self.controls['down']]:
            self.direction = pygame.math.Vector2(0, 1)
            moved = True

        if moved:
            self.update_image()  # 更新图像以反映方向变化
            new_position = self.rect.center + self.direction * self.speed
            if self.is_within_bounds(new_position) and not self.collides_with_walls(new_position, walls):
                self.rect.center = new_position

    def is_within_bounds(self, position):
        x, y = position
        return 0 <= x <= SCREEN_WIDTH and 0 <= y <= SCREEN_HEIGHT

    def collides_with_walls(self, position, walls):
        temp_rect = self.rect.copy()
        temp_rect.center = position
        return any(temp_rect.colliderect(wall.rect) for wall in walls)

    def shoot(self):
        return Bullet(self.rect.center, self.direction, self)
