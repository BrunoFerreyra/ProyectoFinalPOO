import sys
import pygame #Paquetes necesarios para la creación del juego

#Definición de colores
BLACK = (0, 0, 0)

#Definición de resolución de pantalla
RESOLUCION = (1100, 550)

#Clase del juego llamado Adventure Time
class Adventure_Time:
    def __init__(self):
        pygame.init()                                      #Inicialización de pygame
        self.screen = pygame.display.set_mode(RESOLUCION)  #Creación de ventana 1100 px ancho 550 px alto
        pygame.display.set_caption("Adventure Time")       #Nombre que aparece en ventana
    
    def corre_juego(self):                                 #Método necesario para que el juego corra
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            self.screen.fill(BLACK)
            pygame.display.update()                        #Actualiza la pantalla en cada ciclo

if __name__ == "__main__":                                 #Se crea el objeto juego y luego se llama al método que lo hace correr
    adventure_time_juego = Adventure_Time()
    adventure_time_juego.corre_juego()