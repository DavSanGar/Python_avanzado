'''Crea un script que solicite una contraseña, analice si es segura y si no lo es
sugiera una nueva contraseña. Para ello puedes crear un script validador.py
que contenga una funcion validar_contrasena que reciba una cadena y
verifique si cumple con los requisitos mínimos de una contraseña segura
(por ejemplo, longitud mínima, presencia de letras mayúsculas, letras
minúsculas, números y caracteres especiales). La función debe devolver un
valor booleano que indique si la contraseña es válida o no. 

Por otro lado
puedes crear otro script creador.py con una función llamada
generar_contrasena que genere contraseñas seguras de forma aleatoria. La
función debe permitir especificar la longitud de la contraseña y qué tipos de
caracteres deben incluirse (por ejemplo, letras mayúsculas, letras
minúsculas, números y caracteres especiales).
(Para el generador de contraseñas puedes probar a usar los modulos
random y string)'''

import validador
import generador


def solicitar_contraseña_segura():
    contraseña = input("Ingrese una contraseña: ")
    valido = validador.validar_contraseña(contraseña)

    if valido:
        print("La contraseña es válida")
    else:
        print("La contraseña es incorrecta. Se sugiere una nueva contraseña")
        sugerencia = generador.generar_contraseña_segura(8)
        print("Sugerencia de la contraseña", sugerencia)
solicitar_contraseña_segura()