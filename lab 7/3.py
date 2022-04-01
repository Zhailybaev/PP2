import pygame
pygame.init()
screen = pygame.display.set_mode((500, 500))  # Surface
running = True
x=0
y=0
RED = (255, 0, 0)
WHITE = (255, 255, 255)
clock = pygame.time.Clock()
while running :
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT] :
        x=x-20
    if keys[pygame.K_RIGHT] :
        x=x+20
    if keys[pygame.K_UP] :
        y=y-20
    if keys[pygame.K_DOWN] :
        y=y+20
    if x>450  :
        x=450
    if x<50 :
        x=50 
    if y>450 :
         y=450
    if y<50 :
        y=50
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             running = False
    
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (x, y), 25)
    pygame.display.flip()
    clock.tick(10)

        
        
            
    