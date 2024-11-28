# settings.py
import pygame
TANK_SPEED = 5
BULLET_SPEED = 10
# 配置文件
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BG_COLOR = (255, 255, 255)
BULLET_LIMIT = 3

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
    ((SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 - 100), (100, 200)),
    ((SCREEN_WIDTH // 4 - 50, SCREEN_HEIGHT // 4 - 50), (100, 100)),
    ((3 * SCREEN_WIDTH // 4 - 50, SCREEN_HEIGHT // 4 - 50), (100, 100)),
    ((SCREEN_WIDTH // 4 - 50, 3 * SCREEN_HEIGHT // 4 - 50), (100, 100)),
    ((3 * SCREEN_WIDTH // 4 - 50, 3 * SCREEN_HEIGHT // 4 - 50), (100, 100)),
    ((SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 50), (300, 100)),
    ((SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 - 150), (100, 300)),
]

WALL_POSITIONS1 = [
    ((100, 100), (200, 50)),  # 左上角
    ((SCREEN_WIDTH - 300, 100), (200, 50)),  # 右上角
    ((100, SCREEN_HEIGHT - 150), (200, 50)),  # 左下角
    ((SCREEN_WIDTH - 300, SCREEN_HEIGHT - 150), (200, 50)),  # 右下角
    ((SCREEN_WIDTH // 2 - 40, SCREEN_HEIGHT // 2 - 100), (90, 200)),  # 中心
    ((SCREEN_WIDTH // 4 - 50, SCREEN_HEIGHT // 4 - 50), (100, 100)),  # 左上
    ((3 * SCREEN_WIDTH // 4 - 50, SCREEN_HEIGHT // 4 - 50), (100, 100)),  # 右上
    ((SCREEN_WIDTH // 4 - 50, 3 * SCREEN_HEIGHT // 4 - 50), (100, 100)),  # 左下
    ((3 * SCREEN_WIDTH // 4 - 50, 3 * SCREEN_HEIGHT // 4 - 50), (100, 100)),  # 右下
]

WALL_POSITIONS2 = [((250, 0), (50, 50)), ((550, 0), (50, 50)),
                    ((250, 50), (50, 50)), ((550, 50), (50, 50)), ((700, 100), (50, 50)), 
                    ((650, 150), (50, 50)), ((250, 200), (50, 50)), ((450, 200), (50, 50)),
                      ((650, 200), (50, 50)), ((450, 250), (50, 50)), ((250, 300), (50, 50)),
                        ((450, 300), (50, 50)), ((600, 400), (50, 50)), ((100, 450), (50, 50)),
                          ((350, 450), (50, 50)), ((50, 500), (50, 50)), ((300, 500), (50, 50)),
                            ((0, 550), (50, 50)), ((250, 550), (50, 50)), ((600, 550), (50, 50))]

MAP_POOL = [WALL_POSITIONS, WALL_POSITIONS1, WALL_POSITIONS2] # 地图池