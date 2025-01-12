#Import statements are to enable the code to use the functions from the library
from re import X
import pygame
import sys
import os
import random

from custom_classes import wall
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
CIRCLEPOS = CENTRE

COLLISION = False

LEFT = 10
TOP = 10

RADIUS = 10

ZEROINTENSITY = 0
MAXINTENSITY = 255

COUNT = 0

BLACK = (0,0,0)
GREY = (80,80,80)
ObjectiveGold = (83,69,22)
RED = (255,0,0)
TEAL = (00,80,80) 
WHITE =(255,255,255)
COLOR = (random.randint(ZEROINTENSITY, MAXINTENSITY), random.randint(ZEROINTENSITY, MAXINTENSITY), random.randint(ZEROINTENSITY, MAXINTENSITY))

walls = []

#Setup map
def generate_walls(gapSize):
    wallHeight = 100
    xLocation = random.randint(100, SCREENWIDTH - 100)
    yLocation = SCREENHEIGHT * 2 / 3

    walls.append(pygame.Rect(0, yLocation, xLocation, wallHeight))
    walls.append(pygame.Rect(xLocation + gapSize, yLocation, SCREENWIDTH, wallHeight))

generate_walls(100)
playerColour = RED

def display(inputWalls, spriteX, spriteY, spriteColour):
    # draw all the walls
    for i in walls:
        pygame.draw.rect(SCREEN, GREY, i)

    # draw sprite
    player_sprite(spriteColour , spriteX , spriteY , RADIUS)

def player_sprite(COLOR, X , Y, RADIUS):
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
    pygame.draw.rect(SCREEN , COLOR , rect1 , 0 )
    return rect1

def FullCircle(COLOR,LOCATION,RADIUS):
    pygame.draw.circle(SCREEN ,COLOR ,LOCATION , RADIUS , 0)

def FullRectangle(COLOR, RECTHEIGHT , RECTWIDTH , X , Y ):
    RECTWIDTH = 10
    RECTHEIGHT = 10
    RECTCOORD = (X , Y , RECTWIDTH , RECTHEIGHT)
    rect1 = pygame.Rect(RECTCOORD)
    pygame.draw.rect(SCREEN, COLOR, rect1 , 0)

def gravity(X ,Y):
    Y = Y + 10
    if Y < 0:
        Y = SCREENHEIGHT
    elif COLLISION == True:
        MOVE == False
    CIRCLEPOS = (X,Y)
    return CIRCLEPOS

def Movement(X, Y):
    existingX = X
    existingY = Y

    if (user_input[pygame.K_w ]):
        Y = Y - 50 
        if Y <= 0:
            Y = SCREENHEIGHT 
            
    if(user_input[pygame.K_a ]):
        X = X - 10
        if X <= 0:
            X = 0
    
    if(user_input[pygame.K_d ]):
        X = X + 10
        if X >= SCREENWIDTH:
            X = SCREENWIDTH
            
    if(user_input[pygame.K_s ]):
        Y = Y + 10
        if Y >= SCREENHEIGHT :
            Y = 0

    finalLocation = gravity(X,Y)

    #Check collisions 
    collided = False
    newSprite = player_sprite(playerColour, finalLocation[0], finalLocation[1], RADIUS)
    for wall in walls:
        if (newSprite.colliderect(wall)):
            collided = True
            break

    if (collided):
        CIRCLEPOS = [existingX, existingY]
    else:
        CIRCLEPOS = finalLocation
        
    return CIRCLEPOS



MOVE = True
running = False

FullCircle(RED, CIRCLEPOS, RADIUS)

pygame.display.update()

print("please press space to start the game")
while running == False:
    SCREEN.fill(GREY)
    pygame.draw.circle(SCREEN, BLACK, CENTRE, 100 , 0)
    for events in pygame.event.get():
        user_input = pygame.key.get_pressed()
        if (user_input[pygame.K_SPACE]):
            running = True
        else:
            running = False
    pygame.display.update()

print("welcome to the game")
while running == True:
    SCREEN.fill(TEAL)
    
    for events in pygame.event.get():
        user_input = pygame.key.get_pressed()
        if(user_input[pygame.K_c]):
            COLOR = (random.randint(ZEROINTENSITY, MAXINTENSITY), random.randint(ZEROINTENSITY, MAXINTENSITY), random.randint(ZEROINTENSITY, MAXINTENSITY))
        elif(user_input[pygame.K_ESCAPE]):
            running = False
            quit
   
    CIRCLEPOS = Movement(CIRCLEPOS[0],CIRCLEPOS[1])
     
    COUNT = COUNT + 1
    if COUNT >= 30:
        if (COUNT % 30) == 0:
            if playerColour == RED:
                playerColour = WHITE
            else:
                playerColour = RED
    elif COUNT >= 1000:
        COUNT ==0
    
    display(walls, CIRCLEPOS[0], CIRCLEPOS[1], playerColour )    

    pygame.display.update()
    clock.tick(FPS)

