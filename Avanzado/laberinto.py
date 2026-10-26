'''Problema de Resolución de Laberinto:

Imagina que eres parte de un equipo de desarrollo de IA que se encarga de
crear un sistema para que un robot resuelva laberintos. El laberinto está
representado por una matriz, donde ciertos valores indican caminos permitidos
( 0 ), paredes ( 1 ), y la salida ( 9 ). Tu tarea es implementar una función
recursiva que encuentre la ruta más corta para que el robot salga del laberinto.
Toma en cuenta los siguientes puntos:
1. La matriz representa el laberinto, donde los valores son:

0: Camino permitido.
1: Pared, no se puede atravesar.
9: Salida del laberinto.

laberinto = [
[1,0,1,1,1,1,1
 1,0,0,1,1,1,1
 1,0,0,1,1,1,1
 0,0,1,1,1,1,1
 0,1,0,0,0,0,1
 0,0,0,1,1,0,9]
]
2. Debes implementar la función resolver
_
laberinto que utiliza recursividad
para encontrar la ruta más corta desde una posición inicial hasta la salida.
3. La función debe devolver una lista de coordenadas que representan la ruta
desde la posición inicial hasta la salida.
4. Puedes usar una lista de movimientos posibles: arriba ( (-1, 0) ), abajo( (1,
0) ), izquierda ( (0,
-1) ), derecha ( (0, 1) ).


A continuacion un ejemplo de una posible entrada y salida de la solucion:

Entrada
 Laberinto (matriz)
- IIndice de nicio (fila)
- Indice de Inicio (columna)

Salida
Camino para salir del laberinto: (1,1),(1,2),
(),()…
'''

def resolver_laberinto(laberinto, fila, columna, camino=None):
    if camino is None:
      camino = []  

    if not (0<=fila<len(laberinto)) or not (0<=columna<len(laberinto)) or laberinto[fila][columna]==1 or (fila,columna) in camino:
       return None
    camino.append((fila, columna))

    #caso base // si nos encontramos en la salida

    if laberinto[fila][columna] == 9:
       return camino
    
    #definir movimiento posibles

    movimientos = [(-1,0),(1,0),(0,-1),(0,1)]

    for movimiento in movimientos:
       nueva_fila, nueva_columna = fila+movimiento[0], columna+movimiento[1]
       resultado = resolver_laberinto(laberinto, nueva_fila, nueva_columna, camino.copy())
       if resultado:
          return resultado
    return None # No hay solución desde esta posición
          
def imprimir_laberinto (laberinto, camino):
   for fila in range (len(laberinto)):
      for columna in range (len(laberinto[0])):
        if (fila, columna) in camino:
            print('*', end=' ')
        else:
            print(laberinto[fila][columna], end=' ')
      print()


laberinto = [
[1,0,1,1,1,1,1],
[1,0,0,1,1,1,1],
[1,0,0,1,1,1,1],
[0,0,1,1,1,1,1],
[0,1,0,0,0,0,1],
[0,0,0,1,1,9,1],
]
camino_solucion = resolver_laberinto(laberinto, 0, 1)

if camino_solucion:
   print("El camino para salir del laberinto es: ")
   imprimir_laberinto(laberinto, camino_solucion)
else:
   print("no hay solución para este laberinto")