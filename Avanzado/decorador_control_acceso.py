'''Imagina que estás trabajando en el desarrollo de un sistema para una
aplicación de gestión de documentos en un entorno empresarial. Deseas
implementar un decorador llamado "verificar_acceso_entorno"
que permita controlar el acceso a funciones según el entorno de ejecución.
El decorador debe realizar las siguientes acciones:
1. Antes de ejecutar la función, verificar si el entorno de ejecución es
"producción".

2. Si el entorno es "producción", permitir la ejecución de la función y mostrar
un mensaje indicando que el acceso fue permitido en el entorno de
producción.
3. Si el entorno no es "producción", evitar la ejecución de la función y mostrar
un mensaje indicando que el acceso está restringido a entornos de
producción.
Luego, aplica este decorador a dos funciones, subir
_
documento y
eliminar
_
documento . Intenta ejecutar estas funciones con diferentes entornos y
observa el comportamiento del decorador.
'''
def verificar_acceso_entorno(funcion):
    def wrapper(*args, **kwargs):
        entorno = obtener_entorno()
        if entorno == "produccion":
            print("Acceso permitido al entorno de producción")
            return (funcion(*args, **kwargs))
        else:
            print("Acceso denegado al entorno de desarrollo")
    return wrapper

@verificar_acceso_entorno
def subir_documento(documento):
    print(f"Subiendo documento {documento}")


@verificar_acceso_entorno
def eliminar_documento(documento):
    print(f"Eliminando documento {documento}")


# Entorno de produccion
print("//////Entorno de producción/////")
def obtener_entorno():
    return "produccion"
subir_documento("documento A")
eliminar_documento("documento B")

# Entorno de desarrollo
print("//////Entorno de desarrollo/////")
def obtener_entorno():
    return "desarrollo"
subir_documento("documento A")
eliminar_documento("documento B")