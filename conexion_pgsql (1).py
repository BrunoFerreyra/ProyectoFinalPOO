import psycopg2
import json
from constantes import *
"""
def consultas():
    cursor = connection.cursor()
    cursor.execute ('SELECT * from "constantes" ' )
    row = cursor.fetchone()
    print(row)  
    
    results = cursor.fetchall()
    
    for row in results:
        print(row)
"""

def cargar_constantes():
    cursor = connection.cursor()
    # Guarda las constantes en la base de datos
    for nombre, valor in constantes.items():
        cursor.execute("INSERT INTO constantes (nombre, valor) VALUES (%s, %s);", (nombre, valor))
    # Confirma los cambios
    connection.commit()
    # Cierra el cursor y la conexión
    cursor.close()
    connection.close()
    print("las constantes fueron guardadas en bbdd con exito")
"""
def descargar_constantes():
    cursor = connection.cursor()
    
    # Recupera las constantes desde la base de datos
    cursor.execute("SELECT nombre, valor FROM constantes;")
    constantes = {nombre: valor for nombre, valor in cursor.fetchall()}

    # Crea el archivo constantes.py con las constantes recuperadas
    with open('constantesPG.py', 'w') as f:
        f.write('MIS_CONSTANTES = {\n')
        for nombre, valor in constantes.items():
            f.write(f'    "{nombre}": "{valor}",\n')
        f.write('}\n')

    # Cierra el cursor y la conexión
    cursor.close()
    connection.close()
    
    print("constantes cargadas exitosamente")

def descargar_mapa():
    """

def cargar_mapa():
    
    # Convertir la lista a formato JSON
    mapa_json = json.dumps(MAPA)    
    cursor = connection.cursor()

    # Guardar el mapa en la base de datos
    cursor.execute("INSERT INTO mapas (nombre, mapa_json) VALUES (%s, %s);", ('miami', mapa_json))

    # Confirmar los cambios
    connection.commit()

    # Cerrar el cursor y la conexión
    cursor.close()
    connection.close()


def descargar_mapa():
    cursor = connection.cursor()
    # Recuperar el mapa desde la base de datos
    cursor.execute("SELECT  mapa_json FROM mapa WHERE nombre = %s;", ('mapa1',))
    mapa_json = cursor.fetchone()[0]
    
    # Convertir la cadena JSON de vuelta a una lista
    mapa = json.loads(mapa_json)
    print(mapa)
    """
    # Crea el archivo constantes.py con las constantes recuperadas
    with open('mapita.py', 'w') as f:
        for nombre, valor in mapa.items():
            f.write(f'    "{nombre}": "{valor}",\n')
    """    
    # Cierra el cursor y la conexión
    cursor.close()
    connection.close()
    
    print("constantes cargadas exitosamente")
try:
    connection = psycopg2.connect(
        host = 'localhost',
        user = 'postgres',
        password = 'perrito',
        database = 'RPG'
    )
    print("conexion exitosa!")
    
    cargar_constantes()
    
    """
    #----------------------------------------
    cursor = connection.cursor()
    # Recuperar el mapa desde la base de datos
    cursor.execute("SELECT mapa_json FROM mapa WHERE nombre = %s;", ('mapa1',))
    mapa_json = cursor.fetchone()[0]

    # Convertir la cadena JSON de vuelta a una lista
    mapa = json.loads(mapa_json)

    # Usar el mapa en tu código
    print(mapa)
    print("Exito")
    # Cerrar el cursor y la conexión
    cursor.close()
    connection.close()
    #-----------------------------------------  
    """"""
    cursor = connection.cursor()
    
    # Recupera las constantes desde la base de datos
    cursor.execute("SELECT nombre, mapa_json FROM mapa;")
    constantes = {nombre: valor for nombre, valor in cursor.fetchall()}

    # EN VEZ DE CREAR EL ARCHIVO, CREO EL OBJETO
    # Crea el archivo constantes.py con las constantes recuperadas
    with open('mapa.py', 'w') as f:
        for nombre, valor in constantes.items():
            f.write(f'{nombre} = {valor} \n')
        

    # Cierra el cursor y la conexión
    cursor.close()
    connection.close()
    
    print("constantes cargadas exitosamente")
    """
    # ---------------------------------------- 
except Exception as ex:
    print(ex)
    
    
