import pygame
from settings import *
from tank import Tank
from bullet import Bullet
from wall import Wall

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Tank War")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 74)
        self.tank1_controls = {
            'left': pygame.K_a,
            'right': pygame.K_d,
            'up': pygame.K_w,
            'down': pygame.K_s,
            'shoot': pygame.K_SPACE
        }
        self.tank2_controls = {
            'left': pygame.K_LEFT,
            'right': pygame.K_RIGHT,
            'up': pygame.K_UP,
            'down': pygame.K_DOWN,
            'shoot': pygame.K_RETURN
        }
        self.tank1 = Tank((100, SCREEN_HEIGHT // 2), "images/tank1.png", self.tank1_controls)
        self.tank2 = Tank((SCREEN_WIDTH - 100, SCREEN_HEIGHT // 2), "images/tank2.png", self.tank2_controls)
        self.tanks = pygame.sprite.Group(self.tank1, self.tank2)
        self.bullets = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.setup_walls()
        self.running = True

    def setup_walls(self):
        # 添加更多墙壁以创建复杂的地图布局
        self.walls.add(Wall((SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 - 100), (100, 200)))
        self.walls.add(Wall((SCREEN_WIDTH // 4 - 50, SCREEN_HEIGHT // 4 - 50), (100, 100)))
        self.walls.add(Wall((3 * SCREEN_WIDTH // 4 - 50, SCREEN_HEIGHT // 4 - 50), (100, 100)))
        self.walls.add(Wall((SCREEN_WIDTH // 4 - 50, 3 * SCREEN_HEIGHT // 4 - 50), (100, 100)))
        self.walls.add(Wall((3 * SCREEN_WIDTH // 4 - 50, 3 * SCREEN_HEIGHT // 4 - 50), (100, 100)))
        self.walls.add(Wall((SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 50), (300, 100)))
        self.walls.add(Wall((SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 - 150), (100, 300)))

    def show_start_screen(self):
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
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if start_button_rect.collidepoint(event.pos):
                        start_screen = False

    def show_winner_screen(self, winner_text):
        self.screen.fill(BG_COLOR)
        text = self.font.render(winner_text, True, (0, 255, 0))
        text_rect = text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        self.screen.blit(text, text_rect)
        score_text = self.font.render(f"Player 1: {score['Player 1']} - Player 2: {score['Player 2']}", True, (0, 0, 0))
        score_text_rect = score_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 100))
        self.screen.blit(score_text, score_text_rect)
        pygame.display.flip()
        pygame.time.wait(3000)

    def reset_game(self):
        self.__init__()
        self.show_start_screen()

    def run(self):
        self.show_start_screen()
        while self.running:
            keys_pressed = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT or keys_pressed[pygame.K_ESCAPE]:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == self.tank1_controls['shoot']:
                        self.bullets.add(self.tank1.shoot())
                    if event.key == self.tank2_controls['shoot']:
                        self.bullets.add(self.tank2.shoot())

            self.tanks.update(keys_pressed, self.walls)
            self.bullets.update()

            # 检查子弹与墙壁的碰撞
            pygame.sprite.groupcollide(self.bullets, self.walls, True, False)

            # 检查子弹与坦克的碰撞，忽略子弹与发射它的坦克之间的碰撞
            for bullet in self.bullets:
                if True:  
                    hit_tank = pygame.sprite.spritecollideany(bullet, self.tanks)
                    if hit_tank and hit_tank != bullet.shooter:
                        if hit_tank == self.tank1:
                            score["Player 2"] += 1
                            self.show_winner_screen("Green Tank Wins!")
                        elif hit_tank == self.tank2:
                            score["Player 1"] += 1
                            self.show_winner_screen("Red Tank Wins!")
                        bullet.kill()
                        self.reset_game()  # Reset game and return to start screen
                        break

            self.screen.fill((255, 255, 255))
            self.walls.draw(self.screen)
            self.tanks.draw(self.screen)
            self.bullets.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    score = {"Player 1": 0, "Player 2": 0}
    game = Game()
    game.run()