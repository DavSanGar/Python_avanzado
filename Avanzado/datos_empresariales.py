'''Problema de Organización de Datos Empresariales:
Imagina que trabajas en una empresa internacional con equipos distribuidos en
diferentes países. Cada equipo tiene una lista de empleados, representados
como diccionarios, con información sobre el nombre, la edad y el rendimiento
en proyectos recientes.
Tu tarea es organizar una lista consolidada de todos los empleados de la
empresa. La organización debe seguir ciertas reglas:
1. Los empleados se deben ordenar por el rendimiento en proyectos recientes
de forma descendente.
2. Para aquellos con el mismo rendimiento, se deben ordenar por edad de
forma ascendente. Además, deseas agrupar a los empleados por país para
un análisis más efectivo. Utiliza funciones lambda.
A continuacion un ejemplo de una posible entrada y salida de la solucion:

Entrada:  Registro de empleados (json,dic,etc) 
Salida: Empleados guardados
'''

from itertools import groupby

def ordenar_empelados(empleados):
    empleados_ordenados = sorted(empleados, key=lambda emp: (emp["rendimiento"], -emp["edad"]), reverse=True)
    return empleados_ordenados

def agrupar_empleados_por_pais(empleados_ordenados):
    #Agrupar empleados por país
    empleados_agrupados = {pais: list(grupo_empleados) for pais, grupo_empleados in groupby(empleados_ordenados, key=lambda emp: emp["pais"])}
    return empleados_agrupados

def mostrar_empelados_agrupados(empleados_agrupados):
    for pais, grupo_empelados in empleados_agrupados.items():
        print(f"\nPais: {pais}")
        for empleado in grupo_empelados:
            print(empleado)


empleados = [
{"nombre": "Lucía Sánchez", "edad": 34, "pais": "México", "rendimiento": 76},
{"nombre": "Pedro Díaz", "edad": 41, "pais": "Argentina", "rendimiento": 85},
{"nombre": "Valentina Ruiz", "edad": 28, "pais": "Perú", "rendimiento": 91},
{"nombre": "José García", "edad": 50, "pais": "España", "rendimiento": 67},
{"nombre": "Ana Fernández", "edad": 37, "pais": "Chile", "rendimiento": 82},
{"nombre": "Diego López", "edad": 30, "pais": "Colombia", "rendimiento": 95},
{"nombre": "María Martínez", "edad": 44, "pais": "Uruguay", "rendimiento": 74},
{"nombre": "Luis Rodríguez", "edad": 26, "pais": "Bolivia", "rendimiento": 88},
{"nombre": "Sofía Gómez", "edad": 39, "pais": "Ecuador", "rendimiento": 79},
{"nombre": "Juan Pérez", "edad": 33, "pais": "Venezuela", "rendimiento": 93}

]

empleados_ordenados = ordenar_empelados(empleados)
empleados_agrupados = agrupar_empleados_por_pais(empleados_ordenados)
mostrar_empelados_agrupados(empleados_agrupados)