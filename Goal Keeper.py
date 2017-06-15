"""
Instituto Tecnológico de Costa Rica
Ingeniería en Computadores
Proyecto #3
Lenguaje: Python 3.6.1
Versión: 1.0
Fecha de última modificación: 5/18/2017
Estudiantes: Gabriel Abarca Aguiar y Andrés Zuñiga
Carné:2017110442
"""
#Módulos
import sys
import pygame
import time as tiempo
import serial
from pygame.locals import *
import tkinter
# ---------------------------------------------------------------------
#Variables
WIDTH = 1366
HEIGHT = 768
Player1=False
Player2=False
Select1=True
Select2=False
Select3=False
Cunt=1
ContadorDePersonajes=1
#arduino = serial.Serial("COM4", 9600)
# ---------------------------------------------------------------------
#Objetos
# ---------------------------------------------------------------------
class Equipo():
    def __init__(self):
        self.Jugadores=11
class Real_Madrid(Equipo):
    def __init__(self,x,y):
        self.shield=load_image("Images/RealMadridLogo.png",True)
        self.rect = self.shield.get_rect()
        self.rect.centerx=x
        self.rect.centery=y
class Juventus(Equipo):
    def __init__(self,x,y):
        self.shield=load_image("Images/JuventusLogo.png",True)
        self.rect = self.shield.get_rect()
        self.rect.centerx=x
        self.rect.centery=y
class Manchester_United(Equipo):
    def __init__(self,x,y):
        self.shield=load_image("Images/ManchesterLogo.png",True)
        self.rect = self.shield.get_rect()
        self.rect.centerx=x
        self.rect.centery=y
#Funciones
def load_image(filename, transparent=False):#Llama imagenes
        try: image = pygame.image.load(filename)
        except (pygame.error,message):
                raise (SystemExit, message)
        image = image.convert()
        if transparent:
                color = image.get_at((0,0))
                image.set_colorkey(color, RLEACCEL)
        return image
"""
def send_arduino(mesagge):
    global arduino
    tiempo.sleep(2)
    arduino.write(b+message)#mesagge b'9'
    arduino.close()
def read_arduino():
        global arduino
        time.sleep(2)
        rawString = arduino.readline()
        print(rawString)
        arduino.close()
"""
def Selected_Team(Potenciometro,Boton):#Editar luego con el arduino
    RealMadrid=False
    Juventus=False
    Manchester=False
    
def grabartxt(archivo,valor):#Grabar al TXT
        archi=open(archivo,'a')
        archi.write(valor+"\n")
        archi.close()
def readtxt(archivo):#Lector de TXT
        archi=open(archivo,'r')
        linea=archi.readlines()
        save=linea[0][:-1]
        print(save)
        archi.close()
        return save
def texto(texto, posx, posy, color=(255, 255, 255)):#Textos pequeños
        fuente = pygame.font.Font("Font/Soccer Jersey.ttf",120)
        salida = pygame.font.Font.render(fuente, texto, 1, color)
        salida_rect = salida.get_rect()
        salida_rect.centerx = posx
        salida_rect.centery = posy
        return salida, salida_rect
def texto1(texto, posx, posy, color=(255, 255, 255)):#Textos pequeños
        fuente = pygame.font.Font("Font/Soccer Jersey.ttf",24)
        salida = pygame.font.Font.render(fuente, texto, 1, color)
        salida_rect = salida.get_rect()
        salida_rect.x = posx
        salida_rect.y = posy
        return salida, salida_rect
def keyboard1():#Teclado del inicio
        global Select1, Select2 ,Select3,Cunt
        ##print ("Si no imprimo esto, no funciona")
        if Cunt>3:
                Cunt=1
        if Cunt<=0:
                Cunt=3
        if Cunt==1:
                Select1=True
                Select2=False
                Select3=False
        elif Cunt==2:
                Select1=False
                Select2=True
                Select3=False
        elif Cunt==3:
                Select1=False
                Select2=False
                Select3=True
def displayteam(Player):
    if Player==1:
        team=readtxt("Memoria/Jugador1-Equipo.txt")
    elif Player==2:
        team=readtxt("Memoria/Jugador2-Equipo.txt")
    if team=="Real Madrid":
        archi=open("Memoria/RealMadrid-Jugadores.txt",'r')
    elif team=="Juventus":
        archi=open("Memoria/Juventus-Jugadores.txt",'r')
    elif team =="Manchester United":
        archi=open("Memoria/ManchesterUnited-Jugadores.txt",'r')
    linea=archi.readlines()
    Jugador1=elementos(linea[0][:-1])
    Jugador2=elementos(linea[1][:-1])
    Jugador3=elementos(linea[2][:-1])
    Jugador4=elementos(linea[3][:-1])
    Jugador5=elementos(linea[4][:-1])
    Jugador6=elementos(linea[5][:-1])
    Jugador7=elementos(linea[6][:-1])
    Jugador8=elementos(linea[7][:-1])
    Jugador9=elementos(linea[8][:-1])
    Jugador10=elementos(linea[9][:-1])
    archi.close
    Jugadores=[Jugador1,Jugador2,Jugador3,Jugador4,Jugador5,Jugador6,Jugador7,Jugador8,Jugador9,Jugador10]
    print(Jugadores)
    return Jugadores
def displayimages(Player):
    if Player==1:
        team=readtxt("Memoria/Jugador1-Equipo.txt")
    elif Player==2:
        team=readtxt("Memoria/Jugador2-Equipo.txt")
    if team=="Real Madrid":
        dic="Images/Real Madrid/"
    elif team=="Juventus":
        dic="Images/Juventus/"
    elif team =="Manchester United":
        dic="Images/Manchester United/"
    Jugador1=dic+"imagen.jpg"
    Jugador2=dic+"imagen.jpg"
    Jugador3=dic+"imagen.jpg"
    Jugador4=dic+"imagen.jpg"
    Jugador5=dic+"imagen.jpg"
    Jugador6=dic+"imagen.jpg"
    Jugador7=dic+"imagen.jpg"
    Jugador8=dic+"imagen.jpg"
    Jugador9=dic+"imagen.jpg"
    Jugador10=dic+"imagen.jpg"
    Jugadores=[Jugador1,Jugador2,Jugador3,Jugador4,Jugador5,Jugador6,Jugador7,Jugador8,Jugador9,Jugador10]
    print(Jugadores)
    return Jugadores
def elementos(string):
    if isinstance(string,str):
        return elementos_aux(string,"",[])
    else:
        return"Error"
def elementos_aux(string,nombre,lista):
    if string=="":
        lista.append(nombre)
        return lista
    else:
        if string[0]=="\t":
            lista.append(nombre)
            return elementos_aux(string[1:],"",lista)
        else:
            nombre+=string[0]
            return elementos_aux(string[1:],nombre,lista)
# ---------------------------------------------------------------------
#Main
# ---------------------------------------------------------------------
def Team_select1():
    screen = pygame.display.set_mode((WIDTH, HEIGHT),FULLSCREEN)
    background_image=load_image("images/background.jpg")
    clock = pygame.time.Clock()
    Equipo1=Real_Madrid(WIDTH/4,HEIGHT*2/3)
    Equipo2=Juventus(WIDTH/2,HEIGHT*2/3)
    Equipo3=Manchester_United(WIDTH*3/4,HEIGHT*2/3)
    Tittle,Tittle_rect=texto("Player 1, choose your team." ,WIDTH/2 , HEIGHT/3)
    while True:
        time = clock.tick(60)
        keyboard1()
        global Select1, Select2, Select3,Cunt
        for event in pygame.event.get():#Teclado para la Pausa
            if event.type == QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                print (event.key)
                if event.key==pygame.K_d:
                    Cunt+=1
                    print ("presion d", Cunt)
                if event.key==pygame.K_a:
                    Cunt-=1
                    print ("presion a",Cunt)
                if event.key==K_KP_ENTER:#Exit
                    if Select1==True:
                        grabartxt("Memoria/Jugador1-Equipo.txt","Real Madrid")
                        Select1=False
                    if Select2==True:
                        grabartxt("Memoria/Jugador1-Equipo.txt","Juventus")
                        Select1=False
                    if Select3==True:
                        grabartxt("Memoria/Jugador1-Equipo.txt","Manchester United")
                        Select3=False
                    return Team_select2()
        screen.blit(background_image,(0,0))
        screen.blit(Tittle,Tittle_rect)
        screen.blit(Equipo1.shield,Equipo1.rect)
        screen.blit(Equipo2.shield,Equipo2.rect)
        screen.blit(Equipo3.shield,Equipo3.rect)
        pygame.display.flip()
    return 0

def Team_select2():
    screen = pygame.display.set_mode((WIDTH, HEIGHT),FULLSCREEN)
    background_image=load_image("images/background.jpg")
    clock = pygame.time.Clock()
    Equipo1=Real_Madrid(WIDTH/4,HEIGHT*2/3)
    Equipo2=Juventus(WIDTH/2,HEIGHT*2/3)
    Equipo3=Manchester_United(WIDTH*3/4,HEIGHT*2/3)
    Tittle,Tittle_rect=texto("Player 2, choose your team." ,WIDTH/2 , HEIGHT/3)
    while True:
        time = clock.tick(60)
        keyboard1()
        global Select1, Select2, Select3,Cunt
        for event in pygame.event.get():#Teclado para la Pausa
            if event.type == QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                print (event.key)
                if event.key==pygame.K_d:
                    Cunt+=1
                    print ("presion d", Cunt)
                if event.key==pygame.K_a:
                    Cunt-=1
                    print ("presion a",Cunt)
                if event.key==K_KP_ENTER:#Exit
                    if Select1==True:
                        grabartxt("Memoria/Jugador2-Equipo.txt","Real Madrid")
                        return choseplayers1()
                    if Select2==True:
                        grabartxt("Memoria/Jugador2-Equipo.txt","Juventus")
                        return choseplayers1()
                    if Select3==True:
                        grabartxt("Memoria/Jugador2-Equipo.txt","Manchester United")
                        return choseplayers1()
        screen.blit(background_image,(0,0))
        screen.blit(Tittle,Tittle_rect)
        screen.blit(Equipo1.shield,Equipo1.rect)
        screen.blit(Equipo2.shield,Equipo2.rect)
        screen.blit(Equipo3.shield,Equipo3.rect)

        pygame.display.flip()
    return 0
def choseplayers1():
    screen = pygame.display.set_mode((WIDTH, HEIGHT),FULLSCREEN)
    background_image=load_image("images/background.jpg")
    clock = pygame.time.Clock()
    Tittle,Tittle_rect=texto("Player 1, choose your team players." ,WIDTH/2 , HEIGHT/3)
    matriz=displayteam(1)
    imagenes=displayimages(1)
    jugador1=load_image(imagenes[0])
    jug1,jug1_rect=texto1(matriz[0][0],120 ,280)
    nacj1,nacj1_rect=texto1(matriz[0][1],120 ,310)
    nick1,nickj1_rect=texto1(matriz[0][2],120 ,340)
    pos1,posj1_rect=texto1(matriz[0][3],120 ,370)
    jugador2=load_image(imagenes[1])
    jug2,jug2_rect=texto1(matriz[1][0],364 ,280)
    nacj2,nacj2_rect=texto1(matriz[1][1],364 ,310)
    nick2,nickj2_rect=texto1(matriz[1][2],364 ,340)
    pos2,posj2_rect=texto1(matriz[1][3],364 ,370)
    jugador3=load_image(imagenes[2])
    jug3,jug3_rect=texto1(matriz[2][0],608 ,280)
    nacj3,nacj3_rect=texto1(matriz[2][1],608 ,310)
    nick3,nickj3_rect=texto1(matriz[2][2],608 ,340)
    pos3,posj3_rect=texto1(matriz[2][3],608 ,370)
    jugador4=load_image(imagenes[3])
    jug4,jug4_rect=texto1(matriz[3][0],852 ,280)
    nacj4,nacj4_rect=texto1(matriz[3][1],852 ,310)
    nick4,nickj4_rect=texto1(matriz[3][2],852 ,340)
    pos4,posj4_rect=texto1(matriz[3][3],852 ,370)
    jugador5=load_image(imagenes[4])
    jug5,jug5_rect=texto1(matriz[4][0],1095 ,280)
    nacj5,nacj5_rect=texto1(matriz[4][1],1095 ,310)
    nick5,nickj5_rect=texto1(matriz[4][2],1095 ,340)
    pos5,posj5_rect=texto1(matriz[4][3],1095 ,370)
    jugador6=load_image(imagenes[5])
    jug6,jug6_rect=texto1(matriz[5][0],120 ,600)
    nacj6,nacj6_rect=texto1(matriz[5][1],120 ,630)
    nick6,nickj6_rect=texto1(matriz[5][2],120 ,660)
    pos6,posj6_rect=texto1(matriz[5][3],120 ,690)
    jugador7=load_image(imagenes[6])
    jug7,jug7_rect=texto1(matriz[6][0],364 ,600)
    nacj7,nacj7_rect=texto1(matriz[6][1],364 ,630)
    nick7,nickj7_rect=texto1(matriz[6][2],364 ,660)
    pos7,posj7_rect=texto1(matriz[6][3],364 ,690)
    jugador8=load_image(imagenes[7])
    jug8,jug8_rect=texto1(matriz[7][0],608 ,600)
    nacj8,nacj8_rect=texto1(matriz[7][1],608 ,630)
    nick8,nickj8_rect=texto1(matriz[7][2],608 ,660)
    pos8,posj8_rect=texto1(matriz[7][3],608 ,690)
    jugador9=load_image(imagenes[8])
    jug9,jug9_rect=texto1(matriz[8][0],852,600)
    nacj9,nacj9_rect=texto1(matriz[8][1],852 ,630)
    nick9,nickj9_rect=texto1(matriz[8][2],852 ,660)
    pos9,posj9_rect=texto1(matriz[8][3],852,690)
    jugador10=load_image(imagenes[9])
    jug10,jug10_rect=texto1(matriz[9][0],1095 ,600)
    nacj10,nacj10_rect=texto1(matriz[9][1],1095 ,630)
    nick10,nickj10_rect=texto1(matriz[9][2],1095 ,660)
    pos10,posj10_rect=texto1(matriz[9][3],1095,690)
    while True:
        time = clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
        screen.blit(background_image,(0,0))
        screen.blit(jugador1,(120,100))
        screen.blit(jugador2,(364,100))
        screen.blit(jugador3,(608,100))
        screen.blit(jugador4,(852,100))
        screen.blit(jugador5,(1096,100))
        screen.blit(jugador6,(120,420))
        screen.blit(jugador7,(364,420))
        screen.blit(jugador8,(608,420))
        screen.blit(jugador9,(852,420))
        screen.blit(jugador10,(1095,420))
        screen.blit(jug1,jug1_rect)
        screen.blit(nacj1,nacj1_rect)
        screen.blit(nick1,nickj1_rect)
        screen.blit(pos1,posj1_rect)
        screen.blit(jug2,jug2_rect)
        screen.blit(nacj2,nacj2_rect)
        screen.blit(nick2,nickj2_rect)
        screen.blit(pos2,posj2_rect)
        screen.blit(jug3,jug3_rect)
        screen.blit(nacj3,nacj3_rect)
        screen.blit(nick3,nickj3_rect)
        screen.blit(pos3,posj3_rect)
        screen.blit(jug4,jug4_rect)
        screen.blit(nacj4,nacj4_rect)
        screen.blit(nick4,nickj4_rect)
        screen.blit(pos4,posj4_rect)
        screen.blit(jug5,jug5_rect)
        screen.blit(nacj5,nacj5_rect)
        screen.blit(nick5,nickj5_rect)
        screen.blit(pos5,posj5_rect)
        screen.blit(jug6,jug6_rect)
        screen.blit(nacj6,nacj6_rect)
        screen.blit(nick6,nickj6_rect)
        screen.blit(pos6,posj6_rect)
        screen.blit(jug7,jug7_rect)
        screen.blit(nacj7,nacj7_rect)
        screen.blit(nick7,nickj7_rect)
        screen.blit(pos7,posj7_rect)
        screen.blit(jug8,jug8_rect)
        screen.blit(nacj8,nacj8_rect)
        screen.blit(nick8,nickj8_rect)
        screen.blit(pos8,posj8_rect)
        screen.blit(jug9,jug9_rect)
        screen.blit(nacj9,nacj9_rect)
        screen.blit(nick9,nickj9_rect)
        screen.blit(pos9,posj9_rect)
        screen.blit(jug10,jug10_rect)
        screen.blit(nacj10,nacj10_rect)
        screen.blit(nick10,nickj10_rect)
        screen.blit(pos10,posj10_rect)
        pygame.display.flip()
    return 0
if __name__ == '__main__':
        pygame.init()
        Team_select1()
