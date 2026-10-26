'''Imagina que trabajas en una empresa de logística y tu tarea es desarrollar un
sistema de gestión de inventario. El inventario está representado como una lista
de productos ordenados por sus códigos. Cada producto se describe como un
diccionario con las claves 'codigo' y 'cantidad'
.
Tu objetivo es implementar una función recursiva que realice una búsqueda
binaria en este inventario y devuelva la cantidad disponible para un producto
específico, dado su código.
A continuacion un ejemplo de una posible entrada y salida de la solucion:

Entrada
- Inventario de productos (json,dic,etc)
- Codigo de producto buscado
Salida
Cantidad disponible para el producto 307: 80
'''

def buscar_cant_producto(inventario, codigo_producto, inicio = 0, fin = None):
    if fin is None:
        fin = len(inventario) - 1
    #caso base: Si el rango no es válido

    if inicio > fin:
        return 0
    
    medio = (inicio+fin)//2

    #compara el código del producto con el código de la posición media
    if inventario[medio]["codigo"]== codigo_producto:
        #caso base
        return inventario[medio]["cantidad"]
    elif inventario[medio]["codigo"]< codigo_producto:
        #el codigo va a estar en el lado derecha del inventario
        return buscar_cant_producto(inventario, codigo_producto, medio+1, fin)
    else:
        #el codigo va a estar en el lado izquierdo del inventario
        return buscar_cant_producto(inventario, codigo_producto, inicio, medio - 1)
    
    #Declaramos un inventario
inventario = [
    {'codigo': 101, 'cantidad': 50},
    {'codigo': 204, 'cantidad': 30},
    {'codigo': 307, 'cantidad': 80},
    {'codigo': 412, 'cantidad': 20},
    {'codigo': 515, 'cantidad': 40},
    {'codigo': 525, 'cantidad': 50},
    {'codigo': 535, 'cantidad': 60},
    {'codigo': 545, 'cantidad': 70}

]

codigo_producto = 101
cantidad_disponible = buscar_cant_producto(inventario, codigo_producto)
print(f"Cantidad de productos disponibles para el produto {codigo_producto} es de {cantidad_disponible}")