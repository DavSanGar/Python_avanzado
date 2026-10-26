'''Supongamos que estás construyendo un sistema de gestión de empleados
para una empresa. Crea un sistema de clases que maneje la información de
los empleados, incluyendo empleados a tiempo completo y empleados a
tiempo parcial.
- Clase base: `Empleado`
- Atributos: nombre, apellido, salario base
- Clase derivada: `EmpleadoTiempoCompleto` (hereda de `Empleado`)
- Atributo adicional: bono anual
- Clase derivada: `EmpleadoTiempoParcial` (hereda de `Empleado`)
- Atributo adicional: horas trabajadas por semana
Resuelve el problema creando instancias de estas clases y calculando los
salarios totales para diferentes tipos de empleados.'''

class Empleado:
    def __init__(self, nombre, apellido, salario_base):
        self.nombre = nombre
        self.apellido = apellido
        self.salario_base = salario_base

class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, apellido, salario_base, bono_anual):
        super().__init__(nombre, apellido, salario_base)
        self.bono_anual = bono_anual

    def salario_total(self):
        return(self.salario_base + self.bono_anual)
    
etc = EmpleadoTiempoCompleto("Juan", "Rodriguez", 45000, 3000)
print(f"El salario de {etc.nombre} es de {etc.salario_total()}")

class EmpleadoTiempoParcial(Empleado):
    def __init__(self, nombre, apellido, salario_base, extras_semanales):
        super().__init__(nombre, apellido, salario_base)
        self.extras_semanales = extras_semanales

    def salario_total(self):
        costo_horas_extra = (self.extras_semanales * 30) * 52
        return self.salario_base + costo_horas_extra
    
etp = EmpleadoTiempoParcial("David", "Sanchez", 25000, 5)
print(f"El salario de {etp.nombre}, es de {etp.salario_total()}")

