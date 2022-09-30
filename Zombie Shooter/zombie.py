import pygame
import math

class Zombie(pygame.sprite.Sprite):
    def __init__(self, pos, player_pos):
        super().__init__()
        self.original = pygame.image.load('assets/characters/zombie.png').convert_alpha()
        self.image = self.original
        self.rect = self.image.get_rect(center = pos)
        self.speed = 2
        self.angle = 0
        self.rotation_speed = 5
        self.player_pos = player_pos
        self.health = 3
        # print(self.player_pos)

    def move(self):
        # mouse_pos = pygame.mouse.get_pos()
        dx, dy = self.player_pos[0] - self.rect.centerx, self.player_pos[1] - self.rect.centery
        self.angle = math.degrees(math.atan2(-dy, dx))

        self.image = pygame.transform.rotozoom(self.original, self.angle, 1)
        self.rect = self.image.get_rect(center = self.rect.center)

        angle_rad = self.angle * (math.pi / 180)

        dx = math.cos(angle_rad) * 3
        dy = math.sin(-angle_rad) * 3
        # print('dx:', dx, 'dy:', dy)

        self.rect.x += dx
        self.rect.y += dy

    def update(self, player_pos, bullets):
        self.player_pos = player_pos

        if self.health <= 0:
            self.kill()

        # print(bullets)

        if pygame.sprite.spritecollide(self, bullets, True):
            print('ok')
            self.health -= 1

        self.move()

