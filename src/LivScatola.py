import sys, pygame, random
from src import Ref
from pygame.locals import *

class LivScatola:

    def disegnaScatola(self):
            for asseX in range(0, 40*Ref.n, Ref.n):
                for assY in range(0, 30*Ref.n, Ref.n):
                    if asseX == 0 or asseX == 40*Ref.n or assY == 0 or assY == 30*Ref.n:

                        pass


    def __init__(self):
        pygame.init()
        pygame.init()
        pygame.init()
        pygame.init()

        SCREENSURFACE = pygame.display.set_mode((800, 650), 0, 32)
        pygame.display.set_caption(Ref.GAME_NAME + Ref.VERSION)

        #load immagini
        GRIGLIA_DI_GIOCO = pygame.image.load(Ref.BackgroundPath).convert()
        SNAKE1 = pygame.image.load(Ref.SnakePath1).convert_alpha()
        SNAKE2 = pygame.image.load(Ref.SnakePath2).convert_alpha()
        MELA = pygame.image.load(Ref.MelaPath).convert_alpha()
        TESTAleft = pygame.image.load(Ref.testapathleft).convert_alpha()
        TESTAright = pygame.image.load(Ref.testapathright).convert_alpha()
        TESTAdown = pygame.image.load(Ref.testapathdown).convert_alpha()
        TESTAup = pygame.image.load(Ref.testapathup).convert_alpha()
        MATTONCINO = pygame.image.load(Ref.LabMattoncinoPath).convert_alpha()

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        Ref.movex = -Ref.n; Ref.movey = 0
                    elif event.key == K_RIGHT:
                        Ref.movex = +Ref.n; Ref.movey = 0
                    elif event.key == K_UP:
                        Ref.movey = -Ref.n; Ref.movex = 0
                    elif event.key == K_DOWN:
                        Ref.movey = +Ref.n; Ref.movex = 0



            SCREENSURFACE.blit(GRIGLIA_DI_GIOCO, (0, 0))
            for asseX in range(0, 40):
                for assY in range(0, 30):
                    if asseX == 0 or asseX == 39 or assY == 0 or assY == 29:
                        SCREENSURFACE.blit(MATTONCINO, (asseX*Ref.n, assY*Ref.n))



LivScatola()