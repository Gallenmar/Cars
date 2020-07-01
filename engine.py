import pygame
import random
import array as arr
pygame.init()

FRAMERATE = 400
#JUMPHEIGHT = 300
#XSTEP = 2  # how much alien moves side to side
WIDTH = 532; HEIGHT = 850
#XDIM = 50; YDIM = 10 # X and Y dimention (size) of the blocks
#QUANTITY = 20 # QUANTITY of blocks
#UPSPEED = 2 #speed of the screen, but less is faster, 1 - not playeble
BGCOLOR = pygame.Color('black')
FGCOLOR = pygame.Color('white')
#ALCOLOR = pygame.Color('red')
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
SCREEN.fill(BGCOLOR)

class Car:
    _carWidth = 10
    _carHeight = 20
    _carspeed = 1

    def __init__(self,x,y):
        self._x = x
        self._y = y
    def show(self, color):
        global SCREEN
        pygame.draw.rect(
            SCREEN, color, pygame.Rect(self._x, self._y, self._carWidth, self._carHeight))
    def move(self):
        global JUMPHEIGHT
        self.show(BGCOLOR)
        self._y += self.speed
        self.show(FGCOLOR)
        if not self.falls(): 
            self.pixelsJumped +=1
        if self.pixelsJumped == JUMPHEIGHT:
            self.speed = 1
            self.pixelsJumped = 0
    def left(self):
        self.show(BGCOLOR)
        self._x -= self._carspeed
        self.show(FGCOLOR)
    def right(self):
        self.show(BGCOLOR)
        self._x += self._carspeed
        self.show(FGCOLOR)
    def up(self):
        self.show(BGCOLOR)
        self._y -= self._carspeed
        self.show(FGCOLOR)
    def down(self):
        self.show(BGCOLOR)
        self._y += self._carspeed
        self.show(FGCOLOR)
