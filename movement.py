__author__ = 'Volodymyr'
import pygame
from character import Character, DIR_DOWN, DIR_LEFT, DIR_RIGHT, DIR_UP, init


def handle_knight_move(knight, event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            knight.move(DIR_LEFT)
        if event.key == pygame.K_RIGHT:
            knight.move(DIR_RIGHT)
        if event.key == pygame.K_UP:
            knight.move(DIR_UP)
        if event.key == pygame.K_DOWN:
            knight.move(DIR_DOWN)
        if event.key == pygame.K_SPACE:
            knight.stab(1)
    if event.type == pygame.KEYUP:
        knight.stop()
        knight.stab(0)


def handle_zombie_move(zombie, knight):
    x = zombie.rect.centerx - knight.rect.centerx
    y = zombie.rect.centery - knight.rect.centery

    if abs(x) > abs(y):
        if x > 0:
            zombie.move(DIR_LEFT)
        elif x < 0:
            zombie.move(DIR_RIGHT)
    else:
        if y > 0:
            zombie.move(DIR_UP)
        elif y < 0:
            zombie.move(DIR_DOWN)


def has_knight_won(zombie, knight):
    co = pygame.sprite.collide_rect_ratio(0.5)
    if co(zombie, knight):
        if knight.action == 1:
            if zombie.rect.centerx > knight.rect.centerx:
                return knight.direction == DIR_RIGHT
            elif zombie.rect.centerx < knight.rect.centerx:
                return knight.direction == DIR_LEFT
            elif zombie.rect.centery > knight.rect.centery:
                return knight.direction == DIR_UP
            else:
                return knight.direction == DIR_DOWN
        else:
            return False
    return None
