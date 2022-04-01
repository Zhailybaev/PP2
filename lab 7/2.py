import pygame
import os
pygame.init()
pygame.mixer.music.load('Моцарт - Соната для фортепиано No. 11, Турецкое рондо.mp3')
#pygame.mixer.music.play(0)
screen = pygame.display.set_mode((500, 500))  # Surface
running = True
#clock = pygame.time.Clock()
#FPS = 60
l=1
songs = ['Лунная Соната - Бетховен (Remix).mp3', 'Моцарт - Соната для фортепиано No. 11, Турецкое рондо.mp3', 'Чайковский - Танец Феи Драже (Щелкунчик).mp3']
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                pygame.mixer.music.stop()
            if event.key == pygame.K_p :
                pygame.mixer.music.play(0)
            if event.key == pygame.K_n :
                l=l+1
                pygame.mixer.music.load(songs[l])
                pygame.mixer.music.play(0)
            if event.key == pygame.K_r :
                l=l-1
                pygame.mixer.music.load(songs[l])
                pygame.mixer.music.play(0)

    pygame.display.flip()
#    clock.tick(FPS)

