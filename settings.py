# settings.py
import pygame
TANK_SPEED = 5
BULLET_SPEED = 10
BULLET_POWER = 1
TANK_HP = 3
POWERUP_NUMBER = 10
# 配置文件
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BG_COLOR = (255, 255, 255)
BULLET_LIMIT = 1
GLOBAL_VOLUME = 1 # 全局音量大小，在0到1之间

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

WALL_POSITIONS = [((150, 100), (40, 40)), ((200, 100), (40, 40)), ((550, 100), (40, 40)), ((600, 100), (40, 40)), ((150, 150), (40, 40)), ((200, 150), (40, 40)), ((350, 150), (40, 40)), ((400, 150), (40, 40)), ((550, 150), (40, 40)), ((600, 150), (40, 40)), ((350, 200), (40, 40)), ((400, 200), (40, 40)), ((250, 250), (40, 40)), ((300, 250), (40, 40)), ((350, 250), (40, 40)), ((400, 250), (40, 40)), ((450, 250), (40, 40)), ((500, 250), (40, 40)), ((250, 300), (40, 40)), ((300, 300), (40, 40)), ((350, 300), (40, 40)), ((400, 300), (40, 40)), ((450, 300), (40, 40)), ((500, 300), (40, 40)), ((350, 350), (40, 40)), ((400, 350), (40, 40)), ((150, 400), (40, 40)), ((200, 400), (40, 40)), ((350, 400), (40, 40)), ((400, 400), (40, 40)), ((550, 400), (40, 40)), ((600, 400), (40, 40)), ((150, 450), (40, 40)), ((200, 450), (40, 40)), ((550, 450), (40, 40)), ((600, 450), (40, 40))]

WALL_POSITIONS1 = [((100, 100), (40, 40)), ((150, 100), (40, 40)), ((200, 100), (40, 40)), ((550, 100), (40, 40)), ((600, 100), (40, 40)), ((650, 100), (40, 40)), ((150, 150), (40, 40)), ((600, 150), (40, 40)), ((350, 200), (40, 40)), ((400, 200), (40, 40)), ((350, 250), (40, 40)), ((400, 250), (40, 40)), ((350, 300), (40, 40)), ((400, 300), (40, 40)), ((350, 350), (40, 40)), ((400, 350), (40, 40)), ((150, 400), (40, 40)), ((600, 400), (40, 40)), ((100, 450), (40, 40)), ((150, 450), (40, 40)), ((200, 450), (40, 40)), ((550, 450), (40, 40)), ((600, 450), (40, 40)), ((650, 450), (40, 40))]

WALL_POSITIONS2 = [((250, 0), (40, 40)), ((550, 0), (40, 40)),
                   ((250, 50), (40, 40)), ((550, 50), (40, 40)), ((700, 100), (40, 40)), 
                   ((650, 150), (40, 40)), ((250, 200), (40, 40)), ((450, 200), (40, 40)),
                   ((650, 200), (40, 40)), ((450, 250), (40, 40)), ((250, 300), (40, 40)),
                   ((450, 300), (40, 40)), ((600, 400), (40, 40)), ((100, 450), (40, 40)),
                   ((350, 450), (40, 40)), ((50, 500), (40, 40)), ((300, 500), (40, 40)),
                   ((0, 550), (40, 40)), ((250, 550), (40, 40)), ((600, 550), (40, 40))]

WALL_POSITIONS3 = [((350, 100), (40, 40)), ((400, 100), (40, 40)), ((100, 150), (40, 40)), ((150, 150), (40, 40)), ((350, 150), (40, 40)), ((400, 150), (40, 40)), ((600, 150), (40, 40)), ((650, 150), (40, 40)), ((150, 200), (40, 40)), ((600, 200), (40, 40)), ((150, 250), (40, 40)), ((350, 250), (40, 40)), ((400, 250), (40, 40)), ((600, 250), (40, 40)), ((150, 300), (40, 40)), ((350, 300), (40, 40)), ((400, 300), (40, 40)), ((600, 300), (40, 40)), ((150, 350), (40, 40)), ((600, 350), (40, 40)), ((100, 400), (40, 40)), ((150, 400), (40, 40)), ((350, 400), (40, 40)), ((400, 400), (40, 40)), ((600, 400), (40, 40)), ((650, 400), (40, 40)), ((350, 450), (40, 40)), ((400, 450), (40, 40))]
MAP_POOL = [WALL_POSITIONS, WALL_POSITIONS1, WALL_POSITIONS2, WALL_POSITIONS3]  # 地图池
