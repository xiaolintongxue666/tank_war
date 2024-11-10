# tank.py

import pygame
from settings import *
from bullet import Bullet

class Tank(pygame.sprite.Sprite):
    def __init__(self, position, color, controls):
        super().__init__()
        self.image = pygame.Surface((50, 50), pygame.SRCALPHA)
        self.color = color
        self.rect = self.image.get_rect(center=position)
        self.speed = TANK_SPEED
        self.direction = pygame.math.Vector2(0, -1)
        self.controls = controls
        self.update_image()

    def update_image(self):
        self.image.fill((0, 0, 0, 0))  # 清空图像
        # 绘制坦克主体
        pygame.draw.rect(self.image, self.color, (5, 5, 40, 40))
        # 绘制坦克炮塔
        pygame.draw.circle(self.image, (0, 0, 0), (25, 25), 10)
        # 绘制炮管
        pygame.draw.polygon(self.image, (0, 0, 0), [
            (25 + self.direction.x * 20, 25 + self.direction.y * 20),  # 炮管末端
            (25 + self.direction.x * 15 - self.direction.y * 5, 25 + self.direction.y * 15 + self.direction.x * 5),  # 炮管左侧
            (25 + self.direction.x * 15 + self.direction.y * 5, 25 + self.direction.y * 15 - self.direction.x * 5)  # 炮管右侧
        ])

    def update(self, keys_pressed, walls):
        rotation = 0
        if keys_pressed[self.controls['left']]:
            rotation = 5
        if keys_pressed[self.controls['right']]:
            rotation = -5
        self.direction.rotate_ip(rotation)
        self.update_image()  # 更新图像以反映方向变化

        if keys_pressed[self.controls['up']]:
            new_position = self.rect.center + self.direction * self.speed
            if self.is_within_bounds(new_position) and not self.collides_with_walls(new_position, walls):
                self.rect.center = new_position
        if keys_pressed[self.controls['down']]:
            new_position = self.rect.center - self.direction * self.speed
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