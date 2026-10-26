filenames = ["gatos.txt", "perros.txt"]

for archivo in filenames:
    try:
        with open(archivo, "r") as arch:
            contenido = arch.read()
    except FileNotFoundError:
        print("El archivo no existe o no se encuentra en el directorio")          
            
    else:
        print(f"El contenido del archivo {archivo} es:")
        print(contenido)
    
