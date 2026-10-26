'''Crea un sistema de gestión de una biblioteca utilizando clases en Python.
Debes implementar las siguientes clases:
1. “Libro”: Representa un libro con atributos como título, autor y número de
ejemplares disponibles.
2. “Usuario”: Representa a un usuario de la biblioteca con atributos como
nombre, número de identificación y lista de libros prestados.
3. “Biblioteca”: Representa la biblioteca en sí, con métodos para agregar
libros, prestar libros a usuarios, devolver libros y mostrar el inventario.'''


class libro:
    def __init__(self, titulo, autor, ejemplares):
        self.titulo = titulo
        self.autor = autor
        self.ejemplares = ejemplares

class usuario:
    def __init__(self, nombre, id):
        self.nombre = nombre
        self.id = id
        self.libros_prestados = []


class Biblioteca:

    def __init__(self):
        self.libros = []

    
    def agregar_libros(self, libro):
        self.libros.append(libro)
        
    def prestar_libros(self, usuario, titulo):
        for libro in self.libros:
            if libro.titulo == titulo and libro.ejemplares > 0:
                usuario.libros_prestados.append(libro)
                libro.ejemplares -= 1
                print(f"El libro {titulo} ha sido prestado a {usuario.nombre}")

                return
        print("Ese libro no está disponible.")

    def devolver_libros(self, usuario, titulo):
       for libro in usuario.libros_prestados:
           if libro.titulo == titulo:
               usuario.libros_prestados.remove(libro)
               libro.ejemplares += 1
               print(f"El libro {titulo} ha sido devuelto por  {usuario.nombre}")

    def mostrar_listas(self):
        for libro in self.libros:
            print(f"Hay {libro.ejemplares} ejemplares disponibles de el libro '{libro.titulo}' de '{libro.autor}'")


biblioteca = Biblioteca()

libro1 = libro("el jamon", "cerdo iberico", 3)
libro2 = libro("aprende python", "Dr. X", 5)

biblioteca.agregar_libros(libro1)
biblioteca.agregar_libros(libro2)

usuario1 = usuario("David", "1234")
usuario2 = usuario("Nuria", "6789")

biblioteca.mostrar_listas()
biblioteca.prestar_libros(usuario1, "el jamon")
biblioteca.prestar_libros(usuario2, "aprende python")
biblioteca.prestar_libros(usuario2, "la IA")

biblioteca.mostrar_listas()
biblioteca.devolver_libros(usuario2,"aprende python")

biblioteca.mostrar_listas()