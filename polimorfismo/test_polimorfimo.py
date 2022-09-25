from empleado import Empleado
from gerente import Gerente
def inprimir_detalles(objecto):
    print(objecto)
    print(type(objecto))

empleado = Empleado("Beniro", 5000)

inprimir_detalles(empleado)

gerente = Gerente("Karla", 6000, "Gerente")

inprimir_detalles(gerente)