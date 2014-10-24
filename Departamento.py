from mockito import *
from Empleado import Empleado
__author__ = 'Greg'


class Departamento:
    def __init__(self, nombre_depto, id_depto):
        self.nombre_depto = nombre_depto
        self.id_depto = id_depto
        self.empleados = []

    def anyadir_empleado(self, empleado):
        self.empleados.append(empleado)

    def get_salario_total(self):
        s = 0
        for e in self.empleados:
            s += e.get_salario()
        return s