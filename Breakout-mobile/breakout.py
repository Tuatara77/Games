import pygame
import random
import time
import colours

screenwidth = 1600
screenheight = 900

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


class Ball(Sprite):
	def __init__(self, x, y):
		super().__init__(x,y,10,10,colours.white)
		self.velx = random.randint(-5,5)
		self.vely = random.choice([-5,5])
		self.startx = x
		self.starty = y
		
		ballg.add(self)
	
	def hit(self):
		paddlehit = pygame.sprite.spritecollide(self, paddleg, False)
		boxhit = pygame.sprite.spritecollide(self,boxg, True)
		if paddlehit or boxhit:
			self.vely *= -1
			self.velx = random.randint(-5,5)
			
	def move(self):
		if self.rect.left <= -1:
			self.velx *= -1
		elif self.rect.right >= screenwidth:
			self.velx *= -1
		elif self.rect.top <= -1:
			self.vely *= -1
		
		if self.rect.bottom >= screenheight:
			time.sleep(1)
			self.rect.centerx = self.startx
			self.rect.centery = self.starty
		
		self.rect.x += self.velx
		self.rect.y += self.vely
		

class Box(Sprite):
	def __init__(self, x, y):
		super().__init__(x,y,46,10,colours.random_colour())
		boxg.add(self)


pygame.init()
screen = pygame.display.set_mode([screenwidth, screenheight])

paddleg = pygame.sprite.Group()
ballg = pygame.sprite.Group()
boxg = pygame.sprite.Group()

paddle = Paddle(screenwidth/2, screenheight-40)
ball = Ball(screenwidth/2, screenheight/2)

for g in range(48, 256, 16):
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
		
	ball.move()
	ball.hit()
	
	screen.fill(colours.black)
	boxg.draw(screen)
	ballg.draw(screen)
	paddleg.draw(screen)
	
	pygame.display.flip()
pygame.quit()