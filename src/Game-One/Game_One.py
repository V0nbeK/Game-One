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
PLAYERY = CENTRE[1]
CIRCLEPOS = CENTRE
MOUSEPOS = pygame.mouse.get_pos()

EDITMODE = False

RECTWIDTH = 10
RECTHEIGHT = 1
NOOFWALLS = 0
RADIUS = 10

ZEROINTENSITY = 0
MAXINTENSITY = 255


PLAYERCOLOR = (0,0,255)
COLOR = (random.randint(ZEROINTENSITY, MAXINTENSITY), random.randint(ZEROINTENSITY, MAXINTENSITY), random.randint(ZEROINTENSITY, MAXINTENSITY))

maps = []
walls = []


def FullCircle(COLOR,LOCATION,RADIUS):
    pygame.draw.circle(SCREEN ,COLOR ,LOCATION , RADIUS , 0)

def FullRectangle(COLOR,Length,Width ,X,Y):
    pygame.draw.rect(SCREEN, COLOR, X , Y, Length, Width, 0)

def Movement(X , Y):
    if(user_input[pygame.K_w ]):
        Y = Y - 10 
        if Y <= 0:
            Y = Y + 10 
        print("pressed up")
    elif(user_input[pygame.K_a ]):
        X = X - 10
        if X <= 0:
            X = X + 10
        print("pressed left")
    elif(user_input[pygame.K_d ]):
        X = X + 10
        if X >= SCREENWIDTH:
            X = X - 10
        print("pressed right")
    elif(user_input[pygame.K_s ]):
        Y = Y + 10
        if Y >= SCREENHEIGHT :
            Y = Y - 10   
        print("pressed down")
    CIRCLEPOS = (X,Y)
    return CIRCLEPOS

class Wall():
    def __init__(self , x , y):
        self.rect = pygame.Rect(RECTWIDTH,RECTHEIGHT,x,y) 

for i in range(0 , NOOFWALLS):
    wall = Wall(random.randint(0 , SCREENHEIGHT) , random.randint(0 , SCREENWIDTH))
    walls.append(wall)


BLACK = (0,0,0)
GREY = (80,80,80)

MOVE = True
running = False
pygame.display.update()

FullCircle(PLAYERCOLOR, CIRCLEPOS, RADIUS)
print("please press space to start the game")
while running == False:
    for events in pygame.event.get():
        user_input = pygame.key.get_pressed()
        if (user_input[pygame.K_SPACE]):
            running = True
        else:
            running = False
print("welcome to the game")
while running == True:
    SCREEN.fill(BLACK)
    for events in pygame.event.get():
        user_input = pygame.key.get_pressed()
        if (events.type == pygame.MOUSEBUTTONDOWN):
            temp = FullRectangle(GREY,10,10,MOUSEPOS[0],MOUSEPOS[1])
            walls.append(temp)
        elif(user_input[pygame.K_c]):
            COLOR = (random.randint(ZEROINTENSITY, MAXINTENSITY), random.randint(ZEROINTENSITY, MAXINTENSITY), random.randint(ZEROINTENSITY, MAXINTENSITY))
        elif(user_input[pygame.K_ESCAPE]):
            running = False
            quit
    if MOVE == True:
        CIRCLEPOS = Movement(CIRCLEPOS[0],CIRCLEPOS[1])
    FullCircle(PLAYERCOLOR, CIRCLEPOS, RADIUS)


    for i in range(0,NOOFWALLS):
        circlerect = pygame.draw.rect(SCREEN, COLOR, walls[i].rect)
        if(circlerect.colliderect(walls[i].rect)):
            print("collision : " + str(i))
            MOVE = False
        else:
            MOVE = True

    pygame.display.update()
    clock.tick(FPS)
