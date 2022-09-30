import pygame

def display_hud(screen, weapon_img, clip, health, max_health):

    # weapon
    weapon_img.set_alpha(160)

    # bullets
    bullet = pygame.Surface((5, 10))
    bullet.set_alpha(160)
    screen.blit(weapon_img, (10, screen.get_height() - weapon_img.get_height() - 30))
    x = 10
    y = screen.get_height() - 20
    for i in range(clip):
        screen.blit(bullet, (x, y))
        x += 8

    # health
    max_bar_length = max_health * 2
    bar = pygame.Surface((max_bar_length + 4, 14))
    bar.fill('#111111')
    bar.set_alpha(160)
    health_bar = pygame.Surface((health * 2, 10))
    health_bar.fill('#aa0000')
    health_bar.set_alpha(160)
    screen.blit(bar, (screen.get_width() - max_bar_length - 10, screen.get_height() - 20))
    screen.blit(health_bar, (screen.get_width() - max_bar_length - 8, screen.get_height() - 18))