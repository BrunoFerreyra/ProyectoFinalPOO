from mapaDAO import *
import json

mapa = MapaDAO()
dato = mapa.get_all()

    
MAPA = dato [0][1]

print(len(MAPA))