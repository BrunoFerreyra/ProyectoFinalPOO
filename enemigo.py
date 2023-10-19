import pygame
from constantes import *
import math
import random


class Enemigo(pygame.sprite.Sprite): #Clase en pygame para manejar sprites mas facilmente
    def __init__(self, juego, x, y): #x, y: coordenadas de lo que aparezca en pantalla
        self.juego = juego
        #self.capa = CAPA_ENEMIGO #Las capas permiten dar un orden a los sprites
        self.grupos = self.juego.todos_sprites, self.juego.enemigos
        pygame.sprite.Sprite.__init__(self, self.grupos)
        
        self.x = x * TAMANIO_MOSAICO
        self.y = y * TAMANIO_MOSAICO
        self.ancho = TAMANIO_MOSAICO
        self.alto = TAMANIO_MOSAICO
        
        self.x_cambio = 0 #Variables temporales que guardan el cambio de movimiento durante el loop
        self.y_cambio = 0
        
        
        self.image = self.juego.plantilla_enemigo.get_plantilla(3, 2, self.ancho, self.alto)
        self.image.set_colorkey(NEGRO)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
    
        self.direccion = random.choice(['izquierda', 'derecha']) #Sirve para saber en que direccion mira el personaje
        self.bucle_animacion = 1
        self.bucle_movimiento = 0
        self.viaje_maximo = random.randint(30, 50)
        
        self.animaciones_izquierda = [self.juego.plantilla_enemigo.get_plantilla(3, 98, self.ancho, self.alto),
                        self.juego.plantilla_enemigo.get_plantilla(35, 98, self.ancho, self.alto),
                        self.juego.plantilla_enemigo.get_plantilla(68, 98, self.ancho, self.alto)]

        self.animaciones_derecha = [self.juego.plantilla_enemigo.get_plantilla(3, 66, self.ancho, self.alto),
                            self.juego.plantilla_enemigo.get_plantilla(35, 66, self.ancho, self.alto),
                            self.juego.plantilla_enemigo.get_plantilla(68, 66, self.ancho, self.alto)]
        
    def update(self):
        self.movimiento()
        self.animacion()
        
        self.rect.x += self.x_cambio
        self.rect.y += self.y_cambio
        
        self.x_cambio = 0
        self.y_cambio = 0
    
    def movimiento(self):
        if self.direccion == 'izquierda':
            self.x_cambio -= VELOCIDAD_ENEMIGO
            self.bucle_movimiento -= 1
            if self.bucle_movimiento <= -self.viaje_maximo:
                self.direccion = 'derecha'
        if self.direccion == 'derecha':
            self.x_cambio += VELOCIDAD_ENEMIGO
            self.bucle_movimiento += 1
            if self.bucle_movimiento >= self.viaje_maximo:
                self.direccion = 'izquierda'
    
    def animacion(self):
        
        if self.direccion == "izquierda":
            if self.x_cambio == 0: #Si se queda parado
                self.image = self.juego.plantilla_jugador.get_plantilla(3, 98, self.ancho, self.alto)
            else: #Si se mueve hacia abajo
                self.image = self.animaciones_izquierda[math.floor(self.bucle_animacion)]
                self.bucle_animacion += 0.1
                if self.bucle_animacion >= 3:
                    self.bucle_animacion = 1
        
        if self.direccion == "derecha":
            if self.x_cambio == 0: #Si se queda parado
                self.image = self.juego.plantilla_jugador.get_plantilla(3, 66, self.ancho, self.alto)
            else: #Si se mueve hacia abajo
                self.image = self.animaciones_derecha[math.floor(self.bucle_animacion)]
                self.bucle_animacion += 0.1
                if self.bucle_animacion >= 3:
                    self.bucle_animacion = 1
