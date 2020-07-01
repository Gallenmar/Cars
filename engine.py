import pygame
import random
import array as arr
pygame.init()

FRAMERATE = 400
JUMPHEIGHT = 300
XSTEP = 2  # how much alien moves side to side
WIDTH = 532; HEIGHT = 850 # size of the screen
XDIM = 50; YDIM = 10 # X and Y dimention (size) of the blocks
QUANTITY = 20 # QUANTITY of blocks
UPSPEED = 2 #speed of the screen, but less is faster, 1 - not playeble
BGCOLOR = pygame.Color('black')
FGCOLOR = pygame.Color('white')
ALCOLOR = pygame.Color('red')
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT)) # creating screen

class nedoAlien:
    def __init__(self,x,y):
        self.x = x
        self._y = y
    RADIUS = 10
    speed = 1
    pixelsJumped = 0

class Alien(nedoAlien):
    def __init__(self,x,y):
        self.x = x
        self._y = y
    def show(self, color):
        global SCREEN #telling python you are using global var
        pygame.draw.circle(SCREEN, color, (self.x, self._y), self.RADIUS)
    def move(self):
        global JUMPHEIGHT
        self.show(BGCOLOR)
        self._y += self.speed
        self.show(ALCOLOR)
        if not self.falls(): 
            self.pixelsJumped +=1
        if self.pixelsJumped == JUMPHEIGHT:
            self.speed = 1
            self.pixelsJumped = 0
    def lowerBorderY(self):
        return self._y + self.RADIUS
    def falls(self):
        if self.speed > 0 :
            return True
        else:
            return False
    def jump(self):
        self.speed = -1
        self.pixelsJumped = 0
    def inTheZone(self, x1, dim): # x1 left boundry         dim is width
        if (self.x + self.RADIUS)> x1 and (self.x - self.RADIUS) < (x1 + dim):
            return True
        else:
            return False
    def left(self):
        global ALCOLOR, BGCOLOR
        self.show(BGCOLOR)
        self.x -= XSTEP
        self.show(ALCOLOR)
    def right(self):
        global ALCOLOR, BGCOLOR
        self.show(BGCOLOR)
        self.x += XSTEP
        self.show(ALCOLOR)
    def retY(self):
        return self._y
