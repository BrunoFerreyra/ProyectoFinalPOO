from baseDeDatos import *

class MapaDAO:
    
    def __init__(self):
        self.base = BaseDeDatos()   
    
    def get_all(self):
        return self.base.getAll("SELECT * FROM mapas")