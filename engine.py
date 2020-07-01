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

class Alien:
    RADIUS = 10
    speed = 1
    pixelsJumped = 0
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def show(self, color):
        global SCREEN #telling python you are using global var
        pygame.draw.circle(SCREEN, color, (self.x, self.y), self.RADIUS)
    def move(self):
        global JUMPHEIGHT
        self.show(BGCOLOR)
        self.y += self.speed
        self.show(ALCOLOR)
        if not self.falls(): 
            self.pixelsJumped +=1
        if self.pixelsJumped == JUMPHEIGHT:
            self.speed = 1
            self.pixelsJumped = 0
    def lowerBorderY(self):
        return self.y + self.RADIUS
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

def blocks_redraw():
    global QUANTITY, HEIGHT, WIDTH, XDIM, YDIM, FGCOLOR, SCREEN, blockList
    for i in range(0,QUANTITY):
        if blockList[i].y > HEIGHT:
            indentOfBlocks = random.randint(1, (WIDTH - XDIM))
            blockList[i] = pygame.Rect(indentOfBlocks, 0, XDIM, YDIM)
            pygame.draw.rect(SCREEN, FGCOLOR, blockList[i])
        pygame.draw.rect(SCREEN, FGCOLOR, blockList[i])

def alien_move():
    global QUANTITY, HEIGHT, WIDTH, XDIM, RUNNING, BGCOLOR, blockList, ali
    # should it jump?
    for i in range(0, QUANTITY): 
        if ali.inTheZone(blockList[i].x, XDIM) and ali.falls and ali.lowerBorderY() == blockList[i].y:
            ali.jump()
    # just moving
    ali.move()
    key=pygame.key.get_pressed() 
    if key[pygame.K_a]: ali.left()
    if key[pygame.K_d]: ali.right()
    if ali.y > HEIGHT :  RUNNING = False # death
    # if it colides with border it will teleport to other border
    if ali.x < 0:
        ali.show(BGCOLOR)
        ali.x = WIDTH
    elif ali.x > WIDTH:
        ali.show(BGCOLOR)
        ali.x = 0
    # celing
    if ali.y < 0:
        ali.show(BGCOLOR)
        ali.speed = 1

def screen_up():
    global QUANTITY, RUNNING, BGCOLOR, FGCOLOR, SCREEN, blockList, sit, UPSPEED
    sit += 1
    if sit == UPSPEED:
        sit = 0
        for i in range(0,QUANTITY):
            pygame.draw.rect(SCREEN, BGCOLOR, blockList[i])
            blockList[i].y += 1
            pygame.draw.rect(SCREEN, FGCOLOR, blockList[i])

