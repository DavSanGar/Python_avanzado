'''Problema de Transformación y Filtrado de Nombres:
Imagina que te encuentras desarrollando una herramienta de procesamiento de
nombres para una aplicación de gestión de contactos. Tienes una lista de
nombres en el formato "Apellido, Nombre", realiza las siguientes tareas:
1. Utiliza la función lambda para transformar una lista de nombres completos
al nuevo formato.
2. Filtra la lista para incluir solo los nombres que contienen al menos dos
vocales y tienen una longitud mayor a 10 caracteres.
A continuacion un ejemplo de una posible entrada y salida de la solucion:

'''

lista_nombres = ["Perz,John","Lopez,Maria","Garcia, Jose","Martin,Ana"]

def filtrar_nombres(nombres_orden1):
    def nombre_valido(nombre):
        vocales = "aeiouAEIOUáéíóúÁÉÍÓÚ"
        return sum(1 for letra in nombre if letra in vocales) >=2 and len(nombre) >10
    return [nombre for nombre in nombres_orden1 if nombre_valido(nombre)]


nombres_orden = list(map(lambda x: f"{x.split(',')[1]}, {x.split(',')[0]}", lista_nombres))

print("Esta es la lista con comas: ",nombres_orden)

nombres_orden1 = [nombre.replace(',',' ') for nombre in nombres_orden]

print("Esta es la lista sin comas: ",nombres_orden1)

lista_nombres_filtrados = filtrar_nombres(nombres_orden1)
print("Esta es la lista de nombres filtrados",lista_nombres_filtrados)