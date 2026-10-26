'''Escribe un programa que solicite al usuario su número favorito. 
Utiliza json.dump() para almacenar este número en un archivo. 
Escribe un programa separado que lea este valor e imprima el mensaje: “Sé cuál es tu número favorito… Es...” 
Combina ambos programas en un solo archivo (puedes crear tantas funciones como necesites). 
Si el número ya está almacenado, muestra el número favorito al usuario. Si no lo está, 
solicita al usuario su número favorito y guárdalo en un archivo. 
Ejecuta el programa al menos dos veces para asegurarte de que funciona correctamente.'''

import json

'''Comprueba si existe el num favorito y si existe lo devuelve'''

def comprobar_num_fav():
    try:
        with open("num_fav.json", "r") as file:
            n_favorito = json.load(file)
            return(n_favorito)
    except FileNotFoundError:
        return None

def guardar_numero(numero_favorito):
    '''Guarda el numero favorito introducido por el usuario'''
    with open("num_fav.json", "w") as file:
        json.dump(numero_favorito, file)


def preguntar_num_fav():
    n_favorito = int(input("Escribe tu número favorito: "))
    guardar_numero(n_favorito)
    return(n_favorito)

def print_num_fav(numero_favorito):
    print(f"Se cual es tu número favorito. Es {numero_favorito}")



numero_favorito = comprobar_num_fav()

if numero_favorito:
    print_num_fav(numero_favorito)
else: 
    numero_favorito = preguntar_num_fav()
    print(numero_favorito)    