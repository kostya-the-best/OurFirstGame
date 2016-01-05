import pygame
import tmx
import time, random
from character import init
from movement import handle_knight_move, handle_zombie_move, has_knight_won


def init_screen():
    pygame.init()
    screen = pygame.display.set_mode((30*32, 20*32))
    return screen


def load_map(screen):
    tilemap = tmx.load('our_first_map2.tmx', screen.get_size())
    tilemap.set_focus(0, 0)
    return tilemap


def popup(screen, font, result):
    if result:
        msg = "WIN!!!"
    else:
        msg = "Loose :("
    pygame.draw.rect(screen, (0,0,0), (175, 75, 200, 100), 2)
    pygame.display.update()
    screen.blit(font.render(msg, True, (255,0,0)), (200, 100))
    pygame.display.update()


def main():
    screen = init_screen()
    tilemap = load_map(screen)
    clock = pygame.time.Clock()
    font = pygame.font.SysFont('Arial', 25)

    sprite_layer = tmx.SpriteLayer()
    sprite_layer.set_view(0, 0, *screen.get_size())
    tilemap.layers.append(sprite_layer)

    knight,zombie = init(*screen.get_size())
    sprite_layer.add(knight,zombie)

    knight.rect = knight.rect.move(200,0)

    while 1:
        dt = clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            handle_knight_move(knight, event)
        handle_zombie_move(zombie, knight)

        result = has_knight_won(zombie, knight)
        if result is not None:
            popup(screen, font, result)
            time.sleep(1)
            r = pygame.Rect(random.randint(0, 640), random.randint(0, 480), zombie.rect.width, zombie.rect.height)
            zombie.rect = r

        # tilemap.update calls the update method on each layer in the map.
        # The update method can be customized for each layer to include logic
        # for animating sprite positions, and detecting collisions.
        tilemap.update(dt)
        # Fill the screen with an R,G,B color to erase the previous drawings.
        screen.fill((0,0,0))
        # Draw all layers of the tilemap to the screen.
        tilemap.draw(screen)
        # Refresh the display window.
        pygame.display.flip()


main()