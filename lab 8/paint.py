from turtle import position
import pygame,sys

def calculateRect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

pygame.init()
screen = pygame.display.set_mode((640, 480))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

baseLayer = pygame.Surface((640, 480))

clock = pygame.time.Clock()
    
prevX = -1
prevY = -1
currentX = -1
currentY = -1

radius = 50

screen.fill(WHITE)
baseLayer.fill(WHITE)

isMouseDown = False
color=RED

while True:
        
    keys = pygame.key.get_pressed()

    #if isMouseDown and prevX != -1 and prevY != -1 and currentX != -1 and currentY != -1:
                    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: 
                isMouseDown = True
                currentX =  event.pos[0]
                currentY =  event.pos[1]    
                prevX =  event.pos[0]
                prevY =  event.pos[1]

        if event.type == pygame.MOUSEBUTTONUP:
            isMouseDown = False
            baseLayer.blit(screen, (0, 0))

        if event.type == pygame.MOUSEMOTION:
            if isMouseDown:
                currentX =  event.pos[0]
                currentY =  event.pos[1]
#4.Color selection
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_g:
                color=GREEN
            if event.key == pygame.K_b:
                color=BLACK
            if event.key == pygame.K_l:
                color=BLUE
            if event.key == pygame.K_r :
                color=RED
    #1.Draw rectangle    
    if keys[pygame.K_1]  :
        if isMouseDown and prevX != -1 and prevY != -1 and currentX != -1 and currentY != -1:
            screen.blit(baseLayer, (0, 0))
            r = calculateRect(prevX, prevY, currentX, currentY)
            pygame.draw.rect(screen, (color),pygame.Rect(r), 1) 
    #2.Draw circle
    if keys[pygame.K_c] :
        if isMouseDown and prevX != -1 and prevY != -1 and currentX != -1 and currentY != -1:
            x=(prevX-currentX)/2
            y=(prevY-currentY)/2
            screen.blit(baseLayer, (0, 0))
            r = calculateRect(prevX, prevY, currentX, currentY)
            pygame.draw.ellipse(screen,color,r,1)
            
    #3.Eraser
    if keys[pygame.K_e]:
        screen.blit(baseLayer, (0, 0))
        pygame.draw.line(screen, (WHITE), (prevX, prevY), (currentX, currentY), 10)
            
    
    pygame.display.flip()
    clock.tick(60)
        


