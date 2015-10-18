import sys, pygame, time
pygame.init()


DIR_UP = 0
DIR_RIGHT = 1
DIR_DOWN = 2
DIR_LEFT = 3


class Character:

    def __init__(self, width, height, pictures, run = 1):
        self.sprites = []
        for pic in pictures:
            self.sprites.append( pic )
            
        self.rect = self.sprites[0].get_rect()
        self.direction = DIR_UP
        self.width, self.height = width, height
        self.speed = [0,0]
        self.run = run

    def get_sprite(self):
        return self.sprites[self.direction]

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

        if self.rect.left < 0:
            if self.speed[0] < 0:
                self.speed[0] = 0
        if self.rect.right > self.width:
            if self.speed[0] > 0:
                self.speed[0] = 0
        if self.rect.top < 0:
            if self.speed[1] < 0:
                self.speed[1] = 0
        if self.rect.bottom > self.height:
            if self.speed[1] > 0:
                self.speed[1] = 0

    def update(self):
        self.rect = self.rect.move(self.speed)
            
    def stop(self):
        self.speed = [0, 0]


def chase(zombie, knight):
    # print("Z", zombie.rect.centerx, zombie.rect.centery)
    # print("K", knight.rect.centerx, knight.rect.centery)

    if zombie.rect.centerx > knight.rect.centerx:
        zombie.move(DIR_LEFT)
    elif zombie.rect.centerx < knight.rect.centerx:
        zombie.move(DIR_RIGHT)
        
    if zombie.rect.centery > knight.rect.centery:
        zombie.move(DIR_UP)
    elif zombie.rect.centery < knight.rect.centery:
        zombie.move(DIR_DOWN)
        
    # print("ZUZU", zombie.direction, zombie.speed)
        
       
        
        

size = width, height = 640, 480
speed = [0, 0]
background = 255, 255, 255
screen = pygame.display.set_mode(size)




#zombie = pygame.image.load("zombie_up.png")
#zombie_rect = zombie.get_rect()
#zombie_rect = zombie_rect.move( [200, 200] )

#knight_rect.move( [40, 100] )

knight_pics = []
knight_pics.append( pygame.image.load("knight_up.png") )
knight_pics.append( pygame.image.load("knight_right.png") )
knight_pics.append( pygame.image.load("knight_down.png") )
knight_pics.append( pygame.image.load("knight_left.png") )
        
 
zombie_pics = []     
zombie_pics.append( pygame.image.load("zombie_up.png") )
zombie_pics.append( pygame.image.load("zombie_right.png") )
zombie_pics.append( pygame.image.load("zombie_down.png") )
zombie_pics.append( pygame.image.load("zombie_left.png") )
 
 
knight = Character(width, height, knight_pics, 2)
zombie = Character(width, height, zombie_pics)
#zombie.move(DIR_RIGHT)


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                knight.move(DIR_LEFT);
            if event.key == pygame.K_RIGHT:
                knight.move(DIR_RIGHT);
            if event.key == pygame.K_UP:
                knight.move(DIR_UP);
            if event.key == pygame.K_DOWN:
                knight.move(DIR_DOWN);
        if event.type == pygame.KEYUP:
            knight.stop()

    knight.update()
    

    chase(zombie, knight)
            
            
    zombie.update()
    screen.fill(background)
    screen.blit(knight.get_sprite(), knight.rect)
    screen.blit(zombie.get_sprite(), zombie.rect)
    #screen.blit(zombie, zombie_rect)
    
    pygame.display.flip()
    time.sleep(0.01)