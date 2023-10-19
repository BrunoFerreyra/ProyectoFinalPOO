


""""
class Boton:
    def __init__(self, x, y , ancho, alto, color_fuente, color_fondo, contenido, tamaño):
        self.fuente = pygame.font.Font('Arial.ttf', tamaño)
        self.contenido = contenido
        
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto
        
        self.color_fuente = color_fuente
        self.color_fondo = color_fondo
        
        self.image = pygame.Surface((self.ancho, self.alto))
        self.image.fill(self.color_fondo)
        self.rect = self.image.get_rect()
        
        self.rect.x = self.x
        self.rect.y = self.y
        
        self.texto = self.fuente.render(self.contenido, True, self.color_fuente)
        self.texto_rect = self.texto.get_rect(center=(self.ancho/2, self.alto/2))
        self.image.blit(self.texto, self.texto_rect)
    
    def es_presionado (self, pos, presionado):
        if self.rect.collidepoint(pos):
            if presionado[0]:
                return True
            return False
        return False
"""