
import time


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
