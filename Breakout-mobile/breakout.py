import pygame
import random
import time
import colours

screenwidth = 720
screenheight = 1080

ballvel = 6
rowcount = 13
fps = 120

class Sprite(pygame.sprite.Sprite):
	def __init__(self, x, y, xsize, ysize, colour):
		super().__init__()
		self.image = pygame.Surface([xsize,ysize])
		self.rect = self.image.get_rect()
		self.image.fill(colour)
		
		self.rect.centerx = x
		self.rect.centery = y


class Paddle(Sprite):
	def __init__(self,x, y):
		super().__init__(x,y,70,10,colours.white)
		paddleg.add(self)
	
	def move(self, dx):
		self.rect.centerx = dx
		if self.rect.left <= -1:
			self.rect.left = 0
		elif self.rect.right >= screenwidth:
			self.rect.right = screenwidth
	
	def collide(self):
		powerupcollide = pygame.sprite.spritecollide(self, powerupg, True)
		if powerupcollide:
			for _ in range(3):
				Ball(self.rect.centerx, self.rect.centery-20)


class Ball(Sprite):
	def __init__(self, x, y):
		super().__init__(x,y,10,10,colours.white)
		self.velx = random.randint(-ballvel, ballvel)
		self.vely = -ballvel
		
		ballg.add(self)
	
	def hit(self):
		paddlehit = pygame.sprite.spritecollide(self, paddleg, False)
		if paddlehit:
			self.vely *= -1
			self.velx = random.randint(-ballvel, ballvel)
		
		boxhit = pygame.sprite.spritecollide(self,boxg, True)
		if boxhit:
			self.vely *= -1
			self.velx = random.randint(-ballvel, ballvel)
			chance = random.randint(1,4)
			if chance == 1:
					Powerup(self.rect.centerx, self.rect.centery)
					
	def move(self):
		if self.rect.left <= -1:
			self.velx *= -1
			self.rect.left = 0
		elif self.rect.right >= screenwidth:
			self.velx *= -1
			self.rect.right = screenwidth
		elif self.rect.top <= -1:
			self.vely *= -1
			self.rect.top = 0
		
		if self.rect.bottom >= screenheight:
			self.kill()
		
		self.rect.x += self.velx
		self.rect.y += self.vely

	
class Powerup(Sprite):
	def __init__(self,x,y):
		super().__init__(x,y,15,15,colours.white)
		powerupg.add(self)
	
	def move(self):
		self.rect.y += 1

class Box(Sprite):
	def __init__(self, x, y):
		super().__init__(x,y,46,10,colours.random_colour())
		boxg.add(self)


pygame.init()
screen = pygame.display.set_mode([screenwidth, screenheight])

paddleg = pygame.sprite.Group()
ballg = pygame.sprite.Group()
boxg = pygame.sprite.Group()
powerupg = pygame.sprite.Group()

paddle = Paddle(screenwidth/2, screenheight-40)
ball = Ball(screenwidth/2, screenheight/2)

for g in range(48, (rowcount+3)*16, 16):
	for f in range(26,screenwidth,52):
		Box(f,g)

done = False
while not done:
	pygame.time.Clock().tick(fps)
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				done = True

	mousepos = pygame.mouse.get_pos()
	
	if mousepos[0] != paddle.rect.centerx:
		paddle.move(mousepos[0])
	
	for b in ballg:
		b.move()
		b.hit()
	for p in powerupg:
		p.move()
	paddle.collide()
	
	screen.fill(colours.black)
	boxg.draw(screen)
	ballg.draw(screen)
	powerupg.draw(screen)
	paddleg.draw(screen)
	
	if len(ballg) == 0:
		done = True
		time.sleep(0.5)
	
	pygame.display.flip()
pygame.quit()
