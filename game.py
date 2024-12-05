import pygame
from settings import *
from tank import Tank
from wall import Wall
from player import Player
import random
from sound_effect import *
from button import Button
from imgbutton import ImgButton
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
        self.font = pygame.font.Font(None, 60)  
        self.font1 = pygame.font.Font(None, 100)  
        self.running = True        
        pygame.display.set_caption("Tank War")
        self.focus = None  # 初始化焦点属性
        self.music_button = ImgButton('images/music_button.png', (SCREEN_WIDTH - 150, 10), (50, 50), feedback="Music Changed")

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

    def show_settings_screen(self):
        """显示设置界面"""
        global TANK_SPEED, BULLET_SPEED, BULLET_LIMIT  # 将 global 声明移到函数顶部
        settings_screen = True
        tank_speed = str(TANK_SPEED)
        bullet_speed = str(BULLET_SPEED)
        bullet_limit = str(BULLET_LIMIT)
        while settings_screen:
            self.screen.fill(BG_COLOR)
            title_text = self.font1.render("Settings", True, (0, 0, 0))
            title_rect = title_text.get_rect(center=(SCREEN_WIDTH / 2, 100))
            self.screen.blit(title_text, title_rect)
            
            # 坦克速度设置
            tank_speed_text = self.font.render("Tank Speed: ", True, (0, 0, 0))
            tank_speed_rect = tank_speed_text.get_rect(center=(SCREEN_WIDTH / 2, 200))
            self.screen.blit(tank_speed_text, tank_speed_rect)
            tank_speed_input_rect = pygame.Rect(SCREEN_WIDTH / 2 - 50, 220, 100, 30)
            pygame.draw.rect(self.screen, (0, 0, 0), tank_speed_input_rect)
            tank_speed_input_text = self.font.render(tank_speed, True, (255, 255, 255))
            tank_speed_input_text_rect = tank_speed_input_text.get_rect(center=tank_speed_input_rect.center)
            self.screen.blit(tank_speed_input_text, tank_speed_input_text_rect)
            
            # 子弹速度设置
            bullet_speed_text = self.font.render("Bullet Speed: ", True, (0, 0, 0))
            bullet_speed_rect = bullet_speed_text.get_rect(center=(SCREEN_WIDTH / 2, 300))
            self.screen.blit(bullet_speed_text, bullet_speed_rect)
            bullet_speed_input_rect = pygame.Rect(SCREEN_WIDTH / 2 - 50, 320, 100, 30)
            pygame.draw.rect(self.screen, (0, 0, 0), bullet_speed_input_rect)
            bullet_speed_input_text = self.font.render(bullet_speed, True, (255, 255, 255))
            bullet_speed_input_text_rect = bullet_speed_input_text.get_rect(center=bullet_speed_input_rect.center)
            self.screen.blit(bullet_speed_input_text, bullet_speed_input_text_rect)
            
            # 子弹限制设置
            bullet_limit_text = self.font.render("Bullet Limit: ", True, (0, 0, 0))
            bullet_limit_rect = bullet_limit_text.get_rect(center=(SCREEN_WIDTH / 2, 400))
            self.screen.blit(bullet_limit_text, bullet_limit_rect)
            bullet_limit_input_rect = pygame.Rect(SCREEN_WIDTH / 2 - 50, 420, 100, 30)
            pygame.draw.rect(self.screen, (0, 0, 0), bullet_limit_input_rect)
            bullet_limit_input_text = self.font.render(bullet_limit, True, (255, 255, 255))
            bullet_limit_input_text_rect = bullet_limit_input_text.get_rect(center=bullet_limit_input_rect.center)
            self.screen.blit(bullet_limit_input_text, bullet_limit_input_text_rect)
            
            # 绘制保存按钮
            save_button_color = (0, 255, 0)  # 绿色
            save_button_rect = pygame.Rect(SCREEN_WIDTH / 2 - 250, SCREEN_HEIGHT / 2 + 170, 200, 50)
            pygame.draw.rect(self.screen, save_button_color, save_button_rect, 0)
            save_button_text = self.font.render("Save", True, (0, 0, 0))
            save_button_text_rect = save_button_text.get_rect(center=save_button_rect.center)
            self.screen.blit(save_button_text, save_button_text_rect)
            
            # 绘制退出按钮
            quit_button_color = (255, 0, 0)  # 红色
            quit_button_rect = pygame.Rect(SCREEN_WIDTH / 2 + 50, SCREEN_HEIGHT / 2 + 170, 200, 50)
            pygame.draw.rect(self.screen, quit_button_color, quit_button_rect, 0)
            quit_button_text = self.font.render("Quit", True, (0, 0, 0))
            quit_button_text_rect = quit_button_text.get_rect(center=quit_button_rect.center)
            self.screen.blit(quit_button_text, quit_button_text_rect)
            
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    settings_screen = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # 检查退出按钮是否被点击
                    if quit_button_rect.collidepoint(event.pos):
                        settings_screen = False  # 返回开始界面
                    # 检查保存按钮是否被点击
                    elif save_button_rect.collidepoint(event.pos):
                        try:
                            TANK_SPEED = int(tank_speed)
                            BULLET_SPEED = int(bullet_speed)
                            BULLET_LIMIT = int(bullet_limit)
                            settings_screen = False  # 保存后返回
                        except ValueError:
                            # 如果输入不是数字，则忽略
                            pass
                    # 检查输入框是否被点击
                    elif tank_speed_input_rect.collidepoint(event.pos):
                        self.focus = 'tank_speed'
                    elif bullet_speed_input_rect.collidepoint(event.pos):
                        self.focus = 'bullet_speed'
                    elif bullet_limit_input_rect.collidepoint(event.pos):
                        self.focus = 'bullet_limit'
                elif event.type == pygame.KEYDOWN:
                    if self.focus:
                        if event.key == pygame.K_RETURN:  # 保存设置
                            try:
                                if self.focus == 'tank_speed':
                                    TANK_SPEED = int(tank_speed)
                                elif self.focus == 'bullet_speed':
                                    BULLET_SPEED = int(bullet_speed)
                                elif self.focus == 'bullet_limit':
                                    BULLET_LIMIT = int(bullet_limit)
                            except ValueError:
                                pass  # 如果输入不是数字，则忽略
                            self.focus = None  # 取消焦点
                        elif event.key == pygame.K_BACKSPACE:  # 删除字符
                            if self.focus in ['tank_speed', 'bullet_speed', 'bullet_limit']:
                                if tank_speed:
                                    tank_speed = tank_speed[:-1]
                                elif bullet_speed:
                                    bullet_speed = bullet_speed[:-1]
                                elif bullet_limit:
                                    bullet_limit = bullet_limit[:-1]
                        else:  # 输入新字符
                            if event.key in (pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4,
                                             pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9):
                                if self.focus == 'tank_speed':
                                    tank_speed += str(event.unicode)
                                elif self.focus == 'bullet_speed':
                                    bullet_speed += str(event.unicode)
                                elif self.focus == 'bullet_limit':
                                    bullet_limit += str(event.unicode)

            # 绘制文本输入框中的文本
            if self.focus:
                if self.focus == 'tank_speed':
                    tank_speed_text = self.font.render(tank_speed, True, (255, 255, 255))
                elif self.focus == 'bullet_speed':
                    bullet_speed_text = self.font.render(bullet_speed, True, (255, 255, 255))
                elif self.focus == 'bullet_limit':
                    bullet_limit_text = self.font.render(bullet_limit, True, (255, 255, 255))
                # 根据焦点绘制对应的文本
                if self.focus == 'tank_speed':
                    self.screen.blit(tank_speed_text, tank_speed_input_text_rect)
                elif self.focus == 'bullet_speed':
                    self.screen.blit(bullet_speed_text, bullet_speed_input_text_rect)
                elif self.focus == 'bullet_limit':
                    self.screen.blit(bullet_limit_text, bullet_limit_input_text_rect)

        return settings_screen
    
    def show_start_screen(self):
        """显示开始屏幕"""
        start_screen = True
        while start_screen:
            self.screen.fill(BG_COLOR)
            title_text = self.font1.render("Tank War", True, (0, 0, 0))
            title_rect = title_text.get_rect(center=(SCREEN_WIDTH / 2, 200))
            self.screen.blit(title_text, title_rect)
            
            start_button_color = (100, 192, 192)  # 青色
            start_button_rect = pygame.Rect(SCREEN_WIDTH / 2 - 150, SCREEN_HEIGHT / 2 - 50, 300, 90)
            pygame.draw.rect(self.screen, start_button_color, start_button_rect, 0)
            start_button_text = self.font.render("Start Game", True, (0, 0, 0))
            start_button_text_rect = start_button_text.get_rect(center=start_button_rect.center)
            self.screen.blit(start_button_text, start_button_text_rect)
            
            # 添加设置按钮
            settings_button_color = (192, 192, 192)  # 灰色
            settings_button_rect = pygame.Rect(SCREEN_WIDTH / 2 - 150, SCREEN_HEIGHT / 2 + 70, 300, 60)
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
        bullet_wall_collision = pygame.sprite.groupcollide(self.bullets, self.walls, True, False)
        for wall_hit_list in bullet_wall_collision.values():
            for wall_hit in wall_hit_list:
                wall_hit.update_hit()
                break



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
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.music_button.click(event):
                        if pygame.mixer.music.get_busy():
                            pygame.mixer.music.pause()
                        else:
                            pygame.mixer.music.unpause()

                if event.type == pygame.KEYDOWN:
                    cnt1 = 0  
                    cnt2 = 0
                    for bullet_count in self.bullets:
                        if bullet_count.shooter == self.player1.tank:
                            cnt1 += 1
                        else:
                            cnt2 += 1
                    if event.key == self.player1.controls['shoot']:
                        if cnt1 < BULLET_LIMIT:
                            new_bullet = self.player1.shoot()
                            if new_bullet:
                                self.bullets.add(new_bullet)
                                fire_sound.play()
                            else:
                                fail_to_fire_sound.play()
                    if event.key == self.player2.controls['shoot']:
                        if cnt2 < BULLET_LIMIT:
                            new_bullet = self.player2.shoot()
                            if new_bullet:
                                self.bullets.add(new_bullet)
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
