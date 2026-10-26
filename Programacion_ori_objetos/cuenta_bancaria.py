'''Crea una clase "CuentaBancaria" con atributos como número de cuenta y
saldo. Implementa métodos para depositar y retirar dinero, y muestra el
saldo actual.'''

class cuenta_bancaria:
    '''Inicializamos atributos de la cuenta'''
    def __init__(self, n_cuenta, saldo):
        self.n_cuenta = n_cuenta
        self.saldo = saldo
        self.saldo_actual = 0
        print(f"Su saldo es de {saldo}€")
    
    
    def retirar_dinero(self, retirar):
        retirar = int(input("¿Cuánto dinero quieres retirar?"))
        
        while retirar > self.saldo:
            print("Fondos insuficientes. No puedes retirar esa cantidad. Intente de nuevo\n")
            retirar = int(input("¿Cuánto dinero quieres retirar?"))
        else:
            self.saldo_actual = self.saldo - retirar
            print(f"Has retirado {retirar}€. Te queda {self.saldo_actual}€\n")

    
    
    def depositar_saldo(self, depositar):
        depositar = int(input("¿Cuánto saldo quieres depositar?"))

        self.saldo_actual = self.saldo_actual + depositar
        print(f"Has ingresado {depositar}€. Su saldo actual es de {self.saldo_actual}€")
mi_cuenta = cuenta_bancaria(123456789, 500)
mi_cuenta.retirar_dinero(0)
mi_cuenta.depositar_saldo(0)
   