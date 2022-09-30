import pygame
import math
from random import randint

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, angle, screen, objects):
        super().__init__()
        self.original = pygame.Surface((3, 15)).convert_alpha()
        self.image = self.original
        self.image.fill('orange')
        self.rect = self.image.get_rect(center = pos)
        self.angle = angle
        self.timer = 30
        self.alpha = 1
        self.image.set_alpha(50)

        self.original_x = pos[0]
        self.original_y = pos[1]

        self.image = pygame.transform.rotozoom(self.original, self.angle + 90, 1)
        self.rect = self.image.get_rect(center = self.rect.center)

        self.screen = screen
        self.objects = objects
    
    def update(self, zombies):
        self.timer -= 1
        angle_rad = self.angle * (math.pi / 180)
        # # self.rect.x += math.cos(angle_rad) * 10
        # # self.rect.y += math.sin(-angle_rad) * 10
        # # distance = randint(350, 450)

        # dx = None
        # dy = None

        # distance = 0
        
        # begin_time = pygame.time.get_ticks()
        # while distance < 500 and not pygame.sprite.spritecollide(self, self.objects, False):
        #     dx = math.cos(angle_rad) * distance
        #     dy = math.sin(-angle_rad) * distance
        #     self.rect.x = self.original_x + dx
        #     self.rect.y = self.original_y + dy
        #     distance += 1
        #     print('ok')
        # end_time = pygame.time.get_ticks()
        # time = (end_time - begin_time) / 100
        # print(time)

        # if dx != None and dy != None:
        #     pygame.draw.line(self.screen, 'white', (self.original_x, self.original_y), (self.rect.x, self.rect.y))
        # # self.screen.fill('black')

        # if time >= 0.1:
        #     self.timer -= time

        # self.rect.x = self.original_x
        # self.rect.y = self.original_y


        dx = math.cos(angle_rad) * 15
        dy = math.sin(-angle_rad) * 15

        

        self.rect.x += dx
        self.rect.y += dy

        if self.timer <= 0:
            self.kill()