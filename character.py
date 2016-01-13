__author__ = 'Volodymyr and Kostya'
import pygame

DIR_UP = 0
DIR_RIGHT = 1
DIR_DOWN = 2
DIR_LEFT = 3

class Character(pygame.sprite.Sprite):

    def __init__(self, world, pictures, run = 1):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        for pic in pictures:
            self.sprites.append( pic )

        self.rect = self.sprites[0].get_rect()
        self.direction = DIR_UP
        self.world = world
        self.speed = [0,0]
        self.run = run
        self.action = 0

    def get_sprite(self):
        index = self.direction
        if self.action == 1:
            index += 4
        return self.sprites[index]

    def move(self, direction):
        # print("char", direction)
        self.direction = direction
        if direction == DIR_LEFT:
            self.speed = [-self.run, 0]
        if direction == DIR_RIGHT:
            self.speed = [self.run, 0]
        if direction == DIR_UP:
            self.speed = [0, -self.run]
        if direction == DIR_DOWN:
            self.speed = [0, self.run]

        # if self.rect.left < 0:
        #     if self.speed[0] < 0:
        #         self.speed[0] = 0
        # if self.rect.right > self.width:
        #     if self.speed[0] > 0:
        #         self.speed[0] = 0
        # if self.rect.top < 0:
        #     if self.speed[1] < 0:
        #         self.speed[1] = 0
        # if self.rect.bottom > self.height:
        #     if self.speed[1] > 0:
        #         self.speed[1] = 0

    def stab(self, action):
        self.action = action

    def update(self, *args):
        rect = self.rect.move(self.speed)
        if (self.world.able_walk(rect)):
            self.rect = rect
        self.image = self.get_sprite()

    def stop(self):
        self.speed = [0, 0]


def init(world):
    knight_pics = []
    knight_pics.append( pygame.image.load("res/knight_up.png") )
    knight_pics.append( pygame.image.load("res/knight_right.png") )
    knight_pics.append( pygame.image.load("res/knight_down.png") )
    knight_pics.append( pygame.image.load("res/knight_left.png") )
    knight_pics.append( pygame.image.load("res/knight_upstab.png") )
    knight_pics.append( pygame.image.load("res/knight_rightstab.png") )
    knight_pics.append( pygame.image.load("res/knight_downstab.png") )
    knight_pics.append( pygame.image.load("res/knight_leftstab.png") )


    zombie_pics = []
    zombie_pics.append( pygame.image.load("res/zombie_up.png") )
    zombie_pics.append( pygame.image.load("res/zombie_right.png") )
    zombie_pics.append( pygame.image.load("res/zombie_down.png") )
    zombie_pics.append( pygame.image.load("res/zombie_left.png") )


    knight = Character(world, knight_pics, 5)
    zombie = Character(world, zombie_pics, 3)
    return knight, zombie
