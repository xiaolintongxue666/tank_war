from tank import Tank
import pygame

class Player:
    def __init__(self, name, controls, tank_image, initial_position):
        self.name = name
        self.controls = controls
        self.tank = Tank(initial_position, tank_image, controls)
        self.score = 0
        self.last_shot_time = 0

    def shoot(self):
        current_time = pygame.time.get_ticks()
        if (current_time - self.last_shot_time) > 400:  # 1000 milliseconds = 1 second
            bullet = self.tank.shoot()
            self.last_shot_time = current_time
            return bullet
        return None

    def reset(self, position):
        self.tank.reset(position)
        self.last_shot_time = 0  # Reset last shot time when the player resets
