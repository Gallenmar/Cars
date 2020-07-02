import pygame
import random
import array as arr
pygame.init()

FRAMERATE = 400
WIDTH = 960; HEIGHT = 540
BGCOLOR = pygame.Color('black')
FGCOLOR = pygame.Color('white')
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(BGCOLOR)

bg_surface = pygame.image.load('assets/sunset.png').convert()
bg_surface = pygame.transform.scale2x(bg_surface)
road_surface = pygame.image.load('assets/road.png').convert()

class Car:
    _carWidth = 10
    _carHeight = 20
    _carspeed = 1

    car_surface = pygame.image.load('assets/defaultCar.png').convert()
    car_surface = pygame.transform.scale(car_surface, (20,20))
    car_rect = car_surface.get_rect(center = (0,0))

    #@property
    #def x(self):
    #    return self._x
    #@x.setter
    #def x(self,t):
    #    self._x = t
    #@property
    #def y(self):
    #    return self._y
    #@x.setter
    #def x(self,t):
    #    self._y = t
    
    def __init__(self,x,y):
        self.car_surface = pygame.image.load('assets/car.png').convert()
        self.car_surface = pygame.transform.scale(self.car_surface, (20,20))
        self.car_rect = self.car_surface.get_rect(center = (x,y))
    def left(self):
        self.car_rect.centerx -= self._carspeed
    def right(self):
        self.car_rect.centerx += self._carspeed
    def up(self):
        self.car_rect.centery -= self._carspeed
    def down(self):
        self.car_rect.centery += self._carspeed











clock = pygame.time.Clock()

ucar = Car(50,40)
u2car = Car(50,30)
RUNNING = True
while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
        if event.type == pygame.K_ESCAPE:
            RUNNING = False

    
    screen.blit(bg_surface,(0,0))
    screen.blit(road_surface,(0, HEIGHT//2))
    screen.blit(ucar.car_surface, ucar.car_rect)#(ucar.x,ucar.y))
    screen.blit(u2car.car_surface, u2car.car_rect)

    key=pygame.key.get_pressed() 
    if key[pygame.K_a]: ucar.left()
    if key[pygame.K_d]: ucar.right()
    if key[pygame.K_w]: ucar.up()
    if key[pygame.K_s]: ucar.down()

    if key[pygame.K_j]: u2car.left()
    if key[pygame.K_l]: u2car.right()
    if key[pygame.K_i]: u2car.up()
    if key[pygame.K_k]: u2car.down()

    clock.tick(FRAMERATE)
    pygame.display.flip() 
pygame.quit()