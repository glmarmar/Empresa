__author__ = 'Greg'


class Empresa:
    """
        Esta clase representa a una empresa comun.
    """

    def __init__(self, nombre_empresa, cif, razon_social):
        """
        Crea una nueva empresa sin departamentos.

        :param nombre_empresa: Nombre de la empresa
        :param cif: Codigo de Identificacion Fiscal de la empresa
        :param razon_social: Razon social de la empresa
        :return: Nueva empresa
        """
        self.nombre_empresa = nombre_empresa
        self.cif = cif
        self.razon_social = razon_social
        self.departamentos = []