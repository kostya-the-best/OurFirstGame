__author__ = 'Volodymyr'

def chase(zombie, knight):
    # print("Z", zombie.rect.centerx, zombie.rect.centery)
    # print("K", knight.rect.centerx, knight.rect.centery)

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

    # print("ZUZU", zombie.direction, zombie.speed)

def collision(zombie, knight):
    co =  pygame.sprite.collide_rect_ratio(0.5)
    if co(zombie, knight):
        if knight.action == 1:
            if zombie.rect.centerx > knight.rect.centerx:
                if knight.direction == DIR_RIGHT:
                    return "WIN"
                else:
                    return "LOOSE"
            else:
                if knight.direction == DIR_LEFT:
                    return "WIN"
                else:
                    return "LOOSE"
            if zombie.rect.centery > knight.rect.centery:
                if knight.direction == DIR_UP:
                    return "WIN"
                else:
                    return "LOOSE"
            else:
                if knight.direction == DIR_DOWN:
                    return "WIN"
                else:
                    return "LOOSE"
        else:
            return "LOOSE"
    else:
        return ""


def popup(msg):
    pygame.draw.rect(screen, (0,0,0), (175, 75, 200, 100), 2)
    pygame.display.update()
    screen.blit(font.render(msg, True, (255,0,0)), (200, 100))
    pygame.display.update()





















size = width, height = 640, 480
speed = [0, 0]
background = 255, 255, 255
screen = pygame.display.set_mode(size)

font = pygame.font.SysFont('Arial', 25)


#zombie = pygame.image.load("zombie_up.png")
#zombie_rect = zombie.get_rect()
#zombie_rect = zombie_rect.move( [200, 200] )

#knight_rect.move( [40, 100] )

#zombie.move(DIR_RIGHT)

# for i in range(100):
#     zombie.move(DIR_RIGHT)
#     zombie.update()

import tmx


screen.fill(background)
#pygame.display.flip()

tilemap = tmx.load('our_first_map2.tmx', screen.get_size())
tilemap.set_focus(0, 0)
clock = pygame.time.Clock()



while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_LEFT:
#                 knight.move(DIR_LEFT)
#             if event.key == pygame.K_RIGHT:
#                 knight.move(DIR_RIGHT)
#             if event.key == pygame.K_UP:
#                 knight.move(DIR_UP)
#             if event.key == pygame.K_DOWN:
#                 knight.move(DIR_DOWN)
#             if event.key == pygame.K_SPACE:
#                 knight.stab(1)
#         if event.type == pygame.KEYUP:
#             knight.stop()
#             knight.stab(0)
# #
#     knight.update()
#
#
#
#     chase(zombie, knight)
#
#
#     zombie.update()
#     screen.fill(background)
#     screen.blit(knight.get_sprite(), knight.rect)
#     screen.blit(zombie.get_sprite(), zombie.rect)
#     #screen.blit(zombie, zombie_rect)
#
#     pygame.display.flip()
#     time.sleep(0.01)
#
#     result = collision(zombie, knight)
#     if result != "":
#         #print(result)
#         popup(result)
#         time.sleep(1)
#         r = pygame.Rect(random.randint(0, 640), random.randint(0, 480), zombie.rect.width, zombie.rect.height )
#         zombie.rect = r
#         # sys.exit()
