import pygame

class wall():
    def __init__(self , x , y):
        self.rect = pygame.Rect(200,200,x,y)