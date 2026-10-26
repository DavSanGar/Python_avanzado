def contar_palabras(files):

    try:
        with open(files) as f:
            contenido = f.read()
    except FileNotFoundError:
        print("Hay un error. El archivo no existe o no se encuentra en el directorio.")
    else: 
        palabras = contenido.split()
        num_palabras = len(palabras)
        print(f"El número de palabras que tiene {files} es {num_palabras}")
        
        numero_veces = 0
        p_clave = "el"
        for palabra in palabras:
            if palabra == p_clave:
                numero_veces = numero_veces + 1
        print(f"El número de veces que aparece {p_clave}, es de {numero_veces}")

files = ["historia_jamon_iberico.txt","inicios_de_python.txt"]

 
for file in files:
    contar_palabras(file)
    