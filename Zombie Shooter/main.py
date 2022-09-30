from audioop import cross
import pygame
from pygame.math import Vector2
from sys import exit
from crosshairs import Crosshairs
from player import Player
from object import Object
from subroutines import *
from crosshairs import Crosshairs
from random import randint, choice
from zombie import Zombie

'''
Powerups
- Slow
- Double points
- Nuclear blast
- Rapid fire

Pickups
- Extra ammo
- Weapon
- Health

Upgrade player
- Recoil control
- Increase health
- Ammo capacity
- Weapon pouch
- Regenerate health

Weapons
Melee:
- Knife
- Baseball bat
Sidearm
- Pistol
- Revolver
- SMG
- Sawn off shotgun
Main
- Rifle
- Assault Rifle
- Carbine Rifle
- Shotgun


Save and load

Options
- Background sound
- Sound effects
'''



# GAME SETTINGS

screen_width = 640
screen_height = 440

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

# Game states
MENU = 1
PLAYING = 2

game_state = PLAYING

# Events
spawn_zombie = pygame.USEREVENT + 1
pygame.time.set_timer(spawn_zombie, 3000)

# Surfaces
pistol_surf = pygame.image.load('assets/weapons/pistol.png').convert_alpha()
# revolver = pygame.image.load('assets/revolver.png').convert_alpha()
# smg = pygame.image.load('assets/smg.png').convert_alpha()

weapon_surfs = {
    'pistol': pistol_surf
}

cursor = pygame.image.load('assets/misc/cursor.png').convert_alpha()
# crosshairs = 

# Fonts
title_font = pygame.font.Font('Zombies.ttf', 100)
menu_button_font = pygame.font.SysFont('Calibri', 30)



# Objects

object = pygame.sprite.Group()
object.add(Object())

player = pygame.sprite.GroupSingle()
player.add(Player((100, 100), screen, object))

zombies = pygame.sprite.Group()

crosshairs = pygame.sprite.GroupSingle()
crosshairs.add(Crosshairs(pygame.image.load('assets/crosshairs/crosshairs.png').convert_alpha()))

pygame.mouse.set_visible(False)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == spawn_zombie:
            side = choice([0, 1, 2, 3]) # top = 0, right = 1, bottom = 2, left = 3
            if side == 0:
                zombies.add(Zombie((randint(20, screen.get_width() - 20), 20), (player.sprite.centerx, player.sprite.centery)))
            elif side == 1:
                zombies.add(Zombie((screen.get_width() - 20, randint(20, screen.get_height() - 20)), (player.sprite.centerx, player.sprite.centery)))
            elif side == 2:
                zombies.add(Zombie((randint(20, screen.get_width() - 20), screen.get_height() - 20), (player.sprite.centerx, player.sprite.centery)))
            elif side == 3:
                zombies.add(Zombie((20, randint(20, screen.get_height() - 20)), (player.sprite.centerx, player.sprite.centery)))

    

    # screen.blit(pistol, (20, 20))

    if game_state == PLAYING:
        screen.fill('#003300')


        player.draw(screen)
        player.update((crosshairs.sprite.centerx, crosshairs.sprite.centery))

        object.draw(screen)

        player.sprite.bullets.draw(screen)
        player.sprite.bullets.update(zombies)

        

        zombies.draw(screen)
        zombies.update((player.sprite.centerx, player.sprite.centery), player.sprite.bullets)

        crosshairs.draw(screen)
        crosshairs.update()
        display_hud(screen, pygame.transform.scale2x(pygame.transform.scale2x(weapon_surfs[player.sprite.weapon])), player.sprite.clip, player.sprite.health, player.sprite.max_health)
    else:
        screen.fill('#000000')
        title_surf = title_font.render('Zombies', True, (150, 0, 0))
        play_button_surf = menu_button_font.render('Play', True, (225, 225, 225))
        options_button_surf = menu_button_font.render('Options', True, (225, 225, 225))


        screen.blit(title_surf, (10, 30))
        screen.blit(play_button_surf, (20, 200))
        screen.blit(options_button_surf, (20, 250))
        screen.blit(cursor, (pygame.mouse.get_pos()[0] - cursor.get_width()/2, pygame.mouse.get_pos()[1] - cursor.get_height()/2))

    pygame.display.update()
    clock.tick(30)