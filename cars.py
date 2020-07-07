import pygame
from dumbmenu import dumbmenu
#import random
#import array as arr
pygame.init()
#vars
red   = 255,  0,  0
green =   0,255,  0
blue  =   0,  0,255

RUNNING = True
HEIGHSCORE = 0
FRAMERATE = 30
WIDTH = 960; HEIGHT = 540
BOUNDRY = 106
BGCOLOR = pygame.Color('blue')
FGCOLOR = pygame.Color('white')
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(BGCOLOR)

bg_surface = pygame.image.load('assets/Mytrack.png').convert()
#bg_surface = pygame.transform.scale2x(bg_surface)
#road_surface = pygame.image.load('assets/road.png').convert()

clock = pygame.time.Clock()

#classes
class Car:
	_carWidth = 100
	_carHeight = 100
	_carspeed = 2

	car_surface = pygame.image.load('assets/defaultCar.png').convert()
	car_surface = pygame.transform.scale(car_surface, (80,80))
	car_rect = car_surface.get_rect(center = (0,0))

	def __init__(self,x,y,file = 'assets/defaultCar.png'):
		self.car_surface = pygame.image.load(file).convert()
		self.car_surface = pygame.transform.scale(
			self.car_surface, (self._carWidth,self._carHeight))
		self.car_rect = self.car_surface.get_rect(center = (x,y))
	def left(self, speed = _carspeed):
		if self.car_rect.left - speed < BOUNDRY:
			self.car_rect.left = BOUNDRY
		elif not self.car_rect.left - speed == BOUNDRY:
			self.car_rect.centerx -= speed
	def right(self, speed = _carspeed):
		if self.car_rect.right + speed > WIDTH - BOUNDRY:
			self.car_rect.right = WIDTH - BOUNDRY
		elif not self.car_rect.right + speed == WIDTH - BOUNDRY:
			self.car_rect.centerx += speed
	def up(self, speed = _carspeed):
		self.car_rect.centery -= speed
	def down(self, speed = _carspeed):
		self.car_rect.centery += speed

#-funcs-


def options_menu():
	choose = dumbmenu(screen, [
					'Option1',
					'Option2',
					'Back'
					], 64,64,None,32,1.4,green,red)
	if choose == 0:
		print('Option1 was chosen')
		return 1
	elif choose == 1:
		print('Option2 was chosen')
		return 1
	elif choose == 2:
		return 0
	elif choose == -1:
		return -1

def myMenu():   # this is shit
	global RUNNING, HEIGHSCORE
	screen.fill(BGCOLOR)
	choose = dumbmenu(screen, [
						'Start Game',
						'Options',
						'Show Highscore',
						'Quit Game'], 64,64,None,32,1.4,green,red)
	if choose == 0:
		pass
		return 0
	elif choose == 1:
		screen.fill(BGCOLOR)
		opmenu_run = 1
		while opmenu_run == 1:
			opmenu_run = options_menu() # -1 exit, 0 show norn menu, 1 show menu again
			screen.fill(BGCOLOR)
			if opmenu_run == -1:
				return -1
			elif opmenu_run == 0:
				return 1
	elif choose == 2:
		s = 'Your highscore is ' + str(HEIGHSCORE)
		choose2 = screen.fill(BGCOLOR)
		dumbmenu(screen, [ s ], 64,64,None,32,1.4,green,red)
		return True
	elif choose == 3:
		return -1
	elif choose == -1:
		return -1

#-Menu-
menu_run = 1
while menu_run == 1:
	menu_run = myMenu() # -1 exit, 0 start game, 1 show menu again
	if menu_run == -1:
		RUNNING = False
		menu_run = 0
	screen.fill(BGCOLOR)
		



#cars
ucar = Car(500,40,'assets/myCar.png')
u2car = Car(500,300)
tmp_speed = 4
#-game loop-
while RUNNING:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			RUNNING = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				RUNNING = False

		
	screen.blit(bg_surface,(0,0))
	#screen.blit(road_surface,(0, HEIGHT//2))
	screen.blit(ucar.car_surface, ucar.car_rect)
	screen.blit(u2car.car_surface, u2car.car_rect)

		
	key=pygame.key.get_pressed() 
	if key[pygame.K_a]: ucar.left(tmp_speed)
	if key[pygame.K_d]: ucar.right(tmp_speed)
	if key[pygame.K_w]: ucar.up(tmp_speed)
	if key[pygame.K_s]: ucar.down(tmp_speed)

	if key[pygame.K_j]: u2car.left(tmp_speed)
	if key[pygame.K_l]: u2car.right(tmp_speed)
	if key[pygame.K_i]: u2car.up(tmp_speed)
	if key[pygame.K_k]: u2car.down(tmp_speed)

	ucar.down()
	u2car.down()

	clock.tick(FRAMERATE)
	pygame.display.flip() 
pygame.quit()
