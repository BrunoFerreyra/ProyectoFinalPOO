import pygame
from constantes import *
import math
from plantilla_sprites import *

class Ataque(pygame.sprite.Sprite): #Clase en pygame para manejar sprites mas facilmente
    def __init__(self, juego, x, y): #x, y: coordenadas de lo que aparezca en pantalla
        self.juego = juego
        super().__init__(self.juego.todos_sprites)
        
        self.plantilla_ataque = Plantilla_Sprites('imagenes/attack.png')
        self.x = x
        self.y = y
        self.ancho = TAMANIO_MOSAICO
        self.alto = TAMANIO_MOSAICO
        
        self.bucle_animacion = 0
        self.image = self.plantilla_ataque.get_plantilla(0 , 0, self.ancho, self.alto)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
        self.animaciones_derecha = [self.plantilla_ataque.get_plantilla(0, 64, self.ancho, self.alto),
                        self.plantilla_ataque.get_plantilla(32, 64, self.ancho, self.alto),
                        self.plantilla_ataque.get_plantilla(64, 64, self.ancho, self.alto),
                        self.plantilla_ataque.get_plantilla(96, 64, self.ancho, self.alto),
                        self.plantilla_ataque.get_plantilla(128, 64, self.ancho, self.alto)]

        self.animaciones_abajo = [self.plantilla_ataque.get_plantilla(0, 32, self.ancho, self.alto),
                        self.plantilla_ataque.get_plantilla(32, 32, self.ancho, self.alto),
                        self.plantilla_ataque.get_plantilla(64, 32, self.ancho, self.alto),
                        self.plantilla_ataque.get_plantilla(96, 32, self.ancho, self.alto),
                        self.plantilla_ataque.get_plantilla(128, 32, self.ancho, self.alto)]

        self.animaciones_izquierda = [self.plantilla_ataque.get_plantilla(0, 96, self.ancho, self.alto),
                        self.plantilla_ataque.get_plantilla(32, 96, self.ancho, self.alto),
                        self.plantilla_ataque.get_plantilla(64, 96, self.ancho, self.alto),
                        self.plantilla_ataque.get_plantilla(96, 96, self.ancho, self.alto),
                        self.plantilla_ataque.get_plantilla(128, 96, self.ancho, self.alto)]

        self.animaciones_arriba = [self.plantilla_ataque.get_plantilla(0, 0, self.ancho, self.alto),
                        self.plantilla_ataque.get_plantilla(32, 0, self.ancho, self.alto),
                        self.plantilla_ataque.get_plantilla(64, 0, self.ancho, self.alto),
                        self.plantilla_ataque.get_plantilla(96, 0, self.ancho, self.alto),
                        self.plantilla_ataque.get_plantilla(128, 0, self.ancho, self.alto)]
        
    def update(self):
        self.colision()
        self.animacion()
    
    def colision(self):
        #choque = 
        pygame.sprite.spritecollide(self, self.juego.enemigos, True)
    
    def animacion(self):
        
        direccion = self.juego.jugador.direccion
        
        if direccion == 'arriba':
            self.image = self.animaciones_arriba[math.floor(self.bucle_animacion)]
            self.bucle_animacion += 0.5
            if self.bucle_animacion >= 5:
                self.kill()
        
        if direccion == 'abajo':
            self.image = self.animaciones_abajo[math.floor(self.bucle_animacion)]
            self.bucle_animacion += 0.5
            if self.bucle_animacion >= 5:
                self.kill()
        
        if direccion == 'izquierda':
            self.image = self.animaciones_izquierda[math.floor(self.bucle_animacion)]
            self.bucle_animacion += 0.5
            if self.bucle_animacion >= 5:
                self.kill()
        
        if direccion == 'derecha':
            self.image = self.animaciones_derecha[math.floor(self.bucle_animacion)]
            self.bucle_animacion += 0.5
            if self.bucle_animacion >= 5:
                self.kill()
