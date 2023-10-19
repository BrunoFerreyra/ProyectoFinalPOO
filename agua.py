

import pygame
from constantes import *
import math
import random
from Jugador import *




class Agua(pygame.sprite.Sprite):
    def __init__(self, juego, x, y):
        self.juego = juego
        #self.capa = CAPA_AGUA
        self.grupos = self.juego.todos_sprites, self.juego.agua
        pygame.sprite.Sprite.__init__(self, self.grupos)
        
        self.x = x * TAMANIO_MOSAICO
        self.y = y * TAMANIO_MOSAICO
        self.ancho = TAMANIO_MOSAICO
        self.alto = TAMANIO_MOSAICO
        
        self.image = self.juego.plantilla_terreno.get_plantilla(900, 160, self.ancho, self.alto)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
