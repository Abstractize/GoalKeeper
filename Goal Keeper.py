"""
Instituto Tecnológico de Costa Rica
Ingeniería en Computadores
Proyecto #3
Lenguaje: Python 3.6.1
Versión: 1.0
Fecha de última modificación: 5/18/2017
Estudiantes: Gabriel Abarca Aguiar y Andrés Zuñiga Prieto
Carné:2017110442 y 2016228708
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
WIDTH = 1366#Largo de la Pantalla   
HEIGHT = 768#Alto de la Pantalla
Player1=False
Player2=False
Select1=True#Booleanos para escoger
Select2=False
Select3=False
tirador=1#Contador de turno del jugador
Cunt=1#Contador para menus
ContadorDePersonajes=1#Contador para almacenar al jugador
contador=0#contador para almacenar los jugadores
elegidos=""#Jugadores Elegidos
arduino = serial.Serial("COM3", 9600)#Arduino
# ---------------------------------------------------------------------
#Objetos
# ---------------------------------------------------------------------
class Potenciometro():#Intento de meter el potenciometro en el juego
    def __init__(self):
        self.rango=read_arduino()
    def update(self):
        global Cunt
        if 1023>self.rango>0:
            Cunt=1
class Equipo():
    def __init__(self):
        self.Jugadores=11
class Real_Madrid(Equipo):#Equipo del Real Madrid
    def __init__(self,x,y):
        self.shield=load_image("Images/RealMadridLogo.png",True)
        self.rect = self.shield.get_rect()
        self.rect.centerx=x
        self.rect.centery=y
class Juventus(Equipo):#Equipo Juventus
    def __init__(self,x,y):
        self.shield=load_image("Images/JuventusLogo.png",True)
        self.rect = self.shield.get_rect()
        self.rect.centerx=x
        self.rect.centery=y
class Manchester_United(Equipo):#Equipo Manchester
    def __init__(self,x,y):
        self.shield=load_image("Images/ManchesterLogo.png",True)
        self.rect = self.shield.get_rect()
        self.rect.centerx=x
        self.rect.centery=y
class Flecha():#Flecha de selección
    def __init__(self,player):
        if player==1:#Cambia de color según el jugador
            self.image=load_image("Images/FlechaAzul.png",True)
        elif player==2:
            self.image=load_image("Images/FlechaRoja.png",True)
        self.rect=self.image.get_rect()
    def update_1(self):#Usa el contador para seleccionar la posición de la flecha
        global Cunt
        self.rect.centery=HEIGHT/6
        if Cunt==1:
            self.rect.centerx=WIDTH/4
        elif Cunt==2:
            self.rect.centerx=WIDTH/2
        elif Cunt==3:
            self.rect.centerx=WIDTH*3/4
    def update_2(self):#Usa el contador, pero esta vez llega hasta 7 debido a que son 7 jugadores
        global ContadorDePersonajes
        if 1<=ContadorDePersonajes<=5:#Posición en Y, alta
            self.rect.centery=50
        elif 6<=ContadorDePersonajes<=10:#Posición en Y, baja
            self.rect.centery=370
        if ContadorDePersonajes%5==1:#Posición 1 y 6 en X
            self.rect.centerx=195
        elif ContadorDePersonajes%5==2:#Posición 2 y 7 en X
            self.rect.centerx=364+75
        elif ContadorDePersonajes%5==3:#Posición 3 en X
            self.rect.centerx=608+75
        elif ContadorDePersonajes%5==4:#Posición 4 en X
            self.rect.centerx=852+75
        elif ContadorDePersonajes%5==0:#Posición 5 en X
            self.rect.centerx=1096+75
        if ContadorDePersonajes<1:#Si el número es menor a los solicitados
            ContadorDePersonajes=7
        elif ContadorDePersonajes>7:#Si el número es mayor a los solicitados
            ContadorDePersonajes=1
    def update_3(self):#Igual que el primero, pero esta vez cambia la altura de la flecha
        global Cunt
        self.rect.centery=HEIGHT/2
        if Cunt==1:
            self.rect.centerx=WIDTH/4
        elif Cunt==2:
            self.rect.centerx=WIDTH/2
        elif Cunt==3:
            self.rect.centerx=WIDTH*3/4
#Funciones
def load_image(filename, transparent=False):#Llama imagenes, agarrado de el proyecto de Donkey Kong de Gabriel Abarca
        try: image = pygame.image.load(filename)#Llama la imagen en caso de ser posible
        except (pygame.error,message):#Si no es posible tira error
                raise (SystemExit, message)
        image = image.convert()
        if transparent:#Si es transparente
                color = image.get_at((0,0))#Agarra el fondo y lo pone transparente
                image.set_colorkey(color, RLEACCEL)
        return image#Retorna la imagen

def send_arduino(mesagge):#Función que manda mensajes al arduino
    global arduino
    tiempo.sleep(2)#Delay de tiempo
    arduino.write(b+message)#ejemplo: mesagge=b'9'
    arduino.close()#cierra el puerto del arduino
def read_arduino():#Lee los mensajes del Arduino
        global arduino
        tiempo.sleep(2)#Delay
        rawString = arduino.readline()#lee la linea del arduino
        print(rawString)#La imprime como verificación
        arduino.close()
        return rawString#la retorna para ser usada con las funciones
    
def grabartxt(archivo,valor):#Grabar al TXT
        archi=open(archivo,'w')#Esta función le escribe encima al txt
        archi.write(valor+"\n")#deja un "enter"
        archi.close()
def agregartxt(archivo,valor):#Grabar al TXT
        archi=open(archivo,'a')#Esta función no le escribe encima
        archi.write(valor+"\n")#deja un "enter"
        archi.close()
def readtxt(archivo):#Lector de TXT
        archi=open(archivo,'r')#lee el archivo
        linea=archi.readlines()
        save=linea[0][:-1]#guarda la primera linea menos el "enter"
        archi.close()
        return save
def texto(texto, posx, posy, color=(255, 255, 255)):#Textos Grandes
        fuente = pygame.font.Font("Font/Soccer Jersey.ttf",120)
        salida = pygame.font.Font.render(fuente, texto, 1, color)
        salida_rect = salida.get_rect()#Sitúa en el centro
        salida_rect.centerx = posx
        salida_rect.centery = posy
        return salida, salida_rect
def texto1(texto, posx, posy, color=(255, 255, 255)):#Textos pequeños
        fuente = pygame.font.Font("Font/Soccer Jersey.ttf",24)
        salida = pygame.font.Font.render(fuente, texto, 1, color)
        salida_rect = salida.get_rect()#Sitúa en la esquina superior izquierda
        salida_rect.x = posx
        salida_rect.y = posy
        return salida, salida_rect
def texto2(texto, posx, posy, color=(255, 255, 255)):#Textos pequeños
        fuente = pygame.font.Font("Font/Soccer Jersey.ttf",24)
        salida = pygame.font.Font.render(fuente, texto, 1, color)
        salida_rect = salida.get_rect()#Situa en el centro
        salida_rect.centerx = posx
        salida_rect.centery = posy
        return salida, salida_rect
def keyboard1():#Teclado de los menús, inspirado en la progra de DK de Gabriel Abarca
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
def keyboard2():#Teclado de escoger al arbitro, la diferencia es que invalida el Booleano2 para que no se use la posición del centro
        global Select1, Select2 ,Select3,Cunt
        ##print ("Si no imprimo esto, no funciona")
        if Cunt>3:
                Cunt=1
        if Cunt<=0:
                Cunt=3
        if Cunt==2:
            Cunt=1
        if Cunt==1:
                Select1=True
                Select2=False
                Select3=False
        elif Cunt==3:
                Select1=False
                Select2=False
                Select3=True

def displayteam(Player):#Muestra las imágenes según el equipo escogido
    if Player==1:
        team=readtxt("Memoria/Jugador1-Equipo.txt")#Lee el txt del jugador1
    elif Player==2:
        team=readtxt("Memoria/Jugador2-Equipo.txt")#Lee el txt dle jugador2
    if team=="Real Madrid":
        archi=open("Memoria/RealMadrid-Jugadores.txt",'r')#Abre los jugadores del equipo escogido
    elif team=="Juventus":
        archi=open("Memoria/Juventus-Jugadores.txt",'r')
    elif team =="Manchester United":
        archi=open("Memoria/ManchesterUnited-Jugadores.txt",'r')
    linea=archi.readlines()
    Jugador1=elementos(linea[0][:-1])#Guarda los jugadores en variabes
    Jugador2=elementos(linea[1][:-1])
    Jugador3=elementos(linea[2][:-1])
    Jugador4=elementos(linea[3][:-1])#Función elementos es una función que quita los demilitadores y acoomoda los nombres
    Jugador5=elementos(linea[4][:-1])
    Jugador6=elementos(linea[5][:-1])
    Jugador7=elementos(linea[6][:-1])
    archi.close
    Jugadores=[Jugador1,Jugador2,Jugador3,Jugador4,Jugador5,Jugador6,Jugador7]
    return Jugadores#Retorna los jugadores en una lista
def displaykeeper(Player):
    if Player==1:#Funciona igual que displayteam, pero a diferencia de ese, muestra solo los porteros
        team=readtxt("Memoria/Jugador1-Equipo.txt")
    elif Player==2:
        team=readtxt("Memoria/Jugador2-Equipo.txt")
    if team=="Real Madrid":
        archi=open("Memoria/RealMadrid-Porteros.txt",'r')
    elif team=="Juventus":
        archi=open("Memoria/Juventus-Porteros.txt",'r')
    elif team =="Manchester United":
        archi=open("Memoria/ManchesterUnited-Porteros.txt",'r')
    linea=archi.readlines()
    Jugador11=elementos(linea[0][:-1])
    Jugador12=elementos(linea[1][:-1])
    Jugador13=elementos(linea[2][:-1])
    archi.close
    Jugadores=[Jugador11,Jugador12,Jugador13]
    return Jugadores
def displayimages(Player):#Muestra las imagenes de lso jugadores
    if Player==1:#Lee la memoria del equipo elegido
        team=readtxt("Memoria/Jugador1-Equipo.txt")
    elif Player==2:
        team=readtxt("Memoria/Jugador2-Equipo.txt")
    if team=="Real Madrid":
        dic="Images/Real Madrid/"
    elif team=="Juventus":
        dic="Images/Juventus/"
    elif team =="Manchester United":
        dic="Images/Manchester United/"
    Jugador1=dic+"jugador1.jpg"#Agrega un dic, que es le directorio en el cual se encuentran las imagenes distribuidas por equipo
    Jugador2=dic+"jugador2.jpg"
    Jugador3=dic+"jugador3.jpg"
    Jugador4=dic+"jugador4.jpg"
    Jugador5=dic+"jugador5.jpg"
    Jugador6=dic+"jugador6.jpg"
    Jugador7=dic+"jugador7.jpg"
    Jugadores=[Jugador1,Jugador2,Jugador3,Jugador4,Jugador5,Jugador6,Jugador7]
    return Jugadores#Retorna las direcciones de las imagenes
def displayimagesk(Player):#Funciona igual que displayimages(), pero con los porteros
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
    Jugador11=dic+"jugador11.jpg"#Los porteros están como jugador1+1,2 o 3
    Jugador12=dic+"jugador12.jpg"
    Jugador13=dic+"jugador13.jpg"
    Jugadores=[Jugador11,Jugador12,Jugador13]
    return Jugadores#Retorna los directorios
def elementos(string):#Funcion recursiva que acomoda el txt en una matriz
    if isinstance(string,str):
        return elementos_aux(string,"",[])#Validación
    else:
        return"Error"
def elementos_aux(string,nombre,lista):#Función recursiva
    if string=="":
        lista.append(nombre)
        return lista
    else:
        if string[0]=="\t":#Encuentra el delimitador y separa
            lista.append(nombre)
            return elementos_aux(string[1:],"",lista)#Retorna a la recursiva
        else:
            nombre+=string[0]
            return elementos_aux(string[1:],nombre,lista)#Retorna a la recursiva
def mostrarjugadores(Player):#Muestra las imagenes de los jugadores escogidos
    mod=".jpg"#guarda el .jpg en una variable
    if Player==1:#en caso del jugador uno, lee las memoras del jugador
        team=readtxt("Memoria/Jugador1-Equipo.txt")
        artilleros=open("Memoria/Jugador1-Elegidos.txt",'r')
        keeper=open("Memoria/Jugador1-Portero.txt",'r')
    elif Player==2:#Al igual que en el jugador dos.
        team=readtxt("Memoria/Jugador2-Equipo.txt")
        artilleros=open("Memoria/Jugador2-Elegidos.txt",'r')
        keeper=open("Memoria/Jugador2-Portero.txt",'r')
    if team=="Real Madrid":#agrega direcciones de acuerdo al equipo escogido
        dic="Images/Real Madrid/"
    elif team=="Juventus":
        dic="Images/Juventus/"
    elif team =="Manchester United":
        dic="Images/Manchester United/"
    linea=artilleros.readlines()
    lineas=keeper.readlines()
    chosen1=dic+linea[0][:-1]+mod#agarra al jugador que fue escogido y le agrega el .jpg
    chosen2=dic+linea[1][:-1]+mod
    chosen3=dic+linea[2][:-1]+mod
    chosen4=dic+lineas[0][:-1]+mod#El portero está guardado en txt diferente
    Chosen=[chosen1,chosen2,chosen3,chosen4]
    artilleros.close
    keeper.close
    return (Chosen)#Retorna las imagenes de lso jugadores escogidos
def logodis(Player):#Mostrador de logos en la parte del VS
    if Player==1:
        team=readtxt("Memoria/Jugador1-Equipo.txt")
    elif Player==2:
        team=readtxt("Memoria/Jugador2-Equipo.txt")
    if team=="Real Madrid":
        image=load_image("Images/RealMadridLogo.png",True)
    elif team=="Juventus":
        image=load_image("Images/JuventusLogo.png",True)
    elif team =="Manchester United":
        image=load_image("Images/ManchesterLogo.png",True)
    return image#Retorna las imagenes de acuerdo al jugador
        
def portero():#agarra número aleartorios para usarlos como el portero
    dif=readtxt("Dificultad.txt")
    lista=[1,2,3,4,5,6]
    if dif=="Easy":#Depende de la dificultad escogida la inicio
        return [random.choice(lista),random.choice(lista)]
    elif dif=="Medium":
        return [random.choice(lista),random.choice(lista),random.choice(lista)]
    elif dif=="Hard":
        return [random.choice(lista),random.choice(lista),random.choice(lista),random.choice(lista)]


def compuerta():#Corregir luego con el arduino
    lista=[1,2,3,4,5,6]
    return random,choice(lista)
def comparador(portero,compuerta):#Compara que el número de la compuerto esté dentro de los numúeros elegidos
    for compuerta in portero:
        return False#si pasa retorna falso debido a que no hubo Gol
    else:
        return True#Si no pasa, retorna verdadero, si hubo Gol
    
# ---------------------------------------------------------------------
#Pantallas
# ---------------------------------------------------------------------
def Team_select1():#Pantalla de Selección de Equipo de Jugador 1
    screen = pygame.display.set_mode((WIDTH, HEIGHT),FULLSCREEN)#Pantalla
    background_image=load_image("images/background.jpg")#Imagen de Fondo
    clock = pygame.time.Clock()#Reloj
    selector=Flecha(1)#Flecha
    Equipo1=Real_Madrid(WIDTH/4,HEIGHT*2/3)#Escudos
    Equipo2=Juventus(WIDTH/2,HEIGHT*2/3)
    Equipo3=Manchester_United(WIDTH*3/4,HEIGHT*2/3)
    Tittle,Tittle_rect=texto("Player 1, choose your team." ,WIDTH/2 , HEIGHT/3)#Títulos
    while True:
        time = clock.tick(60)
        keyboard1()#Se llama el teclado de contador
        selector.update_1()#se llama el uso de los movimientos del selector
        global Select1, Select2, Select3,Cunt
        for event in pygame.event.get():#Teclado para probar
            if event.type == QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_d:
                    Cunt+=1#Suma 1 al contador
                if event.key==pygame.K_a:
                    Cunt-=1#Resta 1 al contador
                if event.key==K_KP_ENTER:#Exit
                    if Select1==True:
                        grabartxt("Memoria/Jugador1-Equipo.txt","Real Madrid")
                        Select1=False#Guarda en la memoria y retorna el Booleano Falso
                    if Select2==True:
                        grabartxt("Memoria/Jugador1-Equipo.txt","Juventus")
                        Select1=False
                    if Select3==True:
                        grabartxt("Memoria/Jugador1-Equipo.txt","Manchester United")
                        Select3=False
                    return main(1)
        #Muestra las imagenes
        screen.blit(background_image,(0,0))
        screen.blit(Tittle,Tittle_rect)
        screen.blit(Equipo1.shield,Equipo1.rect)
        screen.blit(Equipo2.shield,Equipo2.rect)
        screen.blit(Equipo3.shield,Equipo3.rect)
        screen.blit(selector.image,selector.rect)
        pygame.display.flip()
    return 0

def Team_select2():#Pantalla de Selección para el jugador 2
    screen = pygame.display.set_mode((WIDTH, HEIGHT),FULLSCREEN)#Pantalla
    background_image=load_image("images/background.jpg")#Imagen de Fondo
    clock = pygame.time.Clock()#reloj
    Equipo1=Real_Madrid(WIDTH/4,HEIGHT*2/3)#Logo del Real
    Equipo2=Juventus(WIDTH/2,HEIGHT*2/3)#Logo del Juventus
    Equipo3=Manchester_United(WIDTH*3/4,HEIGHT*2/3)#Logo del Manchester
    selector=Flecha(2)#Flecha color rojo
    Tittle,Tittle_rect=texto("Player 2, choose your team." ,WIDTH/2 , HEIGHT/3)#Título
    while True:
        time = clock.tick(60)
        keyboard1()#Se llama el mismo teclado
        selector.update_1()#Mismo uso de la flecha
        global Select1, Select2, Select3,Cunt
        for event in pygame.event.get():#Teclado para la Pausa
            if event.type == QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_d:
                    Cunt+=1
                if event.key==pygame.K_a:
                    Cunt-=1
                if event.key==K_KP_ENTER:#Graban el equipo elegido
                    if Select1==True:
                        grabartxt("Memoria/Jugador2-Equipo.txt","Real Madrid")
                        Select1=False
                        return main(2)
                    if Select2==True:
                        grabartxt("Memoria/Jugador2-Equipo.txt","Juventus")
                        Select2=False
                        return main(2)
                    if Select3==True:
                        grabartxt("Memoria/Jugador2-Equipo.txt","Manchester United")
                        Select3=False
                        return main(2)
        #Llama las imágenes
        screen.blit(background_image,(0,0))
        screen.blit(Tittle,Tittle_rect)
        screen.blit(Equipo1.shield,Equipo1.rect)
        screen.blit(Equipo2.shield,Equipo2.rect)
        screen.blit(Equipo3.shield,Equipo3.rect)
        screen.blit(selector.image,selector.rect)

        pygame.display.flip()
    return 0
def choseplayers1(player):
    screen = pygame.display.set_mode((WIDTH, HEIGHT),FULLSCREEN)
    background_image=load_image("images/background.jpg")
    clock = pygame.time.Clock()
    #Dependiendo del jugador muestra un título diferente
    if player == 1:
        Tittle,Tittle_rect=texto2("Player 1, choose your team players." ,WIDTH/2 , HEIGHT/16)
    elif player == 2:
        Tittle,Tittle_rect=texto2("Player 2, choose your team players." ,WIDTH/2 , HEIGHT/16)
    matriz=displayteam(player)#Llama el display team para mostras la info de 
    selector=Flecha(player)
    imagenes=displayimages(player)#Llama las imagenes de los jugadores según el jugador que entre como parámetro
    #Display de la información y las imagenes
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
    font = pygame.font.Font(None, 24)#Se agregan valores que muestran los jugadores escogidos
    while True:
        time = clock.tick(60)
        selector.update_2()
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                global ContadorDePersonajes,contador,elegidos
                if event.key==K_a:
                    ContadorDePersonajes-=1
                if event.key==K_d:
                    ContadorDePersonajes+=1
                #Se usa un contador, si es 0 reescribe en el txt, y en el resto agrega valores
                if player==1:
                    if contador==0:
                        if event.key==K_KP_ENTER:
                            elegidos+=matriz[ContadorDePersonajes-1][0]+","
                            grabartxt('Memoria/Jugador1-Elegidos.txt',"jugador"+str(ContadorDePersonajes))
                            contador+=1
                    elif 0<contador<2:
                        if event.key==K_KP_ENTER:
                            elegidos+=matriz[ContadorDePersonajes-1][0]+","
                            agregartxt('Memoria/Jugador1-Elegidos.txt',"jugador"+str(ContadorDePersonajes))
                            contador+=1
                    elif contador == 2:
                        if event.key==K_KP_ENTER:
                            elegidos=""
                            contador=0
                            agregartxt('Memoria/Jugador1-Elegidos.txt',"jugador"+str(ContadorDePersonajes))
                            return main(3)#En el tercer jugador devuelve a la main y guarda los valores
                elif player==2:
                    if contador==0:
                        if event.key==K_KP_ENTER:
                            elegidos+=matriz[ContadorDePersonajes-1][0]+","
                            grabartxt('Memoria/Jugador2-Elegidos.txt',"jugador"+str(ContadorDePersonajes))
                            contador+=1
                    elif 0<contador<2:
                        if event.key==K_KP_ENTER:
                            elegidos+=matriz[ContadorDePersonajes-1][0]+","
                            agregartxt('Memoria/Jugador2-Elegidos.txt',"jugador"+str(ContadorDePersonajes))
                            contador+=1
                    elif contador == 2:
                        if event.key==K_KP_ENTER:
                            elegidos=""
                            contador=0
                            agregartxt('Memoria/Jugador2-Elegidos.txt',"jugador"+str(ContadorDePersonajes))
                            return main(4)
        #Display de todas las imagenes y títulos
        block = font.render("Elegidos:"+elegidos, True, (255, 255, 255))
        screen.blit(background_image,(0,0))
        screen.blit(selector.image,selector.rect)
        screen.blit(jugador1,(120,100))
        screen.blit(block, (200 ,740))
        screen.blit(jugador2,(364,100))
        screen.blit(jugador3,(608,100))
        screen.blit(jugador4,(852,100))
        screen.blit(jugador5,(1096,100))
        screen.blit(jugador6,(120,420))
        screen.blit(jugador7,(364,420))
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
        screen.blit(Tittle,Tittle_rect)
        pygame.display.flip()
    return 0
def VS():#Pantalla que muestra los jugadores seleccionados
    screen = pygame.display.set_mode((WIDTH, HEIGHT),FULLSCREEN)
    background_image=load_image("images/background.jpg")
    clock = pygame.time.Clock()
    Tittle,Tittle_rect=texto("VS" ,WIDTH/2 , HEIGHT/2)
    pl1=mostrarjugadores(1)#Jugadores del jugador 1
    pl2=mostrarjugadores(2)#Jugadores del jugador 2
    logo1=logodis(1)#Muestra el logo del jugador 1
    logo2=logodis(2)#Muestra el logo del jugador 2
    #Jugador 1
    art10=load_image(pl1[3])#Portero
    art11=load_image(pl1[0])#Artillero 1
    art12=load_image(pl1[1])#Artillero 2
    art13=load_image(pl1[2])#Artillero 3
    #Jugador 2
    art20=load_image(pl2[3])#Portero
    art21=load_image(pl2[0])#Artillero 1
    art22=load_image(pl2[1])#Artilerro 2
    art23=load_image(pl2[2])#Artillero 3
    while True:
        time = clock.tick(60)
        keyboard1()
        global Select1, Select2, Select3,Cunt
        for event in pygame.event.get():#Teclado
            if event.type == QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key==K_KP_ENTER:#Exit
                    return main(8)
        #Muestra las imágenes
        screen.blit(background_image,(0,0))
        screen.blit(Tittle,Tittle_rect)
        screen.blit(art10,(WIDTH/5-75 ,HEIGHT/4-90))
        screen.blit(art11,(WIDTH*2/5-75 ,HEIGHT/4-90))
        screen.blit(art12,(WIDTH*3/5-75 ,HEIGHT/4-90))
        screen.blit(art13,(WIDTH*4/5-75 ,HEIGHT/4-90))
        screen.blit(art20,(WIDTH/5-75 ,HEIGHT*3/4-90))
        screen.blit(art21,(WIDTH*2/5-75 ,HEIGHT*3/4-90))
        screen.blit(art22,(WIDTH*3/5-75 ,HEIGHT*3/4-90))
        screen.blit(art23,(WIDTH*4/5-75 ,HEIGHT*3/4-90))
        screen.blit(logo1,(0 ,0))
        screen.blit(logo2,(WIDTH*4/5+90 ,HEIGHT/2))

        pygame.display.flip()
    return 0
def Principal():#Menú Principal
    screen = pygame.display.set_mode((WIDTH, HEIGHT),FULLSCREEN)
    background_image=load_image("images/background.jpg")
    clock = pygame.time.Clock()
    selector=Flecha(1)#Flecha para seleccionar acción
    Tittle,Tittle_rect=texto("Goal Keeper!!" ,WIDTH/2 , HEIGHT/3)#Título
    Facil,Facil_rect=texto("Stats" ,WIDTH/4,HEIGHT*2/3)#Stats y About
    Intermedio,Intermedio_rect=texto("Play" ,WIDTH/2,HEIGHT*2/3)#Jugar
    Difícil,Difícil_rect=texto("Exit" ,WIDTH*3/4,HEIGHT*2/3)#Salir
    while True:
        time = clock.tick(60)
        keyboard1()
        selector.update_3()
        global Select1, Select2, Select3,Cunt
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            #Mismo método del contador y de los booleanos para el menú
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_d:
                    Cunt+=1
                if event.key==pygame.K_a:
                    Cunt-=1
                if event.key==K_KP_ENTER:
                    if Select1==True:
                        Select1=False
                        return main(-3)
                    if Select2==True:
                        Select2=False
                        return main(-1)
                    if Select3==True:
                        Select3=False
                        return sys.exit
        #Muestras títulos o imagenes
        screen.blit(background_image,(0,0))
        screen.blit(Tittle,Tittle_rect)
        screen.blit(Facil,Facil_rect)
        screen.blit(Intermedio,Intermedio_rect)
        screen.blit(Difícil,Difícil_rect)
        screen.blit(selector.image,selector.rect)

        pygame.display.flip()
    return 0
def choose_goalkeeper(player):#Escoger portero
    screen = pygame.display.set_mode((WIDTH, HEIGHT),FULLSCREEN)
    background_image=load_image("images/background.jpg")
    clock = pygame.time.Clock()
    if player == 1:
        Tittle,Tittle_rect=texto2("Player 1, choose your Goal Keeper." ,WIDTH/2 , HEIGHT/16)
    elif player == 2:
        Tittle,Tittle_rect=texto2("Player 2, choose your Goal Keeper." ,WIDTH/2 , HEIGHT/16)
    matriz=displaykeeper(player)#Establece una lista con los porteros
    selector=Flecha(player)
    imagenes=displayimagesk(player)#Establece una lista con las imágenes de los porteros
    #Carga imágenes y textos de los porteros
    jugador1=load_image(imagenes[0])
    jug1,jug1_rect=texto1(matriz[0][0],WIDTH/4-75 ,HEIGHT/4+180)
    nacj1,nacj1_rect=texto1(matriz[0][1],WIDTH/4-75 ,HEIGHT/4+180+30)
    nick1,nickj1_rect=texto1(matriz[0][2],WIDTH/4-75 ,HEIGHT/4+180+(30*2))
    pos1,posj1_rect=texto1(matriz[0][3],WIDTH/4-75 ,HEIGHT/4+180+(30*3))
    jugador2=load_image(imagenes[1])
    jug2,jug2_rect=texto1(matriz[1][0],WIDTH/2-75 ,HEIGHT/4+180)
    nacj2,nacj2_rect=texto1(matriz[1][1],WIDTH/2-75 ,HEIGHT/4+180+30)
    nick2,nickj2_rect=texto1(matriz[1][2],WIDTH/2-75 ,HEIGHT/4+180+(30*2))
    pos2,posj2_rect=texto1(matriz[1][3],WIDTH/2-75 ,HEIGHT/4+180+(30*3))
    jugador3=load_image(imagenes[2])
    jug3,jug3_rect=texto1(matriz[2][0],WIDTH*3/4-75 ,HEIGHT/4+180)
    nacj3,nacj3_rect=texto1(matriz[2][1],WIDTH*3/4-75 ,HEIGHT/4+180+30)
    nick3,nickj3_rect=texto1(matriz[2][2],WIDTH*3/4-75 ,HEIGHT/4+180+(30*2))
    pos3,posj3_rect=texto1(matriz[2][3],WIDTH*3/4-75,HEIGHT/4+180+(30*3))
    while True:
        time = clock.tick(60)
        selector.update_1()
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                global Cunt
                if event.key==K_a:
                    Cunt-=1
                if event.key==K_d:
                    Cunt+=1
                #Guarda la información del portero según el jugador
                if player==1:
                    if event.key==K_KP_ENTER:
                        grabartxt('Memoria/Jugador1-Portero.txt',"jugador1"+str(Cunt))
                        return main(5)
                elif player==2:
                    if event.key==K_KP_ENTER:
                        grabartxt('Memoria/Jugador2-Portero.txt',"jugador1"+str(Cunt))
                        return main(6)
        #Muestra las imágenes y los títulos
        screen.blit(background_image,(0,0))
        screen.blit(jugador1,(WIDTH/4-75,HEIGHT/4))
        screen.blit(jugador2,(WIDTH/2-75,HEIGHT/4))
        screen.blit(jugador3,(WIDTH*3/4-75,HEIGHT/4))
        screen.blit(Tittle,Tittle_rect)
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
        screen.blit(selector.image,selector.rect)
        pygame.display.flip()
    return 0
def MenuDificultad():#Escoge la dificultad del juego
    screen = pygame.display.set_mode((WIDTH, HEIGHT),FULLSCREEN)#}
    background_image=load_image("images/background.jpg")
    clock = pygame.time.Clock()
    selector=Flecha(1)#Flecha
    #Títulos
    Tittle,Tittle_rect=texto("Goal Keeper!!" ,WIDTH/2 , HEIGHT/3)
    Facil,Facil_rect=texto("Easy" ,WIDTH/4,HEIGHT*2/3)
    Intermedio,Intermedio_rect=texto("Medium" ,WIDTH/2,HEIGHT*2/3)
    Difícil,Difícil_rect=texto("Hard" ,WIDTH*3/4,HEIGHT*2/3)
    while True:
        time = clock.tick(60)
        keyboard1()
        selector.update_3()
        global Select1, Select2, Select3,Cunt
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_d:
                    Cunt+=1
                if event.key==pygame.K_a:
                    Cunt-=1
                if event.key==K_KP_ENTER:#Guarda la dificultad según el booleano elegido
                    if Select1==True:
                        grabartxt("Memoria/Dificultad.txt","Easy")
                        Select1=False
                    if Select2==True:
                        grabartxt("Memoria/Dificultad.txt","Medium")
                        Select2=False
                    if Select3==True:
                        grabartxt("Memoria/Dificultad.txt","Hard")
                        Select3=False
                    return main(0)
        #Muestra las imágenes
        screen.blit(background_image,(0,0))
        screen.blit(Tittle,Tittle_rect)
        screen.blit(Facil,Facil_rect)
        screen.blit(Intermedio,Intermedio_rect)
        screen.blit(Difícil,Difícil_rect)
        screen.blit(selector.image,selector.rect)

        pygame.display.flip()
    return 0

def choosereferee():#Escoger el arbitro
    screen = pygame.display.set_mode((WIDTH, HEIGHT),FULLSCREEN)
    background_image=load_image("images/background.jpg")
    clock = pygame.time.Clock()
    selector=Flecha(1)#Flecha
    #Títulos
    Tittle,Tittle_rect=texto("Choose your referee" ,WIDTH/2 , HEIGHT/3)
    Facil,Facil_rect=texto("Gabriel" ,WIDTH/4,HEIGHT*2/3)
    Difícil,Difícil_rect=texto("Andrés" ,WIDTH*3/4,HEIGHT*2/3)
    while True:
        time = clock.tick(60)
        keyboard2()
        selector.update_1()
        global Select1, Select2, Select3,Cunt
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_d:
                    Cunt+=2
                if event.key==pygame.K_a:
                    Cunt-=2
                #Guarda si escogió a Gabriel o Andrés
                if event.key==K_KP_ENTER:
                    if Select1==True:
                        Select1=False
                        grabartxt("Memoria/Arbitro.txt","Gabriel")
                        return main(7)
                    if Select3==True:
                        Select3=False
                        grabartxt("Memoria/Arbitro.txt","Andres")
                        return main(7)
        #Muestra imágenes
        screen.blit(background_image,(0,0))
        screen.blit(Tittle,Tittle_rect)
        screen.blit(Facil,Facil_rect)
        screen.blit(Difícil,Difícil_rect)
        screen.blit(selector.image,selector.rect)
        pygame.display.flip()
    return 0
def ahoratirando(jugador,turno):#Función que debería mostrar el artillero, el portero, penales cobrados, fallados, y retornaría a mostrar si hubo Gol o no
    return sys.exit
#Main
#---------------------------------------------------------------------------------
def main(pantalla):#Función Main que llama las otras pantallas dependiendo del parametro que le entra
    if pantalla==-2:
        return Principal()
    elif pantalla==-1:
        return MenuDificultad()
    elif pantalla == 0:
        return Team_select1()
    elif pantalla==1:
        return Team_select2()
    elif pantalla==2:
        return choseplayers1(1)
    elif pantalla==3:
        return choseplayers1(2)
    elif pantalla==4:
        return choose_goalkeeper(1)
    elif pantalla==5:
        return choose_goalkeeper(2)
    elif pantalla == 6:
        return choosereferee()
    elif pantalla == 7:
        return VS()
    elif pantalla== 8:
        return ahoratirando(1,tirador)
    elif pantalla==9:
        return ahoratirando(2,tirador)
if __name__ == '__main__':
        pygame.init()
        main(-2)
