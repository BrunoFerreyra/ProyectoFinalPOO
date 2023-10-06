#Paquetes necesarios para la creación del juego
import sys
import pygame
from boton import Boton

#Definición de colores
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
CYAN =  (  0, 255, 255)

#Definición de resolución de pantalla
PANTALLA_ANCHO = 800
PANTALLA_ALTO = 600
x = 0

#Creación de ventana
screen = pygame.display.set_mode((PANTALLA_ANCHO, PANTALLA_ALTO))  
#Nombre que aparece en ventana
pygame.display.set_caption("Adventure Time")

#Carga de imagenes
titulo_img = pygame.image.load('imagenes/adventure_time.png').convert_alpha()
fondo_img = pygame.image.load('imagenes/fondo.png').convert_alpha()
play_img = pygame.image.load('imagenes/play_btn.png').convert_alpha()
option_img = pygame.image.load('imagenes/option_btn.png').convert_alpha()
quit_img = pygame.image.load('imagenes/quit_btn.png').convert_alpha()

#Instancias de botones
boton_play = Boton(300, 250, play_img, 1)
boton_option = Boton(300, 350, option_img, 1)
boton_quit = Boton(300, 450, quit_img, 1)

run = True
while run:
    
    x_relativa = x % fondo_img.get_rect().width
    screen.blit(fondo_img, (x_relativa-fondo_img.get_rect().width,0))
    if x_relativa < PANTALLA_ANCHO:
        screen.blit(fondo_img, (x_relativa,0))
    x -= 1
    
    screen.blit(titulo_img, [50,-70])
    
    if boton_play.dibujar(screen):
        play = True
        while play:
            screen.fill(BLACK)
            #CODIGO DE JUEGO
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    play = False
            pygame.display.update()
        pygame.quit()
    
    if boton_option.dibujar(screen):
        print('OPTION')
    
    if boton_quit.dibujar(screen):
        run = False
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    #Actualiza la pantalla en cada ciclo
    pygame.display.update()

pygame.quit()