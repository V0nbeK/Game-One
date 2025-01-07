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
SCREENHEIGHT = 700
SCREENSIZE = [SCREENWIDTH, SCREENHEIGHT]
SCREEN = pygame.display.set_mode(SCREENSIZE)
CENTRE = [(SCREENWIDTH/2) ,(SCREENHEIGHT/2)]
PLAYERX = CENTRE[0]
PLAYERY = CENTRE[1]
CIRCLEPOS = CENTRE
MOUSEPOS = pygame.mouse.get_pos()
EDITMODE = False
RECTWIDTH = 100
RECTHEIGHT = 20
NOOFWALLS = 0
RECTCOORD = [ PLAYERX , PLAYERY , RECTWIDTH , RECTHEIGHT ]
Rect1 = pygame.Rect(RECTCOORD)
RADIUS = 10
ZEROINTENSITY = 0
MAXINTENSITY = 255
RECTWIDTH = 100
RECTHEIGHT = 20
NOOFWALLS = 0
MAPSIZE = 0
COLOR = (random.randint(ZEROINTENSITY, MAXINTENSITY), random.randint(ZEROINTENSITY, MAXINTENSITY), random.randint(ZEROINTENSITY, MAXINTENSITY))

maps = []
walls = []

def FullCircle(COLOR,LOCATION,RADIUS):
pygame.draw.circle(SCREEN ,COLOR ,LOCATION , RADIUS , 0)

def FullRectangle(COLOR,Length,Width ,X ,Y):
RectCoord = [X, Y, Length, Width]
Rect1 = pygame.Rect(RectCoord)
pygame.draw.rect(SCREEN, COLOR, Rect1, 0)

def Movement(X , Y):
if(user_input[pygame.K_w ]):
    Y = Y - 1 
    if Y <= 0:
        Y = Y + 1 
    print("pressed up")
elif(user_input[pygame.K_a ]):
    X = X - 1
    if X <= 0:
        X = X + 1
    print("pressed up")
elif(user_input[pygame.K_d ]):
    X = X + 1
    if X >= SCREENWIDTH:
        X = X - 1
    print("pressed up")
elif(user_input[pygame.K_s ]):
    Y = Y + 1
    if Y >= SCREENHEIGHT :
        Y = Y - 1   
    print("pressed up")
PLAYERX = X
PLAYERY = Y
return PLAYERX and PLAYERY
class Wall():
def __init__(self , POSITION):
    self.rect = pygame.Rect(POSITION,RECTWIDTH,RECTHEIGHT) 

for i in range(0 , NOOFWALLS):
wall = Wall(MOUSEPOS)
walls.append(wall)



BLACK = (0,0,0)
GREY = (80,80,80)

running = True
MOVE = True

print("before game loop")

while running:
print("just stared running")
for events in pygame.event.get():
    user_input = pygame.key.get_pressed()
    print("geting inputs")
    if (events.type == pygame.MOUSEBUTTONDOWN) and EDITMODE == True:
        FullCircle(GREY,MOUSEPOS)
        maps.append([GREY,MOUSEPOS,10])  
        print("in edit mode")
    elif (user_input[pygame.K_e]):
        if EDITMODE == True:
            EDITMODE = False
            print("editmode has been turned off")
        else:
            EDITMODE = True
            print("editmode has been turned on")
            
    elif(user_input[pygame.K_c]):
        COLOR = (random.randint(ZEROINTENSITY, MAXINTENSITY), random.randint(ZEROINTENSITY, MAXINTENSITY), random.randint(ZEROINTENSITY, MAXINTENSITY))
    
    elif(user_input[pygame.K_ESCAPE]):
        running = False
        quit
        
Movement(PLAYERX,PLAYERY)

SCREEN.fill(BLACK)
CIRCLEPOS = (PLAYERX,PLAYERY)
circlerect = pygame.draw.circle(SCREEN, COLOR, CIRCLEPOS, RADIUS)

print("about to start collisions")
for i in range(0,NOOFWALLS):
    pygame.draw.rect(SCREEN, COLOR, walls[i].rect)
    if(circlerect.colliderect(walls[i].rect)):
        print("collision : " + str(i))
        MOVE = False
    else:
        MOVE = True
print("update and fps")
clock.tick(FPS)
pygame.display.update()

pygame.display.update()

