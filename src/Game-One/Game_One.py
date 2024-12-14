#Import statements are to enable the code to use the functions from the library
import pygame.draw
import pygame.mouse
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

pygame.display.set_caption("My first game in pygame")

SCREENWIDTH = 1500
SCREENHEIGHT = 700
SCREENSIZE = [SCREENWIDTH, SCREENHEIGHT]
SCREEN = pygame.display.set_mode(SCREENSIZE)
CENTRE = [(SCREENWIDTH/2) ,(SCREENHEIGHT/2)]
X = CENTRE[0]
Y = CENTRE[1]
CIRCLEPOS = CENTRE
MOUSEPOS = pygame.mouse.get_pos()
EDITMODE = False

RECTWIDTH = 100
RECTHEIGHT = 20
NOOFWALLS = 0
RECTCOORD = [ X , Y , RECTWIDTH , RECTHEIGHT ]
Rect1 = pygame.Rect(RECTCOORD)

RADIUS = 10
ZEROINTENSITY = 0
MAXINTENSITY = 255

COLOR = (random.randint(ZEROINTENSITY, MAXINTENSITY), random.randint(ZEROINTENSITY, MAXINTENSITY), random.randint(ZEROINTENSITY, MAXINTENSITY))
circlerect = pygame.draw.circle(SCREEN, COLOR, CIRCLEPOS, RADIUS)
pygame.display.update(circlerect)

RECTWIDTH = 100
RECTHEIGHT = 20
NOOFWALLS = 0
MAPSIZE = 0

maps = [[],[]]
walls = []

def FullCircle(COLOR,LOCATION,RADIUS):
    pygame.draw.circle(SCREEN ,COLOR ,LOCATION , RADIUS , 0)

class Wall():
    def __init__(self , POSITION):
        self.rect = pygame.Rect(POSITION,RECTWIDTH,RECTHEIGHT) 

for i in range(0 , NOOFWALLS):
    wall = Wall(MOUSEPOS)
    walls.append(wall)



BLACK = (0,0,0)
GREY = (80,80,80)

running = True

while running:
    user_input = pygame.key.get_pressed()
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif (events.type == pygame.MOUSEBUTTONDOWN) and EDITMODE == True:
            FullCircle(GREY,MOUSEPOS,10)
            maps.append([GREY,MOUSEPOS,10])
            
        elif (user_input[pygame.K_e]):
            if EDITMODE == True:
                EDITMODE = False
                print("editmode has been turned off")
            else:
                EDITMODE = True
                print("editmode has been turned on")
    
    if(user_input[pygame.K_w ]):
        Y = Y - 1 
        if Y <= 0:
            Y = Y + 1 
    elif(user_input[pygame.K_a ]):
        X = X - 1
        if X <= 0:
            X = X + 1
    elif(user_input[pygame.K_d ]):
        X = X + 1
        if X >= SCREENWIDTH:
            X = X - 1
    elif(user_input[pygame.K_s ]):
        Y = Y + 1
        if Y >= SCREENHEIGHT :
            Y = Y - 1
    elif(user_input[pygame.K_c]):
        COLOR = (random.randint(ZEROINTENSITY, MAXINTENSITY), random.randint(ZEROINTENSITY, MAXINTENSITY), random.randint(ZEROINTENSITY, MAXINTENSITY))
        circlerect = pygame.draw.circle(SCREEN, COLOR, CIRCLEPOS, RADIUS)
        pygame.display.update(circlerect)
    elif(user_input[pygame.K_ESCAPE]):
        running = False
        quit



    SCREEN.fill(BLACK)
    circlerect = pygame.draw.circle(SCREEN, COLOR, CIRCLEPOS, RADIUS)
    CIRCLEPOS = (X,Y)

    for i in range(0,NOOFWALLS):
        pygame.draw.rect(SCREEN, COLOR, walls[i].rect)
        if(circlerect.colliderect(walls[i].rect)):
            print("collision : " + str(i))
            
    pygame.display.update()

