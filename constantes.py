from constantesDAO import *
import ast

constantes = ConstantesDao()
datos = constantes.get_all()

#Resolución de pantalla
PANTALLA_ANCHO = int(datos[0][1])
PANTALLA_ALTO = int(datos[1][1])
#Colores
NEGRO =  list( ast.literal_eval( datos[2][1]))
BLANCO = list( ast.literal_eval( datos[3][1]))
ROJO =   list( ast.literal_eval( datos[4][1]))
AZUL =   list( ast.literal_eval( datos[5][1]))
#Detalles de sprite
TAMANIO_MOSAICO = int(datos[6][1])
VELOCIDAD_JUGADOR = int(datos[7][1])
VELOCIDAD_REDUCIDA = int(datos[8][1])
VELOCIDAD_DISPARO = int(datos[9][1])
FPS = int(datos[10][1])
VIDA_INICIAL = int(datos[11][1])
INTERVALO_DISPARO = int(datos[12][1])
CAPA = list( ast.literal_eval( datos[13][1]))

