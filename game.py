import pygame
from settings import *
from tank import Tank
from wall import Wall
from player import Player
import random
from sound_effect import *
from button import Button
from imgbutton import ImgButton
from powerup import Powerup
class Game:
    def __init__(self):
        pygame.init()
        # 音效设置
        pygame.mixer.init()
        pygame.mixer.music.set_volume(GLOBAL_VOLUME)
        pygame.mixer.music.load('sounds/YMCA.mp3')
        pygame.mixer.music.play(-1)
        # 设置所有音效的音量
        for channel in range(pygame.mixer.get_num_channels()):
            pygame.mixer.Channel(channel).set_volume(GLOBAL_VOLUME)

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Tank War")
        self.clock = pygame.time.Clock()
        # 创建字体对象时指定字体大小
        self.powerups = pygame.sprite.Group()
        for _ in range(POWERUP_NUMBER):
            self.generate_powerups()
        self.font = pygame.font.Font(None, 60)  
        self.font1 = pygame.font.Font(None, 100)  
        self.running = True        
        pygame.display.set_caption("Tank War")

        
        # 创建音乐播放/静音按钮
        self.music_button = ImgButton('images/music_button.png', (SCREEN_WIDTH - 150, 10), (50, 50), feedback="Music Changed")

        # 玩家初始化
        self.player1 = Player("Player 1", TANK1_CONTROLS, "images/tank1.png", (100, SCREEN_HEIGHT // 2))
        self.player2 = Player("Player 2", TANK2_CONTROLS, "images/tank2.png", (SCREEN_WIDTH - 100, SCREEN_HEIGHT // 2))
        self.tanks = pygame.sprite.Group(self.player1.tank, self.player2.tank)
        self.bullets = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.setup_walls()

    def generate_powerups(self):
            """生成道具"""
            powerup_positions = [(random.randint(50, SCREEN_WIDTH - 50), random.randint(50, SCREEN_HEIGHT - 50)) for _ in range(1)]
            powerup_images = {
                'speed_up': 'images/powerup_speed.png',
                'bullet_power_up': 'images/powerup_bullet.png',
                'bullet_limit_increase': 'images/powerup_limit.png'
            }

            for position in powerup_positions:
                effect = random.choice(list(powerup_images.keys()))
                imgprocess = pygame.image.load(powerup_images[effect]).convert_alpha()
                imgprocess = pygame.transform.scale(imgprocess, (40,40))
                self.powerups.add(Powerup(position, imgprocess, effect))

    def setup_walls(self):
        """创建墙壁"""
        self.walls = pygame.sprite.Group()  # 确保墙壁组是空的
        pick_map = random.choice(MAP_POOL)
        color = (random.randint(1,128),random.randint(1,128),random.randint(1,128)) 
        for position, size in pick_map:
            self.walls.add(Wall(position, size,color))

    def show_settings_screen(self):
        """显示设置界面"""
        settings_screen = True
        while settings_screen:
            self.screen.fill(BG_COLOR)
            title_text = self.font1.render("Settings", True, (0, 0, 0))
            title_rect = title_text.get_rect(center=(SCREEN_WIDTH / 2, 100))
            self.screen.blit(title_text, title_rect)
            
            # 坦克速度设置
            tank_speed_text = self.font.render("Tank Speed: " + str(TANK_SPEED), True, (0, 0, 0))
            tank_speed_rect = tank_speed_text.get_rect(center=(SCREEN_WIDTH / 2, 200))
            self.screen.blit(tank_speed_text, tank_speed_rect)
            
            # 子弹速度设置
            bullet_speed_text = self.font.render("Bullet Speed: " + str(BULLET_SPEED), True, (0, 0, 0))
            bullet_speed_rect = bullet_speed_text.get_rect(center=(SCREEN_WIDTH / 2, 300))
            self.screen.blit(bullet_speed_text, bullet_speed_rect)
            
            # 子弹限制设置
            bullet_limit_text = self.font.render("Bullet Limit: " + str(BULLET_LIMIT), True, (0, 0, 0))
            bullet_limit_rect = bullet_limit_text.get_rect(center=(SCREEN_WIDTH / 2, 400))
            self.screen.blit(bullet_limit_text, bullet_limit_rect)
            
            # 绘制退出按钮
            quit_button_color = (255, 0, 0)  # 红色
            quit_button_rect = pygame.Rect(SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT / 2 + 150, 200, 50)
            pygame.draw.rect(self.screen, quit_button_color, quit_button_rect, 0)
            quit_button_text = self.font.render("Quit", True, (0, 0, 0))
            quit_button_text_rect = quit_button_text.get_rect(center=quit_button_rect.center)
            self.screen.blit(quit_button_text, quit_button_text_rect)
            
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    settings_screen = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:  # 假设按回车键保存设置
                        # 保存设置到文件或变量
                        settings_screen = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # 检查退出按钮是否被点击
                    if quit_button_rect.collidepoint(event.pos):
                        settings_screen = False  # 返回开始界面

        return settings_screen
    def show_start_screen(self):
        """显示开始屏幕"""
        start_screen = True
        while start_screen:
            self.screen.fill(BG_COLOR)
            title_text = self.font1.render("Tank War", True, (0, 0, 0))
            title_rect = title_text.get_rect(center=(SCREEN_WIDTH / 2, 200))
            self.screen.blit(title_text, title_rect)
            
            start_button_color = (192, 192, 192)  # 灰色
            start_button_rect = pygame.Rect(SCREEN_WIDTH / 2 - 150, SCREEN_HEIGHT / 2 + 50, 300, 50)
            pygame.draw.rect(self.screen, start_button_color, start_button_rect, 0)
            start_button_text = self.font.render("Start Game", True, (0, 0, 0))
            start_button_text_rect = start_button_text.get_rect(center=start_button_rect.center)
            self.screen.blit(start_button_text, start_button_text_rect)
            
            # 添加设置按钮
            settings_button_color = (192, 192, 192)  # 灰色
            settings_button_rect = pygame.Rect(SCREEN_WIDTH / 2 - 150, SCREEN_HEIGHT / 2 - 50, 300, 50)
            pygame.draw.rect(self.screen, settings_button_color, settings_button_rect, 0)
            settings_button_text = self.font.render("Settings", True, (0, 0, 0))
            settings_button_text_rect = settings_button_text.get_rect(center=settings_button_rect.center)
            self.screen.blit(settings_button_text, settings_button_text_rect)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    start_screen = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if start_button_rect.collidepoint(event.pos):
                        start_screen = False
                    elif settings_button_rect.collidepoint(event.pos):  # 调用设置界面
                        self.show_settings_screen()  # 用户返回后，游戏继续
                        if not self.running:  # 如果用户在设置中退出游戏，则结束
                            start_screen = False

        return start_screen
    
    def show_winner_screen(self, winner_text):
        """显示获胜画面"""
        victory_sound.play()
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
        self.powerups.empty()
        self.setup_walls()  # 重新设置墙壁
        for _ in range(POWERUP_NUMBER):
            self.generate_powerups()

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
        bullet_wall_collision = pygame.sprite.groupcollide(self.bullets, self.walls, True, False)
        for wall_hit_list in bullet_wall_collision.values():
            for wall_hit in wall_hit_list:
                wall_hit.update_hit()
                break

         # 检测坦克与道具的碰撞

        for tank in self.tanks:
            hit_powerup = pygame.sprite.spritecollideany(tank, self.powerups)
            if hit_powerup:
                hit_powerup.apply_effect(tank)
                hit_powerup.kill()
                 #self.generate_powerups()  # 重新生成道具


    def draw_health_bars(self):
        """绘制玩家血条"""
        bar_height = 10

        bar_width = 100

        bar_x = 20

        bar_y = 50

        # 绘制玩家1的血条

        pygame.draw.rect(self.screen, (255, 0, 0), (bar_x, bar_y, bar_width, bar_height))  # 红色背景

        pygame.draw.rect(self.screen, (0, 255, 0), (bar_x, bar_y, bar_width * (self.player1.tank.HP / 3), bar_height))  # 绿色血量

        health_text = self.font.render(f"HP: {self.player1.tank.HP}/3", True, (0, 0, 0))
        self.screen.blit(health_text, (bar_x + bar_width + 10, bar_y - 5))

        # 绘制玩家2的血条

        bar_x = SCREEN_WIDTH - bar_width - 20

        pygame.draw.rect(self.screen, (255, 0, 0), (bar_x, bar_y, bar_width, bar_height))  # 红色背景

        pygame.draw.rect(self.screen, (0, 255, 0), (bar_x, bar_y, bar_width * (self.player2.tank.HP / 3), bar_height))  # 绿色血量

        health_text = self.font.render(f"HP: {self.player2.tank.HP}/3", True, (0, 0, 0))
        self.screen.blit(health_text, (bar_x - 100, bar_y - 5))


        for bullet in self.bullets:
            hit_tank = pygame.sprite.spritecollideany(bullet, self.tanks)
            if hit_tank and hit_tank != bullet.shooter:
                dmg = bullet.shooter.bullet_power
                bullet.kill()
                hit_tank.take_damage(dmg)
                if hit_tank == self.player1.tank and hit_tank.HP <= 0:
                    self.player2.score += 1
                    self.show_winner_screen(f"{self.player2.name} Wins!")
                    self.reset_game()
                elif hit_tank == self.player2.tank and hit_tank.HP <= 0:
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
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.music_button.click(event):
                        if pygame.mixer.music.get_busy():
                            pygame.mixer.music.pause()
                        else:
                            pygame.mixer.music.unpause()

                if event.type == pygame.KEYDOWN:
                    cnt1 = 0 # 场上最多有BULLET_LIMIT个子弹
                    cnt2 = 0
                    for bullet_count in self.bullets:
                        if bullet_count.shooter == self.player1.tank:
                            cnt1 += 1
                        else:
                            cnt2 += 1
                    if event.key == self.player1.controls['shoot']:
                        if cnt1 < self.player1.tank.bullet_limit:
                            self.bullets.add(self.player1.tank.shoot())
                            fire_sound.play()
                        else:
                            fail_to_fire_sound.play()
                    if event.key == self.player2.controls['shoot']:
                        if cnt2 < self.player2.tank.bullet_limit:
                            self.bullets.add(self.player2.tank.shoot())
                            fire_sound.play()
                        else:
                            fail_to_fire_sound.play()
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
            self.music_button.show(self.screen)
            self.draw_health_bars()
            self.powerups.draw(self.screen)  # 绘制道具

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
