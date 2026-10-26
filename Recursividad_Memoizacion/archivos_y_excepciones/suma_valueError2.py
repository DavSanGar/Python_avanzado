
while True:
    try:
        numero1 = int(input("Escriba el primer número: "))
        numero2 = int(input("Escriba el segundo número: "))

        suma = numero1 + numero2
        print("La suma de ambos números es: ", suma)
        break
    except ValueError:
        print("Error. Por favor, introduzca sólo números enteros")
        
    