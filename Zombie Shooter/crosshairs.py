import pygame
from random import randint

class Crosshairs(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center = (10, 10))
        self.centerx = self.rect.centerx
        self.centery = self.rect.centery

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        # self.rect.x = mouse_pos[0]
        # self.rect.y = mouse_pos[1]
        dx = mouse_pos[0] - self.rect.centerx
        dy = mouse_pos[1] - self.rect.centery

        self.rect.centerx += (dx / 5)
        self.rect.centery += (dy / 5)

        mouse_press = pygame.mouse.get_pressed()[0]

        if mouse_press:
            self.rect.centerx += randint(-100, 100)
            self.rect.centery += randint(-100, 100)

        self.centerx = self.rect.centerx
        self.centery = self.rect.centery