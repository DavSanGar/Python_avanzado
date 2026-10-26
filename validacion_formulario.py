"""
Crea un programa que valide un formulario de registro. Crea una función
llamada validar_formulario que reciba diferentes campos de un formulario
(nombre, correo electrónico y número de teléfono) y verifique si los valores
ingresados cumplen con los requisitos especificados, siendo estos:
1. Que el nombre tenga una longitud minima de 3 caracteres
2. Que el teléfono este conformado por dígitos y tenga una longitud de 9
caracteres
3. Que el email contenga un “@“ y un “.”

"""

def validar_formulario(nombre, mail, telefono):
    
    if len(nombre) < 3:
        return False

    
    if len(telefono) != 9 or not telefono.isdigit():
        return False
    
    if "." not in mail or "@" not in mail:
        return False

    return True

          

                
nombre = input("Introduce nombre: ")
mail = input("Introduce tu mail: ")
telefono = input("Introduce tu número: ")

valido = validar_formulario(nombre, mail, telefono)

if valido:
    print("Formulario válido")
else:
    print("Formulario invalido")

