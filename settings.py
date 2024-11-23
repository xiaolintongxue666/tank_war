# settings.py
import pygame
TANK_SPEED = 5
BULLET_SPEED = 10
# 配置文件
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BG_COLOR = (255, 255, 255)

TANK1_CONTROLS = {
    'left': pygame.K_a,
    'right': pygame.K_d,
    'up': pygame.K_w,
    'down': pygame.K_s,
    'shoot': pygame.K_SPACE,
}

TANK2_CONTROLS = {
    'left': pygame.K_LEFT,
    'right': pygame.K_RIGHT,
    'up': pygame.K_UP,
    'down': pygame.K_DOWN,
    'shoot': pygame.K_RETURN,
}

WALL_POSITIONS = [
    ((400, 250), (100, 200)),
    ((200, 150), (100, 100)),
    ((600, 150), (100, 100)),
    ((200, 450), (100, 100)),
    ((600, 450), (100, 100)),
    ((350, 300), (300, 100)),
    ((400, 200), (100, 300)),
]

