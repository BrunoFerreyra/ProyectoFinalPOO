# ProyectoFinalPOO
 Este proyecto constará de crear un juego RPG single-player, como trabajo final de la materia Programacion Orientada a Objetos.

4/10/2023
Creación de archivo juego "adventure_time.py". Objetivo: correr el juego.

5/10/2023
Creación de la clase Boton que permite la configuracion de los botones del menú.
Se eligen nuevos botones y se modifica un poco de código.
Se agrega una imagen de título y se agrega fondo sin fin.

6/10/2023
Se agrega sonido de menú.
Se consigue crear un menú principal con configuración básica de sonido y un menú para juego en ejecución
también con configuración básica de sonido.
Tenemos el espacio para insertar luego el código del juego propiamente dicho.

7/10/2023
Se optimiza el código de menús (anteriormente, de un ciclo while, se entraba a otro ciclo while y luego a otro
para cumplir con los objetivos, ahora se utiliza una serie de marcadores de estado de juego para saber a que porción de código entrar, para un mismo while).
Al apretar el botón de musica_on se superponían las pistas. Se solucionó con marcadores de encendido, apagado.

16/10/2023
Se consigue realizar una clase juego, en donde se encuentra el constructor y los procedimientos necesarios para hacer correr el juego.
El juego a estas alturas es temporal, se quieren cambiar algunos sprites.
Cuenta con menú de inicio, de pausa y de game_over.
Se conserva la utilización de marcadores para realizar tareas.
En el archivo sprites.py se acumulan todas las clases y procedimientos que son necesarios para las interacciones del jugador con el medio en el que se encuentra, el próximo objetivo es dividir este archivo en más para mayor prolijidad y entendibilidad.
En resumen, a estas alturas, tenemos la base de nuestro juego.

18/10/2023
Se agrega el sprite de agua y se acondiciona el mapa para que no aparezcan espacios negros.

21/10/2023
La carga de sprites se realiza en las clases correspondientes.
Se utiliza super() en cada clase para heredar de pygame.sprite.Sprites.
Problema: la carga de sprites en las clases correspondientes ralentizó en demasía al juego.