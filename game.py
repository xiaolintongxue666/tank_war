import pygame
from settings import *
from tank import Tank
from wall import Wall
from player import Player

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Tank War")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 74)
        self.running = True

        # 玩家初始化
        self.player1 = Player("Player 1", TANK1_CONTROLS, "images/tank1.png", (100, SCREEN_HEIGHT // 2))
        self.player2 = Player("Player 2", TANK2_CONTROLS, "images/tank2.png", (SCREEN_WIDTH - 100, SCREEN_HEIGHT // 2))
        self.tanks = pygame.sprite.Group(self.player1.tank, self.player2.tank)
        self.bullets = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.setup_walls()

    def setup_walls(self):
        """创建墙壁"""
        for position, size in WALL_POSITIONS:
            self.walls.add(Wall(position, size))

    def show_start_screen(self):
        """显示开始屏幕"""
        start_screen = True
        while start_screen:
            self.screen.fill(BG_COLOR)
            title_text = self.font.render("Tank War", True, (0, 0, 0))
            start_button = self.font.render("Start Game", True, (0, 0, 0))
            start_button_rect = start_button.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
            self.screen.blit(title_text, (SCREEN_WIDTH / 2 - 100, 100))
            self.screen.blit(start_button, start_button_rect)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    start_screen = False
                elif event.type == pygame.MOUSEBUTTONDOWN and start_button_rect.collidepoint(event.pos):
                    start_screen = False

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

    def pause_game(self):
        """暂停功能"""
        paused = True
        while paused:
            pause_text = self.font.render("Paused - Press P to Resume", True, (0, 0, 0))
            self.screen.blit(pause_text, (SCREEN_WIDTH / 2 - 200, SCREEN_HEIGHT / 2))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    paused = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                    paused = False

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
                    if event.key == self.player1.controls['shoot']:
                        self.bullets.add(self.player1.tank.shoot())
                    if event.key == self.player2.controls['shoot']:
                        self.bullets.add(self.player2.tank.shoot())
                    if event.key == pygame.K_p:
                        self.pause_game()

            self.tanks.update(keys_pressed, self.walls)
            self.bullets.update()
            self.check_collisions()

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
