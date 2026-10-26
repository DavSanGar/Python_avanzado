'''Imagina que estás trabajando en un sistema de gestión de costos de envío para
una empresa de logística. El sistema debe calcular el costo de envío para
diferentes destinos, distancias y pesos de paquetes. Implementa una función
llamada calcular_costo_envio que tome como entrada un destino, una distancia
en kilómetros y un peso en kilogramos, y devuelva el costo total del envío.
Requerimientos:
1. El costo base de envío es de $5.0.
2. El costo por kilómetro de distancia es de $0.1.
3. El costo por kilogramo de peso es de $0.2.
Implementa la función de manera eficiente utilizando memoización para evitar
recalcular el costo para los mismos destinos, distancias y pesos.
'''

import functools
import time

@functools.lru_cache(maxsize=None)
def calcular_costo_envio(destino,distancia,peso):
    costo_base = 5
    costo_distancia = distancia * 0.1
    costo_peso = peso * 0.2
    costo_total = costo_base + costo_distancia + costo_peso
    return costo_total

#Ejemplo uso
#Sin memoizacion

inicio=time.time()
destino_1 = "ciudad a"
distancia_1 = 150
peso_1 = 2.5
costo_sin_memo_1 = calcular_costo_envio(destino_1,distancia_1,peso_1)

destino_2 = "ciudad b"
distancia_2 = 100
peso_2 = 4.5
costo_sin_memo_2 = calcular_costo_envio(destino_2, distancia_2,peso_2)
final = time.time()


#Con memoizacion
inicio_2=time.time()
destino_1 = "ciudad a"
distancia_1 = 150
peso_1 = 2.5
costo_con_memo_1 = calcular_costo_envio(destino_1, distancia_1,peso_1)

destino_2 = "ciudad b"
distancia_2 = 100
peso_2 = 4.5
costo_con_memo_2 = calcular_costo_envio(destino_2, distancia_2,peso_2)
final_2 = time.time()

print("Costo sin memo para ciudad a es de :", costo_sin_memo_1)
print("Costo sin memo para ciudad b es de :", costo_sin_memo_2)
print("Costo con memo para ciudad a es de :", costo_con_memo_1)
print("Costo con memo para ciudad b es de :", costo_con_memo_2)

print(f"El tiempo de calculo sin memo es: {final-inicio}")
print(f"El tiempo de calculo con memo es: {final_2-inicio_2}")

