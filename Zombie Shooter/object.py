import pygame

class Object(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill('red')
        self.rect = self.image.get_rect(center = (200, 200))