from engine import *
clock = pygame.time.Clock()





car = Car(20,40)



car.show(FGCOLOR)

RUNNING = True
while RUNNING:
    for event in pygame.event.get(): # wating to close (otherwise window wouldnt close)
        if event.type == pygame.QUIT:
            RUNNING = False
        if event.type == pygame.K_ESCAPE:
            RUNNING = False


    key=pygame.key.get_pressed() 

    if key[pygame.K_a]: car.left()
    if key[pygame.K_d]: car.right()
    if key[pygame.K_w]: car.up()
    if key[pygame.K_s]: car.down()

    clock.tick(FRAMERATE)
    pygame.display.flip() # updating the screen to see the changes
pygame.quit()