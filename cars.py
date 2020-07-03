import pygame
#import random
#import array as arr
import dumbmenu as dm
pygame.init()

#vars
red   = 255,  0,  0
green =   0,255,  0
blue  =   0,  0,255

RUNNING = True
HEIGHSCORE = 0
FRAMERATE = 30
WIDTH = 960; HEIGHT = 540
BGCOLOR = pygame.Color('blue')
FGCOLOR = pygame.Color('white')
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(BGCOLOR)

bg_surface = pygame.image.load('assets/sunset.png').convert()
bg_surface = pygame.transform.scale2x(bg_surface)
road_surface = pygame.image.load('assets/road.png').convert()

clock = pygame.time.Clock()

#classes
class Car:
    _carWidth = 10
    _carHeight = 20
    _carspeed = 1

    car_surface = pygame.image.load('assets/defaultCar.png').convert()
    car_surface = pygame.transform.scale(car_surface, (20,20))
    car_rect = car_surface.get_rect(center = (0,0))

    def __init__(self,x,y,file = 'assets/defaultCar.png'):
        self.car_surface = pygame.image.load(file).convert()
        #self.car_surface = pygame.transform.scale(self.car_surface, (20,20))
        self.car_rect = self.car_surface.get_rect(center = (x,y))
    def left(self):
        self.car_rect.centerx -= self._carspeed
    def right(self):
        self.car_rect.centerx += self._carspeed
    def up(self):
        self.car_rect.centery -= self._carspeed
    def down(self):
        self.car_rect.centery += self._carspeed

#-funcs-
def dumbmenu(screen, menu, x_pos = 100, y_pos = 100, font = None,
            size = 70, distance = 1.4, fgcolor = (255,255,255),
            cursorcolor = (255,0,0), exitAllowed = True):
	"""
	Version: 0.40
	Author: Manuel Kammermeier aka Astorek
	License: MIT
	"""
	# Draw the Menupoints
	pygame.font.init()
	if font == None:
		myfont = pygame.font.Font(None, size)
	else:
		myfont = pygame.font.SysFont(font, size)
	cursorpos = 0
	renderWithChars = False
	for i in menu:
		if renderWithChars == False:
			text =  myfont.render(str(cursorpos + 1)+".  " + i,
				True, fgcolor)
		else:
			text =  myfont.render(chr(char)+".  " + i,
				True, fgcolor)
			char += 1
		textrect = text.get_rect()
		textrect = textrect.move(x_pos, 
		           (size // distance * cursorpos) + y_pos)
		screen.blit(text, textrect)
		pygame.display.update(textrect)
		cursorpos += 1
		if cursorpos == 9:
			renderWithChars = True
			char = 65
	# Draw the ">", the Cursor
	cursorpos = 0
	cursor = myfont.render(">", True, cursorcolor)
	cursorrect = cursor.get_rect()
	cursorrect = cursorrect.move(x_pos - (size // distance),
	             (size // distance * cursorpos) + y_pos)

	# The whole While-loop takes care to show the Cursor, move the
	# Cursor and getting the Keys (1-9) to work...
	ArrowPressed = True
	exitMenu = False
	clock = pygame.time.Clock()
	filler = pygame.Surface.copy(screen)
	fillerrect = filler.get_rect()
	while True:
		clock.tick(30)
		if ArrowPressed == True:
			screen.blit(filler, fillerrect)
			pygame.display.update(fillerrect)#BY GALLENMAR
			pygame.display.update(cursorrect)
			cursorrect = cursor.get_rect()
			cursorrect = cursorrect.move(x_pos - (size // distance),
			             (size // distance * cursorpos) + y_pos)
			screen.blit(cursor, cursorrect)
			pygame.display.update(cursorrect)
			ArrowPressed = False
		if exitMenu == True:
			break
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return -1
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE and exitAllowed == True:
					if cursorpos == len(menu) - 1:
						exitMenu = True
					else:
						cursorpos = len(menu) - 1; ArrowPressed = True
				# This Section is huge and ugly, I know... But I don't
				# know a better method for this^^
				if event.key == pygame.K_1:
					cursorpos = 0; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_2 and len(menu) >= 2:
					cursorpos = 1; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_3 and len(menu) >= 3:
					cursorpos = 2; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_4 and len(menu) >= 4:
					cursorpos = 3; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_5 and len(menu) >= 5:
					cursorpos = 4; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_6 and len(menu) >= 6:
					cursorpos = 5; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_7 and len(menu) >= 7:
					cursorpos = 6; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_8 and len(menu) >= 8:
					cursorpos = 7; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_9 and len(menu) >= 9:
					cursorpos = 8; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_UP:
					ArrowPressed = True
					if cursorpos == 0:
						cursorpos = len(menu) - 1
					else:
						cursorpos -= 1
				elif event.key == pygame.K_DOWN:
					ArrowPressed = True
					if cursorpos == len(menu) - 1:
						cursorpos = 0
					else:
						cursorpos += 1
				elif event.key == pygame.K_KP_ENTER or \
				     event.key == pygame.K_RETURN:
							exitMenu = True
	
	return cursorpos
# end of dumb menu

def options_menu():
    choose = dm.dumbmenu(screen, [
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
    choose = dm.dumbmenu(screen, [
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
        dm.dumbmenu(screen, [ s ], 64,64,None,32,1.4,green,red)
        return True
    elif choose == 3:
        return -1
    elif choose == -1:
        return -1

#-Start-
menu_run = 1
while menu_run == 1:
    menu_run = myMenu() # -1 exit, 0 start game, 1 show menu again
    if menu_run == -1:
        RUNNING = False
        menu_run = 0
    screen.fill(BGCOLOR)
    



#cars
ucar = Car(50,40,'assets/myCar.png')
u2car = Car(50,30)

#-game loop-
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