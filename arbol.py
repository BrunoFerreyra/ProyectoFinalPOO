import pygame
from constantes import *
from jugador import *

class Arbol(pygame.sprite.Sprite):
    def __init__(self, juego, x, y):
        self.juego = juego
        super().__init__(self.juego.todos_sprites, self.juego.arboles)
        
        self.plantilla_arboles = Plantilla_Sprites('imagenes/arboles.png')
        self.x = x * TAMANIO_MOSAICO
        self.y = y * TAMANIO_MOSAICO
        self.ancho = TAMANIO_MOSAICO
        self.alto = TAMANIO_MOSAICO
        
        self.image = self.plantilla_arboles.get_plantilla(102, 49, self.ancho, self.alto)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
