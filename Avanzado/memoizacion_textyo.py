'''Imagina que estás trabajando en un sistema de análisis de texto que requiere
calcular la frecuencia de ocurrencia de palabras en un conjunto de
documentos. Implementa una función llamada calcular_frecuencia_palabras que
tome como entrada un texto y devuelva un diccionario que muestre la
frecuencia de cada palabra en el texto.
1. La función debe ser capaz de manejar textos y ser insensible a
mayúsculas/minúsculas (por ejemplo, "Hola" y "hola" se consideran la
misma palabra).
2. Se deben excluir las palabras comunes (artículos, preposiciones, etc.) que
no aportan información relevante al análisis.
3. Utiliza memoización para evitar recalcular la frecuencia de palabras para el
mismo texto.'''
import functools
import re
import time

@functools.lru_cache(maxsize=None)
def calcular_frecuencia_palabras(texto):
    #Pre procesamiento texto:
    #1. Ajustamos texto todo a minuscula
    texto = texto.lower()
    #2. Eliminamos puntuacion y caracteres no deseados.
    texto = re.sub(r'[^a-z\s]','', texto)
    palabras = texto.split()

    #Excluir palabras comunes
    palabras_comunes = set(["el", "la", "los", "las", "de", "en", "y", "a", "con", "es", "un", "una", "para"])

    palabras = [palabra for palabra in palabras if palabra not in palabras_comunes]

    #Conteo de frecuencia

    frecuencia = {}

    for palabra in palabras:
        frecuencia[palabra] = frecuencia.get(palabra,0)+1
    return frecuencia

#Ejemplos de uso
texto_1 = "Este es un ejemplo de análisis de texto, Este texto tiene varias palabras repetidas"
texto_2 = "Otro ejemplo de Análisis de texto con palabras repetidas. Ejemplo y texto se repiten"

inicio_1 = time.time()
frecuencia_sin_memo_1 = calcular_frecuencia_palabras(texto_1)
frecuencia_sin_memo_2 = calcular_frecuencia_palabras(texto_2)
fin_1 = time.time()
inicio_2 = time.time()
frecuencia_con_memo_1 = calcular_frecuencia_palabras(texto_1)
frecuencia_con_memo_2 = calcular_frecuencia_palabras(texto_2)
fin_2 = time.time()

print("Frecuencia de palabras para texto_1 sin memoización:", frecuencia_sin_memo_1)
print("Frecuencia de palabras para texto_2 sin memoización:", frecuencia_sin_memo_2)
print("Frecuencia de palabras para texto_1 con memoización:", frecuencia_sin_memo_1)
print("Frecuencia de palabras para texto_2 con memoización:", frecuencia_sin_memo_2)

print("Tiempo sin memoización: ", (fin_1 - inicio_1))
print("Tiempo con memoización: ", (fin_2 - inicio_2))
