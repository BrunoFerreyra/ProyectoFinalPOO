#Paquetes necesarios para la creación del juego
import sys
import pygame
import boton

#Definición de colores
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
CYAN =  (  0, 255, 255)

#Definición de resolución de pantalla
PANTALLA_ANCHO = 800
PANTALLA_ALTO = 600

#Creación de ventana
screen = pygame.display.set_mode((PANTALLA_ANCHO, PANTALLA_ALTO))  
#Nombre que aparece en ventana
pygame.display.set_caption("Adventure Time")

#Carga de imagenes de botones
play_img = pygame.image.load('botones/play_btn.png').convert_alpha()
quit_img = pygame.image.load('botones/quit_btn.png').convert_alpha()

#Instancias de botones
boton_play = boton.Boton(300, 200, play_img, 1)
boton_quit = boton.Boton(300, 300, quit_img, 1)

run = True
while run:

    screen.fill(CYAN)

    if boton_play.dibujar(screen):
        print('PLAY')
    if boton_quit.dibujar(screen):
        run = False
            
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #Actualiza la pantalla en cada ciclo
    pygame.display.update()

pygame.quit()