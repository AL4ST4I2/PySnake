import sys, pygame, random
from pygame.locals import *

def moveSnake(l, xyCoo):
    l.pop(len(l)-1)
    l.insert(0, xyCoo)
    return l

def testo(param):
    #_slist = font.render(("lista: " + str(SnakeCoo)), True, RED)
    _GameScore = font.render(("Score: " + str(param)), True, WHITE)
    SCREENDISPLAY.blit(_GameScore, (345, 605))
    #SCREENDISPLAY.blit(_slist, (802, 200))
#------
pygame.init()
pygame.init()#Inizializzo il gioco
#---VARIABILI
RED, GREEN, BLUE, WHITE = (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 255)
score = 0
FPS = 5
fpsclock = pygame.time.Clock()
n = 20
movex, movey = 0, 0
x, y = 0, 0
startPos, spos, pod = 0, 0, 0
melaCoo = (100, 100)
SnakeCoo = [(18*n, 15*n), (17*n, 15*n), (16*n, 15*n),(15*n,15*n)]
xy = (18*n, 15*n)
#---PATH IMMAGINI
BackgroundPath = "C:\\Users\\Raen\\Desktop\\PySnake\\resources\\Background - Copia.jpg"
SnakePath1 = "C:\\Users\\Raen\\Desktop\\PySnake\\resources\\striscia1.png"
SnakePath2 = "C:\\Users\\Raen\\Desktop\\PySnake\\resources\\striscia2.png"
MelaPath = "C:\\Users\\Raen\\Desktop\\PySnake\\resources\\mela1.png"
testapathleft = "C:\\Users\\Raen\\Desktop\\PySnake\\resources\\testasx.png"
testapathright = "C:\\Users\\Raen\\Desktop\\PySnake\\resources\\testadx.png"
testapathdown = "C:\\Users\\Raen\\Desktop\\PySnake\\resources\\testagx.png"
testapathup = "C:\\Users\\Raen\\Desktop\\PySnake\\resources\\testaupx.png"
programma = "C:\\Users\\Paolo\\Desktop\\UNIVERSITA'\\snake\\snake3.py"
# --- FONTS
font = pygame.font.SysFont("Times New Roman", 30)


#Crea La Finestra Principale:
SCREENDISPLAY = pygame.display.set_mode((800, 650), 0, 32)
pygame.display.set_caption("PySnake!  -- Beta v1.3")

# Carica Imagini
GRIGLIA_DI_GIOCO = pygame.image.load(BackgroundPath).convert()
SNAKE1 = pygame.image.load(SnakePath1).convert_alpha()
SNAKE2 = pygame.image.load(SnakePath2).convert_alpha()
MELA = pygame.image.load(MelaPath).convert_alpha()
TESTAleft = pygame.image.load(testapathleft).convert_alpha()
TESTAright = pygame.image.load(testapathright).convert_alpha()
TESTAdown = pygame.image.load(testapathdown).convert_alpha()
TESTAup = pygame.image.load(testapathup).convert_alpha()

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
                startPos = 1
            elif event.key == K_RIGHT:
                movex = +n
                movey = 0
                startPos = 1
            elif event.key == K_UP:
                movey = -n
                movex = 0
                startPos = 1
            elif event.key == K_DOWN:
                movey = +n
                movex = 0
                startPos = 1

    x += movex
    y += movey
    #'''
    if x >= 440: x = -360
    elif x < -360 : x = 420 #'''
    elif y < -360 : y = 280
    elif y >= 300 : y = -300 #'''

    #printa immagini
    SCREENDISPLAY.blit(GRIGLIA_DI_GIOCO, (0, 0))
    SCREENDISPLAY.blit(MELA, melaCoo)

    for i in range(0, len(SnakeCoo), 2):
        if i == 0:
            if movex == -n:
                SCREENDISPLAY.blit(TESTAleft, SnakeCoo[i])
            elif movex == n:
                SCREENDISPLAY.blit(TESTAright, SnakeCoo[i])
            elif movey == -n:
                SCREENDISPLAY.blit(TESTAup, SnakeCoo[i])
            else:
                SCREENDISPLAY.blit(TESTAdown, SnakeCoo[i])
        else:
            SCREENDISPLAY.blit(SNAKE1, SnakeCoo[i])
    for i in range(1, len(SnakeCoo), 2):
        SCREENDISPLAY.blit(SNAKE2, SnakeCoo[i])
    if melaCoo in SnakeCoo:
        melaCoo = (random.randint(1,39)*20, random.randint(1, 29)*20)
        SnakeCoo.insert(len(SnakeCoo)-1, SnakeCoo[len(SnakeCoo)-1])
        score += FPS
    for i in range(len(SnakeCoo)-1):
        if SnakeCoo[0] == SnakeCoo[i+1]:
            startPos = 0
            pygame.event.clear()
    if startPos != 0:
        xy = (18*n+x, 15*n+y)
        SnakeCoo = moveSnake(SnakeCoo, xy)

    testo(score)
    print("Score: ", score)
    '''
    print("\t\t Tupla movente", xy, "\tX: ", x, "\tY: ", y, end="")
    print("\nComponenti Serpente: ", SnakeCoo)
    print()#'''

    #VelocitÃ  di gioco e Update
    fpsclock.tick(FPS)
    pygame.display.update()



