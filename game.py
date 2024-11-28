import pygame
from settings import *
from tank import Tank
from wall import Wall
from player import Player
import random

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Tank War")
        self.clock = pygame.time.Clock()
        # 创建字体对象时指定字体大小
        self.font = pygame.font.Font(None, 60)  
        self.font1 = pygame.font.Font(None, 100)  
        self.running = True        
        pygame.display.set_caption("Tank War")

        # 玩家初始化
        self.player1 = Player("Player 1", TANK1_CONTROLS, "images/tank1.png", (100, SCREEN_HEIGHT // 2))
        self.player2 = Player("Player 2", TANK2_CONTROLS, "images/tank2.png", (SCREEN_WIDTH - 100, SCREEN_HEIGHT // 2))
        self.tanks = pygame.sprite.Group(self.player1.tank, self.player2.tank)
        self.bullets = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.setup_walls()

    def setup_walls(self):
        """创建墙壁"""
        self.walls = pygame.sprite.Group()  # 确保墙壁组是空的
        pick_map = random.choice(MAP_POOL)
        color = (random.randint(1,128),random.randint(1,128),random.randint(1,128))
        for position, size in pick_map:
            self.walls.add(Wall(position, size,color))

    def show_start_screen(self):
        """显示开始屏幕"""
        start_screen = True
        while start_screen:
            self.screen.fill(BG_COLOR)
            # 直接渲染标题，不需要size参数
            title_text = self.font1.render("Tank War", True, (0, 0, 0))
            title_rect = title_text.get_rect(center=(SCREEN_WIDTH / 2, 200))
            self.screen.blit(title_text, title_rect)
            
            # 绘制灰色按钮的代码...
            start_button_color = (192, 192, 192)  # 灰色
            start_button_rect = pygame.Rect(SCREEN_WIDTH / 2 - 150, SCREEN_HEIGHT / 2 + 50, 300, 50)  # 按钮位置和大小
            pygame.draw.rect(self.screen, start_button_color, start_button_rect, 0)  # 绘制灰色矩形
            start_button_text = self.font.render("Start Game", True, (0, 0, 0))
            start_button_text_rect = start_button_text.get_rect(center=start_button_rect.center)  # 文本居中
            self.screen.blit(start_button_text, start_button_text_rect)              
            # 确保你在这里添加了绘制灰色按钮的代码

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    start_screen = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if start_button_rect.collidepoint(event.pos):  # 确保你已经定义了start_button_rect
                        start_screen = False

        return start_screen
    
    def show_winner_screen(self, winner_text):
        """显示获胜画面"""
        self.screen.fill(BG_COLOR)
        text = self.font.render(winner_text, True, (0, 255, 0))
        text_rect = text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        self.screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.wait(3000)

    def reset_game(self):
        """重置游戏"""
        self.player1.reset((100, SCREEN_HEIGHT // 2))
        self.player2.reset((SCREEN_WIDTH - 100, SCREEN_HEIGHT // 2))
        self.bullets.empty()
        self.setup_walls()  # 重新设置墙壁

    def pause_game(self):
        """暂停功能"""
        paused = True
        while paused:
            pygame.draw.rect(self.screen, (0, 0, 0, 128), (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))  # 绘制半透明背景
            pause_text = self.font.render("Paused - Press P to Resume", True, (255, 255, 255))
            pause_rect = pause_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT/2))
            self.screen.blit(pause_text, pause_rect)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    paused = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                    paused = False

    def check_tank_collisions(self):
        for tank1 in self.tanks:
            for tank2 in self.tanks:
                if tank1 != tank2 and tank1.rect.colliderect(tank2.rect):
                    # 处理碰撞
                    self.handle_collision(tank1, tank2)

    def handle_collision(self,tank1, tank2):
        # 计算两个坦克的相对位置
        dx = tank2.rect.centerx - tank1.rect.centerx
        dy = tank2.rect.centery - tank1.rect.centery
        distance = (dx ** 2 + dy ** 2) ** 0.5  # 两点之间的距离

        # 计算单位向量
        unit_vector_x = dx / distance
        unit_vector_y = dy / distance

        # 弹开的力，可以根据需要调整这个值
        force = 0.5

        # 更新坦克1的方向和位置
        tank1.rect.centerx += -unit_vector_x * force * tank1.speed
        tank1.rect.centery += -unit_vector_y * force * tank1.speed

        # 更新坦克2的方向和位置

        tank2.rect.centerx += unit_vector_x * force * tank2.speed
        tank2.rect.centery += unit_vector_y * force * tank2.speed

        # 确保坦克不会离开屏幕
        tank1.rect.x = max(0, min(SCREEN_WIDTH - tank1.rect.width, tank1.rect.x))
        tank1.rect.y = max(0, min(SCREEN_HEIGHT - tank1.rect.height, tank1.rect.y))
        tank2.rect.x = max(0, min(SCREEN_WIDTH - tank2.rect.width, tank2.rect.x))
        tank2.rect.y = max(0, min(SCREEN_HEIGHT - tank2.rect.height, tank2.rect.y))
        
    def check_collisions(self):
        """检查子弹与墙壁、坦克的碰撞"""
        pygame.sprite.groupcollide(self.bullets, self.walls, True, False)

        for bullet in self.bullets:
            hit_tank = pygame.sprite.spritecollideany(bullet, self.tanks)
            if hit_tank and hit_tank != bullet.shooter:
                bullet.kill()
                if hit_tank == self.player1.tank:
                    self.player2.score += 1
                    self.show_winner_screen(f"{self.player2.name} Wins!")
                elif hit_tank == self.player2.tank:
                    self.player1.score += 1
                    self.show_winner_screen(f"{self.player1.name} Wins!")
                self.reset_game()
                break

    def run(self):
        """主游戏循环"""
        self.show_start_screen()
        while self.running:
            keys_pressed = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    cnt1 = 0 # 场上最多有BULLET_LIMIT个子弹
                    cnt2 = 0
                    for bullet_count in self.bullets:
                        if bullet_count.shooter == self.player1.tank:
                            cnt1 += 1
                        else:
                            cnt2 += 1
                    if event.key == self.player1.controls['shoot'] and cnt1 < BULLET_LIMIT:
                        self.bullets.add(self.player1.tank.shoot())
                    if event.key == self.player2.controls['shoot'] and cnt2 < BULLET_LIMIT:
                        self.bullets.add(self.player2.tank.shoot())
                    if event.key == pygame.K_p:
                        self.pause_game()

            self.tanks.update(keys_pressed, self.walls)
            self.bullets.update()
            self.check_collisions()
            self.check_tank_collisions()

            self.screen.fill(BG_COLOR)
            self.walls.draw(self.screen)
            self.tanks.draw(self.screen)
            self.bullets.draw(self.screen)

            score_text = self.font.render(
                f"{self.player1.name}: {self.player1.score} - {self.player2.name}: {self.player2.score}",
                True,
                (0, 0, 0)
            )
            self.screen.blit(score_text, (20, 20))
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    game = Game()
    game.run()
