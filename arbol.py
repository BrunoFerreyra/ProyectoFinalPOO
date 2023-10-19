
import pygame
from constantes import *
import math
import random
from Jugador import *


class Arbol(pygame.sprite.Sprite):
    def __init__(self, juego, x, y):
        self.juego = juego
        #self.capa = CAPA_ARBOL
        self.grupos = self.juego.todos_sprites, self.juego.arboles
        pygame.sprite.Sprite.__init__(self, self.grupos)
        
        self.x = x * TAMANIO_MOSAICO
        self.y = y * TAMANIO_MOSAICO
        self.ancho = TAMANIO_MOSAICO
        self.alto = TAMANIO_MOSAICO
        # if para elegir tipoelemento
        self.image = self.juego.plantilla_arboles.get_plantilla(102, 49, self.ancho, self.alto)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
