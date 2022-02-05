import pygame
import colours

tilesize = 40

ground = pygame.image.load("./sprites/ground.png")
ground.set_colorkey(colours.white)

dino_stationary = pygame.image.load("./sprites/dino/dino.png")
dino_step_left = pygame.image.load("./sprites/dino/dino-step-left.png")
dino_step_right = pygame.image.load("./sprites/dino/dino-step-right.png")
dino_hit = pygame.image.load("./sprites/dino/dino-hit.png")
dino_crouch_right = pygame.image.load("./sprites/dino/dino-crouch-right.png")

cactus_1 = pygame.image.load("./sprites/cactus/cactus-1.png")
cactus_1_big = pygame.image.load("./sprites/cactus/cactus-1-big.png")
cactus_2 = pygame.image.load("./sprites/cactus/cactus-2.png")
cactus_2_big = pygame.image.load("./sprites/cactus/cactus-2-big.png")
cactus_3 = pygame.image.load("./sprites/cactus/cactus-3.png")

dino_stationary.set_colorkey(colours.white)
dino_step_left.set_colorkey(colours.white)
dino_step_right.set_colorkey(colours.white)
dino_hit.set_colorkey(colours.white)
dino_crouch_right.set_colorkey(colours.white)

cactus_1.set_colorkey(colours.white)
cactus_1_big.set_colorkey(colours.white)
cactus_2.set_colorkey(colours.white)
cactus_2_big.set_colorkey(colours.white)
cactus_3.set_colorkey(colours.white)

# pygame.transform.scale(dino_crouch_right, [28,59])

cactuslist = [cactus_1, cactus_1_big, cactus_2, cactus_2_big, cactus_3]