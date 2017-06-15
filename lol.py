"""
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
WIDTH = 1366
HEIGHT = 768
WIDTH = 1366
HEIGHT = 768
Player1=False
Player2=False
Select1=True
Select2=False
Select3=False
Cunt=1
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
def keyboard1():#Teclado del inicio
        global Select1, Select2 ,Select3,Cunt
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
def Team_select1():
    background_image=load_image("images/background.jpg")
    clock = pygame.time.Clock()
    while True:
        screen = pygame.display.set_mode((WIDTH, HEIGHT),FULLSCREEN)
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
                        print ("Hola")
    pygame.display.flip()
    return 0
if __name__ == '__main__':
        pygame.init()
        Team_select1()
