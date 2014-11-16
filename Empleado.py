__author__ = 'Greg'


class Empleado:
    """
        Esta clase representa a un empleado tipico de empresa.
    """

    def __init__(self, nombre, apellidos, dni, direccion, edad, email, salario):
        """
        Crea un nuevo empleado.

        :param nombre: Nombre del empleado
        :param apellidos: Apellidos del empleado
        :param dni: Documento Nacional de Identidad del empleado
        :param direccion: Direccion de residencia del empleado
        :param edad: Edad del empleado
        :param email: Email del empleado
        :param salario: Salario anual del empleado
        :return: Nuevo empleado
        """
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
        self.direccion = direccion
        self.edad = edad
        self.email = email
        self.salario = salario

    def get_salario(self):
        """
        Obtiene el salario anual del empleado.

        :return: Salario anual del empleado
        """
        return self.salario

    def get_dni(self):
        """
        Obtiene el DNI del empleado.

        :return: DNI del empleado
        """
        return self.dni

    def get_nombre_apellidos(self):
        """
        Obtiene el nombre completo del empleado.

        :return: Nombre completo del empleado
        """
        return self.nombre + ' ' + self.apellidos

    # EPD 2

    def get_edad(self):
        """
        Obtiene la edad del empleado.

        :return: Edad del empleado
        """
        return self.edad

    def get_email(self):
        """
        Obtiene el email del empleado.

        :return: Email del empleado
        """
        return self.email

    def get_direccion(self):
        """
        Obtiene la direccion del empleado.

        :return: Direccion del departamento
        """
        return self.direccion

    def get_salario_mensual(self):
        """
        Obtiene el salario mensual del empleado.

        :return: Salario mensual del empleado
        """
        return self.salario / 12.0

