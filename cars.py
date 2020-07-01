from engine import *

clock = pygame.time.Clock()
#---------------------start----------
# title, icon and screen
pygame.display.set_caption('Doodle jump')
Sprite = pygame.image.load('doodle.png')
pygame.display.set_icon(Sprite)
SCREEN.fill(BGCOLOR) # making screen in bg color

# drawing some starting blocks 
# and one block at the bottom (so that Alien wouldnt fall every other time)
blockList = []
for i in range(0, QUANTITY -1):
    indentOfBlocks = random.randint(1, (WIDTH - XDIM))
    heightOfBlocks = HEIGHT//QUANTITY * i
    blockList.append(pygame.Rect(indentOfBlocks, heightOfBlocks, XDIM, YDIM))
    pygame.draw.rect(SCREEN, FGCOLOR, blockList[i])
indentOfBlocks = (WIDTH//2)-(XDIM//2) # to center the block
heightOfBlocks = HEIGHT - YDIM -100
blockList.append(pygame.Rect(indentOfBlocks, heightOfBlocks, XDIM, YDIM))
pygame.draw.rect(SCREEN, FGCOLOR, blockList[i + 1])

# creating an alien
ali = Alien((WIDTH//2), (HEIGHT - YDIM - Alien.RADIUS -130))
ali.show(ALCOLOR)

# creating clock for better experience (othervise it will be too fast)
clock = pygame.time.Clock()

sit = 0 # screen iterator (like i in for but it)
#-------------------funcs-------------
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




#-------------------------------primary game loop-

RUNNING = True
while RUNNING:
    for event in pygame.event.get(): # wating to close (otherwise window wouldnt close)
        if event.type == pygame.QUIT:
            RUNNING = False
        if event.type == pygame.K_ESCAPE:
            RUNNING = False
    
    clock.tick(FRAMERATE)
    pygame.display.flip() # updating the screen to see the changes

    blocks_redraw() # draw blocks every time so that alien wouldnt erace them
    alien_move() #alien moving
    screen_up() # screen moving up

# the end
pygame.quit()
#BLM