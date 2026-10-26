'''Un problema común al solicitar una entrada numérica ocurre cuando las personas ingresan texto 
en lugar de números. Cuando intentas convertir la entrada a un entero (int), obtendrás un ValueError. 
Escribe un programa que solicite dos números. Suma los números y muestra el resultado. Captura el ValueError 
si alguno de los valores de entrada no es un número e imprime un mensaje de error amigable. 
Prueba tu programa ingresando dos números y luego ingresando texto en lugar de un número. 
Envuelve tu código del en un bucle while para que el usuario 
pueda continuar ingresando números incluso si comete un error ingresando texto en lugar de un número.'''



print("Escribe dos números para hacer la suma\n")


while True:
    numero1 = input("Introduce el primer número: ")
    if not numero1.isdigit():
        print("El dígito introducido no es un número. Repítalo\n")
        continue

    numero2 = input("Introduce el segundo número: ")
    if not numero2.isdigit():
        print("El dígito introducido no es un número. Repítalo\n")
        continue

    int1 = int(numero1)
    int2 = int(numero2)
    resultado = int1 + int2
    print("La suma de", int1, "y", int2 ," es: ", resultado)
    break


