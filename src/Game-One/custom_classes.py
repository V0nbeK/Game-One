import pygame

class wall():
    def __init__(self, height, width, x , y):
        self.rect = pygame.Rect(x, y, height, width)