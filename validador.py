def validar_contraseña(contraseña):
    '''Esta función valida la contraseña que recibimos como argumento'''
    logitud_minima = 8
    tiene_minus = False
    tiene_mayus = False
    tiene_num = False
    tiene_carac_esp = False

    if len(contraseña) < logitud_minima:
        return False
    
    for caracter in contraseña:
        if caracter.islower():
            tiene_minus = True
        elif caracter.isupper():
            tiene_mayus = True
        elif caracter.isdigit():
            tiene_num = True
        else:
            tiene_carac_esp = True

    return tiene_minus and tiene_mayus and tiene_num and tiene_carac_esp
