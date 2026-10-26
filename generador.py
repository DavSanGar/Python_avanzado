import random
import string

def generar_contraseña_segura(longitud, inclu_minus=True, inclu_mayus=True, inclu_num=True, inclu_car_especial=True):
    '''Genera una contraseña segura dada una longitud, al menos con una mayus, una mimus, un número y un caracter especial'''

    caracteres = ""

    if inclu_minus:
        caracteres += string.ascii_lowercase
    if inclu_mayus:
        caracteres += string.ascii_uppercase
    if inclu_num:
        caracteres += string.digits
    if inclu_car_especial:
        caracteres += string.punctuation

    contraseña = "".join(random.choice(caracteres) for i in range(longitud))

    return contraseña