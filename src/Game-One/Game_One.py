#Import statements are to enable the code to use the functions from the library
import pygame
import sys
import os
import random
from pygame.locals import *

#instructions to windows to center the game window in the center of
#the screen, which it might ignore
os.environ["SDL_VIDEO_CENTERED"] = "1"

#initialize pygame
pygame.init()

#Right way
SCREENWIDTH = 1000
SCREENHEIGHT = 700
SCREENSIZE = [SCREENWIDTH, SCREENHEIGHT]
SCREEN = pygame.display.set_mode(SCREENSIZE)

#caption for the game
pygame.display.set_caption("My first game in pygame")

RADIUS = 20
ZEROINTENSITY = 0
MAXINTENSITY = 255

X = 40
Y = 40
CIRCLEPOS = (X, Y)
COLOR = (random.randint(ZEROINTENSITY, MAXINTENSITY), random.randint(ZEROINTENSITY, MAXINTENSITY), random.randint(ZEROINTENSITY, MAXINTENSITY))
circlerect = pygame.draw.circle(SCREEN, COLOR, CIRCLEPOS, RADIUS)
pygame.display.update(circlerect)

#Draw a rectangle to collide with
RECTWIDTH = 100
RECTHEIGHT = 20
NOOFWALLS = 100



class Wall():
    def __init__(self , x ,y):
        self.rect = pygame.Rect(x,y,RECTWIDTH,RECTHEIGHT) 


walls = []

for i in range(0 , NOOFWALLS):
    wall = Wall(random.randint(0 ,SCREENHEIGHT),random.randint(0,SCREENWIDTH))
    walls.append(wall)





BLACK = (0,0,0)

while True:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if (events.type == pygame.MOUSEBUTTONDOWN):
            COLOR = (random.randint(ZEROINTENSITY, MAXINTENSITY), random.randint(ZEROINTENSITY, MAXINTENSITY), random.randint(ZEROINTENSITY, MAXINTENSITY))
            #note- we have skipped the last parameter and by default, 0 is taken
            circlerect = pygame.draw.circle(SCREEN, COLOR, CIRCLEPOS, RADIUS)
            pygame.display.update(circlerect)

    user_input = pygame.key.get_pressed()
    
    if(user_input[pygame.K_UP]):
        Y=Y-1
        if(SCREENHEIGHT):Y=0
    elif(user_input[pygame.K_LEFT]):
        X=X-1
        if(SCREENWIDTH):X=0
    CIRCLEPOS = (X,Y)

#Loop to check for collisions against all of the walls
    SCREEN.fill(BLACK)
    circlerect = pygame.draw.circle(SCREEN, COLOR, CIRCLEPOS, RADIUS)
    
    for i in range(0,NOOFWALLS):
        pygame.draw.rect(SCREEN, COLOR, walls[i].rect)
        if(circlerect.colliderect(walls[i].rect)):
            print("collision : " + str(i))
    pygame.display.update()

