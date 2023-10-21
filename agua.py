import pygame
from constantes import *
from jugador import *

class Agua(pygame.sprite.Sprite):
    def __init__(self, juego, x, y):
        self.juego = juego
        super().__init__(self.juego.todos_sprites, self.juego.agua)
        
        self.plantilla_terreno = Plantilla_Sprites('imagenes/terrain.png')
        self.x = x * TAMANIO_MOSAICO
        self.y = y * TAMANIO_MOSAICO
        self.ancho = TAMANIO_MOSAICO
        self.alto = TAMANIO_MOSAICO
        
        self.image = self.plantilla_terreno.get_plantilla(900, 160, self.ancho, self.alto)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
