from unittest import TestCase
from Departamento import *

__author__ = 'Greg'


class TestDepartamento(TestCase):
    def test_get_salario_total(self):
        dep = Departamento("Desarrollo de pruebas", 1)
        i = 1
        while i <= 3:
            emock = mock(Empleado)
            when(emock).get_salario().thenReturn(i * 1000)
            dep.anyadir_empleado(emock)
            i += 1
        self.assertEqual(dep.get_salario_total(),6000)