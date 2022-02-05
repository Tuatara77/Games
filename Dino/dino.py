import pygame
import random
import time
import sprites
import colours

fps = 60
scrollrate = 7
gravity = 15

screenwidth, screenheight = 800, 400
tilesize = 40
playerwidth, playerheight = 25, 50
playercoordx, playercoordy = 5*tilesize, screenheight-3*tilesize

def groundspawn():
    for f in range(0, screenwidth+screenwidth//2, (screenwidth//2)-20):
         Ground(f,screenheight-2*tilesize, sprites.ground)

def spawn():
    Cactus(840, screenheight-3*tilesize, random.choice(sprites.cactuslist))


class Sprite(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()

        self.rect.left = x
        self.rect.bottom = y # makes bottom left corner be the point of reference
        self.startx = x
        self.starty = y

        spriteg.add(self)
    
    def scroll(self, count):
        self.rect.x -= scrollrate
    
    def restart(self):
        self.rect.left = self.startx
        self.rect.bottom = self.starty


class Dino(Sprite):
    def __init__(self, x, y, image):
        super().__init__(x,y,image)

        self.dy = 0
        self.falling = False
        self.grounded = True

        dinog.add(self)
    
    def restart(self):
        self.image = sprites.dino_stationary
        self.rect.left = self.startx
        self.rect.bottom = self.starty
        self.dy = 0
        self.falling = False
        self.grounded = True

    def scroll(self, count):
        if count % 8 == 0:
            if self.image == sprites.dino_crouch_right and keys[pygame.K_s] or keys[pygame.K_DOWN]:
                pass
            elif self.image == sprites.dino_step_left:
                self.image = sprites.dino_step_right
            else:
                if self.image == sprites.dino_crouch_right:
                    self.image = sprites.dino_step_left
                    self.rect = self.image.get_rect()
                    self.rect.left = playercoordx
                    self.rect.bottom = playercoordy
                else:
                    self.image = sprites.dino_step_left
    
    def fall(self):
        if self.falling:
            self.dy += 1
        if self.dy > gravity:
            self.dy = gravity
        
        self.rect.y += self.dy

    def jump(self):
        if self.grounded:
            self.image = sprites.dino_stationary
            self.dy = -gravity
            self.falling = True
            self.grounded = False
    
    def crouch(self):
        if self.image != sprites.dino_crouch_right:
            self.image = sprites.dino_crouch_right
            self.rect = self.image.get_rect()
            self.rect.left = playercoordx
            self.rect.y = playercoordy

    def collide(self):
        groundcollide = pygame.sprite.spritecollide(self, groundg, False)
        for land in groundcollide:           
            self.rect.bottom = land.rect.top
            self.grounded = land
            self.falling = False
            self.dy = 0
        
        cactuscollide = pygame.sprite.spritecollide(self,cactusg,False)
        if cactuscollide:
            self.image = sprites.dino_hit
            pygame.display.flip()
            time.sleep(0.5)
            for thing in spriteg:
                thing.restart()
        

class Cactus(Sprite):
    def __init__(self, x, y, image):
        super().__init__(x,y,image)
        cactusg.add(self)

class Ground(Sprite):
    def __init__(self,x,y,image):
        super().__init__(x,y,image)
        groundg.add(self)


pygame.init()
screen = pygame.display.set_mode([screenwidth, screenheight])
pygame.display.set_caption("Dino")

spriteg = pygame.sprite.Group()
dinog = pygame.sprite.Group()
cactusg = pygame.sprite.Group()
pterag = pygame.sprite.Group()
groundg = pygame.sprite.Group()

dino = Dino(playercoordx, playercoordy, sprites.dino_stationary)
groundspawn()

pause = False
count = 0

done = False
while not done:
    pygame.time.Clock().tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
            elif event.key == pygame.K_TAB:
                for thing in spriteg:
                    thing.restart()
            elif event.key == pygame.K_LSHIFT:
                if not pause:
                    pause = True
                    scrollrate = 0
                else:
                    pause = False
                    scrollrate = 7

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] or keys[pygame.K_UP] or keys[pygame.K_w]:
        dino.jump()
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        dino.crouch()
    
    dino.fall()
    dino.collide()

    count += 1
    if count % random.randrange(70,140,35) == 0 and not pause:
        spawn()

    for thing in spriteg:
        if thing.rect.right < -tilesize:
            if thing in groundg:
                thing.rect.left = 840
            else:
                thing.kill()
        thing.scroll(count)
    
    screen.fill(colours.white)
    cactusg.draw(screen)
    pterag.draw(screen)
    dinog.draw(screen)
    groundg.draw(screen)

    pygame.display.flip()
pygame.quit()