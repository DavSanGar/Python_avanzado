'''Crea una clase "Producto" con atributos como nombre, precio y cantidad en
stock. Luego, crea una clase "Tienda" que contenga una lista de productos
disponibles y métodos para agregar productos, mostrar el inventario y
realizar una compra'''

class producto:

    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

class tienda:

    def __init__(self):
        self.lista_productos = []

    def agregar_producto(self, producto):
        self.lista_productos.append(producto)

    def mostrar_inventario(self):
        for producto in self.lista_productos:
            print(f"{producto.nombre} - Precio: {producto.precio}€ - € - Stock {producto.stock}")

    def comprar_producto(self, nombre, cantidad):
        for producto in self.lista_productos:
            if producto.nombre == nombre:
                if producto.stock >= cantidad:
                    producto.stock -= cantidad
                    print(f"Has gastado {producto.precio * cantidad} €")
                else:
                    print("No hay suficiente stock")
                return
        print("Producto no encontrado")

mi_tienda = tienda()
producto1 = producto("camiseta", 20, 50)
producto2 = producto("pantalon", 30, 30)

mi_tienda.agregar_producto(producto1)
mi_tienda.agregar_producto(producto2)

mi_tienda.mostrar_inventario()

mi_tienda.comprar_producto("camiseta", 2)
mi_tienda.mostrar_inventario()