import pygame
class ImgButton:
    def __init__(self, image_path, pos, size, feedback=""):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect(topleft=pos)
        self.feedback = feedback

    def show(self, screen):
        screen.blit(self.image, self.rect)

    def click(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    return True

        return False