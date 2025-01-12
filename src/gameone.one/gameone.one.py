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

pygame.display.set_caption("My first game in pygame")
clock = pygame.time.Clock()
FPS = 30


SCREENWIDTH = 1500
SCREENHEIGHT = 800
SCREENSIZE = [SCREENWIDTH, SCREENHEIGHT]
SCREEN = pygame.display.set_mode(SCREENSIZE)
CENTRE = [(SCREENWIDTH/2) ,(SCREENHEIGHT/2)]


PLAYERX = CENTRE[0]
PLAYERY = 0
CIRCLEPOS = CENTRE

COLLISION = False

LEFT = 10
TOP = 10
RECTWIDTH = 100
RECTHEIGHT = 100
NOOFWALLS = 0
RADIUS = 10
RECTCOORD = (LEFT , TOP , RECTWIDTH , RECTHEIGHT)
rect1 = pygame.Rect(RECTCOORD)

ZEROINTENSITY = 0
MAXINTENSITY = 255

COUNT = 0

BLACK = (0,0,0)
GREY = (80,80,80)
ObjectiveGold = (83,69,22)
PLAYERCOLOR = (255,0,0)
TEAL = (00,80,80) 
WHITE =( 255 , 255 , 255 )
COLOR = (random.randint(ZEROINTENSITY, MAXINTENSITY), random.randint(ZEROINTENSITY, MAXINTENSITY), random.randint(ZEROINTENSITY, MAXINTENSITY))

COINS = []
maps = []
walls = []


        

def FullCircle(COLOR,LOCATION,RADIUS):
    pygame.draw.circle(SCREEN ,COLOR ,LOCATION , RADIUS , 0)

def FullRectangle(COLOR, RECTHEIGHT , RECTWIDTH , X , Y ):
    RECTWIDTH = 10
    RECTHEIGHT = 10
    RECTCOORD = (X , Y , RECTWIDTH , RECTHEIGHT)
    rect1 = pygame.Rect(RECTCOORD)
    pygame.draw.rect(SCREEN, COLOR, rect1 , 0)

def Movement(X , Y):
    if (user_input[pygame.K_w ]):
        Y = Y - 100 
        if Y <= 0:
            Y = SCREENHEIGHT  
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
            Y = 0  
    CIRCLEPOS = (X,Y)
    return CIRCLEPOS

def gravity(X ,Y):
    Y = Y + 10
    if Y < 0:
        Y = SCREENHEIGHT
    elif COLLISION == True:
        MOVE == False
    CIRCLEPOS = (X,Y)
    return CIRCLEPOS

class SpawnObjectivePoint:
    def __init__(self,POS):
        pygame.draw.circle(SCREEN , ObjectiveGold ,POS, 30 , 0)

class PlayerSprite:
    def __init__(self,COLOR,POS, RADIUS):
        self.POS = POS
        X = POS[0]
        Y = POS[1]
        RECTWIDTH = 30
        RECTHEIGHT = 10
        RECTCOORD = (X , Y + 5 , RECTWIDTH , RECTHEIGHT)
        rect1 = pygame.Rect(RECTCOORD)
        POS = ( X + 40 , Y )
        FullCircle( COLOR , POS , RADIUS)
        POS = ( X - 10 , Y )
        FullCircle( COLOR , POS , RADIUS)
        pygame.draw.rect(SCREEN , TEAL , rect1 , 0 )
        RECTCOORD = (X , Y , RECTWIDTH , RECTHEIGHT)
        pygame.draw.rect(SCREEN , PLAYERCOLOR , rect1 , 0 )

class Wall():
    def __init__(self , x , y):
        self.rect = pygame.Rect(RECTWIDTH,RECTHEIGHT,x,y) 

for i in range(0 , NOOFWALLS):
    left = 10
    top = 10
    rectwidth = SCREENWIDTH
    rectheight = 50
    RECTCOORD = (left , top , rectwidth , rectheight)
    rect1 = pygame.Rect(RECTCOORD)
    wall = Wall(0 , random.randint(0 , SCREENHEIGHT))
    walls.append(wall)

MOVE = True
running = False
pygame.display.update()

print("please press space to start the game")

while running == False:
    SCREEN.fill(GREY)
    POS = CENTRE
    pygame.draw.circle(SCREEN , BLACK , POS , 100 , 0)
    POS = (CENTRE[0]-40,CENTRE[1]-15)
    pygame.draw.circle(SCREEN , WHITE , POS , 20 , 0)
    POS = (CENTRE[0]+40,CENTRE[1]-15)
    pygame.draw.circle(SCREEN , WHITE , POS , 20 , 0)
    POS = (CENTRE[0],CENTRE[1]+30)
    pygame.draw.circle(SCREEN , WHITE , POS , 20 , 0)
    POS = (CENTRE[0],CENTRE[1]+25)
    pygame.draw.circle(SCREEN , BLACK , POS , 20 , 0)
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
    MOUSEPOS = pygame.mouse.get_pos()
    for events in pygame.event.get():
        user_input = pygame.key.get_pressed()
        if (events.type == pygame.MOUSEBUTTONDOWN):
            FullRectangle(GREY , 100 , 100 , MOUSEPOS[0] , MOUSEPOS[1])
        elif(user_input[pygame.K_c]):
            COLOR = (random.randint(ZEROINTENSITY, MAXINTENSITY), random.randint(ZEROINTENSITY, MAXINTENSITY), random.randint(ZEROINTENSITY, MAXINTENSITY))
        elif(user_input[pygame.K_ESCAPE]):
            running = False
            quit

    if MOVE == True:
        CIRCLEPOS = Movement(CIRCLEPOS[0],CIRCLEPOS[1])
    if COLLISION == False:
        CIRCLEPOS = gravity(CIRCLEPOS[0],CIRCLEPOS[1])
    PlayerSprite(PLAYERCOLOR ,CIRCLEPOS , RADIUS)


    for i in range(0,NOOFWALLS):
        player = PlayerSprite(PLAYERCOLOR , CIRCLEPOS, RADIUS)
        centrewall = FullRectangle(GREY , 100 , 100 , CENTRE[0] , CENTRE[1])
        if player.sprite.colliderect(centrewall.CENTER):
            print("collision : " + str(i))
            COLLISION = True 
            MOVE = False
        else:
            MOVE = True
            COLLISION = False
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
