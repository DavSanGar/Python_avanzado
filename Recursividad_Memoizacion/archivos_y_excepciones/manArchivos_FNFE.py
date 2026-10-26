'''
Crea dos archivos, cats.txt y dogs.txt. Almacena al menos tres nombres de gatos en el primer archivo y tres nombres 
de perros en el segundo archivo. Escribe un programa que intente leer estos archivos e imprima el contenido de 
cada archivo en la pantalla. Envuelve tu código en un bloque try-except para capturar 
el error de FileNotFoundError, e imprime un mensaje amigable si falta algún archivo. 
Mueve uno de los archivos a una ubicación diferente en tu sistema y asegúrate de que el código en 
el bloque except se ejecute correctamente. 
Modifica tu bloque except para que falle en silencio si falta alguno de los archivos.
'''

perros_dir = '/Users/david/Desktop/Desarrollo_FullStack/Python/Python avanzado/Recursividad_Memoizacion/archivos y excepciones/dogs.txt'
perros = "dogs.txt"
gatos_dir = '/Users/david/Desktop/Desarrollo_FullStack/Python/Python avanzado/Recursividad_Memoizacion/archivos y excepciones/cats.txt'
gatos = "cats.txt"
try:
    with open(perros_dir) as p:
        contenido1 = p.read()
except FileNotFoundError:
    print("Lo siento, el archivo", perros, "no existe o no se encuetra en el directorio.") 
else:
    print("Los nombres de perros contenidos en la lista son: ", contenido1)

try:
    with open(gatos_dir) as g:
        contenido2 = g.read()
except FileNotFoundError:
    print("Lo siento, el archivo", gatos, "no existe o no se encuetra en el directorio.") 
else:
    print("Los nombres de gatos contenidos en la lista son: ", contenido2)