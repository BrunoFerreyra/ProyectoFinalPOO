#Paquetes necesarios para la creación del juego
import sys
import pygame
import boton

#Definición de colores
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)

#Definición de resolución de pantalla
PANTALLA_ANCHO = 1100
PANTALLA_ALTO = 550

#Creación de ventana 1100 px ancho 550 px alto
screen = pygame.display.set_mode((PANTALLA_ANCHO, PANTALLA_ALTO))  
#Nombre que aparece en ventana
pygame.display.set_caption("Adventure Time")

#Carga de imagenes de botones
play_img = pygame.image.load('botones/play_btn.png').convert_alpha()
exit_img = pygame.image.load('botones/exit_btn.png').convert_alpha()
play_img.set_colorkey(WHITE)
exit_img.set_colorkey(WHITE)

#Instancias de botones
boton_play = boton.Boton(400, 200, play_img, 1.5)
boton_exit = boton.Boton(400, 300, exit_img, 1.5)

run = True
while run:

    screen.fill(WHITE)

    if boton_play.dibujar(screen):
        print('PLAY')
    if boton_exit.dibujar(screen):
        run = False
            
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #Actualiza la pantalla en cada ciclo
    pygame.display.update()

pygame.quit()