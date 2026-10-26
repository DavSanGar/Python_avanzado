'''Busca si tu fecha de nacimiento esta en los primeros 10000 digitos de pi 
(y en que posición. Puedes usar find()). Puedes usar el archivo pi_10000.txt'''

try:
    with open("pi_10000.txt") as p:
        contenido = p.read()
except FileNotFoundError:
    msj = "El archivo no existe o no se encuentra en el directorio. Por favor, revíselo"
    print(msj)
else:
    if "2901" in contenido:
        print("Esa numeración se encuentra en el texto de pi_10000.txt")
    else:
        print("Esa numeración no se encuentra en el texto de pi_10000.txt")