import sys, pygame, time
from character import Character, DIR_DOWN, DIR_LEFT, DIR_RIGHT, DIR_UP


pygame.init()






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
        
def collision(zombie, knight):
    if pygame.sprite.collide_rect(zombie, knight):
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








size = width, height = 640, 480
speed = [0, 0]
background = 255, 255, 255
screen = pygame.display.set_mode(size)




#zombie = pygame.image.load("zombie_up.png")
#zombie_rect = zombie.get_rect()
#zombie_rect = zombie_rect.move( [200, 200] )

#knight_rect.move( [40, 100] )

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
 
 
knight = Character(width, height, knight_pics, 2)
zombie = Character(width, height, zombie_pics)
#zombie.move(DIR_RIGHT)

for i in range(100):
    zombie.move(DIR_RIGHT)
    zombie.update()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
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

    knight.update()
    

    chase(zombie, knight)
   
    result = collision(zombie, knight)
    if result != "":
        print(result)
        sys.exit()
            

    zombie.update()
    screen.fill(background)
    screen.blit(knight.get_sprite(), knight.rect)
    screen.blit(zombie.get_sprite(), zombie.rect)
    #screen.blit(zombie, zombie_rect)
    
    pygame.display.flip()
    time.sleep(0.01)