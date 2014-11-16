__author__ = 'Greg'


class Departamento:
    """
        Esta clase representa a un departamento tipico de empresa.
    """

    def __init__(self, nombre_depto, id_depto):
        """
        Crea un nuevo departamento sin empleados.

        :param nombre_depto: Nombre del departamento
        :param id_depto:  Identificador del departamento
        :return: Nuevo departamento
        """
        self.nombre_depto = nombre_depto
        self.id_depto = id_depto
        self.empleados = []

    def anyadir_empleado(self, empleado):
        """
        Incluye un empleado en el departamento.

        :param empleado: Empleado
        """
        self.empleados.append(empleado)

    def get_salario_total(self):
        """
        Obtiene la suma de los salarios anuales del departamento.

        :return: Salario total anual del departamento
        """
        s = 0
        for e in self.empleados:
            s += e.get_salario()
        return s

    # EPD 2

    def get_nombre_depto(self):
        """
        Obtiene el nombre del departamento.

        :return: Nombre del departamento
        """
        return self.nombre_depto

    def get_salario_total_mensual(self):
        """
        Obtiene la suma de los salarios mensuales del departamento.

        :return: Salario total mensual del departamento
        """
        s = 0
        for e in self.empleados:
            s += e.get_salario_mensual()
        return s