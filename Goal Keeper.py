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
import sys, pygame
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
        linea=archis.readlines()
        save=linea[0][:-1]
        print(save)
        archis.close()
        archin.close()
        return save
def texto(texto, posx, posy, color=(255, 255, 255)):#Textos pequeños
        fuente = pygame.font.Font("Font/Soccer Jersey.ttf",120)
        salida = pygame.font.Font.render(fuente, texto, 1, color)
        salida_rect = salida.get_rect()
        salida_rect.centerx = posx
        salida_rect.centery = posy
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
# ---------------------------------------------------------------------
#Main
# ---------------------------------------------------------------------
def Team_select1():
    screen = pygame.display.set_mode((WIDTH, HEIGHT),FULLSCREEN)
    background_image=load_image("images/background.jpg")
    clock = pygame.time.Clock()
    events = pygame.event.get()
    Equipo1=Real_Madrid(WIDTH/4,HEIGHT*2/3)
    Equipo2=Juventus(WIDTH/2,HEIGHT*2/3)
    Equipo3=Manchester_United(WIDTH*3/4,HEIGHT*2/3)
    Tittle,Tittle_rect=texto("Player 1, choose your team." ,WIDTH/2 , HEIGHT/3)
    while True:
        time = clock.tick(60)
        keyboard1()
        global Select1, Select2, Select3,Cunt
        for event in events:#Teclado para la Pausa
                if event.type == QUIT:
                        sys.exit(0)
                if event.type == pygame.KEYDOWN:
                    print (event.key)
                    if event.key==pygame.K_d:
                                        Cunt+=1
                                        print ("presion s", Cunt)
                    if event.key==pygame.K_a:
                                        Cunt-=1
                                        print ("presion w",Cunt)
                    if event.key==K_KP_ENTER:#Exit
                            if Select1==True:
                                grabartxt("Memoria/Jugador1-Equipo","Real Madrid")
                            if Select2==True:
                                grabartxt("Memoria/Jugador1-Equipo","Juventus")
                            if Select3==True:
                                grabartxt("Memoria/Jugador1-Equipo","Manchester United")
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
        global Select1, Select2, Select3
        for event in pygame.event.get():#Teclado para la Pausa
                if event.type == QUIT:
                        sys.exit(0)
                if event.type==pygame.KEYDOWN:
                        if event.key==K_KP_ENTER:#Exit
                                        return Team_select1()
        screen.blit(background_image,(0,0))
        screen.blit(Tittle,Tittle_rect)
        screen.blit(Equipo1.shield,Equipo1.rect)
        screen.blit(Equipo2.shield,Equipo2.rect)
        screen.blit(Equipo3.shield,Equipo3.rect)
        pygame.display.flip()
        return 0
if __name__ == '__main__':
        pygame.init()
        Team_select1()
"""
Referencias
https://www.luisllamas.es/controlar-arduino-con-python-y-la-libreria-pyserial/
"""
