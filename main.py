import pygame
import tmx
from character import Character, DIR_DOWN, DIR_LEFT, DIR_RIGHT, DIR_UP


def init_screen():
    pygame.init()
    screen = pygame.display.set_mode((30*32, 20*32))
    return screen

def load_map(screen):
    tilemap = tmx.load('res/our_first_map2.tmx', screen.get_size())
    tilemap.set_focus(0, 0)
    return tilemap

def main():
    screen = init_screen()
    tilemap = load_map(screen)
    clock = pygame.time.Clock()


    l = tilemap.layers['Charz']
    print(">", l)
    k = l.objects[0]
    print(">>>>", k)


    while 1:
        dt = clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        k.px += 1

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