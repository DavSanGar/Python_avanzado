def buscar_en_pi(filename, string):
    '''Busca la porción de string que queramos detnro de 10000 cifras pi'''

    with open(filename, "r") as f:
        contenido = f.read()
        posicion = contenido.find(string)
        return (posicion)

filename = "pi_10000.txt"
fecha = "0709"

posicion = buscar_en_pi(filename, fecha)
if posicion != -1:
    print(f"Tu fecha de nacimiento '{fecha}' se encuentra en la posición {posicion}")
else:
    print(f"Tu fecha no se encuentra en los primeros 10000 dígitos del número pi")