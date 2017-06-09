#Módulos
from tkinter import *
import sys, pygame
from pygame.locals import *
# ---------------------------------------------------------------------
#Variables
WIDTH = 1366
HEIGHT = 768
# ---------------------------------------------------------------------
#Objetos
# ---------------------------------------------------------------------
class Equipo():
    def __init__(self,escudo):
        self.Jugadores=11
        self.shield=escudo
    
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
# ---------------------------------------------------------------------
#Main
# ---------------------------------------------------------------------
def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT),FULLSCREEN)
    background_image=load_image("images/background.jpg")
    while True:
        screen.blit(background_image,(0,0))
        pygame.display.flip()

        return 0

if __name__ == '__main__':
        pygame.init()
        main()
        
            
    
