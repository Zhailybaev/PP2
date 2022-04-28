import pygame, sys
import random
import time
import psycopg2


con = psycopg2.connect(
  host="localhost",
  database="snake",
  user="adia",
  password="passw0rd"
)

cur = con.cursor()


pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

radius = 10
body = [[100, 100], [0, 0], [0, 0]]


block = 15
dx, dy = block, 0

def own_round(value, base=15):
  return base * round(value / 15)

# 2 task
def set_random_position():
  return own_round(random.randint(10, WINDOW_WIDTH-20)), own_round(random.randint(10, WINDOW_HEIGHT-20))
# 1 task
font_style = pygame.font.SysFont("Verdana", 20)
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [WINDOW_WIDTH / 6, WINDOW_HEIGHT / 3])


    

food_x, food_y = set_random_position()
x1, y1 = set_random_position()
score=0
level=1

game_over = False
game_close= False
pause= False

FPS = 5
FramePerSec = pygame.time.Clock()
SPEED=0
k=0



username=str(input())



cur.execute (f"select level from user_score where name = \'{username}\' ")
lev=cur.fetchone()
if lev is not None:
  level=int(lev[0])


cur.execute (f"select score from user_score where name = \'{username}\' ")
sc=cur.fetchone()
if sc is not None:
  score=int(sc[0])

while not game_over:

  def paused():
    paus=False
    cur.execute(f"INSERT INTO USER_SCORE (NAME,SCORE,LEVEL) VALUES ('{username}', {score} , {level})")
    print("Record inserted successfully")  
    con.commit()  
    while not paus:
      
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
        if event.type==pygame.KEYDOWN:
          if event.key==pygame.K_p:
            paus = True
      screen.fill(BLACK)
      message("PAUSE", RED)
      pygame.display.update()
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      game_over = True
      sys.exit()
      
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RIGHT:
        dx = block
        dy = 0
      if event.key == pygame.K_LEFT:
        dx = -block
        dy = 0
      if event.key == pygame.K_UP:
        dx = 0
        dy = -block
      if event.key == pygame.K_DOWN:
        dx = 0
        dy = block
      if event.key == pygame.K_s:
        paused()
     
  if body[0][0] ==food_x+5  and body[0][1]== food_y+5 or body[0][0] ==x1+5  and body[0][1]== y1+5: 
    body.append([0, 0])
    food_x, food_y = set_random_position()
    x1, y1 = set_random_position()
#1.Randomly generating food with different weights
    score=score+1
    if score%3==0 and score!=0  :
      level=level+1
      FPS=FPS+0.5
      k=0
      if level%3==0:
        k=k+1
  if body[0][0] ==food_x-5  and body[0][1]== food_y-5 or body[0][0] ==x1-5  and body[0][1]== y1-5 : 
    body.append([0, 0])
    food_x, food_y = set_random_position()
    x1, y1 = set_random_position()
#1.Randomly generating food with different weights
    score=score+1
    if score%3==0 and score!=0  :
      level=level+1
      k=0
      FPS=FPS+0.5
      if level%3==0:
        k=k+1
      
  for i in range(len(body) - 1, 0, -1):
    body[i][0] = body[i - 1][0]
    body[i][1] = body[i - 1][1]
  # 1 task
  if body[0][0] >= 500 or body[0][0] < 0 or body[0][1] >= 500 or body[0][1] < 0:
    game_close = True
  body[0][0] += dx
  body[0][1] += dy
  # 1 task
  while game_close == True:
    screen.fill(BLACK)
    message("GAME OVER", RED)
    pygame.display.update()
    time.sleep(2)
    pygame.quit()
    sys.exit()

    
  
  # Check for Food eating, if so, add one item to Snake body

  screen.fill(BLACK)

  # Draw food
  pygame.draw.circle(screen, BLUE, (food_x, food_y), radius)
  #Lab9 2.Foods which are disappearing after some time(timer)
  if level>1 and k==0:
    
    pygame.draw.circle(screen,BLUE,(x1,y1),radius)
  
  
  # Draw snake
  for i, (x, y) in enumerate(body):
    color = RED if i == 0 else GREEN
    pygame.draw.circle(screen, color, (x, y), radius)
  scores = font_style.render("SCORE:"+str(score), True, RED)
  screen.blit(scores, (10,10))

  levels = font_style.render("LEVEL:"+str(level), True, RED)
  screen.blit(levels, (10,30))

  #cur.execute(f"INSERT INTO USER_SCORE (USERNAME,SCORE,LEVEL) VALUES ('{username}', {score} , {level})")
  #con.commit()  
  #print("Record inserted successfully")  
  pygame.display.flip()
    
   
  clock.tick(FPS)

con.close() 
pygame.quit()