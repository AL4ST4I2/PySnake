'''
file che contiene tutte le variabili e costanti del gioco
'''
''' Roba da smanettoni '''
GAME_NAME = "PySnake!"
VERSION = str(0.1)

''' Important Game Costants '''
FPS = 8
n = 20
movex, movey = 0, 0
x, y = 0, 0
SnakeCoo = [(18*n, 15*n), (17*n, 15*n), (16*n, 15*n), (15*n,15*n)]
xy = (18*n, 15*n)

startPos, spos, pod = 0, 0, 0

'''    Colori:    '''
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GIALLO = (255, 255, 150)

''' path immagini '''
path = "C:\\Users\\Raen\\Desktop\\PySnake\\resources\\"

BackgroundPath = path+"Background - Copia.jpg"
LabMattoncinoPath = path+"mattoncino.png"
SnakePath1 = path+"striscia1.png"
SnakePath2 = path+"striscia2.png"
MelaPath = path+"mela1.png"
testapathleft = path+"testasx.png"
testapathright = path+"testadx.png"
testapathdown = path+"testagx.png"
testapathup = path+"testaupx.png"


