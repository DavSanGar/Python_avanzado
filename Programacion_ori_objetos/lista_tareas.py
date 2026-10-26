'''Crea una clase "ListaTareas" que contenga una lista de tareas pendientes.
Implementa métodos para agregar una tarea, marcar una tarea como
completada y mostrar todas las tareas'''

tareas = ["recoger", "cocinar"]
tareas_completadas = []
class lista_tareas:
    print(f"Esta es la lista de tareas actuales: {tareas}\n")
    
    def agregar_tarea(self):
        tarea = input("¿Qué tarea deseas añadir?")
        tareas.append(tarea)
        

    def tarea_completada(self):
        completada = input("¿Qué tarea deseas marcar como completada? Si no hay completadas, escribe 'n' ")
        while True:
            if completada in tareas:
                tareas.remove(completada)
                tareas_completadas.append(completada)
                print(f"Esta es la lista de tareas completadas {tareas_completadas}\n")
                print(f"Esta es la lista de tareas actuales: {tareas}\n")
                completada = input("¿Qué tarea deseas marcar como completada? Si no hay completadas, escribe 'n' ")
            elif completada == 'n':
                print("No se han completado más tareas")
                break


    def mostrar_lista(self):
        print(f"Esta es la lista de tareas pendientes: {tareas}")

mi_lista = lista_tareas()
mi_lista.agregar_tarea()
mi_lista.tarea_completada()
mi_lista.mostrar_lista()