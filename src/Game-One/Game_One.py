#Import statements are to enable the code to use the functions from the library
from tkinter import LEFT
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
clock = pygame.time.Clock()
FPS = 30


SCREENWIDTH = 1500
SCREENHEIGHT = 800
SCREENSIZE = [SCREENWIDTH, SCREENHEIGHT]
SCREEN = pygame.display.set_mode(SCREENSIZE)
CENTRE = [(SCREENWIDTH/2) ,(SCREENHEIGHT/2)]


PLAYERX = CENTRE[0]
PLAYERY = CENTRE[1]
CIRCLEPOS = CENTRE
MOUSEPOS = pygame.mouse.get_pos()

COLLISION = False

LEFT = 10
TOP = 10
RECTWIDTH = 10
RECTHEIGHT = 10
NOOFWALLS = 0
RADIUS = 10
RECTCOORD = (LEFT , TOP , RECTWIDTH , RECTHEIGHT)
rect1 = pygame.Rect(RECTCOORD)

ZEROINTENSITY = 0
MAXINTENSITY = 255

GravitationalPull = 10
COUNT = 0

BLACK = (0,0,0)
GREY = (80,80,80)
ObjectiveGold = (83,69,22)
PLAYERCOLOR = (255,0,0)
TEAL = (00,80,80) 
WHITE =( 255 , 255 , 255 )
COLOR = (random.randint(ZEROINTENSITY, MAXINTENSITY), random.randint(ZEROINTENSITY, MAXINTENSITY), random.randint(ZEROINTENSITY, MAXINTENSITY))

maps = []
walls = []

def PlayerSprite(COLOR, X , Y, RADIUS):
    RECTWIDTH = 10
    RECTHEIGHT = 10
    RECTCOORD = (X , Y + 5 , RECTWIDTH , RECTHEIGHT)
    rect1 = pygame.Rect(RECTCOORD)
    POS = ( X , Y )
    FullCircle( COLOR , POS , RADIUS)
    pygame.draw.rect(SCREEN , TEAL , rect1 , 0 )
    RECTCOORD = (X , Y - 5 , RECTWIDTH , RECTHEIGHT)
    pygame.draw.rect(SCREEN , PLAYERCOLOR , rect1 , 0 )


def FullCircle(COLOR,LOCATION,RADIUS):
    pygame.draw.circle(SCREEN ,COLOR ,LOCATION , RADIUS , 0)

def FullRectangle(COLOR, RECTHEIGHT , RECTWIDTH , X , Y ):
    RECTWIDTH = 10
    RECTHEIGHT = 10
    RECTCOORD = (X , Y , RECTWIDTH , RECTHEIGHT)
    rect1 = pygame.Rect(RECTCOORD)
    pygame.draw.rect(SCREEN, COLOR, rect1 , 0)

def Movement(X , Y):
    if(user_input[pygame.K_w ]):
        Y = Y - 20 
        if Y <= 0:
            Y = 0
    elif(user_input[pygame.K_a ]):
        X = X - 10
        if X <= 0:
            X = 0
    elif(user_input[pygame.K_d ]):
        X = X + 10
        if X >= SCREENWIDTH:
            X = SCREENWIDTH
    elif(user_input[pygame.K_s ]):
        Y = Y + 10
        if Y >= SCREENHEIGHT :
            Y = SCREENHEIGHT  
    CIRCLEPOS = (X,Y)
    return CIRCLEPOS

def gravity(X ,Y):
    print("down")
    Y = Y + 10
    if Y <= 0:
        Y = 0
    elif COLLISION == True:
        MOVE == False
    CIRCLEPOS = (X,Y)
    return CIRCLEPOS

def SpawnObjectivePoint(X,Y):
    pygame.draw.circle(SCREEN , ObjectiveGold ,X , Y , 30 , 0)

class Wall():
    def __init__(self , x , y):
        self.rect = pygame.Rect(RECTWIDTH,RECTHEIGHT,x,y) 

for i in range(0 , NOOFWALLS):
    wall = Wall(random.randint(0 , SCREENWIDTH) , random.randint(0 , SCREENHEIGHT))
    walls.append(wall)

MOVE = True
running = False

FullCircle(PLAYERCOLOR, CIRCLEPOS, RADIUS)

pygame.display.update()
print("please press space to start the game")
while running == False:
    SCREEN.fill(GREY)
    pygame.draw.circle(SCREEN , BLACK , CENTRE , 100 , 0)
    for events in pygame.event.get():
        user_input = pygame.key.get_pressed()
        if (user_input[pygame.K_SPACE]):
            running = True
        else:
            running = False
    pygame.display.update()

print("welcome to the game")

while running == True:
    SCREEN.fill(BLACK)
    for events in pygame.event.get():
        user_input = pygame.key.get_pressed()
        if (events.type == pygame.MOUSEBUTTONDOWN):
            FullRectangle(GREY , 10 , 10 , MOUSEPOS[0] , MOUSEPOS[1])
            walls.append(FullRectangle(GREY , 10 , 10 , MOUSEPOS[0] , MOUSEPOS[1]))
        elif(user_input[pygame.K_c]):
            COLOR = (random.randint(ZEROINTENSITY, MAXINTENSITY), random.randint(ZEROINTENSITY, MAXINTENSITY), random.randint(ZEROINTENSITY, MAXINTENSITY))
        elif(user_input[pygame.K_ESCAPE]):
            running = False
            quit

    if MOVE == True:
        CIRCLEPOS = Movement(CIRCLEPOS[0],CIRCLEPOS[1])
        gravity(CIRCLEPOS[0],CIRCLEPOS[1])
    PlayerSprite(PLAYERCOLOR , CIRCLEPOS[0] , CIRCLEPOS[1] , RADIUS)


    for i in range(0,NOOFWALLS):
        circlerect = pygame.draw.rect(SCREEN, COLOR, walls[i].rect)
        if(circlerect.colliderect(walls[i].rect)):
            print("collision : " + str(i))
            COLLISION = True
            MOVE = False
        else:
            MOVE = True

    COUNT = COUNT + 1
    if COUNT >= 30:
        if (COUNT % 30) == 0:
            if PLAYERCOLOR == (255,0,0):
                PLAYERCOLOR = (255,255,255)
            else:
                PLAYERCOLOR = (255,0,0)
    elif (COUNT % 500) == 0:
        SpawnObjectivePoint(random.ranint(0,SCREENWIDTH),random.ranint(0,SCREENHEIGHT))
    elif COUNT >= 1000:
        COUNT ==0

    pygame.display.update()
    clock.tick(FPS)
