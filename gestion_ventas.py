'''Crea un programa que permita gestionar las ventas de una tienda. Utiliza una
estructura de datos adecuada para almacenar la información de las ventas
(por ejemplo, una lista de diccionarios). Implementa dos funciones, una para
agregar el producto vendido con su precio y otro para mostrar las ventas de
productos con sus respectivos precios.
(La base de datos puede tener la forma [{“Producto”: producto1, “Precio”:
precio1}, {“Producto”: producto2, “Precio”: precio2}…])'''

base_datos = []

def entrada_productos(producto, precio):
    '''agrega ventas a nuestra base de datos'''
    ventas = {
        "producto":producto,
        "precio": precio,
        }

    base_datos.append(ventas)



def mostrar_ventas():
   for venta in base_datos:
    print("Articulo: ", venta["producto"])
    print("Precio: ", venta["precio"])


entrada_productos("Camisa", 25.5)
entrada_productos("Sudadera", 56.5)
entrada_productos("Zapatos", 70.4)

mostrar_ventas()