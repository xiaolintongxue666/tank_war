import pygame
from settings import *
from tank import Tank
from bullet import Bullet
from wall import Wall

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tank War")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 74)

tank1_controls = {
    'left': pygame.K_a,
    'right': pygame.K_d,
    'up': pygame.K_w,
    'down': pygame.K_s,
    'shoot': pygame.K_SPACE
}

tank2_controls = {
    'left': pygame.K_LEFT,
    'right': pygame.K_RIGHT,
    'up': pygame.K_UP,
    'down': pygame.K_DOWN,
    'shoot': pygame.K_RETURN
}

tank1 = Tank((100, SCREEN_HEIGHT // 2), "images/tank1.png", tank1_controls)
tank2 = Tank((SCREEN_WIDTH - 100, SCREEN_HEIGHT // 2), "images/tank2.png", tank2_controls)

tanks = pygame.sprite.Group(tank1, tank2)
bullets = pygame.sprite.Group()
walls = pygame.sprite.Group()

# 添加更多墙壁以创建复杂的地图布局
walls.add(Wall((SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 - 100), (100, 200)))
walls.add(Wall((SCREEN_WIDTH // 4 - 50, SCREEN_HEIGHT // 4 - 50), (100, 100)))
walls.add(Wall((3 * SCREEN_WIDTH // 4 - 50, SCREEN_HEIGHT // 4 - 50), (100, 100)))
walls.add(Wall((SCREEN_WIDTH // 4 - 50, 3 * SCREEN_HEIGHT // 4 - 50), (100, 100)))
walls.add(Wall((3 * SCREEN_WIDTH // 4 - 50, 3 * SCREEN_HEIGHT // 4 - 50), (100, 100)))
walls.add(Wall((SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 50), (300, 100)))
walls.add(Wall((SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 - 150), (100, 300)))

running = True
winner = None

while running:
    keys_pressed = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys_pressed[pygame.K_ESCAPE]:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == tank1_controls['shoot']:
                bullets.add(tank1.shoot())
            if event.key == tank2_controls['shoot']:
                bullets.add(tank2.shoot())

    tanks.update(keys_pressed, walls)
    bullets.update()

    # 检查子弹与墙壁的碰撞
    pygame.sprite.groupcollide(bullets, walls, True, False)

    # 检查子弹与坦克的碰撞，忽略子弹与发射它的坦克之间的碰撞
    for bullet in bullets:
        if bullet.timer > 10:  # 忽略子弹发射后的前10帧
            hit_tank = pygame.sprite.spritecollideany(bullet, tanks)
            if hit_tank and hit_tank != bullet.shooter:
                if hit_tank == tank1:
                    winner = "Blue Tank Wins!"
                elif hit_tank == tank2:
                    winner = "Red Tank Wins!"
                hit_tank.kill()
                bullet.kill()
                running = False
                break

    screen.fill((255, 255, 255))
    walls.draw(screen)
    tanks.draw(screen)
    bullets.draw(screen)
    pygame.display.flip()
    clock.tick(60)

# 显示赢家信息
if winner:
    screen.fill(BG_COLOR)
    text = font.render(winner, True, (0, 255, 0))
    text_rect = text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.wait(3000)

pygame.quit()
