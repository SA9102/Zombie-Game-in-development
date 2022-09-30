import pygame
import math
from bullet import Bullet
from random import uniform
from settings import weapons

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, screen, objects):
        super().__init__()
        self.original = pygame.image.load('assets/characters/player.png').convert_alpha()
        self.image = self.original
        self.rect = self.image.get_rect(center = pos)
        self.speed = 4
        self.angle = 0
        self.rotation_speed = 5
        self.centerx = self.rect.centerx
        self.centery = self.rect.centery

        self.pause = False

        self.max_health = 100
        self.health = self.max_health

        self.weapon = 'pistol'
        self.clip = weapons[self.weapon]['clip']
        self.extra_ammo = weapons[self.weapon]['extra ammo']
        self.firing_timer = weapons[self.weapon]['fire rate']
        self.reload_speed = weapons[self.weapon]['reload speed']

        # self.firing_timer = 0 # Determines fire rate - higher number results in lower fire rate
        self.screen = screen
        self.objects = objects

        self.bullets = pygame.sprite.Group()
        # self.bullet_num

    # def rotate(self, direction):
    #     if direction == 1:
    #         self.angle -= self.rotation_speed
    #     else:
    #         self.angle += self.rotation_speed

    #     self.image = pygame.transform.rotozoom(self.original, self.angle, 1)
    #     self.rect = self.image.get_rect(center = self.rect.center)

    def shoot(self):
        if self.firing_timer <= 0 and self.clip > 0 and self.pause == False:
            self.bullets.add(Bullet(self.rect.center, self.angle + uniform(-5, 5), self.screen, self.objects))
            # self.firing_timer = weapons[self.weapon]['fire rate']
            self.clip -= 1
            self.pause = True
            self.angle += 20

    def reload(self):
        self.reload_speed -= 1
        if self.reload_speed <= 0:
            self.clip = weapons[self.weapon]['clip']
            self.extra_ammo -= self.clip
            self.reload_speed = weapons[self.weapon]['reload speed']


    def rotate(self, crosshairs_pos):
        dx, dy = crosshairs_pos[0] - self.rect.centerx, crosshairs_pos[1] - self.rect.centery
        self.angle = math.degrees(math.atan2(-dy, dx))

        self.image = pygame.transform.rotozoom(self.original, self.angle, 1)
        self.rect = self.image.get_rect(center = self.rect.center)

    def action(self, crosshairs_pos):
        key = pygame.key.get_pressed()
        mouse_press = pygame.mouse.get_pressed()[0]
        if not mouse_press:
            self.pause = False

        # Move
        if key[pygame.K_d]: self.rect.x += self.speed
        if key[pygame.K_a]: self.rect.x -= self.speed
        if key[pygame.K_w]: self.rect.y -= self.speed
        if key[pygame.K_s]: self.rect.y += self.speed

        # # Turn
        # if key[pygame.K_RIGHT]: self.rotate(1)
        # if key[pygame.K_LEFT]: self.rotate(-1)

        # Fire
        if mouse_press: self.shoot()

        # Reload
        if key[pygame.K_r]: pass

        # Switch weapon
        if key[pygame.K_e]: pass

        # Grenade
        if key[pygame.K_q]: pass

        # mouse_pos = pygame.mouse.get_pos()
        self.rotate(crosshairs_pos)

    def update(self, crosshairs_pos):
        if self.firing_timer > 0:
            self.firing_timer -= 1

        if self.clip <= 0:
            self.reload()

        self.action(crosshairs_pos)
        self.centerx = self.rect.centerx
        self.centery = self.rect.centery