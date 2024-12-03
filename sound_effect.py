# https://pixabay.com/zh/sound-effects/search/%E6%B8%B8%E6%88%8F%E9%9F%B3%E6%95%88
import pygame
pygame.init()
pygame.mixer.init()

victory_sound = pygame.mixer.Sound('sounds/victorymale-version-230553.mp3')
fire_sound = pygame.mixer.Sound('sounds/8-bit-jump-001-171817.mp3')
fail_to_fire_sound = pygame.mixer.Sound('sounds/retro-spell-sfx-85574.mp3')
