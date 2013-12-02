import sys, pygame, random
from pygame.locals import *

def moveSnake(l, xyCoo):
    l.pop(len(l)-1)
    l.insert(0, xyCoo)
    return l

#------
pygame.init()   #Inizializzo il gioco
#Tutte le VARIABILI vanno qui!
FPS = 8
fpsclock = pygame.time.Clock()
n = 20
BackgroundPath = "C:\\Users\\Raen\Desktop\\PySnake\\resources\\Background.jpg"
SnakePath = "C:\\Users\\Raen\\Desktop\\PySnake\\resources\\Snake.png"
MelaPath = "C:\\Users\\Raen\\Desktop\\PySnake\\resources\\Mela.png"
testapath = "C:\\Users\\Raen\\Desktop\\PySnake\\resources\\testa.png"
movex, movey = 0, 0
x, y = 0, 0
startPos, spos = 0, 0
melaCoo = (100, 100)
SnakeCoo = [(3*n, 0), (2*n, 0), (1*n, 0)]

#Crea La Finestra Principale:
SCREENDISPLAY = pygame.display.set_mode((1000, 800), 0, 32)
pygame.display.set_caption("PySnake!")

# Carica Imagini
GRIGLIA_DI_GIOCO = pygame.image.load(BackgroundPath).convert()
SNAKE = pygame.image.load(SnakePath).convert_alpha()
MELA = pygame.image.load(MelaPath).convert_alpha()
TESTA = pygame.image.load(testapath).convert_alpha()

#GameLoop0
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                movex = -n
                movey = 0
            elif event.key == K_RIGHT:
                movex = +n
                movey = 0
            elif event.key == K_UP:
                movey = -n
                movex = 0
            elif event.key == K_DOWN:
                movey = +n
                movex = 0
    x += movex
    y += movey
    if x >= 800:
        x = 0
    elif x < 0:
        x = 800
    elif y < 0:
        y = 600
    elif y >= 600:
        y = 0
    xy = (3*n+x, y)



    #Limitazioni della griglia


    #printa immagini
    SCREENDISPLAY.blit(GRIGLIA_DI_GIOCO, (0, 0))
    SCREENDISPLAY.blit(MELA, melaCoo)
    for i in range(len(SnakeCoo)):
        if i == 0:
            SCREENDISPLAY.blit(TESTA, SnakeCoo[i])
        else:
            SCREENDISPLAY.blit(SNAKE, SnakeCoo[i])
    if melaCoo in SnakeCoo:
        melaCoo = (random.randint(1,39)*20, random.randint(1, 29)*20)

    SnakeCoo = moveSnake(SnakeCoo, xy)
    #Velocità di gioco e Update
    fpsclock.tick(FPS)
    pygame.display.update()


