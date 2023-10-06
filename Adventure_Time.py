#Paquetes necesarios para la creación del juego
import sys
import pygame
from boton import Boton

pygame.init()

#Definición de colores
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
CYAN =  (  0, 255, 255)

#Definición de resolución de pantalla
PANTALLA_ANCHO = 800
PANTALLA_ALTO = 600
movimiento_fondo = 0

#Creación y nombre de ventana
screen = pygame.display.set_mode((PANTALLA_ANCHO, PANTALLA_ALTO))  
pygame.display.set_caption("Adventure Time")

#Carga de imagenes
titulo_img = pygame.image.load('imagenes/adventure_time.png').convert_alpha()
fondo_img = pygame.image.load('imagenes/fondo.png').convert_alpha()
play_img = pygame.image.load('imagenes/play_btn.png').convert_alpha()
option_img = pygame.image.load('imagenes/option_btn.png').convert_alpha()
quit_img = pygame.image.load('imagenes/quit_btn.png').convert_alpha()

#Carga de música de fondo
pygame.mixer.music.load('sonidos/menu_theme.ogg')
pygame.mixer.music.play(-1) #-1 para reproducción infinita

#Instancias de botones
boton_play = Boton(300, 250, play_img, 1)
boton_option = Boton(300, 350, option_img, 1)
boton_quit = Boton(300, 450, quit_img, 1)

run = True
while run:
    
    #Fondo en movimiento
    movimiento_fondo_relativo = movimiento_fondo % fondo_img.get_rect().width
    screen.blit(fondo_img, (movimiento_fondo_relativo - fondo_img.get_rect().width,0))
    if movimiento_fondo_relativo < PANTALLA_ANCHO:
        screen.blit(fondo_img, (movimiento_fondo_relativo,0))
    movimiento_fondo -= 1
    
    
    #Título del juego
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