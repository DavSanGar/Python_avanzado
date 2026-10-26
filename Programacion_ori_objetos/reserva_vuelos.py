'''Imagina que estás desarrollando un sistema de reservas de vuelos para una
aerolínea. Crea un sistema de clases que permita a los usuarios realizar
reservas de vuelos. Aquí tienes una posible estructura:
- Clase base: `Vuelo`
- Atributos: número de vuelo, origen, destino, capacidad máxima, lista de
pasajeros
- Métodos: agregar pasajero, verificar disponibilidad de asientos
- Clase derivada: `VueloEspecial` (hereda de `Vuelo`)
- Atributos adicionales: motivo del vuelo especial (por ejemplo, vacaciones,
trabajo)
Resuelve el problema creando instancias de estas clases y realizando
reservas para diferentes vuelos y tipos de vuelos especiales.'''

class Vuelo:
    def __init__(self, n_vuelo, origen, destino, cap_maxima):
        self.n_vuelo = n_vuelo
        self.origen = origen
        self.destino = destino
        self.cap_maxima = cap_maxima
        self.lista_pasajeros = []


    def agregar_pasajero(self, pasajero):
        if len(self.lista_pasajeros) < self.cap_maxima:
            self.lista_pasajeros.append(pasajero)
            print(f"Pasajero {pasajero} agregado al vuelo {self.n_vuelo}")
        else:
            print("No hay asientos disponibles")
            
    def asientos_disponibles(self):
        return(self.cap_maxima - len(self.lista_pasajeros))

class Vuelo_especial(Vuelo):
   def __init__(self, n_vuelo, origen, destino, cap_maxima, motivo):
    super().__init__(n_vuelo, origen, destino, cap_maxima)
    self.motivo = motivo           


vuelo1 = Vuelo(1234, "Madrid", "Oporto", 150)
vuelo2 = Vuelo(5664, "Madrid", "Tenerife", 189)
vuelo3 = Vuelo(8390, "Madrid", "Funchal-Madeira", 144)
vuelo4 = Vuelo(7775, "Madrid", "Nueva York", 245)

vuelo1.agregar_pasajero("David")
print(f"Asientos disponibles en {vuelo1.asientos_disponibles()}")

vuelo_especial = Vuelo_especial(9116, "Madrid", "Bahamas", 310, "Vacaciones")
vuelo_especial.agregar_pasajero("Antonio")
print(f"Asientos disponibles en el vuelo especial: {vuelo_especial.asientos_disponibles()}")
print(f"Motivo del vuelo especial: {vuelo_especial.motivo}")